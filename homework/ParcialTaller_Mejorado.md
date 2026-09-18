# Parcial Taller Individual: integración y preparación de datos

**Asignatura:** Gestión de Datos  
**Institución:** Pontificia Universidad Javeriana  
**Departamento:** Departamento de Ingeniería de Sistemas  
**Duración:** 4 horas  
**Puntaje:** 50 puntos  
**Modalidad:** Individual  

---

## Objetivo

Construir un flujo reproducible de extracción, integración, evaluación de calidad, limpieza y preparación de una vista minable a partir de fuentes tabulares y jerárquicas.

El parcial utiliza archivos congelados. **No use APIs vivas ni páginas web como fuentes de datos diferentes de los enlaces de descarga indicados.** Los resultados se califican contra los conteos, esquemas y reglas definidos en este documento.

## Caso funcional

Una empresa de distribución de contenido digital está organizando sus datos para atender dos necesidades internas:

1. **Finanzas internacionales** debe preparar el cierre corporativo en pesos colombianos (COP). La empresa factura contenido digital en la moneda local del país de facturación y la sede en Colombia necesita convertir cada operación a una referencia común y auditable. Hoy el monto de la factura está en la base transaccional, la moneda se deduce mediante un catálogo de países y la conversión requiere una fuente congelada de tasas de cambio.
2. **Analítica de clientes** recibió una base independiente de perfiles y necesita determinar si tiene la calidad suficiente para futuros ejercicios de segmentación y modelos basados en distancia. Antes de modelar, el equipo debe diagnosticar, limpiar y transformar los datos.

Los dos frentes no se cruzan entre sí: Chinook se usa para el reporte financiero y `Customers.csv` para la preparación analítica de clientes. Ambos deben quedar documentados dentro de un mismo flujo reproducible y auditable.

## Estructura del parcial

| Parte | Necesidad | Insumos | Productos | Puntos |
|---|---|---|---|---:|
| **I. Consolidación de facturas en COP** | Convertir cada factura desde su moneda local a COP y dejar una trazabilidad auditable | Chinook, países y una tabla de tasas | `01_facturacion.csv` a `04_facturacion_cop.csv` | 22 |
| **II. Calidad y preparación de clientes** | Diagnosticar, limpiar y transformar perfiles para analítica | `Customers.csv` | `05_reporte_calidad.csv` a `08_vista_minable.csv` | 28 |

> **Regla de separación:** no cruce `Customers.csv` con Chinook, países o tasas. Los datos de una parte no se usan para calcular resultados de la otra.

## Entrega

Entregue un único archivo comprimido llamado:

```text
ParcialTaller_<codigo>.zip
```

El archivo debe contener exactamente esta estructura:

```text
ParcialTaller_<codigo>.ipynb
salidas/
├── 01_facturacion.csv
├── 02_paises_monedas.csv
├── 03_tasas.csv
├── 04_facturacion_cop.csv
├── 05_reporte_calidad.csv
├── 06_correlaciones.csv
├── 07_clientes_limpios.csv
└── 08_vista_minable.csv
```

No incluya los archivos de entrada dentro del ZIP. Los cuatro insumos están almacenados en `homework/assets/parcial_taller/` de este repositorio y el cuaderno debe descargarlos usando las URL de este enunciado.

### Condiciones obligatorias del cuaderno

1. El nombre del cuaderno debe ser `ParcialTaller_<codigo>.ipynb`.
2. Todas las celdas deben estar ejecutadas y sus salidas deben quedar visibles.
3. El cuaderno debe ejecutarse de principio a fin después de reiniciar el entorno de Colab.
4. Use exactamente estos encabezados Markdown, en este orden:

```text
# PARTE_I_CONSOLIDACION_COP
## 1_INSUMOS_PARTE_I
## 2_SQL_Y_GRANULARIDAD
## 3_FUENTES_JERARQUICAS_E_INTEGRACION
## 4_RESPUESTAS_PARTE_I
# PARTE_II_PREPARACION_CLIENTES
## 5_INSUMO_PARTE_II
## 6_EDA_Y_CALIDAD
## 7_LIMPIEZA
## 8_VISTA_MINABLE
## 9_RESPUESTAS_PARTE_II
# 10_LINAJE_DBML
```

5. En la primera celda de texto incluya únicamente:

```text
NOMBRE_COMPLETO=<nombre y apellidos>
CODIGO=<código institucional>
```

6. Puede usar `pandas`, `numpy`, `matplotlib`, `seaborn`, `sqlite3`, `requests`, `json`, `re` y `scikit-learn`. No se requiere ninguna otra librería.

---

## Contrato general de los CSV

Todos los archivos deben cumplir estas reglas:

- Codificación `UTF-8`.
- Separador coma: `,`.
- Punto como separador decimal.
- Encabezados exactamente iguales a los definidos en este enunciado.
- Columnas en el orden indicado.
- Sin índice de Pandas: `index=False`.
- Sin columnas adicionales.
- Sin filas duplicadas, salvo que el enunciado indique lo contrario.
- Ordenar las filas antes de exportar usando el criterio indicado para cada archivo.
- Hacer cálculos y cruces con la precisión completa. Redondear únicamente las columnas y archivos para los que se especifica una cantidad de decimales.

