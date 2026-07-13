# Reglas del Proyecto

## Presentaciones (Quarto / Reveal.js)
- **Límite de líneas:** Cada slide debe tener como máximo 11 o 12 líneas de texto en total para evitar desbordamientos verticales/horizontales y mantener una estética limpia con la fuente elegida.
- **Concisión:** Resumir o limitar el número de caracteres por línea. Priorizar textos cortos y directos para que los elementos visuales y de texto queden bien balanceados.
- **Imágenes y Desbordamiento Vertical:** Para evitar que el contenido se salga de los márgenes inferiores (overflow), controla el tamaño de las imágenes. Si la imagen es vertical (portrait), no uses solo porcentajes de `width`. Fija su altura máxima con el atributo `height` (por ejemplo: `{height="350px" fig-align="center"}`). También puedes usar columnas (`::: {.columns}`) para colocar texto junto a la imagen.
- **Fragmentos y Espacio:** Al usar fragmentos (`. . .`), recuerda que TODO el contenido (pregunta, respuesta e imagen) ocupa espacio en la misma pantalla. Si la suma del contenido es extensa, **NO uses fragmentos**. Divide el contenido en dos diapositivas distintas (una para la pregunta y otra nueva para la respuesta).
