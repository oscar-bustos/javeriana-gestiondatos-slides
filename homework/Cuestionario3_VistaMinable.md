# Cuestionario 3: Preparación y Generación de Vistas Minables

Este cuestionario evalúa los conceptos teóricos de transformación de variables (escalamiento, codificación categórica, transformación logarítmica, discretización) y balanceo de clases vistos en clase y en las lecturas, así como los hallazgos prácticos de la Tarea 3 sobre el dataset del **Titanic** (`titanic.csv`).

**Instrucciones:** Seleccione la respuesta correcta. Al final, deberá adjuntar el enlace a su cuaderno de Google Colab.

---

### Preguntas Teóricas

**1. ¿Por qué los algoritmos basados en optimización por gradiente (como Redes Neuronales o Regresión Logística) o basados en cálculo de distancias (como KNN y SVM) requieren que las variables numéricas estén en una escala homogénea (estandarizadas o normalizadas)?**
- [ ] A. Porque las variables con magnitudes numéricas grandes (ej. tarifas o salarios) dominarán artificialmente las funciones de coste y el cálculo de distancias euclidianas, reduciendo la influencia de variables con rangos pequeños (ej. edad o tamaño familiar).
- [ ] B. Porque las redes neuronales solo pueden procesar números enteros positivos entre 0 y 10.
- [ ] C. Porque los modelos basados en gradientes no admiten variables continuas, únicamente variables booleanas.
- [ ] D. Porque el escalamiento elimina de forma automática los valores nulos y registros duplicados.

**2. ¿Cuál es la principal diferencia conceptual y práctica entre `StandardScaler` (Z-Score) y `MinMaxScaler` (Normalización)?**
- [ ] A. `StandardScaler` transforma los datos a un rango rígido $[0, 1]$, mientras que `MinMaxScaler` centra los datos con media $\mu = 0$ y varianza $\sigma^2 = 1$.
- [ ] B. `StandardScaler` centra los datos en media 0 y varianza 1 (sin acotar un rango mínimo/máximo fijo), mientras que `MinMaxScaler` comprime los datos al intervalo $[0, 1]$, siendo este último altamente sensible a valores atípicos extremos.
- [ ] C. `StandardScaler` solo se puede aplicar a variables de texto y `MinMaxScaler` a variables booleanas.
- [ ] D. Ambos transformadores producen matrices idénticas independientemente de los datos.

**3. Si se tiene una variable con marcada asimetría positiva (*cola larga* o *heavy-tailed distribution*), como `Fare` o los ingresos de una persona, ¿por qué es recomendable aplicar una transformación logarítmica ($\log(1+x)$) antes de entrenar un modelo lineal o de distancias?**
- [ ] A. Porque convierte efectos multiplicativos en aditivos, estabiliza la varianza y comprime los valores extremos acercando la distribución a una forma más simétrica o acampanada.
- [ ] B. Porque transforma automáticamente las variables continuas en variables categóricas nominales.
- [ ] C. Porque duplica la cantidad de registros en el dataset evitando el sobreajuste.
- [ ] D. Porque elimina la necesidad de separar los datos en conjuntos de entrenamiento y prueba.

**4. ¿Por qué en variables categóricas nominales (sin jerarquía intrínseca, como `Sex` o `Embarked`) se debe utilizar One-Hot Encoding en lugar de asignar números secuenciales arbitrarios (ej. C=1, Q=2, S=3) para modelos algebraicos o de gradiente?**
- [ ] A. Porque la asignación de números secuenciales impone un orden y unas distancias numéricas ficticias que el algoritmo interpretará erróneamente (ej. asumir que $S > C$ o que la diferencia entre $Q$ y $C$ es unitaria).
- [ ] B. Porque One-Hot Encoding reduce a la mitad el número total de columnas del DataFrame.
- [ ] C. Porque los modelos algebraicos fallan si reciben matrices de ceros y unos.
- [ ] D. Porque la asignación ordinal requiere siempre un número impar de categorías.

**5. Al utilizar `KBinsDiscretizer` de Scikit-Learn con `strategy='quantile'` frente a `strategy='uniform'`, ¿cuál es la principal ventaja de la estrategia `'quantile'` en variables con distribuciones sesgadas?**
- [ ] A. `'quantile'` genera intervalos de igual ancho numérico, lo que garantiza que no haya saltos.
- [ ] B. `'quantile'` distribuye los puntos de corte de forma que cada contenedor (*bin*) tenga aproximadamente la misma cantidad de registros (frecuencia balanceada), evitando que un solo intervalo concentre el 90%+ de las observaciones.
- [ ] C. `'quantile'` solo admite variables con más de 1,000,000 de registros.
- [ ] D. `'quantile'` crea automáticamente una columna de tipo texto sin números.

