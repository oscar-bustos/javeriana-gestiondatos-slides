# Gestión de Datos - Presentaciones

Este repositorio contiene las presentaciones interactivas y el material de clase para la asignatura de **Gestión de Datos** en la **Pontificia Universidad Javeriana**, desarrolladas utilizando [Quarto](https://quarto.org/) y [Reveal.js](https://revealjs.com/).

La página web del proyecto está diseñada para ser alojada fácilmente en plataformas como **GitHub Pages**, sirviendo un índice interactivo desde la raíz.

---

## 📂 Estructura del Repositorio

El proyecto se organiza de la siguiente manera:

* **`quarto/`**: Directorio raíz de los contenidos fuente. Cada tema o sesión tiene su propia subcarpeta:
  * `comprension_datos/`: Metodologías y Análisis Exploratorio de Datos (Sesión oficial de plantilla de estilos).
  * `big_data_grandes_volumenes/`: Big Data Parte 2.
  * `big_data_sin_estructura/`: Big Data Parte 1.
  * `extraccion_datos_tabular/`: Tipos de Datos y Extracción.
  * `fuentes_jerarquicas/`: JSON/XML y fuentes semiestructuradas.
  * `limpieza_datos/`: Técnicas de Limpieza y Calidad de Datos.
  * `vista_minable/`: Construcción de la Vista Minable.
  * *Cada subcarpeta contiene su archivo fuente principal `index.qmd`, recursos de estilo `custom.scss` y assets locales (imágenes, bibliografías).*
* **`docs/`**: Carpeta de salida pública. Contiene las diapositivas HTML autocontenidas compiladas a partir de las fuentes.
* **`index.html`**: Página de entrada de la biblioteca de presentaciones. Generada automáticamente con un diseño premium moderno y responsivo para facilitar la navegación por temas.
* **`.agents/`**: Utilidades y scripts de automatización en Python para el procesamiento, compilación y publicación del material de clase.

---

## 🚀 Guía de Uso y Compilación

### Prerrequisitos
1. **Quarto CLI**: Asegúrate de tener instalado Quarto en tu sistema. Puedes descargarlo desde [quarto.org](https://quarto.org/docs/get-started/).
2. **Python 3**: Requerido para ejecutar los scripts de automatización del repositorio.

---

### 🛠️ Comandos de Compilación

Los scripts están ubicados en `.agents/scripts/` y deben ejecutarse desde la raíz del workspace:

#### 1. Compilar una presentación individual
Para compilar los cambios de una sola presentación localmente sin regenerar el índice global:
```bash
python .agents/scripts/compile_quarto.py "quarto/<nombre_carpeta>/index.qmd"
```

#### 2. Compilar y publicar todas las presentaciones (Flujo Completo)
Para compilar todas las diapositivas en bloque, copiar los archivos HTML autocontenidos resultantes al directorio `/docs` y regenerar automáticamente la landing page `index.html` con las tarjetas de cada tema:
```bash
python .agents/scripts/publish_docs.py
```

---

## 🎨 Guía de Estilo Oficial

Todas las presentaciones han sido unificadas para utilizar un tema premium estandarizado mediante el archivo `custom.scss`:
* **Tipografías**: *Montserrat* (para títulos y encabezados de Reveal.js) e *Inter* (para el texto de cuerpo, listas y notas).
* **Colores**: Basado en una paleta corporativa y moderna con el azul marino oficial (`#003576`), fondos limpios sobre blanco, bordes y sombreados suaves en contenedores tipo callout, y soporte optimizado para bloques de código con fuentes monoespaciadas legibles.
* **Encabezado YAML estándar**:
  ```yaml
  format:
    revealjs:
      embed-resources: true
      theme: [default, custom.scss]
      slide-number: true
      show-slide-number: all
      transition: slide
      chalkboard: false
      width: 1050
      height: 700
      logo: assets/logo_RGB.png
  ```