Una diferencia en el nombre, mayúsculas, orden, tipo, redondeo o número de columnas se considera incumplimiento del contrato de salida.

---

# PARTE I. Consolidación de facturas en COP — 22 puntos

Esta parte termina en `04_facturacion_cop.csv`. Utilice únicamente Chinook, el catálogo JSON de países y la tabla HTML de tasas de Vancouver. **No use `Customers.csv` en ningún ejercicio de esta parte.**

### Propósito funcional de la Parte I

La sede financiera de la empresa está en Colombia y su cierre corporativo se revisa en COP. Las facturas de venta están registradas en la moneda local del país facturado; por ello, antes de consolidar el cierre, Finanzas debe identificar esa moneda y convertir cada factura directamente a COP usando el corte oficial de tasas entregado por Tesorería.

El ejercicio consiste en crear la base de consolidación: identificar cada factura sin duplicarla, reconocer la moneda del país facturado, normalizar las tasas expresadas frente a COP y dejar visible la tasa usada para cada conversión. El archivo final conserva el valor local original, la tasa local-COP y el valor consolidado en COP para que el equipo contable pueda auditar cada registro.

> **Alcance:** este parcial consolida cada factura a COP. Las columnas y la fórmula de `04_facturacion_cop.csv` son exactamente las definidas más adelante; no agregue una columna de salida adicional.

## 1. Insumos de la Parte I

### Necesidad funcional

Todos los analistas deben comenzar con los mismos insumos financieros y con el mismo corte de tasas frente a COP para que la preparación del cierre sea comparable. La carpeta del parcial actúa como el paquete oficial entregado por las áreas propietarias de estos datos.

> **Resultado funcional:** disponer en Colab de la base de facturación, el catálogo de países y la fuente de tasas con referencia COP requerida por esta parte.

Descargue exactamente los siguientes archivos desde la carpeta `homework/assets/parcial_taller/` de este repositorio:

| Archivo local | URL de descarga |
|---|---|
| [`chinook.db`](assets/parcial_taller/chinook.db) | `https://raw.githubusercontent.com/oscar-bustos/javeriana-gestiondatos-slides/main/homework/assets/parcial_taller/chinook.db` |
| [`countries_v5_snapshot_2026-09-04.json`](assets/parcial_taller/countries_v5_snapshot_2026-09-04.json) | `https://raw.githubusercontent.com/oscar-bustos/javeriana-gestiondatos-slides/main/homework/assets/parcial_taller/countries_v5_snapshot_2026-09-04.json` |
| [`cambios_vancouver_2026-09-04.html`](assets/parcial_taller/cambios_vancouver_2026-09-04.html) | `https://raw.githubusercontent.com/oscar-bustos/javeriana-gestiondatos-slides/main/homework/assets/parcial_taller/cambios_vancouver_2026-09-04.html` |

Guarde estos tres archivos en el directorio de trabajo de Colab con los nombres indicados en la primera columna. No se exige una validación adicional de integridad.

---

## 2. SQL y granularidad — 10 puntos

### Necesidad funcional

El área financiera consulta facturas y clientes en tablas separadas. Para incluir una operación en el cierre colombiano, necesita una tabla sencilla que permita rastrear cada factura hasta su cliente, fecha, país facturado y valor local cobrado. La tabla debe conservar el nivel de detalle de factura: un mismo cliente puede tener varias facturas y ninguna factura debe multiplicarse por sus líneas de detalle.

> **Resultado funcional:** un archivo maestro de facturación, con una fila identificable por factura, que sirva como punto de partida para la consolidación en COP.

### 2.1 Extracción SQL

Use `sqlite3` y una única consulta SQL ejecutada con `pandas.read_sql_query()`.

La consulta debe:

- Partir de `invoices`.
- Unir `customers` mediante `CustomerId`.
- Conservar exactamente una fila por factura.
- Construir `customer_name` como `FirstName`, un espacio y `LastName`, sin espacios en los extremos.
- Convertir `InvoiceDate` al formato `YYYY-MM-DD`.
- Ordenar el resultado por `invoice_id` ascendente.

Exporte `salidas/01_facturacion.csv` con este contrato:

| Posición | Columna | Tipo | Regla |
|---:|---|---|---|
| 1 | `invoice_id` | entero | `InvoiceId` de `invoices` |
| 2 | `customer_name` | texto | Nombre y apellido concatenados |
| 3 | `invoice_date` | texto | Fecha `YYYY-MM-DD` |
| 4 | `billing_country` | texto | `BillingCountry` sin modificación |
| 5 | `total_local` | decimal | `Total`, con 2 decimales; monto facturado en la moneda local de `billing_country` |

**Granularidad:** una fila por factura.  
**Clave:** `invoice_id`.  
**Orden:** `invoice_id` ascendente.  
**Dimensión esperada:** 412 filas y 5 columnas.

Para este parcial, interprete `Total` de Chinook como el monto originalmente facturado en la moneda local de `billing_country`. La moneda exacta se resolverá en la sección 3 mediante el catálogo JSON. No trate este valor como USD.

