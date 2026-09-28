#!/usr/bin/env python3
"""Block likely student records in staged files and outgoing Git objects."""

from __future__ import annotations

import io
import re
import subprocess
import sys
import zipfile


MAX_BYTES = 25 * 1024 * 1024
ZERO_SHA = "0" * 40
PRIVATE_PATH = re.compile(
    r"(?:^|/)(?:class20\d{2}-[12]|estudiantes|students|submissions|"
    r"entregas|calificaciones|grades)(?:/|$)|"
    r"detalles[ _-]+de[ _-]+los[ _-]+intentos|"
    r"reporte_modalidad_taller\d+|"
    r"taller\d+_[A-Za-z0-9_-]{20,}\.ipynb$",
    re.IGNORECASE,
)
EMAIL = re.compile(r"(?<![\w.+-])[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}(?![\w.-])")
STUDENT_ID = re.compile(
    r"(?:c[oó]digo|identificaci[oó]n|student[_ ]?id|c[eé]dula|"
    r"documento)\s*[:=,\t]\s*\d{6,12}\b",
    re.IGNORECASE,
)
PLACEHOLDER_DOMAINS = {"example.com", "example.org", "example.net"}


def git(*args: str) -> bytes:
    result = subprocess.run(
        ["git", *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False
    )
    if result.returncode:
        raise RuntimeError(result.stderr.decode("utf-8", "replace").strip())
    return result.stdout


def text_parts(data: bytes):
    if len(data) > MAX_BYTES:
        raise ValueError("archivo demasiado grande para revisar")
    if zipfile.is_zipfile(io.BytesIO(data)):
        total = 0
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            for item in archive.infolist():
                if not item.filename.lower().endswith((".xml", ".txt", ".csv", ".json")):
                    continue
                total += item.file_size
                if total > MAX_BYTES:
                    raise ValueError("contenido comprimido demasiado grande para revisar")
                yield archive.read(item).decode("utf-8", "replace")
    else:
        yield data.decode("utf-8", "replace")


def check_blob(path: str, data: bytes) -> str | None:
    if PRIVATE_PATH.search(path):
        return "ruta reservada para información de estudiantes"
    for content in text_parts(data):
        for address in EMAIL.findall(content):
            if address.rsplit("@", 1)[1].lower() not in PLACEHOLDER_DOMAINS:
                return "dirección de correo real"
        if STUDENT_ID.search(content):
            return "identificador personal"
    return None


def staged_blobs():
    paths = git("diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z")
    for raw_path in filter(None, paths.split(b"\0")):
        path = raw_path.decode("utf-8", "surrogateescape")
        yield path, git("show", f":{path}")


def outgoing_blobs(remote_name: str):
    seen = set()
    for line in sys.stdin:
        fields = line.split()
        if len(fields) != 4:
            raise ValueError("entrada inesperada del hook pre-push")
        _local_ref, local_sha, _remote_ref, remote_sha = fields
        if local_sha == ZERO_SHA:
            continue
        if remote_sha == ZERO_SHA:
            commits = git("rev-list", local_sha, f"--remotes={remote_name}")
        else:
            commits = git("rev-list", local_sha, f"^{remote_sha}")
        for raw_commit in commits.splitlines():
            commit = raw_commit.decode("ascii")
            paths = git(
                "diff-tree", "--root", "--no-commit-id", "--name-only",
                "--diff-filter=ACMR", "-r", "-m", "-z", commit,
            )
            for raw_path in filter(None, paths.split(b"\0")):
                path = raw_path.decode("utf-8", "surrogateescape")
                if (commit, path) in seen:
                    continue
                seen.add((commit, path))
                yield path, git("show", f"{commit}:{path}")


def main() -> int:
    try:
        if len(sys.argv) == 2 and sys.argv[1] == "staged":
            blobs = staged_blobs()
        elif len(sys.argv) >= 3 and sys.argv[1] == "push":
            blobs = outgoing_blobs(sys.argv[2])
        else:
            print("Uso: check_student_privacy.py staged | push REMOTE", file=sys.stderr)
            return 2
        issues = []
        for path, data in blobs:
            try:
                reason = check_blob(path, data)
            except ValueError as exc:
                reason = str(exc)
            if reason:
                issues.append((path, reason))
        if issues:
            print("Bloqueado: posible información de estudiantes:", file=sys.stderr)
            for path, reason in issues:
                print(f"  {path}: {reason}", file=sys.stderr)
            print("Retira estos datos del commit antes de continuar.", file=sys.stderr)
            return 1
        return 0
    except (OSError, RuntimeError, ValueError) as exc:
        print(f"No se pudo completar la revisión de privacidad: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
