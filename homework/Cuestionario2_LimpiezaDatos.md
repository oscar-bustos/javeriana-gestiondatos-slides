# Cuestionario 2: Limpieza de Datos (Faltantes y Outliers)

Este cuestionario evalúa los conceptos teóricos de limpieza de datos vistos en clase y en las lecturas, así como los hallazgos de la Tarea 2 sobre el dataset del Titanic.

**Instrucciones:** Seleccione la respuesta correcta. Al final, deberá adjuntar el enlace a su cuaderno de Colab.

---

### Preguntas Teóricas

**1. ¿Cuál es el propósito principal de crear una variable binaria (True/False) basada en los datos nulos (por ejemplo, usando `isna()`) durante la fase de diagnóstico de valores faltantes?**
- [ ] A. Poder borrar más fácilmente las filas nulas del dataset.
- [ ] B. Investigar si existe una relación estadística entre la ocurrencia de un dato faltante y las otras variables del dataset para clasificarlo como MCAR, MAR o MNAR.
- [ ] C. Convertir una variable numérica en categórica para modelos de clasificación.
- [ ] D. Calcular el límite superior de los outliers usando el rango intercuartílico.

**2. Si en su diagnóstico encuentra que la falta de registro en la variable Edad (`Age`) está fuertemente correlacionada con la clase del pasajero (`Pclass`), ¿qué tipo de mecanismo de datos perdidos representa esto?**
- [ ] A. Missing Completely at Random (MCAR)
- [ ] B. Missing at Random (MAR)
- [ ] C. Missing Not at Random (MNAR)
- [ ] D. Data Leakage (Fuga de datos)

**3. En el tratamiento de valores atípicos (*outliers*) univariados usando el método de Rango Intercuartílico (IQR), ¿cuál es la fórmula estándar para calcular el Límite Superior (*Upper Cap*)?**
- [ ] A. Promedio + 3 * Desviación Estándar
- [ ] B. Mediana + 1.5 * IQR
- [ ] C. $Q_3 + 1.5 \times \text{IQR}$
- [ ] D. $Q_1 + 1.5 \times \text{IQR}$

**4. Según la literatura de preprocesamiento de datos (ej. *Hands-On Data Preprocessing*), ¿cuál de las siguientes opciones es generalmente considerada como la aproximación menos deseable (último recurso) para tratar outliers válidos en un conjunto de datos?**
- [ ] A. Aplicar un tope (Capping) reemplazando los outliers con los límites superior o inferior.
- [ ] B. No hacer nada (si el algoritmo a utilizar es robusto a outliers, como los árboles de decisión).
- [ ] C. Transformación logarítmica para reducir el sesgo.
- [ ] D. Remover/Borrar por completo los registros (filas) que contienen los outliers.

**5. Si decide aplicar la técnica de *Capping* (Tope) a la variable `Fare` (Tarifa), ¿qué sucede exactamente con los pasajeros cuyas tarifas originales eran de 500 dólares si el límite superior calculado era de 65 dólares?**
- [ ] A. Sus registros son eliminados por completo del dataset.
- [ ] B. Su tarifa original (500) se conserva porque representa una observación real.
- [ ] C. El valor de 500 se reemplaza y se sobrescribe por el límite estadístico de 65 dólares.
- [ ] D. El valor se imputa por la media general de todas las tarifas del barco.

---

### Preguntas Prácticas (Basadas en la Tarea 2)

**6. Al analizar los datos faltantes en la variable `Age` (Edad) del dataset del Titanic en conjunto con variables como `Pclass` (Clase), ¿qué comportamiento general es el más esperado estadísticamente y qué mecanismo representaría?**
- [ ] A. La proporción de datos perdidos es idéntica y uniforme en todas las clases, lo que representa un mecanismo MCAR.
- [ ] B. Existe una mayor proporción de datos perdidos dependiente de la clase (ej. en tercera clase `Pclass=3`), indicando una relación sistemática que representa un mecanismo MAR.
- [ ] C. Los datos faltan exclusivamente porque las personas mayores ocultaron intencionalmente su edad, lo que es un claro ejemplo de mecanismo MCAR.
- [ ] D. Los datos de la edad se perdieron completamente al azar debido a un fallo en la recolección general del barco, lo que representa MNAR.

**7. Teniendo en cuenta que el mecanismo de datos perdidos para `Age` está relacionado con otras variables observables (como `Pclass`), ¿cuál de los siguientes métodos de imputación con Pandas es el más adecuado y recomendado para evitar introducir sesgos considerables?**
- [ ] A. `df['Age'].fillna(0)` para rellenar rápida y uniformemente todos los vacíos con el valor cero.
- [ ] B. `df['Age'].fillna(df['Age'].mean())` para imputar todos los registros nulos con la misma media global poblacional de las edades.
- [ ] C. Imputar utilizando la mediana de la edad, pero agrupando y calculándola de manera específica para cada subgrupo de la variable `Pclass`.
- [ ] D. Descartar la variable borrando la columna `Age` por completo usando `df.drop(columns=['Age'])`.

**8. Tras calcular el límite superior para la variable `Fare` en su cuaderno, ¿aproximadamente qué rango numérico describe mejor el límite superior (*Upper Cap*) estándar calculado usando el método de IQR?**
- [ ] A. Cerca de 10 a 15
- [ ] B. Cerca de 65 a 70
- [ ] C. Cerca de 150 a 160
- [ ] D. Mayor a 300

**9. Para las variables de alta cardinalidad o valores únicos que no brindan valor predictivo general (ej. `Ticket` o `PassengerId`), ¿qué acción aplicó durante la fase de limpieza Nivel I en Pandas?**
- [ ] A. `df.fillna(method='ffill')`
- [ ] B. `df.clip(lower=0)`
- [ ] C. `df.drop(columns=['Ticket', 'PassengerId'])`
- [ ] D. `pd.get_dummies(df['Ticket'])`

---

### Enlace de Entrega

**10. Pegue a continuación el enlace a su cuaderno único de Colab (asegúrese de que los permisos estén en "Cualquier persona con el enlace puede leer"):**

*(Espacio para enlace)*
