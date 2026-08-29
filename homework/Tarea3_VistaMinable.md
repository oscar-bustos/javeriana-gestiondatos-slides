# Tarea 3: Construcción de Vistas Minables Asistida por IA en Google Colab

**Asignatura:** Gestión de Datos  
**Institución:** Pontificia Universidad Javeriana  
**Departamento:** Departamento de Ingeniería de Sistemas  

---

## 🎯 Objetivo

El objetivo de esta tarea es consolidar el ciclo de preparación de datos construyendo **vistas minables diferenciadas** a partir de la base de datos del **Titanic** (`titanic.csv`) en un **único cuaderno de Google Colab**. 

A lo largo del taller, los estudiantes aplicarán técnicas avanzadas de transformación vistas en clase:
1. **Ingeniería de Características (*Data Massaging*):** Creación de ratios e indicadores sintéticos (`FamilySize`, `IsAlone`) y transformación logarítmica de variables sesgadas (`Fare`).
2. **Conversión Categórico-Numérica:** Codificación One-Hot (`OneHotEncoder`) y Ordinal (`OrdinalEncoder`).
3. **Escalamiento y Discretización:** Estandarización (`StandardScaler`), Normalización (`MinMaxScaler`) y binarización por cuantiles (`KBinsDiscretizer`).
4. **Balanceo de Clases:** Remuestreo con `SMOTE` o `RandomOverSampler` de `imblearn`.
5. **Integración con Pipelines:** Uso de `ColumnTransformer` con `.set_output(transform="pandas")` para estructurar flujos reproducibles sin fuga de datos (*Data Leakage*).

Se diseñarán dos vistas minables adaptadas a los requerimientos de dos familias de algoritmos:
- **Vista 1: Redes Neuronales / Modelos de Distancia y Gradiente** (requiere variables normalizadas/estandarizadas, variables nominales en One-Hot y tratamiento de asimetría).
- **Vista 2: Árboles de Decisión / Sistemas de Reglas** (optimizado con discretización en intervalos interpretables y codificación ordinal).

---

## 📚 Recursos y Referencias