## 3. Fuentes jerárquicas e integración — 12 puntos

### Necesidad funcional

El país escrito en una factura no indica directamente qué moneda debe usar el reporte. Además, la publicación de Tesorería contiene nombres de monedas y valores que deben normalizarse antes de cruzarlos con las facturas. Todas las tasas se expresan frente a COP. Finanzas necesita normalizar esta fuente y convertir únicamente las facturas para las que exista información suficiente y verificable.

> **Resultado funcional:** un reporte de facturación consolidado en COP que indique la moneda local, la tasa utilizada y el valor convertido de cada factura cubierta.

### 3.1 Normalización del JSON

El catálogo de países conserva las monedas dentro de objetos anidados. Para poder cruzarlo con otras fuentes, el equipo necesita convertirlo en una tabla donde cada relación país-moneda pueda consultarse y validarse por separado.

Lea `countries_v5_snapshot_2026-09-04.json`. Los países están en `data.objects` y las monedas de cada país están en el objeto `currencies`.

Construya **una fila por cada combinación país-moneda**:

- Si un país tiene varias monedas, debe producir varias filas.
- Si `currencies` está vacío, no produzca una fila para ese país.
- No convierta el objeto completo en texto.

Exporte `salidas/02_paises_monedas.csv`:

| Posición | Columna | Tipo | Ruta de origen |
|---:|---|---|---|
| 1 | `country_common` | texto | `names.common` |
| 2 | `country_code_alpha3` | texto | `codes.alpha_3` |
| 3 | `currency_code` | texto | Clave dentro de `currencies` |
| 4 | `currency_name` | texto | `currencies[currency_code].name` |

**Granularidad:** una fila por combinación país-moneda.  
**Clave:** `country_code_alpha3`, `currency_code`.  
**Orden:** `country_common` y luego `currency_code`, ambos ascendentes.  
**Dimensión esperada:** 275 filas y 4 columnas.  
**Países distintos con al menos una moneda:** 246.

### 3.2 Extracción del HTML congelado

Tesorería entregó una publicación congelada de tasas. Antes de usarla para la conciliación, Finanzas necesita llevarla a una tabla con nombres estables para la fuente, el código de moneda, la compra, la venta y la fecha de referencia.

Lea con `pandas.read_html()`:

- `cambios_vancouver_2026-09-04.html`

Para este archivo:

1. Exija que `read_html()` encuentre exactamente una tabla.
2. Asigne los nombres de columnas definidos para la salida.
3. Extraiga el código ISO de tres letras ubicado entre paréntesis en el texto de la moneda. Use el patrón regular `\(([A-Z]{3})\)` y detenga el proceso si una fila no coincide.
4. Convierta compra y venta a números.
5. Calcule `mid_cop = (buy_cop + sell_cop) / 2`.

Para este parcial, `buy_cop`, `sell_cop` y `mid_cop` representan **pesos colombianos por una unidad** de `currency_code`. El texto adicional como `100` en el nombre mostrado de una moneda no modifica el valor: no multiplique ni divida la tasa por 100.

Use exactamente `cambios_vancouver` como valor de `exchange_house` en todas las filas.

Exporte `salidas/03_tasas.csv`:

| Posición | Columna | Tipo | Regla |
|---:|---|---|---|
| 1 | `exchange_house` | texto | Valor fijo `cambios_vancouver` |
| 2 | `currency_code` | texto | Código ISO extraído |
| 3 | `buy_cop` | entero | Precio de compra |
| 4 | `sell_cop` | entero | Precio de venta |
| 5 | `mid_cop` | decimal | Media de compra y venta, 2 decimales |
| 6 | `snapshot_date` | texto | Valor fijo `2026-09-04` |

**Granularidad:** una fila por moneda.  
**Clave:** `exchange_house`, `currency_code`.  
**Orden:** `currency_code` y luego `exchange_house`, ambos ascendentes.  
**Dimensión esperada:** 10 filas y 6 columnas.  
**Monedas distintas esperadas:** 10.

### 3.3 Conversión de facturación

Con el maestro de facturas, el catálogo país-moneda y las tasas ya normalizadas, Finanzas puede construir el producto final. La conversión debe conservar la factura como unidad de análisis y dejar visibles las tasas usadas para que el cálculo pueda auditarse.

Para cada `currency_code`, use el valor único `mid_cop` de `03_tasas.csv` como tasa frente a COP.

Use únicamente estas equivalencias de nombres de país:

```python
COUNTRY_ALIASES = {
    "USA": "United States",
    "Czech Republic": "Czechia",
}
```

Los demás nombres deben conservarse sin modificación.

Integre:

1. `01_facturacion.csv` con `02_paises_monedas.csv` mediante el país común, después de aplicar `COUNTRY_ALIASES`.
2. El resultado con las tasas de `03_tasas.csv` mediante `currency_code`.
3. Conserve únicamente facturas cuyo país tenga exactamente una moneda en el snapshot y cuya moneda aparezca en `03_tasas.csv`.

Para este parcial, `total_local` está expresado en la moneda indicada por `local_currency`. Calcule:

```text
total_cop = total_local × mid_cop_moneda_local
```

