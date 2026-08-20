"""
Generador de imagenes — Vista Minable (Batch 2: Restantes Python).
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
import os

OUTPUT_DIR = r"c:\Users\olbus\Git\Javeriana\javeriana-gestiondatos-slides\quarto\vista_minable\assets"

COLORS = {
    'primary': '#1A56DB',
    'secondary': '#7E3AF2',
    'accent': '#E74694',
    'success': '#0E9F6E',
    'warning': '#FF8A4C',
    'danger': '#F05252',
    'dark': '#1F2937',
    'light': '#F3F4F6',
    'gray': '#6B7280',
    'gold': '#FBBF24',
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
    print(f"  [OK] Guardado: {name}")


# ── Normalización Min-Max (L162) ──
def gen_minmax_before_after():
    print("[*] Generando: minmax_before_after.png")
    np.random.seed(42)
    edad = np.random.randint(18, 70, 200)
    ingresos = np.random.normal(3_500_000, 1_200_000, 200)
    ingresos = np.clip(ingresos, 500_000, 10_000_000)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

    ax = axes[0]
    ax.hist(edad, bins=20, color=COLORS['primary'], alpha=0.7, edgecolor='white', label='Edad')
    ax2 = ax.twinx()
    ax2.hist(ingresos / 1e6, bins=20, color=COLORS['warning'], alpha=0.5, edgecolor='white', label='Ingresos (M$)')
    ax.set_title('Escalas Originales', pad=10)
    ax.set_xlabel('Valor')
    ax.set_ylabel('Frecuencia (Edad)', color=COLORS['primary'])
    ax2.set_ylabel('Frecuencia (Ingresos)', color=COLORS['warning'])
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, fontsize=9, loc='upper right')

    # Normalizar
    edad_norm = (edad - edad.min()) / (edad.max() - edad.min())
    ing_norm = (ingresos - ingresos.min()) / (ingresos.max() - ingresos.min())

    ax = axes[1]
    ax.hist(edad_norm, bins=20, color=COLORS['primary'], alpha=0.7, edgecolor='white', label='Edad [0,1]')
    ax.hist(ing_norm, bins=20, color=COLORS['warning'], alpha=0.5, edgecolor='white', label='Ingresos [0,1]')
    ax.set_title('Despues de Min-Max [0, 1]', pad=10)
    ax.set_xlabel('Valor Normalizado')
    ax.set_ylabel('Frecuencia')
    ax.legend(fontsize=9)

    fig.suptitle('Normalizacion Min-Max: Misma Escala para Todas las Variables', fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    save(fig, 'minmax_before_after.png')


# ── Estandarización Z-Score (L183) ──
def gen_zscore_distribution():
    print("[*] Generando: zscore_distribucion.png")
    np.random.seed(42)
    datos_orig = np.random.normal(170, 15, 5000)  # Estatura cm
    datos_z = (datos_orig - datos_orig.mean()) / datos_orig.std()

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))

    ax = axes[0]
    ax.hist(datos_orig, bins=40, color=COLORS['secondary'], alpha=0.7, edgecolor='white', density=True)
    ax.axvline(datos_orig.mean(), color=COLORS['dark'], linestyle='--', lw=2,
               label=f'Media = {datos_orig.mean():.0f} cm')
    ax.set_title('Distribucion Original', pad=10)
    ax.set_xlabel('Estatura (cm)')
    ax.set_ylabel('Densidad')
    ax.legend(fontsize=9)

    ax = axes[1]
    ax.hist(datos_z, bins=40, color=COLORS['primary'], alpha=0.7, edgecolor='white', density=True)
    ax.axvline(0, color=COLORS['danger'], linestyle='--', lw=2, label='Media = 0')
    # Marcar sigmas
    for sigma in [-3, -2, -1, 1, 2, 3]:
        ax.axvline(sigma, color=COLORS['gray'], linestyle=':', lw=1, alpha=0.6)
        ax.text(sigma, ax.get_ylim()[1] * 0.95 if ax.get_ylim()[1] > 0 else 0.3,
                f'{sigma}s', ha='center', fontsize=9, color=COLORS['gray'])
    ax.set_title('Despues de Z-Score', pad=10)
    ax.set_xlabel('Desviaciones Estandar (z)')
    ax.set_ylabel('Densidad')
    ax.legend(fontsize=9)

    fig.suptitle('Estandarizacion Z-Score: Centrar en 0 y Escalar por Sigma', fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    save(fig, 'zscore_distribucion.png')


# ── Normalización vs. Estandarización (L193) ──
def gen_norm_vs_std():
    print("[*] Generando: norm_vs_estandarizacion.png")
    np.random.seed(42)
    np.random.seed(42)
    data = {
        'Edad': np.random.randint(18, 70, 100).astype(float),
        'Ingresos': np.random.normal(4e6, 2e6, 100),
        'Horas_Trabajo': np.random.normal(42, 8, 100)
    }
    df = pd.DataFrame(data)

    from sklearn.preprocessing import MinMaxScaler, StandardScaler
    minmax = MinMaxScaler()
    zscore = StandardScaler()
    df_mm = pd.DataFrame(minmax.fit_transform(df), columns=df.columns)
    df_zs = pd.DataFrame(zscore.fit_transform(df), columns=df.columns)

    fig, axes = plt.subplots(1, 3, figsize=(14, 4.5))

    # Original
    bp0 = axes[0].boxplot([df[c] for c in df.columns], tick_labels=['Edad', 'Ingresos', 'Horas'],
                          patch_artist=True, medianprops=dict(color='red', linewidth=2))
    for patch, color in zip(bp0['boxes'], [COLORS['primary'], COLORS['warning'], COLORS['success']]):
        patch.set_facecolor(color)
        patch.set_alpha(0.6)
    axes[0].set_title('Datos Originales', pad=10)
    axes[0].set_ylabel('Valor')

    # Min-Max
    bp1 = axes[1].boxplot([df_mm[c] for c in df_mm.columns], tick_labels=['Edad', 'Ingresos', 'Horas'],
                          patch_artist=True, medianprops=dict(color='red', linewidth=2))
    for patch, color in zip(bp1['boxes'], [COLORS['primary'], COLORS['warning'], COLORS['success']]):
        patch.set_facecolor(color)
        patch.set_alpha(0.6)
    axes[1].set_title('Min-Max [0, 1]', pad=10)
    axes[1].set_ylabel('Valor Normalizado')

    # Z-Score
    bp2 = axes[2].boxplot([df_zs[c] for c in df_zs.columns], tick_labels=['Edad', 'Ingresos', 'Horas'],
                          patch_artist=True, medianprops=dict(color='red', linewidth=2))
    for patch, color in zip(bp2['boxes'], [COLORS['primary'], COLORS['warning'], COLORS['success']]):
        patch.set_facecolor(color)
        patch.set_alpha(0.6)
    axes[2].set_title('Z-Score (mu=0, sigma=1)', pad=10)
    axes[2].set_ylabel('Valor Estandarizado')

    fig.suptitle('Comparacion: Datos Originales vs Min-Max vs Z-Score', fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    save(fig, 'norm_vs_estandarizacion.png')


# ── Gradiente Descendente (L147) ──
def gen_gradient_contour():
    print("[*] Generando: gradiente_descendente.png")
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # Sin escalar (elipse)
    x = np.linspace(-5, 5, 200)
    y = np.linspace(-5, 5, 200)
    X, Y = np.meshgrid(x, y)
    Z = 10 * X**2 + Y**2  # eliptica

    ax = axes[0]
    ax.contour(X, Y, Z, levels=15, cmap='RdYlBu_r', linewidths=1.5)
    # Simular trayectoria zigzag
    path_x = [4, 3.5, -2, -1.5, 1, 0.8, -0.3, -0.2, 0.1, 0]
    path_y = [4, -3, 2.5, -2, 1.5, -1, 0.5, -0.3, 0.1, 0]
    ax.plot(path_x, path_y, 'o-', color=COLORS['danger'], markersize=5, lw=2, alpha=0.8)
    ax.plot(path_x[0], path_y[0], 's', color=COLORS['warning'], markersize=12, zorder=5, label='Inicio')
    ax.plot(0, 0, '*', color=COLORS['success'], markersize=15, zorder=5, label='Minimo')
    ax.set_title('Sin Escalar (Eliptica)', pad=10)
    ax.set_xlabel('Variable 1')
    ax.set_ylabel('Variable 2')
    ax.legend(fontsize=9)
    ax.set_aspect('equal')

    # Escalado (circular)
    Z2 = X**2 + Y**2

    ax = axes[1]
    ax.contour(X, Y, Z2, levels=15, cmap='RdYlBu_r', linewidths=1.5)
    # Trayectoria directa
    path_x2 = [4, 2.5, 1.5, 0.8, 0.3, 0]
    path_y2 = [4, 2.5, 1.5, 0.8, 0.3, 0]
    ax.plot(path_x2, path_y2, 'o-', color=COLORS['success'], markersize=5, lw=2, alpha=0.8)
    ax.plot(path_x2[0], path_y2[0], 's', color=COLORS['warning'], markersize=12, zorder=5, label='Inicio')
    ax.plot(0, 0, '*', color=COLORS['success'], markersize=15, zorder=5, label='Minimo')
    ax.set_title('Escalado (Circular)', pad=10)
    ax.set_xlabel('Variable 1')
    ax.set_ylabel('Variable 2')
    ax.legend(fontsize=9)
    ax.set_aspect('equal')

    fig.suptitle('Descenso de Gradiente: Efecto del Escalamiento en la Convergencia', fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    save(fig, 'gradiente_descendente.png')


# ── De Numérico a Categórico (L309) ──
def gen_numeric_to_cat():
    print("[*] Generando: numerico_a_categorico.png")
    np.random.seed(42)
    horas = np.random.normal(42, 10, 500)
    horas = np.clip(horas, 10, 80)

    fig, ax = plt.subplots(figsize=(10, 4.5))
    n, bins, patches = ax.hist(horas, bins=40, color=COLORS['gray'], alpha=0.4, edgecolor='white')

    # Colorear por bin
    corte = 40
    for patch, left_edge in zip(patches, bins[:-1]):
        if left_edge < corte:
            patch.set_facecolor(COLORS['primary'])
            patch.set_alpha(0.7)
        else:
            patch.set_facecolor(COLORS['warning'])
            patch.set_alpha(0.7)

    ax.axvline(corte, color=COLORS['danger'], linestyle='--', lw=3, label=f'Punto de corte: {corte}h')
    ax.text(28, max(n) * 0.8, 'Jornada Normal\n(<=40h)', fontsize=12, ha='center',
            color=COLORS['primary'], fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor=COLORS['primary']))
    ax.text(55, max(n) * 0.8, 'Sobretiempo\n(>40h)', fontsize=12, ha='center',
            color=COLORS['warning'], fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='white', edgecolor=COLORS['warning']))

    ax.set_title('Discretizacion: De Variable Continua a Categorica', pad=10, fontsize=14)
    ax.set_xlabel('Horas Trabajadas por Semana')
    ax.set_ylabel('Frecuencia')
    ax.legend(fontsize=10)
    plt.tight_layout()
    save(fig, 'numerico_a_categorico.png')


# ── Tipos de Discretización (L329) ──
def gen_discretization_types():
    print("[*] Generando: tipos_discretizacion.png")
    np.random.seed(42)
    ingresos = np.concatenate([
        np.random.normal(1_500_000, 400_000, 6000),
        np.random.normal(4_000_000, 1_000_000, 2500),
        np.random.normal(12_000_000, 3_000_000, 1000),
        np.random.normal(40_000_000, 10_000_000, 500)
    ])
    ingresos = ingresos[ingresos > 0] / 1e6

    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))

    # Equal Width
    ax = axes[0]
    ax.hist(ingresos, bins=40, color=COLORS['primary'], alpha=0.5, edgecolor='white')
    ew_bins = np.linspace(ingresos.min(), ingresos.max(), 5)
    for b in ew_bins[1:-1]:
        ax.axvline(b, color=COLORS['danger'], linestyle='--', lw=2)
    ax.set_title('Equal Width', pad=10, fontsize=13)
    ax.set_xlabel('Ingreso (M$)')
    ax.set_ylabel('Frecuencia')

    # Equal Frequency
    ax = axes[1]
    ax.hist(ingresos, bins=40, color=COLORS['success'], alpha=0.5, edgecolor='white')
    ef_bins = np.percentile(ingresos, [25, 50, 75])
    for b in ef_bins:
        ax.axvline(b, color=COLORS['danger'], linestyle='--', lw=2)
    ax.set_title('Equal Frequency (Cuantiles)', pad=10, fontsize=13)
    ax.set_xlabel('Ingreso (M$)')

    # Ad-hoc
    ax = axes[2]
    ax.hist(ingresos, bins=40, color=COLORS['secondary'], alpha=0.5, edgecolor='white')
    adhoc_bins = [1.3, 3.0, 8.0]  # SMLV, clase media, alto
    labels_adhoc = ['Bajo', 'Medio', 'Alto', 'Premium']
    for i, b in enumerate(adhoc_bins):
        ax.axvline(b, color=COLORS['danger'], linestyle='--', lw=2)
        ax.text(b, ax.get_ylim()[1] * 0.9, f'${b}M', ha='center', fontsize=9, color=COLORS['danger'])
    ax.set_title('Ad-hoc (Negocio)', pad=10, fontsize=13)
    ax.set_xlabel('Ingreso (M$)')

    fig.suptitle('Tres Estrategias de Discretizacion con la Misma Variable', fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    save(fig, 'tipos_discretizacion.png')


# ── Variables de Negocio / DTI (L374) ──
def gen_dti_scatter():
    print("[*] Generando: dti_scatter.png")
    np.random.seed(42)
    n = 300
    ingreso = np.random.uniform(1_500_000, 15_000_000, n)
    # Impagos tienden a tener DTI alto
    dti_buenos = np.random.uniform(0.05, 0.35, n // 2)
    dti_malos = np.random.uniform(0.25, 0.8, n // 2)
    dti = np.concatenate([dti_buenos, dti_malos])
    cuota = ingreso * dti
    labels = np.array(['Paga'] * (n // 2) + ['Impago'] * (n // 2))

    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # Sin DTI
    ax = axes[0]
    mask_paga = labels == 'Paga'
    ax.scatter(ingreso[mask_paga] / 1e6, cuota[mask_paga] / 1e6,
               c=COLORS['primary'], alpha=0.5, s=30, label='Paga')
    ax.scatter(ingreso[~mask_paga] / 1e6, cuota[~mask_paga] / 1e6,
               c=COLORS['danger'], alpha=0.5, s=30, label='Impago')
    ax.set_title('Variables Originales', pad=10)
    ax.set_xlabel('Ingreso (M$)')
    ax.set_ylabel('Cuota (M$)')
    ax.legend(fontsize=10)
    ax.text(0.5, 0.95, 'Clases mezcladas', transform=ax.transAxes,
            fontsize=11, ha='center', va='top', color=COLORS['danger'], fontweight='bold')

    # Con DTI
    ax = axes[1]
    ax.scatter(range(n // 2), dti_buenos,
               c=COLORS['primary'], alpha=0.6, s=30, label='Paga')
    ax.scatter(range(n // 2, n), dti_malos,
               c=COLORS['danger'], alpha=0.6, s=30, label='Impago')
    ax.axhline(0.4, color=COLORS['success'], linestyle='--', lw=2, label='Umbral DTI = 0.4')
    ax.set_title('Variable Sintetica: DTI', pad=10)
    ax.set_xlabel('Registro')
    ax.set_ylabel('DTI = Cuota / Ingreso')
    ax.legend(fontsize=10)
    ax.text(0.5, 0.95, 'Clases separadas!', transform=ax.transAxes,
            fontsize=11, ha='center', va='top', color=COLORS['success'], fontweight='bold')

    fig.suptitle('Ingenieria de Caracteristicas: Debt-to-Income (DTI)', fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    save(fig, 'dti_scatter.png')


# ── Señales en Marcas de Tiempo (L396) ──
def gen_timestamp_decomposition():
    print("[*] Generando: timestamp_descomposicion.png")

    fig, ax = plt.subplots(figsize=(12, 5))
    ax.axis('off')

    # Timestamp central
    ax.text(0.5, 0.88, '2026-08-17  03:25:00', fontsize=22, fontweight='bold',
            ha='center', va='center', color=COLORS['dark'],
            bbox=dict(boxstyle='round,pad=0.6', facecolor=COLORS['light'], edgecolor=COLORS['primary'], lw=2))

    # Flechas y variables extraidas
    features = [
        (0.10, 0.45, 'Hora = 3', 'Madrugada', COLORS['secondary']),
        (0.30, 0.45, 'Dia Semana', 'Domingo', COLORS['primary']),
        (0.50, 0.45, 'Es Festivo?', 'Si', COLORS['success']),
        (0.70, 0.45, 'Es Nocturna?', 'Si (00-06h)', COLORS['danger']),
        (0.90, 0.45, 'Fin de Mes?', 'No (dia 17)', COLORS['warning']),
    ]

    for x, y, label, value, color in features:
        ax.annotate('', xy=(x, y + 0.12), xytext=(0.5, 0.75),
                    arrowprops=dict(arrowstyle='->', color=color, lw=2))
        ax.text(x, y, label, fontsize=13, fontweight='bold', ha='center', va='center',
                bbox=dict(boxstyle='round,pad=0.4', facecolor='white', edgecolor=color, lw=2))
        ax.text(x, y - 0.12, value, fontsize=11, ha='center', va='center', color=color, fontweight='bold')

    # Titulo
    ax.text(0.5, 0.15, 'Feature Extraction: de 1 columna de timestamp se extraen 5+ variables predictivas',
            fontsize=12, ha='center', va='center', color=COLORS['gray'], style='italic')

    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(0, 1)
    fig.suptitle('Descomposicion de Marca de Tiempo para Modelo Antifraude', fontsize=14, fontweight='bold')
    save(fig, 'timestamp_descomposicion.png')


# ── Transformación Logarítmica curva (L456) ──
def gen_log_curve():
    print("[*] Generando: curva_logaritmica.png")
    x = np.linspace(0.1, 100, 1000)
    y_log = np.log(x + 1)
    y_identity = x

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(x, y_identity, color=COLORS['gray'], linestyle='--', lw=2, alpha=0.6, label='y = x (identidad)')
    ax.plot(x, y_log, color=COLORS['primary'], lw=3, label='y = log(x + 1)')
    ax.fill_between(x, y_log, y_identity, alpha=0.1, color=COLORS['primary'])

    # Anotar compresion
    ax.annotate('Comprime\nvalores altos', xy=(80, np.log(81)), xytext=(60, 3.0),
                fontsize=11, fontweight='bold', color=COLORS['danger'],
                arrowprops=dict(arrowstyle='->', color=COLORS['danger'], lw=2))
    ax.annotate('Expande\nvalores bajos', xy=(5, np.log(6)), xytext=(20, 1.0),
                fontsize=11, fontweight='bold', color=COLORS['success'],
                arrowprops=dict(arrowstyle='->', color=COLORS['success'], lw=2))

    ax.set_title('Efecto de la Transformacion Logaritmica', pad=10, fontsize=14)
    ax.set_xlabel('Valor Original (x)')
    ax.set_ylabel('Valor Transformado')
    ax.legend(fontsize=11)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 10)
    plt.tight_layout()
    save(fig, 'curva_logaritmica.png')


# ── Detección de Ruido en Sensores (L466) ──
def gen_sensor_noise():
    print("[*] Generando: ruido_sensor.png")
    np.random.seed(42)
    t = np.arange(0, 120, 1)  # 120 segundos
    temp = 75 + 3 * np.sin(t * 0.1) + np.random.normal(0, 0.8, len(t))
    # Insertar spike de ruido
    spike_idx = 65
    temp[spike_idx] = 130  # spike aislado

    fig, ax = plt.subplots(figsize=(12, 4.5))
    ax.plot(t, temp, color=COLORS['primary'], lw=1.5, label='Temperatura Sensor')
    ax.plot(t[spike_idx], temp[spike_idx], 'o', color=COLORS['danger'], markersize=14,
            markeredgecolor='darkred', markeredgewidth=2, label='Lectura Anomala', zorder=5)

    # Ventana de suavizado
    window_start, window_end = spike_idx - 10, spike_idx + 10
    ax.axvspan(t[window_start], t[window_end], alpha=0.15, color=COLORS['warning'], label='Ventana de Analisis')

    ax.annotate('Spike: 130C?\nRuido electrico\no alerta real?',
                xy=(t[spike_idx], temp[spike_idx]),
                xytext=(t[spike_idx] + 15, temp[spike_idx] - 10),
                fontsize=11, fontweight='bold', color=COLORS['danger'],
                arrowprops=dict(arrowstyle='->', color=COLORS['danger'], lw=2),
                bbox=dict(boxstyle='round', facecolor='#FEE2E2', edgecolor=COLORS['danger']))

    ax.set_title('Deteccion de Ruido en Sensor de Temperatura Industrial', pad=10, fontsize=14)
    ax.set_xlabel('Tiempo (s)')
    ax.set_ylabel('Temperatura (C)')
    ax.legend(fontsize=10, loc='lower right')
    plt.tight_layout()
    save(fig, 'ruido_sensor.png')


# ── Suavizado por Ventana Móvil (L505) ──
def gen_rolling_mean():
    print("[*] Generando: rolling_mean.png")
    np.random.seed(42)
    t = np.arange(100)
    signal = 5 * np.sin(t * 0.15) + np.random.normal(0, 1.5, len(t))

    s = pd.Series(signal)
    rolling5 = s.rolling(window=5).mean()
    ewm = s.ewm(alpha=0.2).mean()

    fig, ax = plt.subplots(figsize=(12, 4.5))
    ax.plot(t, signal, color=COLORS['gray'], alpha=0.4, lw=1, label='Senal original')
    ax.plot(t, rolling5, color=COLORS['primary'], lw=2.5, label='Rolling Mean (k=5)')
    ax.plot(t, ewm, color=COLORS['warning'], lw=2.5, linestyle='--', label='EWM (alpha=0.2)')

    # Marcar NaN
    ax.axvspan(0, 4, alpha=0.2, color=COLORS['danger'])
    ax.text(2, ax.get_ylim()[1] * 0.85, 'NaN', fontsize=11, ha='center',
            color=COLORS['danger'], fontweight='bold')

    ax.set_title('Suavizado: Media Movil vs Exponencial Ponderada', pad=10, fontsize=14)
    ax.set_xlabel('Observacion')
    ax.set_ylabel('Valor')
    ax.legend(fontsize=10)
    plt.tight_layout()
    save(fig, 'rolling_mean.png')


# ── Agregación Temporal (L518) ──
def gen_temporal_aggregation():
    print("[*] Generando: agregacion_temporal.png")
    np.random.seed(42)
    dates = pd.date_range('2025-01-01', periods=180, freq='D')
    daily = 50 + 15 * np.sin(np.arange(180) * 0.1) + np.random.normal(0, 8, 180)
    df = pd.DataFrame({'fecha': dates, 'casos': daily})
    df.set_index('fecha', inplace=True)
    weekly = df.resample('W').sum()

    fig, axes = plt.subplots(2, 1, figsize=(12, 6), sharex=False)

    ax = axes[0]
    ax.bar(df.index, df['casos'], color=COLORS['primary'], alpha=0.6, width=1)
    ax.set_title('Serie Diaria (Ruidosa)', pad=10, fontsize=13)
    ax.set_ylabel('Casos')

    ax = axes[1]
    ax.bar(weekly.index, weekly['casos'], color=COLORS['success'], alpha=0.7, width=5)
    ax.set_title('Serie Semanal (Agregada)', pad=10, fontsize=13)
    ax.set_ylabel('Casos Acumulados')
    ax.set_xlabel('Fecha')

    fig.suptitle('Agregacion Temporal: De Dias a Semanas', fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    save(fig, 'agregacion_temporal.png')


# ── Balanceo de Clases / SMOTE (L545) ──
def gen_smote_balance():
    print("[*] Generando: balanceo_smote.png")
    np.random.seed(42)
    # Clase mayoritaria
    X_maj = np.random.normal(3, 1.5, (200, 2))
    # Clase minoritaria
    X_min = np.random.normal(7, 0.8, (15, 2))

    # SMOTE sinteticos (simplificado)
    synth = []
    for _ in range(50):
        i, j = np.random.choice(len(X_min), 2, replace=False)
        alpha = np.random.random()
        synth.append(alpha * X_min[i] + (1 - alpha) * X_min[j])
    X_synth = np.array(synth)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    ax = axes[0]
    ax.scatter(X_maj[:, 0], X_maj[:, 1], c=COLORS['primary'], alpha=0.5, s=30, label='Mayoritaria (200)')
    ax.scatter(X_min[:, 0], X_min[:, 1], c=COLORS['danger'], s=60, zorder=3, label='Minoritaria (15)')
    ax.set_title('Antes: Desbalanceado', pad=10, fontsize=13)
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.legend(fontsize=10)

    ax = axes[1]
    ax.scatter(X_maj[:, 0], X_maj[:, 1], c=COLORS['primary'], alpha=0.5, s=30, label='Mayoritaria (200)')
    ax.scatter(X_min[:, 0], X_min[:, 1], c=COLORS['danger'], s=60, zorder=3, label='Minoritaria (15)')
    ax.scatter(X_synth[:, 0], X_synth[:, 1], c=COLORS['warning'], s=40, marker='D',
               alpha=0.7, zorder=2, label='Sinteticos SMOTE (50)')
    ax.set_title('Despues: SMOTE Aplicado', pad=10, fontsize=13)
    ax.set_xlabel('Feature 1')
    ax.set_ylabel('Feature 2')
    ax.legend(fontsize=10)

    fig.suptitle('Balanceo de Clases con SMOTE (Oversampling)', fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    save(fig, 'balanceo_smote.png')


# ── Biplot PCA (L436) ──
def gen_pca_biplot():
    print("[*] Generando: pca_biplot.png")
    np.random.seed(42)
    n = 200
    X = np.random.multivariate_normal([5, 3, 7], [[3, 1.5, 0.5], [1.5, 2, 0.3], [0.5, 0.3, 4]], n)

    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler
    X_std = StandardScaler().fit_transform(X)
    pca = PCA(n_components=2)
    scores = pca.fit_transform(X_std)

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(scores[:, 0], scores[:, 1], c=COLORS['primary'], alpha=0.4, s=30)

    # Vectores de carga
    feature_names = ['Var_1', 'Var_2', 'Var_3']
    colors_vec = [COLORS['danger'], COLORS['success'], COLORS['secondary']]
    scale = 3
    for i, (name, color) in enumerate(zip(feature_names, colors_vec)):
        ax.annotate('', xy=(pca.components_[0, i] * scale, pca.components_[1, i] * scale),
                    xytext=(0, 0),
                    arrowprops=dict(arrowstyle='->', color=color, lw=2.5))
        ax.text(pca.components_[0, i] * scale * 1.15, pca.components_[1, i] * scale * 1.15,
                name, fontsize=12, fontweight='bold', color=color)

    var_exp = pca.explained_variance_ratio_
    ax.set_xlabel(f'PC1 ({var_exp[0]*100:.1f}% varianza)', fontsize=12)
    ax.set_ylabel(f'PC2 ({var_exp[1]*100:.1f}% varianza)', fontsize=12)
    ax.set_title('Biplot PCA: Reduccion como Extraccion', pad=10, fontsize=14)
    ax.axhline(0, color='gray', lw=0.5)
    ax.axvline(0, color='gray', lw=0.5)
    plt.tight_layout()
    save(fig, 'pca_biplot.png')


# ── Ejecutar todo ──
if __name__ == '__main__':
    print("=" * 60)
    print("  Generando imagenes Batch 2 — Vista Minable")
    print("=" * 60)

    gen_minmax_before_after()
    gen_zscore_distribution()
    gen_norm_vs_std()
    gen_gradient_contour()
    gen_numeric_to_cat()
    gen_discretization_types()
    gen_dti_scatter()
    gen_timestamp_decomposition()
    gen_log_curve()
    gen_sensor_noise()
    gen_rolling_mean()
    gen_temporal_aggregation()
    gen_smote_balance()
    gen_pca_biplot()

    print("\n" + "=" * 60)
    print("  [OK] Todas las imagenes Batch 2 generadas!")
    print("=" * 60)
