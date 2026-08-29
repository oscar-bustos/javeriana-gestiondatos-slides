# Solucionario - Cuestionario 3: Preparación y Generación de Vistas Minables

**Asignatura:** Gestión de Datos  
**Institución:** Pontificia Universidad Javeriana  
**Departamento:** Departamento de Ingeniería de Sistemas  
**Documento:** Guía de Respuestas y Justificaciones Pedagógicas  

---

## 📋 Resumen de Respuestas

| # | Pregunta / Concepto | Respuesta Correcta | Tema de la Clase |
| :---: | :--- | :---: | :--- |
| **1** | Escalamiento en modelos de gradiente y distancia | **A** | Escalamiento de Atributos & Paradoja de Magnitud |
| **2** | `StandardScaler` (Z-Score) vs `MinMaxScaler` | **B** | Normalización vs Estandarización |
| **3** | Transformación Logarítmica ($\log(1+x)$) | **A** | Transformación Log y Colas Pesadas |
| **4** | One-Hot Encoding vs Codificación Ordinal Arbitraria | **A** | Conversión Categórico-Numérico (Nominales) |
| **5** | `KBinsDiscretizer` (`quantile` vs `uniform`) | **B** | Discretización y Puntos de Corte |
| **6** | Prevención de *Data Leakage* con Pipelines | **A** | Integración y Pipelines con Scikit-Learn |
| **7** | `FamilySize` e Ingeniería de Características | **B** | Construcción de Atributos (*Data Massaging*) |
| **8** | `OneHotEncoder(drop='first')` en `Embarked` | **B** | Codificación Dummy ($K-1$ columnas) |
| **9** | Efecto de `SMOTE` en la variable `Survived` | **A** | Balanceo de Clases (Sampling Sintético) |
| **10** | Diferencia estructural entre `df_redes` y `df_arboles` | **A** | Vistas Minables Diferenciadas por Algoritmo |

---

## 📚 Justificación Detallada por Pregunta

### Sección Teórica

#### **1. ¿Por qué los algoritmos basados en optimización por gradiente o distancias euclidianas requieren variables en una escala homogénea?**
- **Respuesta Correcta:** **[X] A. Porque las variables con magnitudes numéricas grandes (ej. tarifas o salarios) dominarán artificialmente las funciones de coste y el cálculo de distancias euclidianas, reduciendo la influencia de variables con rangos pequeños (ej. edad o tamaño familiar).**
- 💡 **Justificación:** 
  - En modelos de distancia (KNN, K-Means), una diferencia de \$100 dólares en `Fare` opacaría completamente una diferencia de 2 años en `Age` si no se escalan.
  - En optimización por gradiente (Redes Neuronales, Regresión Logística), las escalas dispares generan curvas de nivel elípticas muy alargadas que provocan oscilaciones lentas y dificultan la convergencia.
- ❌ **Distractores:** B es falso (las redes operan con reales continuos); C es falso (admiten continuas); D es falso (el escalamiento no imputa nulos ni elimina duplicados).

---

#### **2. ¿Cuál es la principal diferencia conceptual y práctica entre `StandardScaler` y `MinMaxScaler`?**
- **Respuesta Correcta:** **[X] B. `StandardScaler` centra los datos en media 0 y varianza 1 (sin acotar un rango mínimo/máximo fijo), mientras que `MinMaxScaler` comprime los datos al intervalo $[0, 1]$, siendo este último altamente sensible a valores atípicos extremos.**
- 💡 **Justificación:**
  - `StandardScaler` aplica $z = \frac{x - \mu}{\sigma}$. Permite valores positivos y negativos fuera de $[-3, 3]$ y es más robusto a outliers moderados.
  - `MinMaxScaler` aplica $x' = \frac{x - x_{min}}{x_{max} - x_{min}}$. Si existe un outlier extremo (ej. un pasaje de \$512 cuando la mayoría pagó \$10), todos los registros normales quedan aplastados en un micro-rango cercano a 0.
- ❌ **Distractores:** A invierte las fórmulas; C y D contienen afirmaciones erróneas sobre tipos de datos y equivalencia.

