"""Build a REST Countries v5-compatible teaching snapshot.

The source dataset is the public mledoze/countries dataset. Only fields used by
Taller 5 are retained. The output deliberately mirrors the v5 `data.objects`
envelope so the live and fallback code paths share one interface.
"""

from __future__ import annotations

import json
import urllib.request
from datetime import UTC, datetime
from pathlib import Path


SOURCE_URL = "https://raw.githubusercontent.com/mledoze/countries/master/countries.json"
OUTPUT = Path(__file__).resolve().parents[2] / "homework" / "assets" / "tarea5" / "countries_v5_snapshot_2026-09-04.json"


def main() -> None:
    request = urllib.request.Request(
        SOURCE_URL,
        headers={"User-Agent": "Javeriana-GestionDatos-Taller5/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        countries = json.load(response)

    objects = []
    for country in countries:
        capitals = [
            {"name": name, "primary": index == 0}
            for index, name in enumerate(country.get("capital") or [])
        ]
        objects.append(
            {
                "names": {
                    "common": country.get("name", {}).get("common"),
                    "official": country.get("name", {}).get("official"),
                },
                "codes": {
                    "alpha_2": country.get("cca2"),
                    "alpha_3": country.get("cca3"),
                },
                "capitals": capitals,
                "currencies": country.get("currencies") or {},
                "languages": country.get("languages") or {},
                "population": country.get("population"),
                "gini": country.get("gini") or {},
                "maps": country.get("maps") or {},
            }
        )

    payload = {
        "data": {
            "objects": objects,
            "meta": {
                "total": len(objects),
                "count": len(objects),
                "limit": len(objects),
                "offset": 0,
                "more": False,
                "snapshot": True,
                "source": SOURCE_URL,
                "generated_at": datetime.now(UTC).isoformat(),
            },
        }
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(objects)} countries to {OUTPUT}")


if __name__ == "__main__":
    main()
