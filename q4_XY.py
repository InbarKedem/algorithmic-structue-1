# ~~~ This is a template for question 4 (bonus)  ~~~

#implementation of selection sort

def selection_sort_implementation(input_list=None):
    # Input validation
    if input_list is None:
        input_list = []
    
    if not isinstance(input_list, list) or not all(isinstance(x, (int, float)) for x in input_list):
        raise TypeError('Input must be a list of numbers')
    
    number_of_basic_operations = 1 + len(input_list)  # Input verification operations
    sorted_array = input_list.copy()  # Create a copy to avoid modifying the original
    
    for i in range(len(sorted_array)):
        smallest_index = i
        number_of_basic_operations += 1  # Assignment operation
        
        for j in range(i+1, len(sorted_array)):
            number_of_basic_operations += 1  # Comparison operation
            if sorted_array[smallest_index] > sorted_array[j]:
                smallest_index = j
                number_of_basic_operations += 1  # Assignment operation
        
        # Swap elements
        if smallest_index != i:
            sorted_array[smallest_index], sorted_array[i] = sorted_array[i], sorted_array[smallest_index]
            number_of_basic_operations += 3  # Swap operation (3 assignments)
    
    return sorted_array, number_of_basic_operations




