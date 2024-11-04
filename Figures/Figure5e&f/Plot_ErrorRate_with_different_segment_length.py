import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import FuncFormatter

mpl.rcParams['pdf.fonttype'] = 42
mpl.rcParams['ps.fonttype'] = 42

mpl.rcParams['font.family'] = 'Arial'
mpl.rcParams['font.size'] = 8
mpl.rcParams['font.weight'] = 'regular'
mpl.rcParams['axes.linewidth'] = 0.75
# Load the data from the uploaded CSV file
data_path = 'Errorrate_with_different_segment_length.csv'
data = pd.read_csv(data_path)
# Specify the columns to plot (assuming these columns exist in your data)
columns_to_plot = ['100', '200', '500', '1000', '1500']
# colors =['yellowgreen','#9DBB61','#F3E481','#B9AD4D']
colors =['yellowgreen','#9DBB61','#F3E481','#B9AD4D', '#807A2B']
# Display the first few rows of the dataframe to understand its structure
# Define a function to format the tick labels as percentages without '%'
def to_percent(y, position):
    # Convert the y value to a string showing a percentage without the '%' sign
    return f'{100 * y:.0f}'

formatter = FuncFormatter(to_percent)

# Create a scatter plot with updated specifications
plt.figure(figsize=(1.9, 2.35))

flierprops = dict(marker='o', markerfacecolor='black', markersize=1.5, linestyle='none', markeredgecolor='none')

# Boxplot with patch_artist=True to allow fill with color
bp = plt.boxplot(data[columns_to_plot], patch_artist=True, positions=[1, 2, 3, 4, 5],
                 whiskerprops={'color': 'black', 'linewidth': 0.5},
                 capprops={'color': 'black', 'linewidth': 0.5},
                 medianprops={'color': 'black', 'linewidth': 0.5},
                 boxprops={'edgecolor': 'black', 'linewidth': 0.5},
                 flierprops=flierprops)

# Coloring each box
for box, color in zip(bp['boxes'], colors):
    box.set_facecolor(color)

# Set tick formatter
plt.gca().yaxis.set_major_formatter(formatter)  

plt.xticks([1, 2, 3, 4, 5], ['100', '200', '500', '1000', '1500'],rotation=45)  # Setting custom x-axis tick labels
plt.xlabel('Segment length', fontsize=10)
plt.ylabel('Error rate (%)', fontsize=10)  # Add '%' to the label
# Tight layout for neatness
plt.tight_layout()
# Sive the plot
plt.savefig('Figure5f-ErrorRate.pdf', dpi=600, bbox_inches='tight',transparent=True)

plt.show()