Funcionalmente, `mid_cop_moneda_local` indica cuántos COP equivale una unidad de la moneda local. Por ello, la conversión consiste en multiplicar el valor local de la factura por esa tasa. No cree ni exporte una columna intermedia.

**Ejemplo ilustrativo:** una factura de Europa por `100.00 EUR`, con `mid_cop_EUR = 4325.00`, equivale a `100.00 × 4325.00 = 432500.00 COP`. Por tanto, `total_local` sería `100.00`, `local_currency` sería `EUR` y `total_cop` sería `432500.00`.

Use la precisión completa de las tasas para el cálculo y redondee el resultado final a 2 decimales.

Exporte `salidas/04_facturacion_cop.csv`:

| Posición | Columna | Tipo | Decimales |
|---:|---|---|---:|
| 1 | `invoice_id` | entero | — |
| 2 | `customer_name` | texto | — |
| 3 | `invoice_date` | texto | — |
| 4 | `billing_country` | texto | — |
| 5 | `local_currency` | texto | `currency_code` de `02_paises_monedas.csv` |
| 6 | `total_local` | decimal | Valor de `01_facturacion.csv`, 2 decimales |
| 7 | `rate_local_cop` | decimal | `mid_cop` de la moneda local, 2 decimales |
| 8 | `total_cop` | decimal | `total_local × rate_local_cop`, 2 decimales |

**Granularidad:** una fila por factura con tasa disponible.  
**Clave:** `invoice_id`.  
**Orden:** `invoice_id` ascendente.  
**Dimensión esperada:** 336 filas y 8 columnas.

La suma monetaria de control de la sección siguiente debe calcularse sobre `total_cop` ya redondeado y exportado en `04_facturacion_cop.csv`. No sume `total_local`, porque contiene valores de monedas diferentes.

### 3.4 Evidencias obligatorias

Imprima exactamente:

```text
P2_PARES_PAIS_MONEDA=275
P2_PAISES_CON_MONEDA=246
P2_FILAS_TASAS=10
P2_MONEDAS_TASAS=10
P2_FILAS_FACTURACION_COP=336
P2_TOTAL_COP=6607247.40
```

Los valores deben calcularse a partir de los DataFrames.

---

## 4. Preguntas conceptuales de la Parte I

### Necesidad funcional

Finanzas debe comprobar que el reporte conserva la unidad de análisis correcta y que la reducción de facturas se debe a la cobertura de las tasas, no a una eliminación arbitraria.

> **Resultado funcional:** dejar constancia de que se comprende la granularidad y la cobertura del reporte financiero construido.

Seleccione una sola respuesta por pregunta. En la celda Markdown ubicada bajo `## 4_RESPUESTAS_PARTE_I` escriba únicamente estas dos líneas:

```text
R1=<letra>
R2=<letra>
```

No agregue explicaciones ni otras respuestas en esa celda.

### R1. Granularidad de una unión

Al unir `invoices` con `invoice_items` se obtienen 2240 filas en lugar de 412. ¿Qué representa una fila del resultado?

- A. Un cliente.
- B. Una factura.
- C. Una línea de factura.
- D. Un país de facturación.

### R2. Pérdida controlada en el cruce

¿Por qué `04_facturacion_cop.csv` contiene 336 facturas y no las 412 facturas originales?

- A. Porque se eliminaron facturas duplicadas después de redondear.
- B. Porque el cruce conserva únicamente facturas cuyo país tiene una sola moneda en el catálogo y cuya moneda está cubierta por las tasas congeladas.
- C. Porque las facturas inferiores a una unidad de moneda local se consideran inválidas.
- D. Porque cada cliente puede aparecer una sola vez.

---

# PARTE II. Calidad y preparación de clientes — 28 puntos

Esta parte comienza con `Customers.csv` y termina en `08_vista_minable.csv`. Utilice únicamente la base de perfiles de clientes. **No use Chinook, el catálogo de países ni las tablas de tasas en ningún ejercicio de esta parte.**

## 5. Insumo de la Parte II

### Necesidad funcional

Analítica de Clientes recibió una base independiente de perfiles. El equipo debe descargar esa versión oficial antes de diagnosticarla y transformarla, para que todas las decisiones posteriores partan de los mismos registros.

> **Resultado funcional:** disponer en Colab de la base de perfiles que alimentará exclusivamente el flujo de calidad y preparación analítica.

Descargue exactamente el siguiente archivo desde la carpeta `homework/assets/parcial_taller/` de este repositorio:

| Archivo local | URL de descarga |
|---|---|
| [`Customers.csv`](assets/parcial_taller/Customers.csv) | `https://raw.githubusercontent.com/oscar-bustos/javeriana-gestiondatos-slides/main/homework/assets/parcial_taller/Customers.csv` |

Guarde este archivo en el directorio de trabajo de Colab con el nombre indicado en la primera columna. No se exige una validación adicional de integridad.

---

## 6. EDA y calidad — 10 puntos

### Necesidad funcional

El equipo de Analítica de Clientes todavía no debe entrenar un modelo. Primero necesita un diagnóstico reproducible que responda qué datos recibió, qué reglas incumple, dónde hay faltantes y qué relaciones numéricas aparecen. Este reporte permitirá decidir si la base puede pasar a limpieza y preparación.

