# Cuestionario 6: Big Data — Búsqueda Semántica y Cloud Analytics

Este cuestionario evalúa los conceptos teóricos y prácticos sobre el procesamiento de datos no estructurados, vectorización (*embeddings*), bases de datos vectoriales (ChromaDB) y analítica distribuida en la nube con Google BigQuery, basados en la Tarea 6 y las presentaciones de clase.

**Instrucciones:** Seleccione la respuesta correcta. Al final, deberá adjuntar el enlace a su cuaderno de Colab.

---

### Preguntas Teóricas

**1. Al trabajar con documentos no estructurados (como PDFs o textos largos), ¿cuál es el propósito fundamental de segmentar el texto en fragmentos (*chunks*) con solapamiento (*overlap*) antes de generar embeddings?**
- [ ] A. Reducir el tamaño del archivo PDF para que ocupe menos espacio en disco.
- [ ] B. Evitar que las oraciones o ideas queden cortadas abruptamente en el límite del bloque, garantizando continuidad de contexto semántico a cambio de una duplicación controlada.
- [ ] C. Eliminar automáticamente los caracteres especiales y corregir la ortografía mediante el modelo de lenguaje.
- [ ] D. Convertir el texto no estructurado en una tabla relacional normalizada en tercera forma normal.

**2. En el contexto de bases de datos vectoriales e Information Retrieval, ¿qué representa matemáticamente un *embedding* de texto?**
- [ ] A. Una cadena de caracteres encriptada mediante una función hash criptográfica SHA-256.
- [ ] B. Un número entero que indica la posición del documento dentro del sistema de archivos.
- [ ] C. Un vector numérico denso en un espacio multidimensional donde la proximidad geométrica refleja la afinidad o similitud semántica del contenido.
- [ ] D. Una lista invertida de palabras clave que solo permite coincidencias exactas por término (*exact keyword matching*).

**3. ¿Cuál es el rol de un algoritmo de búsqueda aproximada de vecinos más cercanos como HNSW (*Hierarchical Navigable Small World*) en índices vectoriales?**
- [ ] A. Calcular de manera exhaustiva la distancia contra absolutamente todos los vectores de la base de datos sin omitir ninguno.
- [ ] B. Navegar una estructura de grafo por capas para encontrar candidatos altamente probables en tiempo sublineal, sacrificando una fracción mínima de precisión a cambio de una latencia significativamente menor.
- [ ] C. Comprimir los archivos PDF en formato binario para visualizarlos en la web.
- [ ] D. Traducir automáticamente las consultas de lenguaje natural a sentencias SQL.

**4. En arquitecturas modernas de Big Data, ¿cuál es la característica principal de un servicio como Google Cloud BigQuery frente a un sistema gestor relacional tradicional (RDBMS)?**
- [ ] A. Es un motor serverless con separación total de almacenamiento y cómputo que escala dinámicamente sobre miles de nodos para escanear terabytes o petabytes con consultas SQL distribuidas.
- [ ] B. Requiere aprovisionar y mantener manualmente servidores físicos y configurar índices B-Tree en cada tabla para poder consultar.
- [ ] C. Solo admite datos estructurados de menos de 1 GB de tamaño.
- [ ] D. Es un sistema transaccional OLTP optimizado para registrar inserciones individuales fila por fila a muy alta frecuencia.

---

### Preguntas Prácticas (Basadas en la Tarea 6)

**5. En el Ejercicio 1 de la Tarea 6, al indexar los chunks en ChromaDB, ¿por qué fue crucial almacenar metadatos como `documento`, `pagina` y `chunk_id` junto con los vectores?**
- [ ] A. Porque sin esos campos ChromaDB no permite crear una colección en memoria.
- [ ] B. Para habilitar la trazabilidad y verificabilidad de la información recuperada, permitiendo auditar la fuente original y reconstruir o actualizar el índice si el documento cambia.
- [ ] C. Para aumentar la velocidad del cálculo de la distancia coseno entre vectores.
- [ ] D. Para cifrar los embeddings antes de enviarlos a la memoria RAM.

**6. Al evaluar las consultas semánticas en ChromaDB en la Tarea 6, ¿qué métrica de similitud se utilizó para medir la cercanía entre el vector de la consulta y los fragmentos del documento?**
- [ ] A. Similitud Coseno (calculada a partir de la distancia coseno del espacio HNSW).
- [ ] B. Distancia de Manhattan ($L_1$).
- [ ] C. Coeficiente de correlación de Pearson.
- [ ] D. Distancia de Levenshtein entre caracteres.

**7. En el Ejercicio 2 con Google BigQuery (dataset de nombres de EE.UU.), ¿qué combinación de cláusulas SQL permitió determinar los 5 nombres más frecuentes agrupando por género y sumando los conteos anuales?**
- [ ] A. `WHERE name IS NOT NULL LIMIT 5`
- [ ] B. `GROUP BY name, gender ORDER BY total DESC LIMIT 5`
- [ ] C. `PARTITION BY name ORDER BY total ASC`
- [ ] D. `HAVING COUNT(*) = 5`

---

### Enlace de Entrega

**8. Pegue aquí el enlace público de su cuaderno de Google Colab:**
- Asegúrese de que tenga permisos configurados en **"Cualquier persona con el enlace"** en modo **Lector** (*Viewer*).
- Verifique que contenga las salidas ejecutadas con su propio PDF y la captura/respuesta del ejercicio de BigQuery.
