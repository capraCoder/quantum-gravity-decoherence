import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Publication styling
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 10
rcParams['axes.linewidth'] = 0.8

theta = np.linspace(0, 90, 200)
gamma_ratio = np.cos(np.radians(theta))**2

fig, ax = plt.subplots(figsize=(4.5, 3.2))

# Main curve
ax.plot(theta, gamma_ratio, 'k-', linewidth=1.8)

# Key points
key_angles = [0, 45, 90]
key_values = [1.0, 0.5, 0.0]
ax.scatter(key_angles, key_values, color='black', s=40, zorder=5)

# Annotations - minimal, clear
ax.annotate('Position', xy=(0, 1.0), xytext=(3, 1.05),
            fontsize=9, ha='left', va='bottom')
ax.annotate(r'$\Gamma_0/2$', xy=(45, 0.5), xytext=(47, 0.54),
            fontsize=9, ha='left', va='bottom')
ax.annotate('Momentum', xy=(90, 0.0), xytext=(90, 0.06),
            fontsize=9, ha='right', va='bottom')

# Reference line
ax.axhline(y=0.5, color='gray', linestyle=':', linewidth=0.8, alpha=0.6)

# Axis labels
ax.set_xlabel(r'Measurement basis angle $\theta$ (degrees)', fontsize=10)
ax.set_ylabel(r'$\Gamma(\theta)\,/\,\Gamma_0$', fontsize=10)

# Axis configuration
ax.set_xlim(0, 90)
ax.set_ylim(0, 1.12)
ax.set_xticks([0, 30, 45, 60, 90])
ax.set_yticks([0, 0.25, 0.5, 0.75, 1.0])

# Clean spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Equation in plot
ax.text(55, 0.85, r'$\Gamma(\theta) = \Gamma_0 \cos^2\theta$',
        fontsize=10, ha='left', style='italic')

plt.tight_layout()
plt.savefig('D:/quantum-gravity-paper/figures/figure1.pdf', dpi=300, bbox_inches='tight')
plt.savefig('D:/quantum-gravity-paper/figures/figure1.png', dpi=300, bbox_inches='tight')
print("Figure saved: figure1.pdf and figure1.png")