> **Resultado funcional:** un perfil de calidad por variable y un inventario ordenado de relaciones numéricas, acompañado por visualizaciones que permitan revisar las distribuciones originales.

### 6.1 Carga y nombres de columnas

Los nombres originales son útiles para lectura humana, pero no siguen una convención uniforme para programar. El primer paso consiste en homologarlos sin alterar todavía los registros.

Lea `Customers.csv` y renombre las columnas con este diccionario exacto:

```python
COLUMN_RENAME = {
    "CustomerID": "customer_id",
    "Gender": "gender",
    "Age": "age",
    "Annual Income ($)": "annual_income",
    "Spending Score (1-100)": "spending_score",
    "Profession": "profession",
    "Work Experience": "work_experience",
    "Family Size": "family_size",
}
```

Use el tipo entero para las seis columnas numéricas y el tipo `string` de Pandas para `gender` y `profession`. Las celdas vacías de `profession` deben reconocerse como valores faltantes.

### 6.2 Reglas de calidad

Las áreas de negocio definieron límites mínimos para considerar utilizable un registro. El reporte debe medir los incumplimientos sin corregirlos todavía, de modo que quede evidencia del estado original de la base.

Aplique estas reglas sin cambiarlas:

| Columna | Registro válido |
|---|---|
| `customer_id` | No nulo, mayor que 0 y no duplicado |
| `gender` | Valor exactamente igual a `Female` o `Male` |
| `age` | Entre 18 y 100, incluidos los extremos |
| `annual_income` | Mayor que 0 |
| `spending_score` | Entre 1 y 100, incluidos los extremos |
| `profession` | Texto no vacío y no nulo |
| `work_experience` | Entre 0 y 60, incluidos los extremos |
| `family_size` | Entre 1 y 10, incluidos los extremos |

Construya `salidas/05_reporte_calidad.csv` con una fila por columna, en el orden de `COLUMN_RENAME`:

| Posición | Columna | Regla |
|---:|---|---|
| 1 | `column_name` | Nombre después del renombramiento |
| 2 | `data_type` | Texto `integer` o `string` |
| 3 | `missing_count` | Conteo de nulos |
| 4 | `missing_pct` | Porcentaje sobre 2000 filas, 2 decimales |
| 5 | `unique_count` | `nunique(dropna=True)` |
| 6 | `min` | Mínimo numérico, 4 decimales; vacío para texto |
| 7 | `max` | Máximo numérico, 4 decimales; vacío para texto |
| 8 | `mean` | Media numérica, 4 decimales; vacío para texto |
| 9 | `median` | Mediana numérica, 4 decimales; vacío para texto |
| 10 | `skewness` | `Series.skew()`, 4 decimales; vacío para texto |
| 11 | `invalid_count` | Registros que incumplen la regla de calidad |

**Granularidad:** una fila por columna del archivo original.  
**Orden:** el orden de `COLUMN_RENAME`.  
**Dimensión esperada:** 8 filas y 11 columnas.

### 6.3 Correlaciones

Analítica necesita identificar qué variables numéricas se mueven juntas antes de crear características o modelos. El identificador del cliente se excluye porque organiza registros, pero no describe su comportamiento.

Use únicamente estas cinco variables y en este orden base:

```python
CORRELATION_COLUMNS = [
    "age",
    "annual_income",
    "spending_score",
    "work_experience",
    "family_size",
]
```

Calcule la correlación de Pearson para cada pareja no repetida. No incluya la diagonal, parejas invertidas ni `customer_id`.

Exporte `salidas/06_correlaciones.csv`:

| Posición | Columna | Regla |
|---:|---|---|
| 1 | `variable_1` | Primera variable según `CORRELATION_COLUMNS` |
| 2 | `variable_2` | Segunda variable según `CORRELATION_COLUMNS` |
| 3 | `pearson_r` | Correlación con 6 decimales |
| 4 | `abs_pearson_r` | Valor absoluto con 6 decimales |

Ordene usando la precisión completa de `abs_pearson_r`, de mayor a menor. En caso de empate, use `variable_1` y `variable_2` en orden alfabético ascendente. Redondee después de ordenar.

**Dimensión esperada:** 10 filas y 4 columnas.

### 6.4 Gráficos obligatorios

Las tablas resumen no permiten ver por sí solas la forma de una distribución o la presencia de valores extremos. Los gráficos funcionan como evidencia visual complementaria para la revisión de calidad.

Muestre dentro del cuaderno, sin exportar imágenes:

1. Histograma de `annual_income` con exactamente 20 intervalos, título `Distribución del ingreso anual`, eje X `Ingreso anual` y eje Y `Frecuencia`.
2. Boxplot vertical de `work_experience`, título `Experiencia laboral antes de la limpieza` y eje Y `Años`.

### 6.5 Evidencias obligatorias

Imprima exactamente:

```text
P3_FILAS=2000
P3_COLUMNAS=8
P3_NULOS_PROFESSION=35
P3_DUPLICADOS_COMPLETOS=0
P3_PARES_CORRELACION=10
P3_MAYOR_CORRELACION=<variable_1>|<variable_2>|<pearson_r_con_6_decimales>
```

