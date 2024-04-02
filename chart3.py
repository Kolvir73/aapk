import matplotlib.pyplot as plt
import numpy as np
import pyexcel_ods

# Load data from the .ods file
data = pyexcel_ods.get_data("response3.ods")
# Extracting only the first sheet's data
data = data[list(data.keys())[0]]

# Remove empty rows
data = [row for row in data if any(row)]
cmap = plt.cm.tab10

# Iterate over each column (excluding the first one which contains headers)
for i, column_data in enumerate(zip(*data[1:])):
    header = data[0][i]
    
    # Skip empty columns
    if not any(column_data):
        continue
    
    # Count occurrences of each unique value in the column
    unique_values = [str(value) for value in set(column_data) if value]
    counts = [column_data.count(value) for value in unique_values]
    num_unique_values = len(unique_values)
    colors = [cmap(i % 10) for i in range(num_unique_values)]  # Modulus operation to ensure color cycling
    
    
    # Create a new figure and axis for each chart
    fig, ax = plt.subplots(figsize=(15, 10))
    
    # Create the chart
    bars = ax.bar(range(len(unique_values)), counts, color=colors)
    ax.set_ylabel('Count')
    ax.set_title(f'Summary of {header}')
    
    # Remove x-axis labels
    ax.set_xticks([])
    
    # Create legend with colors
    legend_handles = [plt.Rectangle((0,0),1,1, color=colors[i], label=unique_values[i]) for i in range(len(unique_values))]
    ax.legend(handles=legend_handles, loc='upper center', bbox_to_anchor=(0.5, -0.2), ncol=1, frameon=False)


    plt.tight_layout()  # Adjust layout to prevent overlapping
    plt.show()

