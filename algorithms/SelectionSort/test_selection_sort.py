import unittest
from selection_sort import selection_sort

class SelectionSortTest(unittest.TestCase):
    def setUp(self):
        # Kjøres før hver test
        self.empty = []
        self.single = [42]
        self.sorted_list = [1, 2, 3, 4, 5]
        self.unsorted_list = [5, 3, 1, 4, 2]
        self.duplicates = [3, 1, 2, 3, 2]

    def test_empty_list(self):
        self.assertEqual(selection_sort(self.empty), [],
                         "Empty list should remain empty")

    def test_single_element(self):
        self.assertEqual(selection_sort(self.single), [42],
                         "Single-element list should be unchanged")

    def test_already_sorted(self):
        self.assertEqual(selection_sort(self.sorted_list), self.sorted_list,
                         "Sorted list should be unchanged")

    def test_unsorted(self):
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(selection_sort(self.unsorted_list), expected,
                         "Unsorted list was not sorted correctly")

    def test_with_duplicates(self):
        expected = [1, 2, 2, 3, 3]
        self.assertEqual(selection_sort(self.duplicates), expected,
                         "List with duplicates not sorted correctly")

    def test_original_unchanged(self):
        original = self.unsorted_list.copy()
        _ = selection_sort(self.unsorted_list)
        self.assertEqual(self.unsorted_list, original,
                         "selection_sort must not modify the input list in place")

if __name__ == '__main__':
    unittest.main()