---

#### **3. ¿Por qué es recomendable aplicar una transformación logarítmica ($\log(1+x)$) a variables con marcada asimetría positiva (*cola larga*)?**
- **Respuesta Correcta:** **[X] A. Porque convierte efectos multiplicativos en aditivos, estabiliza la varianza y comprime los valores extremos acercando la distribución a una forma más simétrica o acampanada.**
- 💡 **Justificación:** La función logarítmica contrae drásticamente las diferencias en el extremo superior (la diferencia entre 100 y 1,000 en escala log es igual a la diferencia entre 10 y 100), facilitando que modelos lineales capturen relaciones proporcionales.
- ❌ **Distractores:** B, C y D son conceptualmente incorrectos respecto a la naturaleza matemática de la función logaritmo.

---

#### **4. ¿Por qué en variables categóricas nominales (`Sex`, `Embarked`) se debe utilizar One-Hot Encoding en lugar de asignar números secuenciales arbitrarios (C=1, Q=2, S=3)?**
- **Respuesta Correcta:** **[X] A. Porque la asignación de números secuenciales impone un orden y unas distancias numéricas ficticias que el algoritmo interpretará erróneamente (ej. asumir que $S > C$ o que la diferencia entre $Q$ y $C$ es unitaria).**
- 💡 **Justificación:** Los modelos algebraicos y de gradiente asumen que los números representan magnitudes en una recta real. Asignar $C=1, Q=2, S=3$ obligaría al modelo a calcular gradientes asumiendo que Southampton es "el triple" de Cherburgo, introduciendo un sesgo arbitrario inexistente en el dominio.
- ❌ **Distractores:** B es falso (One-Hot aumenta columnas); C y D son falsedades operativas.

---

#### **5. Al utilizar `KBinsDiscretizer` con `strategy='quantile'` frente a `strategy='uniform'`, ¿cuál es la principal ventaja en variables sesgadas?**
- **Respuesta Correcta:** **[X] B. `'quantile'` distribuye los puntos de corte de forma que cada contenedor (*bin*) tenga aproximadamente la misma cantidad de registros (frecuencia balanceada), evitando que un solo intervalo concentre el 90%+ de las observaciones.**
- 💡 **Justificación:**
  - `strategy='uniform'` (*Equal-Width*) divide el rango $[x_{min}, x_{max}]$ en $k$ partes iguales en ancho. En variables con cola larga (como `Fare`), el 90% de los datos cae en el primer bin y los demás quedan casi vacíos.
  - `strategy='quantile'` (*Equal-Frequency*) ajusta los puntos de corte en los percentiles (ej. cuartiles: 25%, 50%, 75%), garantizando que cada contenedor tenga el mismo número de observaciones.
- ❌ **Distractores:** A describe `'uniform'`, no `'quantile'`; C y D son incorrectos.

---

#### **6. ¿Qué problema metodológico previene el uso de `ColumnTransformer` y `Pipeline` en Scikit-Learn?**
- **Respuesta Correcta:** **[X] A. La fuga de datos (*Data Leakage*), garantizando que los parámetros de transformación (`fit` de media, varianza, cuantiles o categorías) se aprendan exclusivamente sobre el conjunto de entrenamiento y se apliquen sin recalcular sobre test o producción.**
- 💡 **Justificación:** Si se ejecuta `.fit_transform()` sobre la totalidad del DataFrame antes de hacer la partición, la media y desviación estándar de los datos de prueba se habrán filtrado en el preprocesamiento de entrenamiento, produciendo métricas de evaluación artificialmente optimistas.
- ❌ **Distractores:** B, C y D no corresponden al propósito metodológico del encapsulamiento en pipelines.

---

### Sección Práctica (Dataset Titanic)

