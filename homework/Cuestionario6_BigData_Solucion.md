# Solución - Cuestionario 6: Big Data — Búsqueda Semántica y Cloud Analytics

**1. Al trabajar con documentos no estructurados (como PDFs o textos largos), ¿cuál es el propósito fundamental de segmentar el texto en fragmentos (*chunks*) con solapamiento (*overlap*) antes de generar embeddings?**
- [x] B. Evitar que las oraciones o ideas queden cortadas abruptamente en el límite del bloque, garantizando continuidad de contexto semántico a cambio de una duplicación controlada.

**2. En el contexto de bases de datos vectoriales e Information Retrieval, ¿qué representa matemáticamente un *embedding* de texto?**
- [x] C. Un vector numérico denso en un espacio multidimensional donde la proximidad geométrica refleja la afinidad o similitud semántica del contenido.

**3. ¿Cuál es el rol de un algoritmo de búsqueda aproximada de vecinos más cercanos como HNSW (*Hierarchical Navigable Small World*) en índices vectoriales?**
- [x] B. Navegar una estructura de grafo por capas para encontrar candidatos altamente probables en tiempo sublineal, sacrificando una fracción mínima de precisión a cambio de una latencia significativamente menor.

**4. En arquitecturas modernas de Big Data, ¿cuál es la característica principal de un servicio como Google Cloud BigQuery frente a un sistema gestor relacional tradicional (RDBMS)?**
- [x] A. Es un motor serverless con separación total de almacenamiento y cómputo que escala dinámicamente sobre miles de nodos para escanear terabytes o petabytes con consultas SQL distribuidas.

**5. En el Ejercicio 1 de la Tarea 6, al indexar los chunks en ChromaDB, ¿por qué fue crucial almacenar metadatos como `documento`, `pagina` y `chunk_id` junto con los vectores?**
- [x] B. Para habilitar la trazabilidad y verificabilidad de la información recuperada, permitiendo auditar la fuente original y reconstruir o actualizar el índice si el documento cambia.

**6. Al evaluar las consultas semánticas en ChromaDB en la Tarea 6, ¿qué métrica de similitud se utilizó para medir la cercanía entre el vector de la consulta y los fragmentos del documento?**
- [x] A. Similitud Coseno (calculada a partir de la distancia coseno del espacio HNSW).

**7. En el Ejercicio 2 con Google BigQuery (dataset de nombres de EE.UU.), ¿qué combinación de cláusulas SQL permitió determinar los 5 nombres más frecuentes agrupando por género y sumando los conteos anuales?**
- [x] B. `GROUP BY name, gender ORDER BY total DESC LIMIT 5`
