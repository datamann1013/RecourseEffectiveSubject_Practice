import unittest
from heap_sort import heap_sort

class HeapSortTest(unittest.TestCase):
    def setUp(self):
        self.empty = []
        self.single = [42]
        self.sorted_list = [1, 2, 3, 4, 5]
        self.unsorted = [5, 3, 1, 4, 2]
        # Tuples for å teste stabilitet (selv om heap-sort er ustabil)
        self.duplicates = [(2, 'a'), (1, 'b'), (2, 'c'), (1, 'd')]

    def test_empty_list(self):
        """Tom liste skal returnere tom liste"""
        self.assertEqual(heap_sort(self.empty), [])

    def test_single_element(self):
        """Enkelt-element liste forblir uendret"""
        self.assertEqual(heap_sort(self.single), [42])

    def test_already_sorted(self):
        """Allerede sortert liste forblir uendret"""
        self.assertEqual(heap_sort(self.sorted_list), self.sorted_list)

    def test_unsorted_list(self):
        """Typisk usortert liste skal sorteres korrekt"""
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(heap_sort(self.unsorted), expected)

    def test_with_duplicates(self):
        """Ustabilitet: like nøkler kan endre rekkefølge"""
        # Selv om heap-sort ikke er stabil, skal resultatene være sortert
        sorted_vals = heap_sort(self.duplicates)
        self.assertEqual([x[0] for x in sorted_vals], [1, 1, 2, 2])

    def test_original_unchanged(self):
        """Input-listen skal ikke muteres in-place"""
        original = self.unsorted.copy()
        _ = heap_sort(self.unsorted)
        self.assertEqual(self.unsorted, original)

if __name__ == '__main__':
    unittest.main()
