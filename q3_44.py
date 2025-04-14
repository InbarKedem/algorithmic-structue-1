# ~~~ This is a template for question 3  ~~~

#imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from q1_44 import merge_sort_implementation
from q2_44 import insertion_sort_implementation
from q4_44 import selection_sort_implementation

#load data:

# Load the Excel file
data_df = pd.read_excel("data.xlsx")

# Convert to a format suitable for sorting
data = data_df['sort_me'].tolist()  

#sort data and save results:
##insertion sort:
insertion_sort_array, insertion_sort_number_of_operations = insertion_sort_implementation(data)

##merge_sort:
merge_sort_array , merge_sort_number_of_operations = merge_sort_implementation(data)

#plot figure:
# Set up the plot
plt.figure(figsize=(10, 6))
algorithms = ['Insertion Sort', 'Merge Sort']
operations = [insertion_sort_number_of_operations, merge_sort_number_of_operations]

# Create the bar chart
bars = plt.bar(algorithms, operations, color=['#3498db', '#2ecc71'])

# Add title and labels
plt.title('Comparison of Basic Operations for Sorting Algorithms', fontsize=16)
plt.ylabel('Number of Basic Operations', fontsize=12)
plt.xlabel('Sorting Algorithm', fontsize=12)

# Add operation count on top of each bar
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2., height + 0.1,
             f'{int(height):,}', ha='center', fontsize=10)

# Add grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()