- **Dataset URL:** `https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv`
- **Guía de Preprocesamiento de Scikit-Learn:** [Scikit-learn Preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html)
- **Documentación de Pipelines y ColumnTransformer:** [ColumnTransformer Scikit-Learn](https://scikit-learn.org/stable/modules/generated/sklearn.compose.ColumnTransformer.html)
- **Documentación de Imbalanced-Learn:** [Imblearn Documentation](https://imbalanced-learn.org/stable/)

---

## 📋 Instrucciones Generales

1. **Un Único Cuaderno de Google Colab:**
   - Ingrese a [Google Colab](https://colab.research.google.com/) con su cuenta institucional.
   - Cree un **único cuaderno** (*New notebook*) donde desarrollará todos los ejercicios.

2. **Identificación del Grupo:**
   - En la primera celda del cuaderno (Markdown), incluya los nombres completos de los integrantes.

3. **Uso de Asistentes de IA (Google Gemini / Colab AI):**
   - Puede apoyarse en el asistente de IA integrado en Colab para generar las celdas de código y enriquecer las justificaciones metodológicas.

4. **Guardado y Compartición del Cuaderno:**
   - ⚠️ **¡Importante!** Asegúrese de ejecutar **todas las celdas** y verificar que las salidas (DataFrames, gráficos, dimensiones) sean visibles.
   - Renombre el cuaderno con el formato: `Tarea3_VistaMinable_[Apellido1]_[Apellido2]`.
   - Guarde y cambie los permisos de acceso a **"Cualquier persona con el enlace"** en modo **Lector** (*Viewer*).

---

## 🔬 Ejercicio 1 - Carga, Preparación Base e Ingeniería de Características

1. **Carga e Imputación Inicial:**
   - Importe `pandas`, `numpy`, `matplotlib.pyplot` y `seaborn`.
   - Cargue el dataset del Titanic desde la URL indicada.
   - Elimine identificadores de alta cardinalidad irrelevantes para la minería: `PassengerId`, `Name`, `Ticket`, `Cabin`.
   - Impute los valores faltantes residuales para que el dataset esté completo antes de transformar:
     - `Age`: Imputar con la mediana general.
     - `Embarked`: Imputar con la moda (`'S'`).
     - `Fare`: Imputar cualquier nulo residual con la mediana.

2. **Ingeniería de Características (*Data Massaging*):**
   - Construya las siguientes variables sintéticas basadas en conocimiento del dominio:
     a. **`FamilySize`:** Tamaño del grupo familiar a bordo (`SibSp + Parch + 1`).
     b. **`IsAlone`:** Indicador binario (1 si `FamilySize == 1`, 0 en caso contrario).
   - Analice la variable `Fare` (tarifa):
     - Grafique el histograma o boxplot de `Fare` y verifique su marcada asimetría positiva (cola larga).
     - Calcule `Fare_Log = np.log1p(df['Fare'])` y compruebe cómo se estabiliza la distribución.

3. **Diagnóstico de la Variable Objetivo (`Survived`):**
   - Calcule las frecuencias y porcentajes de `Survived` (0 = No sobrevivió, 1 = Sobrevivió).
   - Justifique en Markdown el impacto del desbalance (~61.6% vs ~38.4%) y la conveniencia de aplicar balanceo para no sesgar el clasificador.

---

## 🧠 Ejercicio 2 - Vista Minable para Redes Neuronales y Modelos de Distancia

Los modelos basados en optimización por gradiente (Redes Neuronales, Regresión Logística) y cálculo de distancias (KNN, SVM) requieren que:
- Las variables numéricas estén en escalas homogéneas (media 0 y varianza 1, o rango $[0, 1]$).
- Las distribuciones con cola pesada estén comprimidas.
- Las variables categóricas nominales se codifiquen mediante **One-Hot Encoding** (evitando relaciones de orden artificiales).
- Se use `ColumnTransformer` con `.set_output(transform="pandas")` para mantener la estructura tabular.

### Pasos a Desarrollar:

1. **Definición del Pipeline de Transformación (`ColumnTransformer`):**
   - Importe `ColumnTransformer` desde `sklearn.compose`, junto con `StandardScaler` (o `MinMaxScaler`), `FunctionTransformer` y `OneHotEncoder` desde `sklearn.preprocessing`.
   - Configure el preprocesador para aplicar:
     - **Numéricas Continuas (`Age`, `FamilySize`):** `StandardScaler()` (o `MinMaxScaler()`).
     - **Numérica con Cola Pesada (`Fare`):** `FunctionTransformer(np.log1p)` seguido de `StandardScaler()`.
     - **Categóricas Nominales (`Sex`, `Embarked`):** `OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore')`.
     - **Categórica Ordinal (`Pclass`):** `OneHotEncoder(sparse_output=False)` o escalamiento como ordinal numérico.
   - Aplique `.set_output(transform="pandas")` al `ColumnTransformer` y transforme las variables predictoras $X$.

2. **Balanceo de Clases con SMOTE / OverSampling:**
   - Importe `SMOTE` (o `RandomOverSampler`) de `imblearn.over_sampling`.
   - Aplique el balanceo sobre $(X_{trans}, y)$ para igualar las clases de sobrevivientes y no sobrevivientes.

3. **Exportación de la Vista Minable:**
   - Una las features transformadas y la variable `Survived` balanceada en un único DataFrame `df_redes`.
   - Exporte a CSV: `titanic_vista_redes_neuronales.csv` con `index=False`.

---

## 🌳 Ejercicio 3 - Vista Minable para Árboles de Decisión y Reglas de Negocio

Los modelos basados en árboles y reglas (Decision Trees, Rule Induction) se benefician de representaciones discretas ordenadas y categorías bien definidas que facilitan la generación de reglas interpretables (*ej. IF Edad = 'Infante' AND Tarifa = 'Alta' THEN ...*).

### Pasos a Desarrollar:

1. **Discretización de Variables Continuas (`KBinsDiscretizer`):**
   - Importe `KBinsDiscretizer` y `OrdinalEncoder` de `sklearn.preprocessing`.
   - Configure la discretización para `Age` y `Fare`:
     - Parámetros: `n_bins=4`, `encode='ordinal'`, `strategy='quantile'`.
     - Justifique en Markdown por qué la estrategia `'quantile'` (frecuencia equivalente) es superior a `'uniform'` para variables con asimetría como `Fare`.

2. **Codificación Ordinal / Categórica para Árboles:**
   - Codifique `Sex`, `Embarked`, `Pclass` y `IsAlone` utilizando `OrdinalEncoder` o categorías enteras compactas.

3. **Balanceo de Clases:**
   - Aplique `SMOTE` o `RandomOverSampler` sobre las variables discretizadas y codificadas para balancear la variable `Survived`.

4. **Exportación de la Vista Minable:**
   - Construya el DataFrame resultante `df_arboles` y expórtelo a CSV: `titanic_vista_arboles_decision.csv` con `index=False`.

---

## 🔍 Ejercicio 4 - Verificación, Comparación y Análisis Crítico

1. **Inspección Estructural:**
   - Imprima `.head()`, `.info()` y `.describe()` para `df_redes` y `df_arboles`.
   - Compare el número total de columnas y los tipos de datos generados en cada vista.

2. **Validación del Balanceo:**
   - Verifique con `value_counts()` en `Survived` que ambas vistas minables contengan un 50% / 50% exacto de clases.

3. **Cuadro Comparativo en Markdown:**
   - Complete en el cuaderno una tabla comparativa respondiendo:

| Criterio | Vista Redes Neuronales / Distancias | Vista Árboles / Reglas |
| :--- | :--- | :--- |
| **Tratamiento de `Age` y `Fare`** | *(Estandarización / Log-transform)* | *(Discretización en 4 cuantiles)* |
| **Codificación de `Sex` y `Embarked`** | *(One-Hot Encoding)* | *(Ordinal Encoding / Enteros)* |
| **Impacto de Outliers en la vista** | *(Mitigados con Log y Z-Score)* | *(Absorbidos dentro de los Bins extremos)* |
| **Interpretabilidad de features** | *(Matemática / Continua)* | *(Reglas de partición cualitativas)* |

---

## 📤 Entrega

- Ingrese al **Cuestionario 3 de Vista Minable**.
- Responda las preguntas teóricas y los hallazgos prácticos de su análisis.
- Pegue el enlace público a su **cuaderno único de Google Colab** (permisos de Lector activados).
