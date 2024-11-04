import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42
# 设置字体和字号
mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams['font.size'] = 8
mpl.rcParams['font.weight'] = 'regular'
mpl.rcParams['axes.linewidth'] = 0.75
# Load the data from the uploaded CSV file
data_path = 'Time_with_different_I.csv'
data = pd.read_csv(data_path)
# Specify the columns to plot (assuming these columns exist in your data)
columns_to_plot = ['I=1', 'I=2', 'I=3', 'I=4']
# colors =['yellowgreen','#9DBB61','#F3E481','#B9AD4D']
colors =['yellowgreen','#9DBB61','#F3E481','#B9AD4D']
# Display the first few rows of the dataframe to understand its structure
data.head()
# Create a scatter plot with updated specifications
plt.figure(figsize=(2, 2.4))

flierprops = dict(marker='o', markerfacecolor='k', markersize=1.5, linestyle='none', markeredgecolor='none')

# Boxplot with patch_artist=True to allow fill with color
bp = plt.boxplot(data[columns_to_plot], patch_artist=True, positions=[1, 2, 3, 4],
                 whiskerprops={'color': 'black', 'linewidth': 0.5},
                 capprops={'color': 'black', 'linewidth': 0.5},
                 medianprops={'color': 'black', 'linewidth': 0.5},
                 boxprops={'edgecolor': 'black', 'linewidth': 0.5},
                 flierprops=flierprops)

# Coloring each box
for box, color in zip(bp['boxes'], colors):
    box.set_facecolor(color)
    
plt.xticks([1, 2, 3, 4], ['1', '2', '3', '4'])  # Setting custom x-axis tick labels
plt.xlabel('Consecutive insertion', fontsize=10)
plt.ylabel('Time (s)', fontsize=10)

# Tight layout for neatness
plt.tight_layout()
# Sive the plot
plt.savefig('Figure5e-Time.pdf', dpi=600, bbox_inches='tight',transparent=True)

plt.show()