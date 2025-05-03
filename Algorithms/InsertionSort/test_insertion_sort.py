import unittest
from insertion_sort import insertion_sort

class InsertionSortTest(unittest.TestCase):
    def setUp(self):
        self.empty = []
        self.single = [7]
        self.sorted_list = [1, 2, 3, 4, 5]
        self.unsorted = [4, 2, 5, 1, 3]
        self.duplicates = [(2, 'a'), (1, 'b'), (2, 'c'), (1, 'd')]
        # Ekstra: liste av tuples for å teste stabilitet

    def test_empty_list(self):
        """Tom liste skal returnere tom liste"""
        self.assertEqual(insertion_sort(self.empty), self.empty)

    def test_single_element(self):
        """Enkelt-element liste forblir uendret"""
        self.assertEqual(insertion_sort(self.single), self.single)

    def test_already_sorted(self):
        """Allerede sortert liste forblir uendret"""
        self.assertEqual(insertion_sort(self.sorted_list), self.sorted_list)

    def test_unsorted_list(self):
        """Typisk usortert liste skal sorteres korrekt"""
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(insertion_sort(self.unsorted), expected)

    def test_with_duplicates(self):
        """Liste med duplikate tall skal sorteres korrekt"""
        expected = [(1, 'b'), (1, 'd'), (2, 'a'), (2, 'c')]
        self.assertEqual(insertion_sort(self.duplicates), expected)

    def test_original_unchanged(self):
        """Input-listen skal ikke muteres in-place"""
        original = self.unsorted.copy()
        _ = insertion_sort(self.unsorted)
        self.assertEqual(self.unsorted, original)

if __name__ == '__main__':
    unittest.main()
