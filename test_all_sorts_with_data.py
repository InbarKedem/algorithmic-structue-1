import unittest
import pandas as pd
from q1_44 import merge_sort_implementation
from q2_44 import insertion_sort_implementation
from q4_44 import selection_sort_implementation

class TestAllSortsWithData(unittest.TestCase):
    def setUp(self):
        # Load the data once for all tests
        try:
            data_df = pd.read_excel("data.xlsx")
            self.data = data_df['sort_me'].tolist()
            # Create a correctly sorted version to compare against
            self.correctly_sorted_data = sorted(self.data)
        except Exception as e:
            self.fail(f"Failed to load data.xlsx: {e}")
    
    def test_merge_sort_with_data(self):
        # Test merge sort implementation with the data
        sorted_data, operations = merge_sort_implementation(self.data)
        self.assertEqual(sorted_data, self.correctly_sorted_data)
        self.assertGreater(operations, 0)
        print(f"Merge sort operations: {operations}")
    
    def test_insertion_sort_with_data(self):
        # Test insertion sort implementation with the data
        sorted_data, operations = insertion_sort_implementation(self.data)
        self.assertEqual(sorted_data, self.correctly_sorted_data)
        self.assertGreater(operations, 0)
        print(f"Insertion sort operations: {operations}")
    
    def test_selection_sort_with_data(self):
        # Test selection sort implementation with the data
        sorted_data, operations = selection_sort_implementation(self.data)
        self.assertEqual(sorted_data, self.correctly_sorted_data)
        self.assertGreater(operations, 0)
        print(f"Selection sort operations: {operations}")
    
    def test_compare_operations(self):
        # Compare the number of operations across all three algorithms
        _, merge_ops = merge_sort_implementation(self.data)
        _, insertion_ops = insertion_sort_implementation(self.data)
        _, selection_ops = selection_sort_implementation(self.data)
        
        print("\nOperation count comparison:")
        print(f"Merge sort: {merge_ops}")
        print(f"Insertion sort: {insertion_ops}")
        print(f"Selection sort: {selection_ops}")
        
        # Not testing any specific relation, just printing for information
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
