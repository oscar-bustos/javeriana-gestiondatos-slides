# Tarea 2: Limpieza de Datos Asistida por IA en Google Colab

**Asignatura:** Gestión de Datos  
**Institución:** Pontificia Universidad Javeriana  
**Departamento:** Departamento de Ingeniería de Sistemas  

---

## 🎯 Objetivo

El objetivo de esta tarea es realizar la limpieza de la base de datos del **Titanic** en un **único cuaderno de Google Colab**, enfocándose en el diagnóstico detallado de mecanismos de datos perdidos (MCAR, MAR, MNAR) y en el análisis riguroso de valores atípicos (outliers) utilizando métodos estadísticos de Pandas, apoyándose en los conceptos vistos en clase y en asistentes de Inteligencia Artificial (Google Gemini / Colab AI).

---

## 📋 Instrucciones Generales

1. **Un Único Cuaderno de Google Colab:**
   - Ingrese a [Google Colab](https://colab.research.google.com/) con su cuenta institucional de Google.
   - Cree un **único cuaderno** (*New notebook*) donde desarrollará todo el ejercicio.

2. **Identificación del Grupo:**
   - En la primera celda del cuaderno, cree una celda de **texto (Markdown)** e incluya los nombres completos de los integrantes.

3. **Uso de Asistentes de IA (Google Gemini / Colab AI):**
   - Puede utilizar el asistente de IA integrado en Colab para generar las celdas de código.

4. **Guardado y Compartición del Cuaderno:**
   - ⚠️ **¡Importante!** Asegúrese de haber ejecutado **todas las celdas** y que los resultados sean visibles.
   - Renombre el cuaderno con el formato: `Tarea2_Limpieza_[Apellido1]_[Apellido2]`.
   - Guarde el cuaderno y cambie los permisos de acceso a **"Cualquier persona con el enlace"** en modo **Lector** (*Viewer*).

---

## 🚢 Ejercicio 1 - Diagnóstico y Planeación 

Realice un análisis profundo para planear las actividades de limpieza.

1. **Carga Inicial:**
   - Importe las librerías `pandas`, `matplotlib.pyplot` y `seaborn`.
   - Cargue el Dataset de Titanic: `https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv`.

2. **Diagnóstico Detallado de Mecanismos de Datos Perdidos (MCAR, MAR, MNAR):**
   - La variable `Age` tiene valores faltantes. Debe diagnosticar si son MCAR, MAR o MNAR.
   - **Actividad:** Cree una variable binaria oculta (ej. `Age_Missing`) que sea `True` si la edad es nula y `False` si no lo es (`df['Age'].isna()`).
   - Compare la distribución de otras variables (ej. `Pclass` o `Survived`) entre el grupo de pasajeros con edad faltante y el grupo con edad registrada (puede usar un gráfico de barras o un test de independencia Chi-cuadrado).
   - **Reporte en Markdown:** Concluya si existe una relación sistemática. Si la hay, clasifíquelo como MAR o MNAR; de lo contrario, MCAR. Proponga cómo imputarlo (ej. usando la mediana general, o la mediana por grupos de `Pclass`).

3. **Análisis de Valores Atípicos (Outliers):**
   - La variable `Fare` (Tarifa) suele tener valores extremos.
   - **Actividad Univariada:** Dibuje un Boxplot de la variable `Fare` usando `seaborn`.
   - Calcule los cuartiles $Q_1$, $Q_3$ y el rango intercuartílico (IQR). Determine el límite superior (`upper_cap` = $Q_3 + 1.5 \times \text{IQR}$).
   - Identifique cuántos registros son considerados *fliers* (superan el límite superior).
   - **Reporte en Markdown:** Con base en la literatura, decida cómo tratar estos outliers. ¿Ignorarlos, remover los registros, aplicar un "Tope" (*Capping*) reemplazándolos por el límite superior, o discretizar la variable? Justifique su decisión.

4. **Otros Hallazgos:**
   - Detecte y reporte brevemente qué hará con atributos de alta cardinalidad o únicos (ej. `Ticket`, `PassengerId`, `Name`).

---

## 🧹 Ejercicio 2 - Limpieza de Datos 

Ejecute las acciones planeadas en el punto anterior sobre el DataFrame cargado.

1. **Tratamiento de Datos Faltantes:**
   - Implemente la estrategia de imputación decidida para `Age` (ej. imputación por grupo usando `groupby` y `transform` con la mediana, o simplemente `fillna` de la mediana global).
   - Para columnas irremediables (ej. `Cabin` si decide que tiene demasiados nulos), use `df.drop()`.
   - Para nulos residuales muy pequeños (ej. `Embarked`), use `df.dropna()`.

2. **Tratamiento de Outliers:**
   - Implemente el tratamiento decidido para `Fare`. Si eligió aplicar *Capping* (Tope), use selectores de indexación booleana o la función `clip()` de pandas para limitar los valores extremos al límite superior calculado (`upper_cap`).

3. **Eliminación de Redundancias y Fuga de Datos:**
   - Borre las columnas que identificó que no aportan valor o tienen alta cardinalidad utilizando `df.drop()`.

4. **Generación de Archivo Limpio:**
   - Exporte el DataFrame resultante a un nuevo archivo CSV utilizando `df.to_csv(index=False)`.

---

## 🔍 Ejercicio 3 - Verificación (5 pts)

- Utilice `df.info()` y `df.describe()` (o vuelva a generar un reporte de `ydata-profiling` si lo prefiere) sobre el DataFrame limpio para verificar numéricamente que:
  1. Ya no existan valores nulos.
  2. El valor máximo de `Fare` no supere el límite superior establecido (si aplicó Capping).
  3. No existan variables redundantes o de alta cardinalidad sin valor predictivo.

---

## 📤 Entrega

- Ingrese al **Cuestionario 2 de Limpieza de Datos**.
- Responda las preguntas.
- Pegue el enlace público de su **cuaderno único de Colab**.
