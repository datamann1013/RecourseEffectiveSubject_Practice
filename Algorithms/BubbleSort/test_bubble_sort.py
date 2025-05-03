import unittest
from bubble_sort import bubble_sort

class BubbleSortTest(unittest.TestCase):
    def setUp(self):
        self.empty = []
        self.single = [42]
        self.sorted_list = [1, 2, 3, 4, 5]
        self.unsorted = [5, 1, 4, 2, 3]
        self.duplicates = [(2, 'a'), (1, 'b'), (2, 'c'), (1, 'd')]

    def test_empty_list(self):
        """Tom liste skal returnere tom liste"""
        self.assertEqual(bubble_sort(self.empty), [])

    def test_single_element(self):
        """Enkelt-element liste forblir uendret"""
        self.assertEqual(bubble_sort(self.single), [42])

    def test_already_sorted(self):
        """Allerede sortert liste forblir uendret"""
        self.assertEqual(bubble_sort(self.sorted_list), self.sorted_list)

    def test_unsorted_list(self):
        """Typisk usortert liste skal sorteres korrekt"""
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(bubble_sort(self.unsorted), expected)

    def test_with_duplicates(self):
        """Stabilitet: like elementer beholder rekkefølge"""
        expected = [(1, 'b'), (1, 'd'), (2, 'a'), (2, 'c')]
        self.assertEqual(bubble_sort(self.duplicates), expected)

    def test_original_unchanged(self):
        """Input-listen skal ikke muteres in-place"""
        original = self.unsorted.copy()
        _ = bubble_sort(self.unsorted)
        self.assertEqual(self.unsorted, original)

if __name__ == '__main__':
    unittest.main()
