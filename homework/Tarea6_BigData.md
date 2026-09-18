# Tarea 6: Big Data — Búsqueda Semántica y Google BigQuery

**Asignatura:** Gestión de Datos  
**Institución:** Pontificia Universidad Javeriana  
**Departamento:** Departamento de Ingeniería de Sistemas  

---

## 🎯 Objetivo

Experimentar de forma ágil y práctica los dos pilares de Big Data:
1. **Variedad (Datos No Estructurados):** Extraer texto de un documento PDF propio, generar *embeddings* vectoriales comparando dos modelos locales de Hugging Face y realizar búsqueda semántica con **ChromaDB**.
2. **Volumen (Analítica Cloud):** Ejecutar una consulta SQL sobre millones de registros en **Google Cloud BigQuery**.

---

## 📋 Instrucciones Generales

1. **Un Único Cuaderno de Google Colab:**
   - Abra el cuaderno provisto: [`colab/Taller6_BigData_Busqueda_Semantica.ipynb`](https://colab.research.google.com/drive/1PL9Y6x_yqt9yfo6AxQiUEb7lof7i16me).
   - Guarde una copia en su Google Drive (`Archivo -> Guardar una copia en Drive`).
   - Todo el trabajo (código, resultados y la evidencia de BigQuery) se consolidará en este **único cuaderno**.

2. **Lo que debe modificar en el cuaderno:**
   - **Celda de Identificación:** Cree una celda de texto al inicio con los nombres completos de los integrantes.
   - **Celda de Descripción del Dataset:** Incluya un párrafo breve (2 a 3 líneas) describiendo el archivo PDF propio que seleccionó (de qué tema trata y de dónde proviene).
   - **Sección de Evidencia de BigQuery:** Al final del cuaderno, agregue una celda de texto con la captura de pantalla y la respuesta del Ejercicio 2.

3. **Guardado y Compartición:**
   - ⚠️ Ejecute todas las celdas para que los resultados queden grabados en el cuaderno.
   - Renombre el cuaderno como: `Tarea6_BigData_[Apellido1]_[Apellido2]`.
   - Configure el acceso en **Compartir** a **"Cualquier persona con el enlace"** en modo **Lector** (*Viewer*).

---

## 🔍 Ejercicio 1 - Búsqueda Semántica con su propio Dataset (25 pts)

> 💡 **Nota pedagógica:** **No tiene que programar código nuevo.** El código en Python ya está completamente implementado en el cuaderno. Su tarea es ejecutarlo utilizando su **propio archivo PDF**.

### Pasos a ejecutar:

1. **Seleccione un PDF propio:** Elija cualquier documento PDF de su interés (un artículo académico, un informe público, un manual, apuntes de clase, etc.).
2. **Suba su archivo al cuaderno:**
   - Suba su archivo PDF directamente en la carpeta `input` de Google Colab (o use el panel lateral izquierdo de archivos).
3. **Ejecute el cuaderno completo:**
   - Ejecute secuencialmente las celdas restantes: extracción de texto con `pypdf`, fragmentación (*chunking*), generación de *embeddings* comparando dos modelos locales de Hugging Face e indexación en ChromaDB.
4. **Formule y observe sus consultas:**
   - En la celda de consultas (`CONSULTAS = [...]`), cambie las preguntas por 2 o 3 preguntas relacionadas con el contenido de **su propio PDF**.
   - Ejecute la búsqueda semántica y verifique que los fragmentos recuperados en el Top 3 correspondan al tema consultado.

---

## ☁️ Ejercicio 2 - Laboratorio de Google BigQuery (25 pts)

**Plataforma:** [Google Skills](https://www.skills.google/). Antes de iniciar, regístrese en el plan [Starter](https://www.skills.google/subscriptions), que no tiene costo y ofrece créditos mensuales para laboratorios seleccionados.

### Pasos a ejecutar:

1. **Registrarse e iniciar el laboratorio:**
   - Regístrese o inicie sesión en Google Skills y seleccione el plan **Starter**.
   - Abra una **ventana de incógnito** en su navegador web.
   - Ingrese al laboratorio: 👉 [Exploring a BigQuery Public Dataset](https://www.skills.google/focuses/19078?parent=catalog).
   - Haga clic en **Start lab** y acceda a la consola de Google Cloud con el usuario y la contraseña temporales generados.
2. **Completar el laboratorio:**
   - Siga todas las instrucciones del laboratorio en BigQuery.
   - Consulte el dataset público de nombres de Estados Unidos.
   - Cree el dataset y la tabla solicitados, cargue el archivo de datos y ejecute la consulta final sobre la tabla creada.
3. **Evidencias a registrar en su cuaderno de Colab:**
   - Pegue una **captura de pantalla** del laboratorio completado.
   - Pegue una **captura de pantalla** de la consulta final ejecutada en BigQuery donde se aprecie la tabla de resultados.
   - Responda brevemente: **¿Cuáles son los 5 nombres de niños más comunes de 2014 según la consulta final y cuál fue el total del nombre más popular?**

---

## 📤 Entrega

- Ingrese al espacio de la **Tarea 6** en **Brightspace**.
- Pegue el enlace público a su **cuaderno de Google Colab** (verifique que tenga permisos de lectura abiertos para cualquier persona con el enlace).
