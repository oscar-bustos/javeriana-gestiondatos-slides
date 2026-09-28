# Protección de datos de estudiantes

Activa los hooks en cada clon del repositorio:

```sh
git config core.hooksPath .agents/hooks
```

El hook `pre-commit` revisa los archivos preparados para el commit. El hook
`pre-push` revisa todos los archivos introducidos por los commits que se van a
enviar, incluso si se omitió `pre-commit`.

Se bloquean rutas de entregas, reportes de intentos, correos reales e
identificadores personales. El script inspecciona texto y el contenido XML de
archivos Office comprimidos. Los hooks son una barrera local: no pueden detectar
todos los datos personales en imágenes, PDF o formatos binarios antiguos, ni
impedir un envío realizado desde otro clon sin los hooks activados.
