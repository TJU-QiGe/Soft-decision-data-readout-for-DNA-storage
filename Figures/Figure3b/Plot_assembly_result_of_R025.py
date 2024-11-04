import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib.ticker import FuncFormatter, LogFormatterSciNotation

# Set font and style
mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42
mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams['font.size'] = 8
mpl.rcParams['font.weight'] = 'regular'
mpl.rcParams['axes.linewidth'] = 0.75

# Load data from CSV files
def load_data(file):
    return pd.read_csv(file, index_col=0)

# Format percentage function
def percent_formatter(x, pos):
    return f'{x * 100:.0f}'

def bar_percent_formatter(x, pos):
    return f'{x * 100:.1f}'

# Initialize figure and axis
fig, ax1 = plt.subplots(figsize=(3.1, 1.6))
ax2 = ax1.twinx()

# Load bar chart data
bar_data = load_data('R025_plasmidA_consensus_bit_error.csv')
bar_colors = [(92/255,111/255,180/255)]
# (164/255,179/255,212/255)
x = np.arange(len(bar_data.columns))  # Read numbers
width = 0.4  # Bar width

# Plot bar chart
for i, color in enumerate(bar_colors):
    error_rate = bar_data.loc['soft'].astype(float)
    ax1.bar(x + width/2, error_rate, width * 0.95, color=color)

# Load line chart data
line_data = load_data('R025_plasmidA_recovery_rate.csv')
line_colors = [(252/255,141/255,58/255)]
# (92/255,111/255,180/255)
line_markers = ['^']
line_styles = ['-']

# Plot line chart
for i, (color, marker, linestyle) in enumerate(zip(line_colors, line_markers, line_styles)):
    recoverable_ratio = line_data.loc['soft'].astype(float)
    ax2.plot(x + width/2, recoverable_ratio, marker=marker, markersize=8, markeredgewidth=0.2, color=color, linestyle=linestyle, linewidth=0.75)

# Configure axes
# ax1.set_ylabel('Bit error rate (substitutions)', fontsize=10)
# ax1.set_yscale('log')
ax1.set_xlabel('Coverage', fontsize=10)
ax1.set_xticks(x + width/2)
ax1.set_xticklabels(['8.05×', '10.97×', '13.65×', '16.29×', '19.01×', '22.09×'], rotation=25)
# ax1.set_xticklabels(bar_data.columns)
# Set y-axis for bar chart to linear scale and format as percentage
ax1.set_ylim(0, 0.002)
ax1.set_yticks(np.arange(0, 0.0022, 0.001))
ax1.yaxis.set_major_formatter(FuncFormatter(bar_percent_formatter))
# Set y-axis colors
ax1.tick_params(axis='y', colors=bar_colors[0])
ax1.yaxis.label.set_color(bar_colors[0])
ax1.spines['left'].set_color(bar_colors[0])
# Set y-axis colors
ax2.tick_params(axis='y', colors=line_colors[0])
ax2.yaxis.label.set_color(line_colors[0])
ax2.spines['right'].set_color(line_colors[0])
# ax1.yaxis.set_major_formatter(LogFormatterSciNotation())
# ax1.set_ylim(1e-3, 1e-2)  # Set y-axis limits

# ax2.set_ylabel('Recovery probability (%)', fontsize=10)
ax2.set_ylim(0, 1.1)
ax2.yaxis.set_major_formatter(FuncFormatter(percent_formatter))

plt.tight_layout()
plt.savefig('Figure2b-Assembly-Performance-of-R025.pdf', dpi=600, bbox_inches='tight',transparent=True)
plt.show()

