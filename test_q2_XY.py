import unittest
import random
from q2_44 import insertion_sort_implementation

class TestInsertionSortImplementation(unittest.TestCase):
    def test_empty_list(self):
        result, operations = insertion_sort_implementation([])
        self.assertEqual(result, [])
        self.assertEqual(operations, 1)  # Just the input verification

    def test_single_element(self):
        result, operations = insertion_sort_implementation([5])
        self.assertEqual(result, [5])
        # 1 for verification + length of list (1)
        self.assertEqual(operations, 2)

    def test_already_sorted(self):
        input_list = [1, 2, 3, 4, 5]
        result, operations = insertion_sort_implementation(input_list)
        self.assertEqual(result, input_list)
        self.assertEqual(result, sorted(input_list))

    def test_reverse_sorted(self):
        input_list = [5, 4, 3, 2, 1]
        result, operations = insertion_sort_implementation(input_list)
        self.assertEqual(result, sorted(input_list))

    def test_random_integers(self):
        # Test with different random integer lists
        for _ in range(5):
            size = random.randint(10, 100)
            input_list = [random.randint(-100, 100) for _ in range(size)]
            result, operations = insertion_sort_implementation(input_list)
            self.assertEqual(result, sorted(input_list))

    def test_duplicate_elements(self):
        input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        result, operations = insertion_sort_implementation(input_list)
        self.assertEqual(result, sorted(input_list))

    def test_float_values(self):
        input_list = [3.14, 1.41, 2.71, 0.0, -1.23]
        result, operations = insertion_sort_implementation(input_list)
        self.assertEqual(result, sorted(input_list))
    
    def test_mixed_values(self):
        input_list = [5, -10, 3.5, 0, -2.7]
        result, operations = insertion_sort_implementation(input_list)
        self.assertEqual(result, sorted(input_list))

    def test_invalid_input_not_list(self):
        with self.assertRaises(TypeError):
            insertion_sort_implementation("not a list")
    
    def test_invalid_input_not_numbers(self):
        with self.assertRaises(TypeError):
            insertion_sort_implementation([1, 2, "three", 4])

    def test_operations_count(self):
        # Test that operations are being counted
        input_list = [3, 1, 2]
        result, operations = insertion_sort_implementation(input_list)
        self.assertGreater(operations, 0)

if __name__ == "__main__":
    unittest.main()
