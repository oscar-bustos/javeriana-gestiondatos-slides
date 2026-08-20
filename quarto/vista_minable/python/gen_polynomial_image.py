"""
Generador de imagen — Transformacion Polinomica (Separacion de Dona / Circulos Concentricos).
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os
from sklearn.datasets import make_circles

OUTPUT_DIR = r"c:\Users\olbus\Git\Javeriana\javeriana-gestiondatos-slides\quarto\vista_minable\assets"

COLORS = {
    'primary': '#1A56DB',    # Azul (Centro)
    'danger': '#F05252',     # Rojo/Coral (Dona exterior)
    'success': '#0E9F6E',    # Verde (Frontera)
    'dark': '#1F2937',
    'light': '#F3F4F6',
    'gray': '#6B7280',
}

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Segoe UI', 'Helvetica', 'Arial'],
    'font.size': 11,
    'axes.titlesize': 13,
    'axes.titleweight': 'bold',
    'axes.labelsize': 11,
    'figure.facecolor': 'white',
    'axes.facecolor': '#FAFBFC',
    'axes.grid': True,
    'grid.alpha': 0.3,
    'grid.linestyle': '--',
    'savefig.dpi': 200,
    'savefig.bbox': 'tight',
    'savefig.pad_inches': 0.2,
})

def gen_polynomial_donut():
    print("[*] Generando: transformacion_polinomica.png")
    np.random.seed(42)
    
    # 1. Generar datos tipo Dona / Circulos concentricos
    X, y = make_circles(n_samples=350, factor=0.4, noise=0.08, random_state=42)
    
    fig = plt.figure(figsize=(13, 5))
    
    # Panel 1: Espacio Original 2D (x1, x2)
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.scatter(X[y == 0, 0], X[y == 0, 1], color=COLORS['danger'], label='Clase 1: Dona Exterior', alpha=0.75, s=35, edgecolors='none')
    ax1.scatter(X[y == 1, 0], X[y == 1, 1], color=COLORS['primary'], label='Clase 0: Centro', alpha=0.85, s=35, edgecolors='none')
    
    # Linea de corte imposible
    ax1.plot([-1.4, 1.4], [0.6, -0.6], linestyle='--', color=COLORS['gray'], lw=2, label='Separador lineal (Falla)')
    
    ax1.set_title("1. Espacio Original: $(x_1, x_2)$\nNo separable linealmente", pad=10)
    ax1.set_xlabel("$x_1$")
    ax1.set_ylabel("$x_2$")
    ax1.set_xlim(-1.4, 1.4)
    ax1.set_ylim(-1.4, 1.4)
    ax1.legend(loc='lower left', fontsize=9, framealpha=0.9)
    ax1.set_aspect('equal')
    
    # Panel 2: Espacio Polinomico de Grado 2 (x1^2, x2^2)
    ax2 = fig.add_subplot(1, 2, 2)
    x1_sq = X[:, 0]**2
    x2_sq = X[:, 1]**2
    
    ax2.scatter(x1_sq[y == 0], x2_sq[y == 0], color=COLORS['danger'], label='Clase 1: Dona Exterior', alpha=0.75, s=35, edgecolors='none')
    ax2.scatter(x1_sq[y == 1], x2_sq[y == 1], color=COLORS['primary'], label='Clase 0: Centro', alpha=0.85, s=35, edgecolors='none')
    
    # Frontera de decision lineal en el espacio transformado: x1^2 + x2^2 = r^2
    u_vals = np.linspace(0, 0.9, 100)
    v_vals = 0.38 - u_vals
    ax2.plot(u_vals, v_vals, color=COLORS['success'], lw=2.5, linestyle='-', label='Frontera Lineal: $x_1^2 + x_2^2 = c$')
    
    ax2.annotate('Separable por un\nhiperplano lineal!',
                 xy=(0.18, 0.20), xytext=(0.45, 0.65),
                 fontsize=10, fontweight='bold', color=COLORS['success'],
                 arrowprops=dict(arrowstyle='->', color=COLORS['success'], lw=2),
                 bbox=dict(boxstyle='round,pad=0.4', facecolor='#ECFDF5', edgecolor=COLORS['success']))

    ax2.set_title("2. Espacio Transformado: $(x_1^2, x_2^2)$\nLinealmente separable!", pad=10)
    ax2.set_xlabel("$x_1^2$ (Cuadrado de $x_1$)")
    ax2.set_ylabel("$x_2^2$ (Cuadrado de $x_2$)")
    ax2.set_xlim(-0.05, 1.4)
    ax2.set_ylim(-0.05, 1.4)
    ax2.legend(loc='upper right', fontsize=9, framealpha=0.9)
    ax2.set_aspect('equal')
    
    fig.suptitle('Transformacion Polinomica (Grado 2): Resolviendo No-Linealidad con Modelos Lineales', fontsize=14, fontweight='bold', y=1.03)
    
    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, "transformacion_polinomica.png")
    fig.savefig(out_path, dpi=200, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f"  [OK] Guardado: {out_path}")

if __name__ == '__main__':
    gen_polynomial_donut()