La última línea debe construirse con la primera fila de `06_correlaciones.csv`.

---

## 7. Limpieza determinista — 8 puntos

### Necesidad funcional

Después del diagnóstico, el equipo acordó una política única de limpieza. Se completará la profesión cuando no esté informada, se retirarán registros que contradigan las reglas de dominio y se limitarán valores extremos de experiencia laboral sin eliminar clientes adicionales por ese criterio.

> **Resultado funcional:** una base de clientes válida, sin nulos y con las decisiones de corrección aplicadas de forma consistente y repetible.

Parta del DataFrame cargado y renombrado en la sección 6. Ejecute exactamente estas operaciones y en este orden:

1. Reemplace los faltantes de `profession` por el texto `Unknown` usando `fillna()`.
2. Con Boolean Indexing conserve solo las filas que cumplen simultáneamente:
   - `18 <= age <= 100`
   - `annual_income > 0`
   - `1 <= spending_score <= 100`
   - `0 <= work_experience <= 60`
   - `1 <= family_size <= 10`
3. Sobre las filas conservadas, calcule para `work_experience`:
   - `Q1 = quantile(0.25)`
   - `Q3 = quantile(0.75)`
   - `IQR = Q3 - Q1`
   - `lower_bound = Q1 - 1.5 × IQR`
   - `upper_bound = Q3 + 1.5 × IQR`
4. Aplique `clip(lower_bound, upper_bound)` a `work_experience`. No elimine filas por el criterio IQR. Para `P4_VALORES_CAPADOS`, cuente cuántos valores cambian al aplicar este `clip`.
5. Convierta `work_experience` nuevamente a entero.
6. Ordene por `customer_id` ascendente.

Exporte `salidas/07_clientes_limpios.csv` con exactamente estas columnas:

```text
customer_id
gender
age
annual_income
spending_score
profession
work_experience
family_size
```

**Granularidad:** una fila por cliente válido.  
**Clave:** `customer_id`.  
**Dimensión esperada:** 1665 filas y 8 columnas.  
**Nulos esperados:** 0.

Imprima exactamente:

```text
P4_FILAS_ENTRADA=2000
P4_PROFESSION_IMPUTADAS=35
P4_FILAS_ELIMINADAS=335
P4_FILAS_SALIDA=1665
P4_IQR_Q1=1.00
P4_IQR_Q3=7.00
P4_IQR_LIMITE_INFERIOR=-8.00
P4_IQR_LIMITE_SUPERIOR=16.00
P4_VALORES_CAPADOS=5
P4_NULOS_SALIDA=0
```

---

## 8. Vista minable — 10 puntos

### Necesidad funcional

El siguiente equipo utilizará técnicas de segmentación y modelos basados en distancia. Para evitar que el ingreso domine por su magnitud, que las categorías lleguen como texto o que la edad pierda su interpretación por rangos, necesita una matriz exclusivamente numérica y con transformaciones conocidas.

La vista no incluye una variable objetivo: su propósito es dejar las características preparadas para experimentos posteriores, no entrenar ni evaluar un modelo durante este parcial.

> **Resultado funcional:** una matriz lista para modelamiento, con una fila por cliente válido, escalas comparables y categorías representadas de forma numérica.

Parta de `07_clientes_limpios.csv`, ordenado por `customer_id`.

### 8.1 Ingeniería de características

El ingreso total no tiene el mismo significado para hogares de tamaños distintos. `income_per_person` aproxima la disponibilidad económica por integrante y agrega una señal que no existe directamente en el archivo original.

Calcule con precisión completa:

```text
income_per_person = annual_income / family_size
```

### 8.2 Escalamiento

Los futuros modelos de distancia deben comparar variables sin favorecer automáticamente las que usan unidades o magnitudes mayores. La estandarización lleva las variables seleccionadas a una escala común.

Use `StandardScaler` sobre estas seis variables, ajustándolo con las 1665 filas:

```python
SCALE_COLUMNS = [
    "age",
    "annual_income",
    "spending_score",
    "work_experience",
    "family_size",
    "income_per_person",
]
```

Nombre las columnas resultantes:

```text
age_z
annual_income_z
spending_score_z
work_experience_z
family_size_z
income_per_person_z
```

### 8.3 Discretización

Además de conservar la edad estandarizada, el equipo quiere una representación por etapas amplias que permita comparar grupos de edad de manera uniforme.

Use `KBinsDiscretizer` exclusivamente sobre `age` con estos parámetros:

```python
KBinsDiscretizer(
    n_bins=4,
    encode="ordinal",
    strategy="uniform",
)
```

Convierta el resultado a entero y llame la columna `age_bin`. Los únicos valores permitidos son `0`, `1`, `2` y `3`.

### 8.4 Codificación categórica

Los modelos no pueden operar directamente con los textos de género y profesión. La codificación crea indicadores binarios explícitos y mantiene una columna conocida para profesiones no informadas.

Use `OneHotEncoder` con `handle_unknown="ignore"`, `sparse_output=False`, `dtype=np.int64` y estas categorías explícitas, en este orden:

