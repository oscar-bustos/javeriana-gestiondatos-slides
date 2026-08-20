"""
Generador de imágenes para la presentación Vista Minable.
Top 10 imágenes prioritarias (tipo Python).
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
import os

# ── Configuración global ──────────────────────────────────────
OUTPUT_DIR = r"c:\Users\olbus\Git\Javeriana\javeriana-gestiondatos-slides\quarto\vista_minable\assets"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Colores de la paleta (tonos profesionales/académicos)
COLORS = {
    'primary': '#1A56DB',      # azul profundo
    'secondary': '#7E3AF2',    # púrpura
    'accent': '#E74694',       # rosa/magenta
    'success': '#0E9F6E',      # verde
    'warning': '#FF8A4C',      # naranja
    'danger': '#F05252',       # rojo
    'dark': '#1F2937',         # gris oscuro
    'light': '#F3F4F6',        # gris claro
    'gray': '#6B7280',         # gris medio
    'gold': '#FBBF24',         # dorado
}

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Segoe UI', 'Helvetica', 'Arial'],
    'font.size': 12,
    'axes.titlesize': 16,
    'axes.titleweight': 'bold',
    'axes.labelsize': 13,
    'figure.facecolor': 'white',
    'axes.facecolor': '#FAFBFC',
    'axes.grid': True,
    'grid.alpha': 0.3,
    'grid.linestyle': '--',
    'savefig.dpi': 200,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.3,
})


def save(fig, name):
    path = os.path.join(OUTPUT_DIR, name)
    fig.savefig(path, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"  ✅ Guardado: {name}")


# ══════════════════════════════════════════════════════════════
# 3. El Caso del Atípico Extremo (L171) — Top 3
# ══════════════════════════════════════════════════════════════
def gen_outlier_effect():
    print("[*] Generando: outlier_minmax.png")
    np.random.seed(42)
    salarios = np.random.uniform(1_000_000, 5_000_000, 50)
    salarios_con_outlier = np.append(salarios, 50_000_000_000)

    # Normalizar
    mn, mx = salarios_con_outlier.min(), salarios_con_outlier.max()
    norm = (salarios_con_outlier - mn) / (mx - mn)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5), gridspec_kw={'width_ratios': [1, 1]})

    # Panel izquierdo: datos originales
    ax = axes[0]
    ax.scatter(range(len(salarios)), salarios / 1e6, color=COLORS['primary'], s=40, alpha=0.7, zorder=3, label='Salarios normales')
    ax.scatter(len(salarios), 50_000, color=COLORS['danger'], s=120, zorder=4, marker='D', edgecolors='darkred', linewidths=1.5, label='Outlier ($50,000M)')
    ax.set_title('Datos Originales', pad=10)
    ax.set_ylabel('Salario (Millones $)')
    ax.set_xlabel('Registro')
    ax.legend(fontsize=9, loc='upper left')
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'${x:,.0f}M'))

    # Panel derecho: después de Min-Max
    ax = axes[1]
    ax.scatter(range(len(salarios)), norm[:len(salarios)], color=COLORS['primary'], s=40, alpha=0.7, zorder=3, label='Salarios normales')
    ax.scatter(len(salarios), norm[-1], color=COLORS['danger'], s=120, zorder=4, marker='D', edgecolors='darkred', linewidths=1.5, label='Outlier')
    ax.set_title('Después de Min-Max [0, 1]', pad=10)
    ax.set_ylabel('Valor Normalizado')
    ax.set_xlabel('Registro')
    ax.legend(fontsize=9, loc='center right')

    # Anotación del aplastamiento
    ax.annotate('Todos aplastados\ncerca de 0',
                xy=(25, norm[:len(salarios)].mean()), xytext=(30, 0.45),
                fontsize=10, color=COLORS['danger'], fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=COLORS['danger'], lw=2),
                ha='center')

    fig.suptitle('Efecto de un Atípico Extremo en Normalización Min-Max', fontsize=15, fontweight='bold', y=1.02)
    plt.tight_layout()
    save(fig, 'outlier_minmax.png')


# ══════════════════════════════════════════════════════════════
# 4. Distribuciones con Cola Larga (L444) — Top 4
# ══════════════════════════════════════════════════════════════
def gen_log_transform():
    print("[*] Generando: log_transform_before_after.png")
    np.random.seed(42)
    # Simular precios de vivienda (distribución lognormal)
    precios = np.random.lognormal(mean=19.5, sigma=0.8, size=2000)
    precios = precios / 1e6  # En millones

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

    # Antes
    ax = axes[0]
    ax.hist(precios, bins=50, color=COLORS['accent'], alpha=0.8, edgecolor='white', linewidth=0.5)
    ax.set_title('Distribución Original', pad=10)
    ax.set_xlabel('Precio de Vivienda (Millones $)')
    ax.set_ylabel('Frecuencia')
    ax.axvline(np.median(precios), color=COLORS['dark'], linestyle='--', lw=2, label=f'Mediana: ${np.median(precios):,.0f}M')
    ax.annotate('Cola larga →', xy=(np.percentile(precios, 95), 5), fontsize=11,
                color=COLORS['danger'], fontweight='bold', ha='left')
    ax.legend(fontsize=9)

    # Después
    ax = axes[1]
    log_precios = np.log(precios + 1)
    ax.hist(log_precios, bins=50, color=COLORS['success'], alpha=0.8, edgecolor='white', linewidth=0.5)
    ax.set_title('Después de log(precio + 1)', pad=10)
    ax.set_xlabel('log(Precio + 1)')
    ax.set_ylabel('Frecuencia')
    ax.axvline(np.median(log_precios), color=COLORS['dark'], linestyle='--', lw=2, label=f'Mediana: {np.median(log_precios):.2f}')
    ax.annotate('≈ Simétrica', xy=(np.median(log_precios), ax.get_ylim()[1]*0.8), fontsize=11,
                color=COLORS['success'], fontweight='bold', ha='center')
    ax.legend(fontsize=9)

    fig.suptitle('Transformación Logarítmica: Cola Larga → Distribución Simétrica', fontsize=15, fontweight='bold', y=1.02)
    plt.tight_layout()
    save(fig, 'log_transform_before_after.png')


# ══════════════════════════════════════════════════════════════
# 5. Desafío en Discretización (L317) — Top 5
# ══════════════════════════════════════════════════════════════
def gen_discretization_challenge():
    print("[*] Generando: discretizacion_equal_width.png")
    np.random.seed(42)
    # Distribución asimétrica de ingresos (la mayoría gana el mínimo)
    ingresos_bajos = np.random.normal(1_200_000, 300_000, 9000)
    ingresos_medios = np.random.normal(3_500_000, 800_000, 700)
    ingresos_altos = np.random.normal(15_000_000, 5_000_000, 250)
    ingresos_super = np.random.normal(80_000_000, 20_000_000, 50)
    ingresos = np.concatenate([ingresos_bajos, ingresos_medios, ingresos_altos, ingresos_super])
    ingresos = ingresos[ingresos > 0]

    # Equal width: 4 bins
    mn, mx = ingresos.min(), ingresos.max()
    width = (mx - mn) / 4
    bins_ew = [mn + i * width for i in range(5)]

    fig, ax = plt.subplots(figsize=(11, 5))

    # Histograma base
    counts, edges, patches = ax.hist(ingresos / 1e6, bins=80, color=COLORS['primary'], alpha=0.6,
                                      edgecolor='white', linewidth=0.3, label='Distribución real')

    # Líneas de corte Equal Width
    bin_colors = [COLORS['danger'], COLORS['warning'], COLORS['success'], COLORS['secondary']]
    for i in range(4):
        left = bins_ew[i] / 1e6
        right = bins_ew[i+1] / 1e6
        ax.axvline(right, color='red', linestyle='--', lw=2, alpha=0.7)
        # Calcular porcentaje en cada bin
        count = np.sum((ingresos >= bins_ew[i]) & (ingresos < bins_ew[i+1]))
        pct = count / len(ingresos) * 100
        mid = (left + right) / 2
        ax.annotate(f'Bin {i+1}\n{pct:.1f}%', xy=(mid, ax.get_ylim()[1] * 0.85),
                    fontsize=11, ha='center', fontweight='bold',
                    color=bin_colors[i],
                    bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=bin_colors[i], alpha=0.9))

    ax.set_title('Equal Width con 4 Bins en Distribución Asimétrica de Ingresos', pad=15, fontsize=14)
    ax.set_xlabel('Ingreso (Millones $)')
    ax.set_ylabel('Frecuencia')
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'${x:,.0f}M'))

    # Anotación
    ax.annotate('¡El 95% de los datos\ncae en un solo bin!',
                xy=(bins_ew[1] / 1e6 * 0.3, counts.max() * 0.6),
                fontsize=12, color=COLORS['danger'], fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='#FEE2E2', edgecolor=COLORS['danger']))

    plt.tight_layout()
    save(fig, 'discretizacion_equal_width.png')


# ══════════════════════════════════════════════════════════════
# 6. La Paradoja del Fraude (L533) — Top 6
# ══════════════════════════════════════════════════════════════
def gen_fraud_waffle():
    print("[*] Generando: fraude_desbalance.png")

    fig, axes = plt.subplots(1, 2, figsize=(12, 5), gridspec_kw={'width_ratios': [1.2, 0.8]})

    # Panel izquierdo: Waffle chart (10x10 grid = 10,000 representaciones)
    ax = axes[0]
    grid = np.zeros((50, 200))  # 10,000 celdas
    # Solo 5 celdas son fraude (0.05%)
    fraud_positions = [(25, 100), (10, 50), (40, 150), (5, 30), (35, 180)]
    for r, c in fraud_positions:
        grid[r, c] = 1

    from matplotlib.colors import ListedColormap
    cmap = ListedColormap([COLORS['light'], COLORS['danger']])
    ax.imshow(grid, cmap=cmap, aspect='auto', interpolation='nearest')

    # Marcar los fraudes con círculos
    for r, c in fraud_positions:
        ax.plot(c, r, 'o', markersize=8, markerfacecolor='none',
                markeredgecolor='yellow', markeredgewidth=2.5)

    ax.set_title('10,000 Transacciones', pad=10, fontsize=14)
    ax.set_xticks([])
    ax.set_yticks([])

    # Leyenda manual
    legend_elements = [
        mpatches.Patch(facecolor=COLORS['light'], edgecolor='gray', label='No Fraude (9,995)'),
        mpatches.Patch(facecolor=COLORS['danger'], edgecolor='darkred', label='Fraude (5)'),
    ]
    ax.legend(handles=legend_elements, loc='lower center', fontsize=10,
              ncol=2, bbox_to_anchor=(0.5, -0.12))

    # Panel derecho: Barra de accuracy
    ax = axes[1]
    categories = ['Accuracy\n"Siempre No Fraude"', 'Detección\nde Fraude Real']
    values = [99.95, 0]
    colors = [COLORS['success'], COLORS['danger']]
    bars = ax.barh(categories, values, color=colors, height=0.5, edgecolor='white', linewidth=2)
    ax.set_xlim(0, 110)
    ax.set_title('La Paradoja', pad=10, fontsize=14)
    ax.set_xlabel('Porcentaje (%)')

    # Anotaciones
    ax.text(values[0] + 1, 0, f'{values[0]}%', va='center', fontsize=14, fontweight='bold', color=COLORS['success'])
    ax.text(values[1] + 1, 1, f'{values[1]}%', va='center', fontsize=14, fontweight='bold', color=COLORS['danger'])

    ax.text(55, 1.4, '¡99.95% de precisión\npero completamente inútil!',
            fontsize=11, color=COLORS['danger'], fontweight='bold', ha='center',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#FEE2E2', edgecolor=COLORS['danger']))

    fig.suptitle('La Paradoja del Fraude: Desbalance de Clases', fontsize=15, fontweight='bold', y=1.02)
    plt.tight_layout()
    save(fig, 'fraude_desbalance.png')


# ══════════════════════════════════════════════════════════════
# 7. Extracción Morfológica (L415) — Top 7
# ══════════════════════════════════════════════════════════════
def gen_morphological_extraction():
    print("[*] Generando: extraccion_morfologica.png")
    np.random.seed(42)

    # Simular señal tipo ECG
    t = np.linspace(0, 4, 1000)
    signal = np.zeros_like(t)

    # Crear patrón PQRST repetido
    for offset in [0, 1, 2, 3]:
        # P wave
        signal += 0.15 * np.exp(-((t - (0.15 + offset)) ** 2) / (2 * 0.01 ** 2))
        # Q dip
        signal -= 0.1 * np.exp(-((t - (0.25 + offset)) ** 2) / (2 * 0.005 ** 2))
        # R peak (tall)
        signal += 1.0 * np.exp(-((t - (0.3 + offset)) ** 2) / (2 * 0.005 ** 2))
        # S dip
        signal -= 0.2 * np.exp(-((t - (0.35 + offset)) ** 2) / (2 * 0.005 ** 2))
        # T wave
        signal += 0.3 * np.exp(-((t - (0.55 + offset)) ** 2) / (2 * 0.02 ** 2))

    # Añadir ruido
    signal += np.random.normal(0, 0.03, len(t))

    fig, ax = plt.subplots(figsize=(12, 4.5))
    ax.plot(t, signal, color=COLORS['primary'], lw=1.5, alpha=0.9, label='Señal ECG')

    # Detectar picos
    from scipy.signal import find_peaks
    peaks, props = find_peaks(signal, height=0.5, distance=200)
    valleys, _ = find_peaks(-signal, height=0.05, distance=200)

    ax.plot(t[peaks], signal[peaks], '^', color=COLORS['danger'], markersize=12,
            markeredgecolor='darkred', markeredgewidth=1.5, label=f'Picos R ({len(peaks)})', zorder=5)
    ax.plot(t[valleys], signal[valleys], 'v', color=COLORS['warning'], markersize=10,
            markeredgecolor='darkorange', markeredgewidth=1.5, label=f'Valles ({len(valleys)})', zorder=5)

    # Anotar amplitud en un pico
    if len(peaks) > 1:
        pk = peaks[1]
        ax.annotate(f'Amplitud\n= {signal[pk]:.2f}',
                    xy=(t[pk], signal[pk]), xytext=(t[pk] + 0.15, signal[pk] + 0.2),
                    fontsize=10, fontweight='bold', color=COLORS['danger'],
                    arrowprops=dict(arrowstyle='->', color=COLORS['danger'], lw=1.5))

    # Anotar intervalo R-R
    if len(peaks) >= 2:
        rr = t[peaks[1]] - t[peaks[0]]
        mid = (t[peaks[0]] + t[peaks[1]]) / 2
        y_annot = signal[peaks[0]] + 0.15
        ax.annotate('', xy=(t[peaks[0]], y_annot), xytext=(t[peaks[1]], y_annot),
                    arrowprops=dict(arrowstyle='<->', color=COLORS['secondary'], lw=2))
        ax.text(mid, y_annot + 0.08, f'Intervalo R-R = {rr:.2f}s',
                ha='center', fontsize=10, color=COLORS['secondary'], fontweight='bold')

    ax.set_title('Extracción Morfológica: Detección de Picos y Valles en Señal ECG', pad=12, fontsize=14)
    ax.set_xlabel('Tiempo (s)')
    ax.set_ylabel('Amplitud (mV)')
    ax.legend(loc='upper right', fontsize=10)
    ax.set_xlim(0, 4)

    plt.tight_layout()
    save(fig, 'extraccion_morfologica.png')


# ══════════════════════════════════════════════════════════════
# 8. Binary Coding (One-Hot) (L252) — Top 8
# ══════════════════════════════════════════════════════════════
def gen_onehot_table():
    print("[*] Generando: onehot_encoding.png")

    fig, axes = plt.subplots(1, 2, figsize=(12, 3.5), gridspec_kw={'width_ratios': [0.35, 0.65]})

    # Tabla original
    ax = axes[0]
    ax.axis('off')
    data_orig = [['Ana', 'Europa'], ['Luis', 'Asia'], ['María', 'América'], ['Pedro', 'Europa']]
    cols_orig = ['Nombre', 'Continente']
    table1 = ax.table(cellText=data_orig, colLabels=cols_orig, loc='center',
                       cellLoc='center', colColours=[COLORS['primary']]*2)
    table1.auto_set_font_size(False)
    table1.set_fontsize(12)
    table1.scale(1.2, 1.8)

    # Colorear header
    for key, cell in table1.get_celld().items():
        if key[0] == 0:
            cell.set_text_props(color='white', fontweight='bold')
            cell.set_facecolor(COLORS['primary'])
        else:
            cell.set_facecolor('#F0F4FF')
            cell.set_edgecolor('#D1D5DB')
        cell.set_edgecolor('#D1D5DB')

    ax.set_title('Datos Originales', pad=15, fontsize=13, fontweight='bold')

    # Flecha
    fig.text(0.37, 0.5, '→\nOne-Hot', ha='center', va='center', fontsize=14,
             fontweight='bold', color=COLORS['secondary'])

    # Tabla codificada
    ax = axes[1]
    ax.axis('off')
    data_enc = [
        ['Ana', '0', '1', '0'],
        ['Luis', '1', '0', '0'],
        ['María', '0', '0', '1'],
        ['Pedro', '0', '1', '0'],
    ]
    cols_enc = ['Nombre', 'cont_Asia', 'cont_Europa', 'cont_América']
    table2 = ax.table(cellText=data_enc, colLabels=cols_enc, loc='center',
                       cellLoc='center',
                       colColours=[COLORS['success']]*4)
    table2.auto_set_font_size(False)
    table2.set_fontsize(11)
    table2.scale(1.1, 1.8)

    for key, cell in table2.get_celld().items():
        if key[0] == 0:
            cell.set_text_props(color='white', fontweight='bold')
            cell.set_facecolor(COLORS['success'])
        else:
            # Resaltar las celdas con "1"
            row, col = key
            if col > 0 and row > 0 and data_enc[row-1][col] == '1':
                cell.set_facecolor('#D1FAE5')
            else:
                cell.set_facecolor('#F0FFF4')
            cell.set_edgecolor('#D1D5DB')
        cell.set_edgecolor('#D1D5DB')

    ax.set_title('Codificación One-Hot', pad=15, fontsize=13, fontweight='bold')

    fig.suptitle('Binary Coding: Conversión de Variable Categórica Nominal',
                 fontsize=14, fontweight='bold', y=1.05)
    plt.tight_layout()
    save(fig, 'onehot_encoding.png')


# ══════════════════════════════════════════════════════════════
# 9. El Efecto de las Magnitudes (L134) — Top 9
# ══════════════════════════════════════════════════════════════
def gen_magnitude_effect():
    print("[*] Generando: efecto_magnitudes.png")

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

    # Panel izquierdo: Coeficientes crudos
    ax = axes[0]
    variables = ['Edad\n(β = 50,000)', 'Ingreso\n(β = 0.05)']
    betas = [50_000, 0.05]
    bars = ax.bar(variables, betas, color=[COLORS['primary'], COLORS['warning']],
                  width=0.5, edgecolor='white', linewidth=2)
    ax.set_title('Coeficientes β Crudos', pad=10, fontsize=13)
    ax.set_ylabel('Valor del Coeficiente')
    ax.bar_label(bars, fmt=lambda x: f'{x:,.2f}' if x < 1 else f'{x:,.0f}', fontsize=11, fontweight='bold')

    # Anotación de confusión
    ax.annotate('¿1 millón de\nveces más\nimportante?',
                xy=(0.5, 25_000), fontsize=12, ha='center',
                color=COLORS['danger'], fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='#FEE2E2', edgecolor=COLORS['danger']))

    # Panel derecho: Impacto real equivalente
    ax = axes[1]
    scenarios = ['+1 año\nde Edad', '+$1M\nde Ingreso']
    impactos = [50_000, 50_000]
    bars2 = ax.bar(scenarios, impactos, color=[COLORS['primary'], COLORS['warning']],
                   width=0.5, edgecolor='white', linewidth=2)
    ax.set_title('Impacto Real en ŷ (Gasto)', pad=10, fontsize=13)
    ax.set_ylabel('Cambio en Gasto ($)')
    ax.bar_label(bars2, fmt=lambda x: f'+${x:,.0f}', fontsize=11, fontweight='bold')
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'${x:,.0f}'))

    # Anotación
    ax.annotate('¡Impacto\nIDÉNTICO!',
                xy=(0.5, 40_000), fontsize=13, ha='center',
                color=COLORS['success'], fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='#D1FAE5', edgecolor=COLORS['success']))

    fig.suptitle('Las Unidades Engañan: β Crudos vs Impacto Real', fontsize=15, fontweight='bold', y=1.02)
    plt.tight_layout()
    save(fig, 'efecto_magnitudes.png')


# ══════════════════════════════════════════════════════════════
# 10. Suavizado Funcional vs. Ventana (L485) — Top 10
# ══════════════════════════════════════════════════════════════
def gen_smoothing_comparison():
    print("[*] Generando: suavizado_comparacion.png")
    np.random.seed(42)

    t = np.linspace(0, 10, 300)
    signal_clean = 2 * np.sin(t) + 0.5 * np.sin(3 * t)
    noise = np.random.normal(0, 0.5, len(t))
    signal_noisy = signal_clean + noise

    # Rolling mean (ventana = 15)
    s = pd.Series(signal_noisy)
    rolling = s.rolling(window=15, center=False).mean()

    # Suavizado funcional (spline cúbico)
    from scipy.interpolate import UnivariateSpline
    spline = UnivariateSpline(t, signal_noisy, s=len(t) * 0.25)
    smooth_func = spline(t)

    fig, ax = plt.subplots(figsize=(12, 5))

    ax.plot(t, signal_noisy, color=COLORS['gray'], alpha=0.4, lw=1, label='Señal con ruido', zorder=1)
    ax.plot(t, smooth_func, color=COLORS['primary'], lw=2.5, label='Suavizado Funcional (Spline)', zorder=3)
    ax.plot(t, rolling.values, color=COLORS['warning'], lw=2.5, linestyle='--', label='Ventana Móvil (k=15)', zorder=2)

    # Marcar NaN zone
    ax.axvspan(t[0], t[14], alpha=0.15, color=COLORS['danger'], label='Zona NaN (Rolling)')
    ax.text(t[7], ax.get_ylim()[1] * 0.85, 'NaN', fontsize=11, ha='center',
            color=COLORS['danger'], fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor=COLORS['danger']))

    # Marcar desfase
    # Encontrar un pico en la señal original
    peak_idx = 47  # aprox primer pico de sin
    ax.annotate('Desfase →',
                xy=(t[peak_idx + 7], rolling.values[peak_idx + 7] if not np.isnan(rolling.values[peak_idx + 7]) else 0),
                xytext=(t[peak_idx] - 0.8, 2.0),
                fontsize=10, color=COLORS['warning'], fontweight='bold',
                arrowprops=dict(arrowstyle='->', color=COLORS['warning'], lw=2))

    ax.set_title('Suavizado Funcional (Spline) vs Ventana Móvil (Rolling Mean)', pad=12, fontsize=14)
    ax.set_xlabel('Tiempo')
    ax.set_ylabel('Amplitud')
    ax.legend(loc='lower right', fontsize=10)

    plt.tight_layout()
    save(fig, 'suavizado_comparacion.png')


# ══════════════════════════════════════════════════════════════
# Ejecutar todas las generaciones
# ══════════════════════════════════════════════════════════════
if __name__ == '__main__':
    print("=" * 60)
    print("  Generando imágenes Top 10 — Vista Minable")
    print("=" * 60)

    gen_outlier_effect()         # Top 3
    gen_log_transform()          # Top 4
    gen_discretization_challenge()  # Top 5
    gen_fraud_waffle()           # Top 6
    gen_morphological_extraction()  # Top 7
    gen_onehot_table()           # Top 8
    gen_magnitude_effect()       # Top 9
    gen_smoothing_comparison()   # Top 10

    print("\n" + "=" * 60)
    print("  ✅ ¡Todas las imágenes Top 10 (Python) generadas!")
    print("=" * 60)