#### **7. Al crear la variable sintética `FamilySize = SibSp + Parch + 1`, ¿qué concepto clave de preparación de datos se aplica y cuál es su utilidad?**
- **Respuesta Correcta:** **[X] B. Construcción de Atributos (*Attribute Construction*), fusionando variables crudas correlacionadas en un indicador único con mayor significado de negocio y capacidad explicativa sobre la supervivencia del grupo familiar.**
- 💡 **Justificación:** Es un ejemplo canónico de *Data Massaging* e ingeniería de características: combina hermanos/cónyuges (`SibSp`) y padres/hijos (`Parch`) más el pasajero mismo ($+1$). Históricamente, viajar solo o en familias numerosas ($>4$) redujo drásticamente la tasa de supervivencia frente a familias pequeñas (2 a 4 miembros).
- ❌ **Distractores:** A, C y D corresponden a técnicas totalmente distintas.

---

#### **8. Al procesar `Embarked` con `OneHotEncoder(drop='first', sparse_output=False)` teniendo 3 categorías originales (`'C'`, `'Q'`, `'S'`), ¿cuántas columnas nuevas se generan?**
- **Respuesta Correcta:** **[X] B. 2 columnas (por ejemplo `Embarked_Q` y `Embarked_S`), ya que la categoría de referencia `'C'` queda codificada implícitamente cuando ambas columnas valen 0, evitando colinealidad exacta (*dummy variable trap*).**
- 💡 **Justificación:** Con $K$ categorías nominales, una codificación completa genera $K$ columnas. Para evitar la trampa de variables ficticias (multicolinealidad perfecta en modelos de regresión y redes), el parámetro `drop='first'` omite la primera categoría, generando $K - 1 = 3 - 1 = 2$ columnas.
- ❌ **Distractores:** A sería el resultado con `drop=None`; C y D son incorrectos.

---

#### **9. Al aplicar `SMOTE` sobre la variable objetivo `Survived` (~61.6% clase 0 vs ~38.4% clase 1), ¿qué cambio se observa en la distribución final?**
- **Respuesta Correcta:** **[X] A. Las clases quedan perfectamente equilibradas (50% de clase 0 y 50% de clase 1), mediante la generación sintética de observaciones representativas en el espacio de características de los sobrevivientes.**
- 💡 **Justificación:** SMOTE (*Synthetic Minority Over-sampling Technique*) identifica los $k$-vecinos más cercanos de cada observación de la clase minoritaria (`Survived=1`) y genera nuevas muestras sintéticas interpolando linealmente entre ellas hasta igualar el conteo de la clase mayoritaria (`Survived=0`).
- ❌ **Distractores:** B describe un submuestreo destructivo no uniforme; C y D describen comportamientos erróneos.

---

#### **10. Al comparar la vista minable para Redes Neuronales (`df_redes`) frente a la vista para Árboles de Decisión (`df_arboles`), ¿cuál es la diferencia fundamental en `Age` y `Fare`?**
- **Respuesta Correcta:** **[X] A. En `df_redes` las variables se conservan continuas, estandarizadas a media 0 y varianza 1 (con transformación $\log$ en `Fare`), mientras que en `df_arboles` están particionadas en contenedores discretos enteros (`n_bins=4`) facilitando reglas de decisión cualitativas.**
- 💡 **Justificación:**
  - Los modelos algebraicos y de gradiente necesitan gradientes suaves sobre números reales continuos en escalas comparables.
  - Los modelos de árboles de decisión y reglas se optimizan cuando las variables continuas se traducen en categorías ordenadas (ej. cuartiles 0, 1, 2, 3) que permiten emitir reglas del tipo: *"IF Tarifa == 'Cuantil_4' AND Edad == 'Cuantil_1' THEN Supervivencia = Alta"*.
- ❌ **Distractores:** B, C y D presentan afirmaciones absurdas o incorrectas.

---

#### **11. Enlace al Cuaderno de Google Colab**
- **Criterio de Evaluación:**
  - El enlace debe ser público con permisos de **Lector** activados.
  - El cuaderno debe contener todas las celdas ejecutadas con las salidas y tablas visibles.
  - Debe evidenciarse el uso de `ColumnTransformer`, `StandardScaler`, `KBinsDiscretizer`, `OneHotEncoder` y `SMOTE` / `RandomOverSampler`.
