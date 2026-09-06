# Solución - Cuestionario 5: Fuentes Jerárquicas, APIs y Web Scraping

**1. ¿Cuál es la principal diferencia entre almacenar datos en un modelo relacional versus un modelo documental (como JSON/MongoDB) en cuanto al manejo de relaciones de uno-a-muchos?**
- [x] B. El modelo documental permite anidar (embeber) los datos relacionados dentro de un mismo documento, evitando el costo computacional de múltiples JOINs al leer.

**2. Al convertir un archivo con estructura jerárquica (JSON o XML) a un formato tabular (CSV o DataFrame), ¿cuál es la decisión principal y desafío analítico que debe abordarse?**
- [x] C. Al aplanar la estructura jerárquica se debe decidir la *granularidad* (qué representa una fila) y manejar los datos anidados que se repiten (explotarlos) o se pierden.

**3. En las interacciones con APIs usando la librería `requests` en Python, ¿cuál es el propósito de utilizar el método `raise_for_status()` tras recibir una respuesta?**
- [x] B. Genera una excepción explícita si la API responde con un código de error HTTP (como 401 o 404), evitando que el programa asuma éxito y falle más adelante al procesar la respuesta.

**4. Cuando se utiliza XPath o JSONPath para consultar datos, ¿qué operación conceptual común comparten ambos lenguajes?**
- [x] C. Navegar la jerarquía en árbol del documento utilizando rutas para seleccionar elementos o atributos específicos sin procesar todo el archivo.

**5. En la Tarea 5, al utilizar MongoDB para analizar naufragios cercanos o áreas de estudio en la Costa Este, ¿qué operadores geoespaciales se emplearon sobre los objetos GeoJSON?**
- [x] A. `$near` y `$geoWithin`.

**6. Al realizar web scraping de tasas de cambio utilizando la librería de Pandas (Tarea 5), ¿qué ventaja aporta el método `pd.read_html()`?**
- [x] B. Identifica y extrae directamente las estructuras tabulares (`<table>`, `<tr>`, `<td>`) de una respuesta HTML, devolviéndolas como una lista de DataFrames listos para analizar.

**7. Al procesar la colección de Airbnb en MongoDB, se le solicitó proyectar y limitar resultados, excluyendo el campo `_id`. ¿Cuál es la forma correcta de indicar en una proyección que un campo NO debe ser incluido en la salida?**
- [x] A. Asignando el valor `0` al campo en el diccionario de proyección (ej. `{"_id": 0}`).