```python
OHE_CATEGORIES = [
    ["Female", "Male"],
    [
        "Artist",
        "Doctor",
        "Engineer",
        "Entertainment",
        "Executive",
        "Healthcare",
        "Homemaker",
        "Lawyer",
        "Marketing",
        "Unknown",
    ],
]
```

Aplique el codificador a `gender` y `profession`, en ese orden. No use `drop="first"`.

### 8.5 Contrato de la vista minable

Exporte `salidas/08_vista_minable.csv` con exactamente estas 19 columnas y en este orden:

```text
age_z
annual_income_z
spending_score_z
work_experience_z
family_size_z
income_per_person_z
age_bin
gender_Female
gender_Male
profession_Artist
profession_Doctor
profession_Engineer
profession_Entertainment
profession_Executive
profession_Healthcare
profession_Homemaker
profession_Lawyer
profession_Marketing
profession_Unknown
```

Reglas de formato:

- Las seis columnas terminadas en `_z` deben exportarse con 6 decimales.
- `age_bin` y las columnas one-hot deben ser enteros.
- No incluya `customer_id` en la vista minable.
- No incluya columnas originales sin transformar.
- Conserve el orden de filas de `07_clientes_limpios.csv`.

**Granularidad:** una fila transformada por cliente válido.  
**Dimensión esperada:** 1665 filas y 19 columnas.  
**Nulos esperados:** 0.

Imprima exactamente:

```text
P5_FILAS=1665
P5_COLUMNAS=19
P5_NULOS=0
P5_AGE_BIN_MIN=0
P5_AGE_BIN_MAX=3
P5_COLUMNAS_OHE=12
P5_CUSTOMER_ID_INCLUIDO=NO
```

---

## 9. Preguntas conceptuales de la Parte II

### Necesidad funcional

Analítica de Clientes no solo necesita archivos correctos: también debe comprobar que quien construyó el flujo comprende los límites del diagnóstico de faltantes y las decisiones de preparación para modelos.

> **Resultado funcional:** un registro breve y calificable de las decisiones conceptuales que sostienen la preparación de la base de clientes.

Seleccione una sola respuesta por pregunta. En la celda Markdown ubicada bajo `## 9_RESPUESTAS_PARTE_II` escriba únicamente estas cuatro líneas:

```text
R3=<letra>
R4=<letra>
R5=<letra>
R6=<letra>
```

No agregue explicaciones ni otras respuestas en esa celda.

### R3. Mecanismo de datos faltantes

El archivo tiene 35 valores faltantes en `profession`. ¿Qué puede concluirse sobre el mecanismo de ausencia usando solamente el conteo de nulos?

- A. Los valores son MCAR.
- B. Los valores son MAR.
- C. Los valores son MNAR.
- D. El conteo no permite distinguir entre MCAR, MAR y MNAR.

### R4. Alta cardinalidad

¿Cuál es el riesgo principal de aplicar one-hot encoding a una variable con miles de categorías poco frecuentes?

- A. Convierte automáticamente la variable en ordinal.
- B. Produce muchas columnas dispersas y puede aumentar memoria y sobreajuste.
- C. Elimina todas las categorías poco frecuentes.
- D. Obliga a reemplazar las categorías por la media de la variable objetivo.

### R5. Exclusión del identificador

¿Por qué `customer_id` no se incluye como característica de `08_vista_minable.csv`?

- A. Porque los identificadores siempre contienen valores faltantes.
- B. Porque identifica registros, pero no representa una característica de negocio generalizable.
- C. Porque `StandardScaler` no acepta números enteros.
- D. Porque un CSV no puede almacenar identificadores.

### R6. Escalamiento resistente

Un modelo KNN utilizará variables con escalas diferentes y valores atípicos extremos que deben conservarse. ¿Qué transformador es el más resistente entre las opciones?

- A. Ningún escalamiento.
- B. `MinMaxScaler`.
- C. `StandardScaler`.
- D. `RobustScaler`.

---

# 10. Linaje transversal del parcial en DBML

## Necesidad funcional

Gobierno de Datos necesita responder de dónde proviene cada salida, qué transformaciones la producen y qué productos se verían afectados si cambia una fuente. Este entregable cierra el parcial mostrando sus dos partes en un mismo diagrama, pero **sin crear dependencias ni cruces entre el flujo financiero y el flujo de clientes**.

> **Resultado funcional:** un diagrama como código que muestre las dependencias de tablas y columnas de todo el proyecto.

> **Ubicación en el parcial:** este es el cierre documental de las Partes I y II; no constituye una tercera parte ni solicita integrar sus datos.

