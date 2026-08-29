# Tarea 4: Datos Tabulares con Pandas y SQLite

**Asignatura:** Gestión de Datos  
**Institución:** Pontificia Universidad Javeriana  
**Departamento:** Departamento de Ingeniería de Sistemas  

---

## 🎯 Objetivo

El objetivo de esta tarea es utilizar la librería Pandas en conjunto con SQLite para extraer, procesar, analizar y exportar datos relacionales provenientes de una base de datos local (`chinook.db`). Se busca desarrollar habilidades en la ejecución de consultas SQL desde Python y en la manipulación y visualización de *DataFrames*.

---

## 📋 Instrucciones Generales

1. **Un Único Cuaderno de Google Colab:**
   - Ingrese a [Google Colab](https://colab.research.google.com/) con su cuenta institucional.
   - Cree un **único cuaderno** (*New notebook*) donde desarrollará todo el ejercicio.

2. **Identificación del Grupo:**
   - En la primera celda del cuaderno, cree una celda de **texto (Markdown)** e incluya los nombres completos de los integrantes.

3. **Guardado y Compartición del Cuaderno:**
   - ⚠️ **¡Importante!** Asegúrese de haber ejecutado **todas las celdas** y que los resultados (tablas, gráficos) sean visibles.
   - Renombre el cuaderno con el formato: `Tarea4_Tabulares_[Apellido1]_[Apellido2]`.
   - Guarde el cuaderno y cambie los permisos de acceso a **"Cualquier persona con el enlace"** en modo **Lector** (*Viewer*).

---

## ⚙️ Preparación del Entorno

1. Importe las librerías necesarias: `pandas` y `sqlite3`. (También puede requerir `matplotlib.pyplot` o `seaborn` para los gráficos).
2. Descargue el archivo `chinook.db` del siguiente enlace:
   [chinook.db](https://github.com/oscar-bustos/javeriana-gestiondatos/blob/main/taller4/chinook.db)
3. Lea brevemente qué significan los campos en el siguiente enlace:
   [SQLite Sample Database](https://www.sqlitetutorial.net/sqlite-sample-database/)
4. Puede interactuar con un simulador de esa BD en el siguiente link:
   [Simulador SQLite](https://www.sqlitetutorial.net/tryit/query/sqlite-select/#1)
5. Suba el archivo `chinook.db` al espacio de trabajo de su Google Colab.
6. Conéctese a la base de datos usando `sqlite3.connect('chinook.db')`.

**Ejemplo de código de Referencia:**
```python
import sqlite3
import pandas as pd

# Connect to the chinook.db database
conn = sqlite3.connect('chinook.db')

# Define the SQL query
query = """
SELECT FirstName, LastName, Email
FROM Customers
WHERE Country = 'USA'
"""

# Execute the query and read results into a DataFrame
results_df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Export the DataFrame to a CSV file
results_df.to_csv('usa_customers.csv', index=False)
print("Query results exported to 'usa_customers.csv'")
```

---

## 📊 Ejercicio 1 - Consultas Simples sobre la Base de Datos (20 pts)

Genere, usando únicamente `read_sql_query`, un *DataFrame* resultante de Pandas por cada uno de los siguientes ejercicios. Imprima el resultado en el cuaderno y **exporte a CSV** las consultas:

1. Recupera los nombres y direcciones de correo electrónico de todos los clientes que viven en Estados Unidos o en Canadá.
2. Recupera una lista de pistas (*tracks*) junto con su información de álbum y artista para el género 'Rock'.
3. Recupera las 10 facturas más caras, incluyendo el nombre del cliente, la fecha de la factura y el monto total.
4. Recupere la lista de álbumes y cuente el número de pistas que tiene el álbum.

---

## 📈 Ejercicio 2 - Consultas Agregadas en el tiempo (20 pts)

Genere, usando únicamente `read_sql_query`, un *DataFrame* resultante de Pandas por ejercicio. Usando ese DataFrame, genere un **gráfico de barras o línea** con las siguientes instrucciones (asegúrese de que los gráficos contengan la información impresa en orden cronológico correcto):

1. **Ingresos Totales:** Genera un gráfico que muestre los ingresos totales por mes y año (tabla `invoice`, columna `total`).
   - *Análisis:* Identifique el año y mes donde se vendió en total más y donde se vendió menos.
2. **Ingresos por Día:** Grafica el número de ingresos a diferentes días de la semana (tabla `invoice`, columna `total`).
   - *Análisis:* Identifique el día de la semana donde se vendió más y donde se vendió menos.
3. **Ventas por Género:** Genera un gráfico que muestre la cantidad de ventas (conteo sobre `invoice`) por género musical a lo largo de los años.
   - *Análisis:* Identifique por cada género el año donde se vendió más. ¿Identifica alguna tendencia?
4. **Top 10 Artistas:** Genera un gráfico que muestre la cantidad de ventas de los 10 artistas más populares cada año.

---

## 💾 Ejercicio 3 - Exportar a Distintos Formatos (10 pts)

En el mismo cuaderno de Colab, exporte una a una las tablas de la base de datos en los siguientes formatos:
- **EXCEL**
- **FEATHER**
- **PARQUET**
- **CSV**

*Análisis:* Encuentre cuál es el formato que es menos pesado en bytes, y cuál es el que pesa más para cada uno de los casos. Explique sus hallazgos con sus propias palabras.

---

## 📤 Entrega

- Ingrese al **Cuestionario 4 de Datos Tabulares**.
- Responda las preguntas teóricas y prácticas.
- Pegue el enlace público de su **cuaderno único de Colab** en la última pregunta del cuestionario.
