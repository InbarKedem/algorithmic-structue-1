import unittest
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from q1_44 import merge_sort_implementation
from q2_44 import insertion_sort_implementation
from q4_44 import selection_sort_implementation

class TestQuestion3(unittest.TestCase):
    def setUp(self):
        # Create a small test Excel file for testing
        self.test_data = [5, 3, 1, 4, 2, 7, 6]
        test_df = pd.DataFrame({"sort_me": self.test_data})
        test_df.to_excel("test_data.xlsx", index=False)
    
    def tearDown(self):
        # Clean up test files
        if os.path.exists("test_data.xlsx"):
            os.remove("test_data.xlsx")
        if os.path.exists("test_plot.png"):
            os.remove("test_plot.png")
            
    def test_data_loading(self):
        # Test if data can be loaded from Excel
        loaded_df = pd.read_excel("test_data.xlsx")
        loaded_data = loaded_df['sort_me'].tolist()
        
        self.assertEqual(loaded_data, self.test_data)
    
    def test_sorting_algorithms_results(self):
        # Test if the sorting algorithms produce correct results
        insertion_sorted, insertion_ops = insertion_sort_implementation(self.test_data)
        merge_sorted, merge_ops = merge_sort_implementation(self.test_data)
        selection_sorted, selection_ops = selection_sort_implementation(self.test_data)
        
        expected_sorted = sorted(self.test_data)
        self.assertEqual(insertion_sorted, expected_sorted)
        self.assertEqual(merge_sorted, expected_sorted)
        self.assertEqual(selection_sorted, expected_sorted)
    
    def test_sorting_algorithms_operations(self):
        # Test operations counting for each algorithm
        _, insertion_ops = insertion_sort_implementation(self.test_data)
        _, merge_ops = merge_sort_implementation(self.test_data)
        _, selection_ops = selection_sort_implementation(self.test_data)
        
        # All operation counts should be positive
        self.assertGreater(insertion_ops, 0)
        self.assertGreater(merge_ops, 0)
        self.assertGreater(selection_ops, 0)
        
        # For small datasets, merge sort might not always be more efficient
        # due to overhead of recursion and additional operations
        print(f"\nSmall dataset operations:")
        print(f"Insertion sort: {insertion_ops}")
        print(f"Merge sort: {merge_ops}")
        print(f"Selection sort: {selection_ops}")
    
    def test_plotting_functionality(self):
        # Test if the plotting code works without errors
        insertion_sorted, insertion_ops = insertion_sort_implementation(self.test_data)
        merge_sorted, merge_ops = merge_sort_implementation(self.test_data)
        
        # Create a test plot
        plt.figure(figsize=(8, 5))
        algorithms = ['Insertion Sort', 'Merge Sort']
        operations = [insertion_ops, merge_ops]
        
        plt.bar(algorithms, operations, color=['#3498db', '#2ecc71'])
        plt.title('Test Plot')
        plt.ylabel('Operations')
        plt.savefig("test_plot.png")
        plt.close()
        
        # Check if the plot was created
        self.assertTrue(os.path.exists("test_plot.png"))
    
    def test_theoretical_complexity(self):
        # Test theoretical complexity relationship with larger input
        # Generate a larger random list
        np.random.seed(42)  # For reproducibility
        large_list = np.random.randint(-100, 100, size=500).tolist()
        
        # Get operation counts
        _, insertion_ops = insertion_sort_implementation(large_list)
        _, merge_ops = merge_sort_implementation(large_list)
        
        # For n=500, merge sort should perform significantly fewer operations
        # than insertion sort (typically n log n vs n²)
        self.assertLess(merge_ops, insertion_ops)
        
        # Print operation counts for information
        n = len(large_list)
        print(f"\nFor array size {n}:")
        print(f"Insertion sort operations: {insertion_ops}")
        print(f"Merge sort operations: {merge_ops}")
        print(f"Theoretical insertion sort (n²/2): {(n*n)/2}")
        print(f"Theoretical merge sort (n log n): {n * np.log2(n)}")

if __name__ == "__main__":
    unittest.main()