Consulte la documentación de [Data Lineage de dbdiagram](https://docs.dbdiagram.io/data-lineage/) y escriba el linaje del proyecto usando sintaxis DBML. Puede comprobar el resultado en [dbdiagram.io](https://dbdiagram.io/home).

La **última celda Markdown del cuaderno** debe contener únicamente un bloque de código con lenguaje `dbml`. No entregue una imagen ni un enlace como sustituto del código.

El código debe cumplir estas condiciones:

1. Debe poder copiarse en dbdiagram.io y renderizarse sin errores.
2. Debe declarar exactamente estas cinco fuentes lógicas:
   - `src_customers_chinook`
   - `src_invoices_chinook`
   - `src_countries_json`
   - `src_cambios_vancouver_html`
   - `src_customers_csv`
3. Debe declarar exactamente estos ocho artefactos derivados:
   - `out_01_facturacion`
   - `out_02_paises_monedas`
   - `out_03_tasas`
   - `out_04_facturacion_cop`
   - `out_05_reporte_calidad`
   - `out_06_correlaciones`
   - `out_07_clientes_limpios`
   - `out_08_vista_minable`
4. Cada tabla debe incluir las columnas usadas como clave o como criterio de cruce en el parcial.
5. Use `Dep` para indicar que una tabla o columna se deriva de otra. La flecha debe ir desde la fuente hacia el artefacto derivado: `fuente -> salida`.
6. Use `Ref` únicamente para relaciones reales de clave foránea, como la relación entre facturas y clientes de Chinook. No use `Ref` para representar transformaciones.
7. Agregue una propiedad `note` a cada `Dep` para describir brevemente la transformación aplicada.
8. Incluya dependencias de tabla a tabla para mostrar los dos flujos completos:
   - Chinook + países + tasas → facturación consolidada en COP.
   - `Customers.csv` → reporte de calidad y correlaciones; `Customers.csv` → clientes limpios → vista minable.
9. Incluya al menos cinco dependencias de columna a columna para mostrar el origen de campos relevantes, entre ellos `invoice_id`, `customer_name`, `local_currency`, `total_cop` y `income_per_person_z`.
10. No declare ningún `Dep` ni `Ref` entre las fuentes o artefactos de la Parte I y los de la Parte II.

La celda final debe tener esta forma general:

````markdown
```dbml
Table nombre_tabla {
  campo tipo
}

Table salida {
  campo tipo
}

Dep: nombre_tabla -> salida [note: 'Descripción de la transformación']
Dep: nombre_tabla.campo -> salida.campo
```
````

El ejemplo anterior muestra únicamente la sintaxis de entrega; no constituye el diagrama solicitado.

---

# Rúbrica verificable

## Parte I — Consolidación de facturas en COP (22 puntos)

### Bloque 1 — 10 puntos

| Criterio | Puntos |
|---|---:|
| Descarga y carga correcta de los insumos | 1 |
| Consulta SQL y granularidad correcta | 5 |
| Contrato y exportación | 2 |
| R1 y representación del flujo financiero en el linaje DBML | 2 |

### Bloque 2 — 12 puntos

| Criterio | Puntos |
|---|---:|
| Normalización país-moneda | 3 |
| Extracción y homologación de tasas | 3 |
| Integración y conversión de moneda | 4 |
| Contratos, evidencias y R2 | 2 |

## Parte II — Calidad y preparación de clientes (28 puntos)

### Bloque 3 — 10 puntos

| Criterio | Puntos |
|---|---:|
| Reporte de calidad y reglas de dominio | 4 |
| Correlaciones sin diagonal ni identificador | 2 |
| Gráficos solicitados | 2 |
| Evidencias y R3 | 2 |

### Bloque 4 — 8 puntos

| Criterio | Puntos |
|---|---:|
| Imputación y filtros de dominio | 3 |
| Cálculo y aplicación de IQR | 3 |
| Contrato, exportación y evidencias | 2 |

### Bloque 5 — 10 puntos

| Criterio | Puntos |
|---|---:|
| `income_per_person` y escalamiento | 3 |
| Discretización de edad | 2 |
| Codificación categórica | 2 |
| Contrato y evidencias de la vista minable | 1.5 |
| R4, R5 y R6 | 1.5 |

**Total: 50 puntos.**

El linaje transversal se califica dentro de los criterios de las dos partes y no agrega puntos al total.

Un archivo ausente no puede recibir puntos por su contenido. Un archivo con nombre o esquema diferente pierde los puntos correspondientes al contrato de salida, aunque exista un resultado parecido en el cuaderno.

---

# Lista de verificación antes de entregar

- [ ] El cuaderno se ejecuta desde un entorno reiniciado sin intervención manual.
- [ ] Los cuatro insumos se descargan desde este repositorio.
- [ ] Existen exactamente ocho CSV dentro de `salidas/`.
- [ ] Los CSV no contienen índices de Pandas ni columnas adicionales.
- [ ] Las dimensiones coinciden con las publicadas.
- [ ] Todas las líneas `P2_` a `P5_` aparecen con el formato exacto.
- [ ] Los dos gráficos son visibles.
- [ ] La respuesta de la Parte I contiene únicamente `R1=` y `R2=`.
- [ ] La respuesta de la Parte II contiene únicamente `R3=` a `R6=`.
- [ ] Ningún cálculo ni cruce combina insumos de la Parte I con la Parte II.
- [ ] La última celda contiene el código DBML, separa las dos partes y se renderiza sin errores en dbdiagram.io.
- [ ] El notebook tiene todas sus salidas ejecutadas.
- [ ] El ZIP cumple el nombre y la estructura solicitados.

---
