# Taller 1: Análisis Exploratorio de Datos (EDA) Asistido por IA en Google Colab

**Asignatura:** Gestión de Datos  
**Institución:** Pontificia Universidad Javeriana  
**Departamento:** Departamento de Ingeniería de Sistemas  

---

## 🎯 Objetivo

El objetivo de este taller es realizar un Análisis Exploratorio de Datos (EDA) automático utilizando la librería `ydata-profiling` en **un único cuaderno de Google Colab**, apoyándose en asistentes de Inteligencia Artificial (Google Gemini / Colab AI) para la generación y ejecución del código asistido por IA para ambos conjuntos de datos (**Titanic** y **Diabetes**).

---

## 📋 Instrucciones Generales

1. **Un Único Cuaderno de Google Colab:**
   - Ingrese a [Google Colab](https://colab.research.google.com/) con su cuenta institucional de Google.
   - Cree un **único cuaderno** (*New notebook*) donde desarrollará ambos ejercicios de EDA (Titanic y Diabetes).

2. **Identificación del Grupo:**
   - En la primera celda del cuaderno, cree una celda de **texto (Markdown)** e incluya los nombres completos de los 2 integrantes que entregan el taller.

3. **Uso de Asistentes de IA (Google Gemini / Colab AI):**
   - Para **ambos conjuntos de datos**, debe utilizar el asistente de IA integrado en Colab para generar las celdas de código de carga del dataset y construcción de los reportes exploratorios con `ydata-profiling`.

4. **Guardado y Compartición del Cuaderno:**
   - ⚠️ **¡Importante!** Asegúrese de haber ejecutado **todas las celdas** de ambos ejercicios y que los dos reportes de `ydata-profiling` y las respuestas a las preguntas sean completamente visibles en el archivo.
   - Renombre el cuaderno con el formato: `Tarea1_EDA_[Apellido1]_[Apellido2]`.
   - Guarde el cuaderno (`Archivo -> Guardar` o `Ctrl+S`).
   - Haga clic en **Compartir** (*Share*) en la esquina superior derecha.
   - Cambie los permisos de acceso a **"Cualquier persona con el enlace"** en modo **Lector** (*Viewer*).
   - Copie el enlace público de su cuaderno único.

---

## 🚢 Ejercicio 1 - Análisis Exploratorio de la Base de Datos de Titanic


Realice el análisis exploratorio asistido por IA para el dataset de Titanic dentro del cuaderno:

1. **Generación del Código mediante IA:**
   - Utilice el siguiente prompt en el asistente de Inteligencia Artificial (Google Gemini / Colab AI) para generar el código completo que descarga los datos, instala la librería y genera el reporte exploratorio:

> 🤖 **Prompt sugerido:**  
> *"Escribe el código en Python para Google Colab que descargue el dataset de Titanic desde la URL https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv, instale la última versión de la librería ydata-profiling, y genere un análisis exploratorio de datos (ProfileReport) de este dataset."*

2. **Ejecución y Análisis:**
   - Pegue el código generado en su cuaderno de Colab, ejecútelo y verifique que se muestre el reporte interactivo.
3. **Responder el Cuestionario:**
   - Utilice el reporte interactivo generado para responder las preguntas correspondientes a este dataset en el cuestionario de la tarea (y deje registro de sus análisis dentro del mismo cuaderno si lo considera necesario).

---

## 🩺 Ejercicio 2 - Análisis Exploratorio de la Base de Datos de Diabetes 

En el **mismo cuaderno de Colab**, continúe con el análisis exploratorio asistido por IA para la base de datos de diabetes:

1. **Generación del Código mediante IA:**
   - En una **nueva celda de código** debajo del análisis de Titanic, utilice el siguiente prompt en el asistente de IA para generar el código correspondiente a la base de datos de Diabetes, pidiendo explícitamente que se añada al análisis existente:

> 🤖 **Prompt sugerido:**  
> *"Continuando con el análisis anterior, escribe una nueva sección de código que descargue el dataset de Diabetes desde la URL https://raw.githubusercontent.com/oscar-bustos/javeriana-gestiondatos/main/taller1/diabetes.csv y genere su respectivo análisis exploratorio de datos (ProfileReport). Asegúrate de usar variables distintas para no sobreescribir los datos de Titanic."*

2. **Ejecución y Análisis:**
   - Pegue el código generado en la nueva celda, ejecútelo y analice el nuevo reporte interactivo.
3. **Responder el Cuestionario:**
   - Utilice este nuevo reporte interactivo para responder las preguntas de la sección de Diabetes en el cuestionario de la tarea.

---

## 📤 Entrega

- Ingrese al cuestionario de la tarea, responda las preguntas del formulario para ambos ejercicios y pegue el enlace público del **cuaderno único de Colab** ya compartido.
