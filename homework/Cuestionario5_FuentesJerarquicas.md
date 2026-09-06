# Cuestionario 5: Fuentes Jerárquicas, APIs y Web Scraping

Este cuestionario evalúa los conceptos teóricos y prácticos sobre el manejo de fuentes de datos jerárquicas, interacciones con APIs, web scraping y bases de datos NoSQL como MongoDB, basados en la Tarea 5 y las presentaciones de clase.

**Instrucciones:** Seleccione la respuesta correcta. Al final, deberá adjuntar el enlace a su cuaderno de Colab.

---

### Preguntas Teóricas

**1. ¿Cuál es la principal diferencia entre almacenar datos en un modelo relacional versus un modelo documental (como JSON/MongoDB) en cuanto al manejo de relaciones de uno-a-muchos?**
- [ ] A. El modelo documental siempre obliga a separar los datos en distintas colecciones usando JOINs.
- [ ] B. El modelo documental permite anidar (embeber) los datos relacionados dentro de un mismo documento, evitando el costo computacional de múltiples JOINs al leer.
- [ ] C. El modelo relacional es el único que permite almacenar atributos que sean listas o arreglos.
- [ ] D. No existe diferencia en el acceso a los datos, ambos requieren indexar llaves foráneas para consultar datos relacionados.

**2. Al convertir un archivo con estructura jerárquica (JSON o XML) a un formato tabular (CSV o DataFrame), ¿cuál es la decisión principal y desafío analítico que debe abordarse?**
- [ ] A. El CSV limita la cantidad de datos y no permite guardar números.
- [ ] B. Los archivos jerárquicos no contienen nombres de campos.
- [ ] C. Al aplanar la estructura jerárquica se debe decidir la *granularidad* (qué representa una fila) y manejar los datos anidados que se repiten (explotarlos) o se pierden.
- [ ] D. Pandas no cuenta con herramientas para leer archivos JSON, requiriendo conversiones manuales a texto.

**3. En las interacciones con APIs usando la librería `requests` en Python, ¿cuál es el propósito de utilizar el método `raise_for_status()` tras recibir una respuesta?**
- [ ] A. Acelera la descarga de los datos saltando el límite de tasa de la API.
- [ ] B. Genera una excepción explícita si la API responde con un código de error HTTP (como 401 o 404), evitando que el programa asuma éxito y falle más adelante al procesar la respuesta.
- [ ] C. Convierte automáticamente la respuesta en un DataFrame estructurado.
- [ ] D. Asegura que la API envíe la respuesta siempre en formato XML.

**4. Cuando se utiliza XPath o JSONPath para consultar datos, ¿qué operación conceptual común comparten ambos lenguajes?**
- [ ] A. Convertir bases de datos relacionales en grafos.
- [ ] B. Escribir sentencias SQL de tipo INSERT y UPDATE.
- [ ] C. Navegar la jerarquía en árbol del documento utilizando rutas para seleccionar elementos o atributos específicos sin procesar todo el archivo.
- [ ] D. Comprimir el tamaño de los documentos JSON y XML antes de enviarlos por red.

---

### Preguntas Prácticas (Basadas en la Tarea 5)

**5. En la Tarea 5, al utilizar MongoDB para analizar naufragios cercanos o áreas de estudio en la Costa Este, ¿qué operadores geoespaciales se emplearon sobre los objetos GeoJSON?**
- [ ] A. `$near` y `$geoWithin`.
- [ ] B. `$lookup` y `$match`.
- [ ] C. `$group` y `$project`.
- [ ] D. `LIMIT` y `ORDER BY`.

**6. Al realizar web scraping de tasas de cambio utilizando la librería de Pandas (Tarea 5), ¿qué ventaja aporta el método `pd.read_html()`?**
- [ ] A. Escribe automáticamente los datos recopilados de vuelta a la página web.
- [ ] B. Identifica y extrae directamente las estructuras tabulares (`<table>`, `<tr>`, `<td>`) de una respuesta HTML, devolviéndolas como una lista de DataFrames listos para analizar.
- [ ] C. Se salta automáticamente las protecciones contra bots (como CAPTCHAs) y controles de `robots.txt`.
- [ ] D. Permite visualizar de forma interactiva la página web dentro de Jupyter.

**7. Al procesar la colección de Airbnb en MongoDB, se le solicitó proyectar y limitar resultados, excluyendo el campo `_id`. ¿Cuál es la forma correcta de indicar en una proyección que un campo NO debe ser incluido en la salida?**
- [ ] A. Asignando el valor `0` al campo en el diccionario de proyección (ej. `{"_id": 0}`).
- [ ] B. Usando la palabra clave `DELETE`.
- [ ] C. Filtrando el campo después de descargar los datos en Pandas usando `drop()`.
- [ ] D. Haciendo un `$group` sin agregar el campo.

---

### Enlace de Entrega

**8. Pegue a continuación el enlace a su cuaderno único de Colab de la Tarea 5 (asegúrese de que los permisos estén en "Cualquier persona con el enlace puede leer"):**

*(Espacio para enlace)*
