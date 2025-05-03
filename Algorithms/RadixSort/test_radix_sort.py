import unittest
from radix_sort import radix_sort

class RadixSortTest(unittest.TestCase):
    def setUp(self):
        self.empty       = []
        self.single      = [7]
        self.sorted_list = [1, 2, 3, 4, 5]
        self.unsorted    = [170, 45, 75, 90, 802, 24, 2, 66]
        self.duplicates  = [5, 3, 5, 2, 3, 1]

    def test_empty_list(self):
        """Tom liste → tom liste"""
        self.assertEqual(radix_sort(self.empty), [])

    def test_single_element(self):
        """Én verdi forblir uendret"""
        self.assertEqual(radix_sort(self.single), [7])

    def test_already_sorted(self):
        """Allerede sortert forblir uendret"""
        self.assertEqual(radix_sort(self.sorted_list),
                         self.sorted_list)

    def test_unsorted_list(self):
        """Uordnet liste sorteres riktig"""
        expected = [2, 24, 45, 66, 75, 90, 170, 802]
        self.assertEqual(radix_sort(self.unsorted), expected)

    def test_with_duplicates(self):
        """Stabilitet ved duplikater"""
        expected = [1, 2, 3, 3, 5, 5]
        self.assertEqual(radix_sort(self.duplicates), expected)

    def test_original_unchanged(self):
        """Ingen side‐effekter på input"""
        orig = self.unsorted.copy()
        _ = radix_sort(self.unsorted)
        self.assertEqual(self.unsorted, orig)

if __name__ == '__main__':
    unittest.main()
