# Cuestionario 4: Datos Tabulares con Pandas y SQLite (Solución)

Este cuestionario evalúa los conceptos teóricos y prácticos sobre el manejo de bases de datos relacionales desde Python utilizando SQLite y Pandas, basados en la Tarea 4 (Base de datos Chinook).

**Instrucciones:** Seleccione la respuesta correcta. Al final, deberá adjuntar el enlace a su cuaderno de Colab.

---

### Preguntas Teóricas

**1. Según los conceptos del ciclo de vida de los datos, ¿qué propósito principal cumple el área de "Serving" (Consumo) dentro de una arquitectura analítica?**
- [ ] A. Generar los datos en los sistemas operacionales mediante microservicios.
- [ ] B. Transformar los datos crudos ejecutando complejas sentencias DDL y DML.
- [x] C. Entregar los datos transformados a analistas, modelos de Machine Learning y herramientas de Business Intelligence.
- [ ] D. Almacenar los datos de acceso esporádico (Cold Data) en el nivel más económico posible.

**2. En el ecosistema de la ingeniería de datos, ¿qué ventaja ofrece el paradigma de "Data Mesh" frente a un "Data Warehouse" centralizado tradicional?**
- [ ] A. Obliga a que toda la organización almacene sus datos en un único servidor monolítico.
- [x] B. Promueve un modelo descentralizado donde cada dominio es dueño de sus datos, tratándolos como un producto.
- [ ] C. Utiliza exclusivamente archivos CSV para el intercambio de información entre departamentos.
- [ ] D. Centraliza todas las transformaciones en un solo equipo de ingenieros para mayor control.

**3. ¿Qué ventaja principal ofrecen formatos columnares como Parquet o Feather frente al tradicional CSV al trabajar con grandes volúmenes de datos tabulares?**
- [ ] A. Son formatos de texto plano, lo que permite abrirlos en cualquier bloc de notas sin necesidad de librerías adicionales.
- [x] B. Permiten una mayor compresión en disco y tiempos de lectura/escritura más rápidos, al almacenar los datos por columnas en lugar de filas.
- [ ] C. Son los únicos formatos que soportan exportación desde Pandas.
- [ ] D. No requieren el uso de la librería Pandas para ser manipulados en Python.

**4. ¿Cuál es un beneficio clave de filtrar y agregar grandes conjuntos de datos utilizando el motor de una base de datos (mediante consultas SQL) antes de cargarlos en memoria con Pandas?**
- [ ] A. Ninguno, Pandas siempre procesa grandes volúmenes de datos más rápido que un motor de base de datos especializado.
- [x] B. Permite aprovechar la indexación de la base de datos y reduce significativamente el consumo de memoria RAM de Python.
- [ ] C. Garantiza que los gráficos generados posteriormente en Python tengan mejor resolución.
- [ ] D. Evita tener que usar librerías externas de Python.

**5. En el contexto de Pandas, ¿qué representa fundamentalmente la estructura de datos `DataFrame`?**
- [ ] A. Un arreglo unidimensional, equivalente a una lista simple, diseñado exclusivamente para números.
- [ ] B. Un conector de red que mantiene una sesión activa con el servidor de base de datos.
- [x] C. Una estructura de datos bidimensional y tabular, compuesta por filas y columnas, similar a una tabla relacional.
- [ ] D. Un formato de archivo comprimido en disco diseñado para reemplazar a los archivos Parquet.

**6. Al exportar un DataFrame a un archivo CSV estándar y luego volverlo a importar, ¿cuál es un problema común asociado con los tipos de datos?**
- [ ] A. El archivo CSV encripta los datos, requiriendo credenciales adicionales para su lectura.
- [x] B. Se pierden los tipos de datos nativos (como fechas o categorías) y Pandas debe inferirlos de nuevo, a menudo tratándolos como texto.
- [ ] C. Todas las columnas numéricas se convierten automáticamente en variables de texto irreversibles.
- [ ] D. El archivo CSV no permite almacenar números decimales, redondeándolos a enteros.

---

### Preguntas Prácticas (Basadas en la Tarea 4)


**7. Al analizar las transacciones de ventas (como la tabla `invoice` de la base de datos Chinook) desde la perspectiva del Modelado Dimensional (Kimball), ¿qué tipo de estructura representa esta tabla?**
- [ ] A. Una Tabla de Dimensión, porque contiene los atributos descriptivos del cliente y su historial.
- [x] B. Una Tabla de Hechos (Fact Table), porque almacena las métricas cuantitativas (como el monto total) y las llaves para conectarse al contexto.
- [ ] C. Una Tabla de Metadatos de Referencia.
- [ ] D. Una dimensión lentamente cambiante (SCD Tipo 2).

**8. En el Ejercicio 2, al analizar los ingresos en diferentes días de la semana, ¿qué descubrimiento general suele encontrarse al observar los patrones de compra en una base de datos comercial?**
- [ ] A. Todos los días tienen exactamente la misma cantidad de ventas sin importar el tipo de negocio.
- [ ] B. Los fines de semana (Sábado y Domingo) siempre tienen cero ventas.
- [x] C. Suele haber variaciones en las ventas dependiendo del día de la semana, lo cual es útil para identificar patrones de comportamiento del cliente.
- [ ] D. Los datos de las fechas están incompletos y no se puede realizar el análisis por día.


**9. De acuerdo con los hallazgos del Ejercicio 3 al exportar a distintos formatos, ¿qué formato resulta típicamente ser el más eficiente (menos pesado en disco) para almacenar DataFrames grandes en comparación con un archivo de texto como CSV?**
- [ ] A. Excel (.xlsx)
- [x] B. Parquet o Feather
- [ ] C. CSV
- [ ] D. JSON

---

### Enlace de Entrega

**10. Pegue a continuación el enlace a su cuaderno único de Colab de la Tarea 4 (asegúrese de que los permisos estén en "Cualquier persona con el enlace puede leer"):**

*(Espacio para enlace)*
