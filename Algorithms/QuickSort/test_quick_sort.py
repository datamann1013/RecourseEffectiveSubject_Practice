import unittest
from quick_sort import quick_sort

class QuickSortTest(unittest.TestCase):
    def setUp(self):
        self.empty = []
        self.single = [9]
        self.sorted_list = [1, 2, 3, 4, 5]
        self.unsorted = [3, 6, 1, 5, 2, 4]
        self.duplicates = [(2,'x'), (1,'a'), (2,'y'), (1,'b')]
        # Bruk tuples for å kunne teste stabilitet eksplisitt

    def test_empty_list(self):
        """Tom liste skal returnere tom liste"""
        self.assertEqual(quick_sort(self.empty), [])

    def test_single_element(self):
        """Liste med ett element forblir uendret"""
        self.assertEqual(quick_sort(self.single), [9])

    def test_already_sorted(self):
        """Allerede sortert liste forblir uendret"""
        self.assertEqual(quick_sort(self.sorted_list), self.sorted_list)

    def test_unsorted_list(self):
        """Usortert liste sorteres i stigende rekkefølge"""
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(quick_sort(self.unsorted), expected)

    def test_with_duplicates(self):
        """Test stabilitet: like nøkler beholder rekkefølge innen tuples"""
        expected = [(1,'a'), (1,'b'), (2,'x'), (2,'y')]
        self.assertEqual(quick_sort(self.duplicates), expected)

    def test_original_unchanged(self):
        """Input-listen skal ikke muteres in-place"""
        original = self.unsorted.copy()
        _ = quick_sort(self.unsorted)
        self.assertEqual(self.unsorted, original)

if __name__ == '__main__':
    unittest.main()
