# ~~~ This is a template for question 3  ~~~

#imports
import pandas as pd
from q1_XY import merge_sort_implementation
from q2_template import insertion_sort_implementation

#load data:

# Define the path to your Excel file - adjust the filename as needed
excel_path =   # Update this with the actual file path

# Load the Excel file
data_df = pd.read_excel("data.xlsx")

# Convert to a format suitable for sorting
data = data_df['sort_me'].tolist()  

#sort data and save results:
##insertion sort:


##merge_sort:
merge_sort_array , merge_sort_number_of_operations = merge_sort_implementation(data)


#plot figure: