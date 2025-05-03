import unittest
from merge_sort import merge_sort

class MergeSortTest(unittest.TestCase):
    def setUp(self):
        self.empty = []
        self.single = [99]
        self.sorted_list = [1, 2, 3, 4, 5]
        self.unsorted = [5, 3, 1, 4, 2]
        # Tuples for å teste stabilitet
        self.duplicates = [(2, 'x'), (1, 'a'), (2, 'y'), (1, 'b')]

    def test_empty_list(self):
        """Tom liste skal returnere tom liste"""
        self.assertEqual(merge_sort(self.empty), self.empty)

    def test_single_element(self):
        """Liste med ett element forblir uendret"""
        self.assertEqual(merge_sort(self.single), self.single)

    def test_already_sorted(self):
        """Allerede sortert liste skal forbli uendret"""
        self.assertEqual(merge_sort(self.sorted_list), self.sorted_list)

    def test_unsorted_list(self):
        """Usortert liste skal sorteres korrekt"""
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(merge_sort(self.unsorted), expected)

    def test_with_duplicates(self):
        """Stabilitet: like nøkler bevares i opprinnelig rekkefølge"""
        expected = [(1, 'a'), (1, 'b'), (2, 'x'), (2, 'y')]
        self.assertEqual(merge_sort(self.duplicates), expected)

    def test_original_unchanged(self):
        """Input-listen skal ikke muteres in-place"""
        original = self.unsorted.copy()
        _ = merge_sort(self.unsorted)
        self.assertEqual(self.unsorted, original)

if __name__ == '__main__':
    unittest.main()
