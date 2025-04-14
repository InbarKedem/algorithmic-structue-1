import unittest
import random
from q1_44 import merge_sort_implementation

class TestMergeSortImplementation(unittest.TestCase):
    def test_empty_list(self):
        result, operations = merge_sort_implementation([])
        self.assertEqual(result, [])
        self.assertEqual(operations, 1)  # Just the input verification

    def test_single_element(self):
        result, operations = merge_sort_implementation([5])
        self.assertEqual(result, [5])
        self.assertEqual(operations, 2)  # 1 for verification + 1 for length

    def test_already_sorted(self):
        input_list = [1, 2, 3, 4, 5]
        result, operations = merge_sort_implementation(input_list)
        self.assertEqual(result, input_list)
        # Each element except the first requires at least 1 comparison and 1 assignment
        self.assertEqual(result, sorted(input_list))

    def test_reverse_sorted(self):
        input_list = [5, 4, 3, 2, 1]
        result, operations = merge_sort_implementation(input_list)
        self.assertEqual(result, sorted(input_list))

    def test_random_integers(self):
        # Test with different random integer lists
        for _ in range(5):
            size = random.randint(10, 100)
            input_list = [random.randint(-100, 100) for _ in range(size)]
            result, operations = merge_sort_implementation(input_list)
            self.assertEqual(result, sorted(input_list))

    def test_duplicate_elements(self):
        input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        result, operations = merge_sort_implementation(input_list)
        self.assertEqual(result, sorted(input_list))

    def test_float_values(self):
        input_list = [3.14, 1.41, 2.71, 0.0, -1.23]
        result, operations = merge_sort_implementation(input_list)
        self.assertEqual(result, sorted(input_list))
    
    def test_mixed_values(self):
        input_list = [5, -10, 3.5, 0, -2.7]
        result, operations = merge_sort_implementation(input_list)
        self.assertEqual(result, sorted(input_list))

    def test_invalid_input_not_list(self):
        with self.assertRaises(TypeError):
            merge_sort_implementation("not a list")
    
    def test_invalid_input_not_numbers(self):
        with self.assertRaises(TypeError):
            merge_sort_implementation([1, 2, "three", 4])

    def test_operations_count(self):
        # Test that operations are being counted
        # For a simple case with known operations count
        input_list = [3, 1, 2]
        result, operations = merge_sort_implementation(input_list)
        self.assertGreater(operations, 0)
    
    def test_large_list(self):
        # Test with a larger list to ensure efficiency
        size = 1000
        input_list = [random.randint(-1000, 1000) for _ in range(size)]
        result, operations = merge_sort_implementation(input_list)
        self.assertEqual(result, sorted(input_list))
        self.assertGreater(operations, 0)
        
    def test_negative_numbers_only(self):
        # Test with only negative numbers
        input_list = [-5, -10, -3, -7, -1]
        result, operations = merge_sort_implementation(input_list)
        self.assertEqual(result, sorted(input_list))
        
    def test_identical_elements(self):
        # Test with a list of identical elements
        input_list = [4, 4, 4, 4, 4]
        result, operations = merge_sort_implementation(input_list)
        self.assertEqual(result, input_list)
        
    def test_operations_consistency(self):
        # Test if operations count is consistent for identical inputs
        input_list = [3, 1, 4, 1, 5, 9]
        result1, ops1 = merge_sort_implementation(input_list.copy())
        result2, ops2 = merge_sort_implementation(input_list.copy())
        self.assertEqual(ops1, ops2)
        
    def test_specific_challenging_case(self):
        # Test with a specific challenging pattern (already mostly sorted with few inversions)
        input_list = [1, 2, 3, 5, 4, 6, 7, 8]
        result, operations = merge_sort_implementation(input_list)
        self.assertEqual(result, sorted(input_list))

if __name__ == "__main__":
    unittest.main()
