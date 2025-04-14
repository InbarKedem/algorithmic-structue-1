# ~~~ This is a template for question 2  ~~~

#implementation of insertion sort
    
#this function gets a list and uses insertion sort
def insertion_sort_implementation(input = list):
    
    if not isinstance(input, list) or not all(isinstance(x, (int,float)) for x in input):
        raise TypeError('Input must be a list of numbers')
    
    number_of_basic_operations = 1 + len(input)  # Input verification operations
    sorted_array = input.copy()  # Create a copy to avoid modifying the original
    
    for j in range(1, len(sorted_array)):
        key = sorted_array[j]
        i = j - 1
        number_of_basic_operations += 1  # Assignment operations
        
        while i >= 0 and sorted_array[i] > key:
            sorted_array[i+1] = sorted_array[i]
            i -= 1
            number_of_basic_operations += 3  # Comparison + assignment + decrement
        
        sorted_array[i+1] = key
        number_of_basic_operations += 1  # Assignment operation
    
    return sorted_array, number_of_basic_operations