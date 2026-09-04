# Índice de contenidos de las presentaciones

Este inventario resume el propósito, el recorrido temático y el patrón pedagógico de los archivos Quarto del curso. Se usa como guía para revisar continuidad, repeticiones y oportunidades de conversación con el público.

## Mapa general

| Presentación | Propósito | Recorrido principal | Patrón pedagógico |
|---|---|---|---|
| `comprension_datos` | Introducir el curso, CRISP-DM y EDA | Logística → casos de negocio → CRISP-DM → Titanic → EDA con Python | Casos reconocibles, pregunta, revelación y aplicación |
| `limpieza_datos` | Diagnosticar y corregir problemas de calidad | Repaso → niveles de limpieza → columnas → formato → faltantes → atípicos → observabilidad | Problema visible, clasificación, método y reto aplicado |
| `vista_minable` | Transformar datos limpios para modelamiento | Motivación → escalamiento → codificación → ingeniería de variables → ruido → privacidad → pipelines | Paradojas y preguntas cuantitativas antes de cada técnica |
| `extraccion_datos_tabular` | Ubicar las fuentes tabulares en el ciclo de datos | Lifecycle → metadatos → arquitectura → storage → fuentes → ingestión → SQL → serving | Recorrido de arquitectura con ejemplos y ejercicios |
| `fuentes_jerarquicas` | Mostrar fuentes que no nacen como tablas | Más allá del CSV → árboles → XML → JSON/API → MongoDB → HTML → normalización | Caso conductor, preguntas al público y decisiones de extracción |
| `big_data_sin_estructura` | Introducir variedad y datos no estructurados | Big Data → impulsores → arquitecturas → texto/PDF → embeddings → imágenes | Motivación por casos y demostraciones técnicas |
| `big_data_grandes_volumenes` | Explicar la evolución de arquitecturas por escala | 4V → décadas → RDBMS → DW → Hadoop → Spark → serverless/lakehouse | Narrativa histórica de problema, límite y nueva solución |

## 1. Comprensión de datos

Archivo: `quarto/comprension_datos/index.qmd`

- Presentación, reglas, bibliografía y cronograma.
- Motivación mediante casos Walmart, Target, Capital One, Pokémon GO y Netflix.
- CRISP-DM: negocio, datos, preparación, modelamiento, evaluación y despliegue.
- Caso Titanic y entorno Google Colab.
- Carga, limpieza inicial y análisis univariado y bivariado.
- Flujo de EDA y perfilamiento automatizado.

**Conversación dominante:** “¿qué decisión tomaría?” → hipótesis del público → caso real → concepto formal.

## 2. Limpieza de datos

Archivo: `quarto/limpieza_datos/index.qmd`

- Calidad de datos y actividades de limpieza.
- Nivel I: estructura de la tabla y selección de atributos.
- Nivel II: formato, granularidad y reformulación.
- Nivel III: faltantes, mecanismos MCAR/MAR/MNAR y valores atípicos.
- Funciones de Pandas y herramientas de observabilidad.

**Conversación dominante:** detectar el síntoma, preguntar si realmente es un error y elegir tratamiento según el contexto.

## 3. Vista minable

Archivo: `quarto/vista_minable/index.qmd`

- Por qué limpiar no basta y qué es una vista minable.
- Normalización, estandarización y escalamiento robusto.
- Conversión categórica, cardinalidad y codificación ordinal.
- Discretización e ingeniería de características.
- Transformaciones temporales, logarítmicas y tratamiento de ruido.
- Balanceo, privacidad y pipelines reproducibles.

**Conversación dominante:** paradoja o contraejemplo → pregunta → explicación visual → implementación.

## 4. Extracción de datos tabulares

Archivo: `quarto/extraccion_datos_tabular/index.qmd`

- Ciclo de vida y gestión de datos.
- Metadatos de negocio, técnicos, operacionales y de referencia.
- Data Warehouse, ELT, Data Marts y Data Mesh.
- Capacidad, costo, velocidad y temperatura del almacenamiento.
- Sistemas fuente, IoT, ACID y fuentes tabulares y jerárquicas.
- Push/pull, CDC, batch, streaming, SQL y serving.

**Conversación dominante:** seguir el dato desde su generación hasta el consumo analítico.

## 5. Fuentes jerárquicas

Archivo: `quarto/fuentes_jerarquicas/index.qmd`

- Diferencia entre fuente, formato y método de acceso.
- Caso conductor: preparar un viaje usando XML, API JSON, MongoDB y HTML.
- Mapa conceptual de bases relacionales, documentales, clave–valor, columna ancha y grafos.
- Árboles, rutas, granularidad y normalización.
- XML: elementos, atributos, namespaces y XPath.
- JSON y APIs: objetos, arreglos, contrato HTTP, paginación y contingencia.
- MongoDB: documentos BSON, filtros, proyección, orden y consultas geográficas.
- HTML: DOM, selectores, tablas, BeautifulSoup y scraping responsable.
- Integración final hacia datasets tabulares y Taller 5.

**Conversación dominante:** “¿dónde está el dato y qué representa una fila?” → navegar → extraer → normalizar → validar.

## 6. Big Data sin estructura

Archivo: `quarto/big_data_sin_estructura/index.qmd`

- Volumen, variedad y velocidad.
- Evolución de BI, ETL, Data Warehouse y Data Lake.
- Ecosistemas AWS y GCP.
- Información no estructurada, NLP, PDF y n-gramas.
- Embeddings, imágenes, similitud e implementación con Chroma.

**Conversación dominante:** una fuente deja de caber en filas y columnas; se muestra qué representación permite analizarla.

## 7. Big Data y grandes volúmenes

Archivo: `quarto/big_data_grandes_volumenes/index.qmd`

- Las 4V y fuentes masivas de datos.
- Evolución desde RDBMS monolítico hasta arquitecturas distribuidas.
- Data Warehouse, Hadoop/HDFS, nube, Spark y formatos columnares.
- Streaming, Lambda, Kappa, medallón y serverless.
- Comparación de ecosistemas productivos actuales.

**Conversación dominante:** cada década resuelve el cuello de botella dejado por la arquitectura anterior.

## Criterios comunes para futuras revisiones

1. Abrir cada bloque con una decisión o pregunta, no con una definición.
2. Dar tiempo para que el público formule una hipótesis antes de revelar la respuesta.
3. Explicar **por qué** existe una técnica y **para qué** decisión sirve.
4. Mantener un caso conductor que conecte conceptos aislados.
5. Cerrar cada bloque con una evidencia observable o una comprobación.
6. Respetar el máximo visual de 11–12 líneas por diapositiva.
