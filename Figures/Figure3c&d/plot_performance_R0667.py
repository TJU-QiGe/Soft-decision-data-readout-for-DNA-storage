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


def load_and_process_data(file_path):
    data = pd.read_csv(file_path, header=None)
    data.columns = data.iloc[0]  
    data = data.drop(0).reset_index(drop=True)
    data = data.apply(pd.to_numeric, errors='coerce')
    return data

def load_line_data(file):
    return pd.read_csv(file, index_col=0)


def percent_formatter(x, pos):
    return f'{x * 100:.0f}'


fig, ax1 = plt.subplots(figsize=(3.8, 2.8))
ax2 = ax1.twinx()


file_paths = [
    'R0667-hard-consensus.csv',
    'R0667-soft-consensus.csv'
]
bar_labels = ['Error rate (Hard)', 'Error rate (Soft)']
bar_colors = [(139/255,190/255,197/255), (255/255,203/255,158/255)]
x = np.arange(7)
width = 0.4  
width1 = 0.38

for i, (path, label, color) in enumerate(zip(file_paths, bar_labels, bar_colors)):
    data = load_and_process_data(path)
    ax1.bar(x + i * width, data.mean(), width1, label=label, color=color)


line_files = [
    'duplex-R0667-recovery-hard.csv',
    'duplex-R0667-recovery-soft.csv'
]
line_colors =  [(28/255,138/255,152/255), (252/255,141/255,58/255)]
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
ax1.set_xticklabels(['0.59×', '1.19×', '2.38×', '3.57×', '4.77×', '5.96×', '7.22×'])
legend1=ax1.legend(loc='upper right', bbox_to_anchor=(0.95, 0.8),frameon=False, fontsize=7)
for text in legend1.get_texts():
    text.set_ha('center')  
ax1.yaxis.set_major_formatter(LogFormatterSciNotation())
ax1.set_ylim(1e-3, 1e0)  

ax2.set_ylabel('Recovery probability (%)', fontsize=10)
ax2.yaxis.set_major_formatter(FuncFormatter(percent_formatter))
legend2=ax2.legend(loc='upper right',bbox_to_anchor=(1.02, 0.65), frameon=False, fontsize=7)
for text in legend2.get_texts():
    text.set_ha('center')  
plt.tight_layout()
plt.savefig('Figure3d-Performance-of-R0667.pdf', dpi=600, bbox_inches='tight',transparent=True)
plt.show()