**6. ¿Qué problema metodológico previene el uso de `ColumnTransformer` y `Pipeline` en Scikit-Learn al realizar el preprocesamiento de datos?**
- [ ] A. La fuga de datos (*Data Leakage*), garantizando que los parámetros de transformación (`fit` de media, varianza, cuantiles o categorías) se aprendan exclusivamente sobre el conjunto de entrenamiento y se apliquen sin recalcular sobre test o producción.
- [ ] B. El consumo de memoria RAM al forzar a que todos los datos se procesen como enteros de 8 bits.
- [ ] C. La necesidad de contar con una variable objetivo (`target`) para entrenar modelos no supervisados.
- [ ] D. La generación de valores nulos durante la ejecución de los algoritmos.

---

### Preguntas Prácticas (Basadas en la Tarea 3 - Titanic)

**7. En el Ejercicio 1, al crear la variable sintética `FamilySize = SibSp + Parch + 1`, ¿qué concepto clave de la preparación de datos (*Data Massaging*) se está aplicando y cuál es su utilidad?**
- [ ] A. Normalización Min-Max, para reducir el rango de edad a valores decimales.
- [ ] B. Construcción de Atributos (*Attribute Construction*), fusionando variables crudas correlacionadas en un indicador único con mayor significado de negocio y capacidad explicativa sobre la supervivencia del grupo familiar.
- [ ] C. Anonimización por enmascaramiento de datos personales.
- [ ] D. Discretización no uniforme de series temporales.

**8. En la Vista para Redes Neuronales (Ejercicio 2), al procesar la variable categórica `Embarked` con `OneHotEncoder(drop='first', sparse_output=False)`: si `Embarked` tiene 3 categorías originales (`'C'`, `'Q'`, `'S'`), ¿cuántas columnas nuevas se incorporan a la matriz resultante?**
- [ ] A. 3 columnas (`Embarked_C`, `Embarked_Q`, `Embarked_S`).
- [ ] B. 2 columnas (por ejemplo `Embarked_Q` y `Embarked_S`), ya que la categoría de referencia `'C'` queda codificada implícitamente cuando ambas columnas valen 0, evitando colinealidad exacta (*dummy variable trap*).
- [ ] C. 1 columna con valores continuos calculados mediante la media de supervivencia.
- [ ] D. 0 columnas, ya que `OneHotEncoder` borra las variables con más de 2 categorías.

**9. Al examinar la variable objetivo `Survived` en el dataset del Titanic (~61.6% no sobrevivientes vs ~38.4% sobrevivientes) y aplicar una técnica de sobremuestreo como `SMOTE` en la vista minable, ¿qué cambio se observa en la distribución final de las clases?**
- [ ] A. Las clases quedan perfectamente equilibradas (50% de clase 0 y 50% de clase 1), mediante la generación sintética de observaciones representativas en el espacio de características de los sobrevivientes.
- [ ] B. Se eliminan aleatoriamente todas las filas de la clase 0 hasta dejar solo el 10% del dataset original.
- [ ] C. La variable `Survived` se convierte en una variable numérica continua entre 0 y 1.
- [ ] D. El número total de filas del dataset disminuye en un 50%.

**10. Al comparar la vista minable para Redes Neuronales (`df_redes`) frente a la vista para Árboles de Decisión (`df_arboles`), ¿cuál es la diferencia fundamental en la representación de variables continuas como `Age` y `Fare`?**
- [ ] A. En `df_redes` las variables se conservan continuas, estandarizadas a media 0 y varianza 1 (con transformación $\log$ en `Fare`), mientras que en `df_arboles` están particionadas en contenedores discretos enteros (`n_bins=4`) facilitando reglas de decisión cualitativas.
- [ ] B. En `df_redes` las variables contienen únicamente texto y en `df_arboles` únicamente valores booleanos.
- [ ] C. `df_redes` contiene 1 sola fila y `df_arboles` contiene 10,000 filas.
- [ ] D. Ambas vistas son idénticas al archivo original `titanic.csv` sin ninguna transformación.

---

### Enlace de Entrega

**11. Pegue a continuación el enlace a su cuaderno único de Google Colab (asegúrese de que los permisos estén configurados en "Cualquier persona con el enlace" en modo "Lector"):**

*(Espacio para enlace)*
