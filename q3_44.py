# ~~~ This is a template for question 3  ~~~

#imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from q1_44 import merge_sort_implementation
from q2_44 import insertion_sort_implementation
from q4_44 import selection_sort_implementation

#load data:
# Load the Excel file with all sheets
excel_file = pd.ExcelFile("data.xlsx")

# Get all sheet names
sheet_names = excel_file.sheet_names

# Create a line graph comparing merge sort and insertion sort across sheet numbers
plt.figure(figsize=(12, 8))

# Collect data for each sheet
sheet_numbers = list(range(1, len(sheet_names) + 1))
insertion_operations = []
merge_operations = []

# Get operation counts for each sheet
for sheet_name in sheet_names:
    data_df = pd.read_excel(excel_file, sheet_name=sheet_name)
    data = data_df['sort_me'].tolist()
    
    # Run sorting algorithms
    _, insertion_ops = insertion_sort_implementation(data)
    _, merge_ops = merge_sort_implementation(data)
    
    insertion_operations.append(insertion_ops)
    merge_operations.append(merge_ops)

# Plot the lines - using sheet numbers on x-axis
plt.plot(sheet_numbers, insertion_operations, marker='o', linestyle='-', linewidth=3, 
         color='orange', label='Insertion Sort')
plt.plot(sheet_numbers, merge_operations, marker='', linestyle='-', linewidth=3, 
         color='blue', label='Merge Sort')

# Add title and labels
plt.title('Sorting Algorithm Operations by Sheet', fontsize=16)
plt.xlabel('Sheet No.', fontsize=14)
plt.ylabel('Count Number of Basic Operation', fontsize=14)
plt.legend(fontsize=12, loc='upper right')

# Set x-axis to show whole numbers only
plt.xticks(sheet_numbers)

# Add grid for better readability
plt.grid(False)  # No grid to match the example image

# Format the plot area
plt.tight_layout()

# Save the line graph
plt.savefig("sorting_algorithms_comparison_by_sheet.png")
plt.show()