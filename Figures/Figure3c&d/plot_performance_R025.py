import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib.ticker import FuncFormatter, LogFormatterSciNotation

mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42

mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams['font.size'] = 8
mpl.rcParams['font.weight'] = 'regular'
mpl.rcParams['axes.linewidth'] = 0.75

# Load and process data functions
def load_and_process_data(file_path):
    data = pd.read_csv(file_path, header=None)
    data.columns = data.iloc[0]  
    data = data.drop(0).reset_index(drop=True)
    data = data.apply(pd.to_numeric, errors='coerce')
    return data

# Load line graph data
def load_line_data(file):
    return pd.read_csv(file, index_col=0)

# Format percentage functions
def percent_formatter(x, pos):
    return f'{x * 100:.0f}'

# Initialize graphs and axes
fig, ax1 = plt.subplots(figsize=(3.8, 2.8))
ax2 = ax1.twinx()

# Bar chart settings
file_paths = [
    'R025-hard-consensus.csv',
    'R025-soft-consensus.csv'
]
bar_labels = ['Error rate (Hard)', 'Error rate (Soft)']
bar_colors = [(158/255,225/255,166/255), (164/255,179/255,212/255)]
x = np.arange(7)  
width = 0.4  
width1 = 0.38
# Plotting bar charts
for i, (path, label, color) in enumerate(zip(file_paths, bar_labels, bar_colors)):
    data = load_and_process_data(path)
    ax1.bar(x + i * width, data.mean(), width1, label=label, color=color)

# Line chart setup
line_files = [
    'duplex-R025-recovery-hard.csv',
    'duplex-R025-recovery-soft.csv'
]
line_colors =  [(3/255,175/255,81/255), (92/255,111/255,180/255)]
line_markers = ['o', '^']
line_styles = ['--', '-']
line_labels = ['Recovery rate (Hard)', 'Recovery rate (Soft)']

for i, (file, color, marker, linestyle, label) in enumerate(zip(line_files, line_colors, line_markers, line_styles, line_labels)):
    data = load_line_data(file)
    read_numbers = data.columns.astype(int)
    recoverable_ratio = data.loc['Recoverable ratio'].astype(float)
    
    ax2.plot(x + width/2, recoverable_ratio, marker=marker, markersize=8, markeredgewidth=0.2, color=color, linestyle=linestyle,linewidth=0.75, label=label)


ax1.set_ylabel('Bit error rate (substitutions)', fontsize=10)
ax1.set_yscale('log')
ax1.set_xlabel('Coverage', fontsize=10)
ax1.set_xticks(x + width/2)  
ax1.set_xticklabels(['0.43×', '0.86×', '1.73×', '2.59×', '3.44×', '4.30×', '5.20×'])
legend1=ax1.legend(loc='upper right', bbox_to_anchor=(0.93, 0.9),frameon=False, fontsize=7)
for text in legend1.get_texts():
    text.set_ha('center')  
ax1.yaxis.set_major_formatter(LogFormatterSciNotation())
ax1.set_ylim(1e-3, 1e0)  

ax2.set_ylabel('Recovery probability (%)', fontsize=10)
ax2.yaxis.set_major_formatter(FuncFormatter(percent_formatter))

legend2=ax2.legend(loc='upper right', bbox_to_anchor=(1, 0.75),frameon=False, fontsize=7)
for text in legend2.get_texts():
    text.set_ha('center')  

plt.tight_layout()
plt.savefig('Figure3c-Performance-of-R025.pdf', dpi=600, bbox_inches='tight',transparent=True)
plt.show()
