# Tarea 5: Fuentes Jerárquicas, APIs y Web Scraping

**Asignatura:** Gestión de Datos  
**Institución:** Pontificia Universidad Javeriana  
**Departamento:** Departamento de Ingeniería de Sistemas  

---

## 🎯 Objetivo

Extraer, consultar y convertir datos jerárquicos provenientes de MongoDB, una API JSON y páginas HTML en conjuntos tabulares trazables y verificables.

---

## 📋 Instrucciones Generales

1. **Un Único Cuaderno de Google Colab:**
   - Trabaje en un único cuaderno de Google Colab basado en `Taller5_FuentesJerarquicas_Starter.ipynb`.

2. **Identificación del Grupo:**
   - En la primera celda del cuaderno, cree una celda de texto e identifique los nombres completos de los integrantes.

3. **Manejo Seguro de Credenciales:**
   - Guarde credenciales únicamente en **Colab Secrets** (`MONGODB_URI` y `RESTCOUNTRIES_API_KEY`).
   - No publique cadenas de conexión, usuarios, contraseñas ni claves de API en el código o celdas de salida.

4. **Guardado y Compartición del Cuaderno:**
   - ⚠️ **¡Importante!** Ejecute todas las celdas desde un entorno reiniciado y verifique que los resultados (tablas, DataFrames impresos y mapas) queden visibles en el cuaderno como evidencia.
   - Nombre el cuaderno con el formato: `Tarea5_Jerarquicas_[Apellido1]_[Apellido2]`.
   - Configure los permisos de acceso del enlace a **"Cualquier persona con el enlace"** en modo **Lector** (*Viewer*).

---

## ⚙️ Preparación Previa

1. Cree un [clúster gratuito de MongoDB Atlas](https://www.mongodb.com/docs/atlas/tutorial/deploy-free-tier-cluster/).
2. Cree un usuario de base de datos y autorice su dirección IP.
3. Cargue los [datasets de muestra](https://www.mongodb.com/docs/manual/sample-data/).
4. Confirme que existen las colecciones:
   - `sample_airbnb.listingsAndReviews`
   - `sample_geospatial.shipwrecks`
5. Cree una clave para [REST Countries v5](https://restcountries.com/docs/countries).
6. En Colab Secrets registre `MONGODB_URI` y `RESTCOUNTRIES_API_KEY`, con acceso habilitado para el cuaderno.

> *Nota:* El cuaderno incluye snapshots para la API y las páginas HTML en caso de indisponibilidad del servicio externo. MongoDB Atlas continúa siendo obligatorio para los dos primeros bloques.

---

## 1. MongoDB Documental

**Insumo:** colección `sample_airbnb.listingsAndReviews`.

### 1.1 Selección básica
Use `find()` con proyección ejecutada en MongoDB para recuperar `name`, `summary` y `room_type`. Excluya `_id`, imprima las primeras filas del DataFrame en el cuaderno (ej. con `.head()`) y exporte el resultado como `airbnb_basica.csv`.

### 1.2 Ordenar y limitar
Recupere los diez hospedajes con mayor `weekly_price`:
- Excluya documentos donde `weekly_price` sea nulo o no exista.
- Ordene de mayor a menor en MongoDB y aplique `limit(10)`.
- Proyecte `name`, `weekly_price`, `room_type` y `address.country`.
- Convierta `Decimal128` a un número apto para Pandas.
- Imprima el DataFrame resultante completo (las 10 filas) en el cuaderno como evidencia y exporte `airbnb_top10_semanal.csv`.

---

## 2. MongoDB Geográfico

**Insumo:** colección `sample_geospatial.shipwrecks`. En GeoJSON las coordenadas se expresan como **[longitud, latitud]**.

### 2.1 Proximidad
Desde el punto `[-79.90, 9.30]`, consulte con `$near` los primeros 20 naufragios ubicados a máximo 100 km. Ejecute filtro, orden y límite en MongoDB. Imprima el DataFrame resultante en el cuaderno y exporte `naufragios_cercanos.csv`.

### 2.2 Área de estudio
Use `$geoWithin` y el siguiente polígono aproximado del corredor de la Costa Este (no representa una frontera política):

```python
POLIGONO_COSTA_ESTE = {
    "type": "Polygon",
    "coordinates": [[
        [-82.0, 24.0], [-75.0, 24.0], [-73.0, 35.0],
        [-66.0, 44.8], [-71.0, 47.0], [-82.0, 32.0],
        [-82.0, 24.0]
    ]]
}
```

Imprima las primeras filas del DataFrame obtenido en el cuaderno y exporte `naufragios_costa_este.csv`.

### 2.3 Visualización en Mapa
Seleccione hasta 1.000 naufragios con coordenadas válidas y cree un mapa interactivo con Folium. Muestre el mapa directamente en la salida de la celda de Colab y exporte `mapa_naufragios.html`.

---

## 3. API y JSON

**Insumo principal:** REST Countries v5. Use `requests`, header `Authorization: Bearer ...`, `timeout`, `raise_for_status()` y paginación hasta que `data.meta.more` sea falso. Los registros están en `data.objects`.

Si la API no responde, active el snapshot desde el cuaderno y documente el modo usado.

### 3.1 Países que usan euro
Recupere los países que usan EUR, imprima las primeras filas en el cuaderno y exporte `paises_euro.csv` con:
- `nombre_oficial`
- `capital`
- `google_maps_url`
- `modo_carga`

### 3.2 Idiomas
Construya la unión de países que hablan español, inglés o francés. Conserve una fila por país, imprima una muestra de las filas en el cuaderno y exporte `paises_idiomas.csv` con:
- `nombre_oficial`
- `idiomas_objetivo` — idiomas coincidentes separados por coma
- `poblacion`
- `gini`
- `modo_carga`

Los valores Gini ausentes deben conservarse como nulos; no elimine esos países.

---

## 4. HTML y Web Scraping

**Fuentes vivas:** [Cambios Vancouver](https://cambiosvancouver.com/) y [Cambio Bogotá](https://cambiobogota.com/).

1. Descargue cada página con `requests`, un `User-Agent` identificable y `timeout=30`.
2. Use `pandas.read_html()` para encontrar las tablas de tasas.
3. Si la descarga o el análisis falla, use los snapshots suministrados.
4. Homologue nombres, símbolos monetarios y valores numéricos.
5. Concatene ambas fuentes y calcule `spread_cop = precio_venta_cop - precio_compra_cop`.
6. Imprima el DataFrame consolidado (o sus primeras filas) en el cuaderno y exporte `tasas_cambio_consolidadas.csv` con:

| Columna | Regla |
|---|---|
| `casa_cambio` | Nombre de la fuente |
| `moneda` | Nombre o código normalizado |
| `precio_compra_cop` | Número, sin símbolos ni separadores |
| `precio_venta_cop` | Número, sin símbolos ni separadores |
| `spread_cop` | Venta menos compra |
| `fuente_url` | URL de procedencia |
| `fecha_extraccion_utc` | Fecha y hora ISO 8601 |
| `modo_carga` | `live` o `snapshot` |

Respete los términos de uso, consulte `robots.txt`, limite las solicitudes y no intente eludir autenticación ni controles de acceso.

---

## 📤 Entrega

- Ingrese al **Cuestionario 5 de Fuentes Jerárquicas** en la plataforma **Brightspace**.
- Responda las preguntas teóricas y prácticas correspondientes.
- Pegue el enlace de su **cuaderno único de Google Colab** en la última pregunta del cuestionario (asegúrese de que los permisos estén configurados como **públicos** con **"Cualquier persona con el enlace"** en modo **Lector**).
