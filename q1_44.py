# ~~~ This is a template for question 1  ~~~

#implementation of merge sort

def merge(left, right, ops_count):
    """Merge two sorted arrays into one sorted array."""
    result = []
    i = j = 0
    
    # Merge the two arrays by selecting the smaller element each time
    while i < len(left) and j < len(right):
        ops_count += 1  # Comparison operation
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        ops_count += 1  # Assignment operation (appending)
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    ops_count += 2  # Two extend operations
    
    return result, ops_count

def merge_sort(arr, ops_count):
    """Recursively sort the array using merge sort."""
    # Base case: arrays of size 0 or 1 are already sorted
    if len(arr) <= 1:
        ops_count += 1  # Length check
        return arr, ops_count
    
    # Divide the array into two halves
    mid = len(arr) // 2
    ops_count += 1  # Division operation
    
    # Recursively sort both halves
    left, ops_count = merge_sort(arr[:mid], ops_count)
    right, ops_count = merge_sort(arr[mid:], ops_count)
    
    # Merge the sorted halves
    return merge(left, right, ops_count)

#this function gets a list and uses merge sort
def merge_sort_implementation(_input = list):
    # Input validation
    if not isinstance(_input, list):
        raise TypeError('Input must be a list of numbers')
    
    if not all(isinstance(x, (int, float)) for x in _input):
        raise TypeError('Input must be a list of numbers')
    
    # Create a copy to avoid modifying the original
    arr = _input.copy()
    
    # Initialize operation counter
    number_of_basic_operations = 1  # For input validation
    
    # Handle empty list case
    if not arr:
        return arr, number_of_basic_operations
    
    # Call the recursive merge sort function
    sorted_array, number_of_basic_operations = merge_sort(arr, number_of_basic_operations)
    
    return sorted_array, number_of_basic_operations