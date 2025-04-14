# ~~~ This is a template for question 2  ~~~

#implementation of insertion sort


    
    
    
#this function gets a list and uses insertion sort
def merge_sort_implementation(input = list):
    if not isinstance(input, list) or not all(isinstance(x, (int,float)) for x in input): # Input verification
        raise TypeError('Input must be a list of numbers')
    number_of_basic_operations = 1 + len(input) # Initialize number of operations as the number of comparisons in the input verification
    sorted_array = input.copy() # Create a copy list as to not modify the original list
    for j in range(1, len(sorted_array)):  # Use sorted_array consistently
        newnum = sorted_array[j] # Get the j-th element in the list
        i = j - 1 # Get the previous index to j
        number_of_basic_operations += 1 # Add an operation for calculating variable i.
        while i >= 0 and newnum < sorted_array[i]: # repeat for all elements to the left of j, or until a smaller element is found.
            sorted_array[i+1] = sorted_array[i] # Shift element at index i to the right
            i -= 1 # Move to next index on the left
            number_of_basic_operations += 3 # Add operations for while loop comparisons and assignment
        sorted_array[i+1] = newnum # Insert element j after all the elements to the left of it are smaller.
        number_of_basic_operations += 1 # Add operation for the assignment outside the loop
    
    return sorted_array, number_of_basic_operations