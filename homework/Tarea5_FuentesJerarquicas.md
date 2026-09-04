# Tarea 5: Fuentes jerárquicas, APIs y web scraping

**Asignatura:** Gestión de Datos  
**Institución:** Pontificia Universidad Javeriana  
**Docente:** Oscar Leonardo Bustos  
**Puntaje total:** 50 puntos

---

## Objetivo

Extraer, consultar y convertir datos jerárquicos provenientes de MongoDB, una API JSON y páginas HTML en conjuntos tabulares trazables y verificables.

## Entrega

Trabaje en un único cuaderno de Google Colab basado en `Taller5_FuentesJerarquicas_Starter.ipynb`.

1. Identifique a los integrantes en la primera celda.
2. Guarde credenciales únicamente en **Colab Secrets**.
3. Ejecute todas las celdas desde un entorno reiniciado.
4. Comparta el cuaderno como **lector** y entregue los ocho archivos solicitados.
5. Nombre el cuaderno `Tarea5_Jerarquicas_Apellido1_Apellido2`.

No publique cadenas de conexión, usuarios, contraseñas ni claves de API.

## Preparación previa

1. Cree un [clúster gratuito de MongoDB Atlas](https://www.mongodb.com/docs/atlas/tutorial/deploy-free-tier-cluster/).
2. Cree un usuario de base de datos y autorice su dirección IP.
3. Cargue los [datasets de muestra](https://www.mongodb.com/docs/manual/sample-data/).
4. Confirme que existen:
   - `sample_airbnb.listingsAndReviews`
   - `sample_geospatial.shipwrecks`
5. Cree una clave para [REST Countries v5](https://restcountries.com/docs/countries).
6. En Colab Secrets registre `MONGODB_URI` y `RESTCOUNTRIES_API_KEY`, con acceso habilitado para el cuaderno.

El cuaderno incluye snapshots para la API y las páginas HTML. MongoDB Atlas continúa siendo obligatorio para los dos primeros bloques.

---

## 1. MongoDB documental (10 puntos)

**Insumo:** colección `sample_airbnb.listingsAndReviews`.

### 1.1 Selección básica — 4 puntos

Use `find()` con proyección ejecutada en MongoDB para recuperar `name`, `summary` y `room_type`. Excluya `_id` y exporte el resultado como `airbnb_basica.csv`.

**Aceptación:** el archivo contiene filas, exactamente las tres columnas solicitadas y no incluye `_id`.

### 1.2 Ordenar y limitar — 6 puntos

Recupere los diez hospedajes con mayor `weekly_price`:

- Excluya documentos donde `weekly_price` sea nulo o no exista.
- Ordene de mayor a menor en MongoDB y aplique `limit(10)`.
- Proyecte `name`, `weekly_price`, `room_type` y `address.country`.
- Convierta `Decimal128` a un número apto para Pandas.
- Exporte `airbnb_top10_semanal.csv`.

**Aceptación:** hay 10 filas; `weekly_price` es numérico, no contiene nulos y está en orden descendente.

---

## 2. MongoDB geográfico (10 puntos)

**Insumo:** colección `sample_geospatial.shipwrecks`. En GeoJSON las coordenadas se expresan como **[longitud, latitud]**.

### 2.1 Proximidad — 4 puntos

Desde el punto `[-79.90, 9.30]`, consulte con `$near` los primeros 20 naufragios ubicados a máximo 100 km. Ejecute filtro, orden y límite en MongoDB. Exporte `naufragios_cercanos.csv`.

**Aceptación:** máximo 20 filas, sin coordenadas inválidas y ordenadas desde la ubicación más cercana.

### 2.2 Área de estudio — 3 puntos

Use `$geoWithin` y el siguiente polígono aproximado del corredor de la Costa Este. No representa una frontera política.

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

Exporte `naufragios_costa_este.csv`.

**Aceptación:** todas las coordenadas recuperadas se encuentran dentro del polígono entregado.

### 2.3 Mapa — 3 puntos

Seleccione hasta 1.000 naufragios con coordenadas válidas y cree un mapa interactivo con Folium. Exporte `mapa_naufragios.html`.

**Aceptación:** el HTML abre localmente y muestra marcadores o agrupaciones de naufragios.

---

## 3. API y JSON (15 puntos)

**Insumo principal:** REST Countries v5. Use `requests`, header `Authorization: Bearer ...`, `timeout`, `raise_for_status()` y paginación hasta que `data.meta.more` sea falso. Los registros están en `data.objects`.

Si la API no responde, active el snapshot desde el cuaderno y documente el modo usado.

### 3.1 Países que usan euro — 7 puntos

Recupere los países que usan EUR y exporte `paises_euro.csv` con:

- `nombre_oficial`
- `capital`
- `google_maps_url`
- `modo_carga`

**Aceptación:** una fila por país, sin nombres oficiales vacíos y con modo `live` o `snapshot`.

### 3.2 Idiomas — 8 puntos

Construya la unión de países que hablan español, inglés o francés. Conserve una fila por país y exporte `paises_idiomas.csv` con:

- `nombre_oficial`
- `idiomas_objetivo` — idiomas coincidentes separados por coma
- `poblacion`
- `gini`
- `modo_carga`

Los valores Gini ausentes deben conservarse como nulos; no elimine esos países.

**Aceptación:** no hay países duplicados, población es numérica y cada fila contiene al menos uno de los tres idiomas.

---

## 4. HTML y web scraping (15 puntos)

**Fuentes vivas:** [Cambios Vancouver](https://cambiosvancouver.com/) y [Cambio Bogotá](https://cambiobogota.com/).

1. Descargue cada página con `requests`, un `User-Agent` identificable y `timeout=30`.
2. Use `pandas.read_html()` para encontrar las tablas de tasas.
3. Si la descarga o el análisis falla, use los snapshots suministrados.
4. Homologue nombres, símbolos monetarios y valores numéricos.
5. Concatene ambas fuentes y calcule `spread_cop = precio_venta_cop - precio_compra_cop`.
6. Exporte `tasas_cambio_consolidadas.csv` con:

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

**Aceptación:** contiene datos de las dos casas, columnas exactas, precios numéricos y spreads no negativos. Incluya una explicación breve si descarta una fila anómala.

Respete los términos de uso, consulte `robots.txt`, limite las solicitudes y no intente eludir autenticación ni controles de acceso.

---

## Lista de archivos

- [ ] `airbnb_basica.csv`
- [ ] `airbnb_top10_semanal.csv`
- [ ] `naufragios_cercanos.csv`
- [ ] `naufragios_costa_este.csv`
- [ ] `mapa_naufragios.html`
- [ ] `paises_euro.csv`
- [ ] `paises_idiomas.csv`
- [ ] `tasas_cambio_consolidadas.csv`

## Rúbrica transversal

En cada bloque se evaluará: consulta correcta en la fuente, transformación reproducible, salida con el esquema solicitado, manejo explícito de errores y explicación breve de decisiones o anomalías.
