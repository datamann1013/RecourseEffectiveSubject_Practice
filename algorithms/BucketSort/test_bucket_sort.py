import unittest
from bucket_sort import bucket_sort

class BucketSortTest(unittest.TestCase):
    def setUp(self):
        self.empty = []
        self.single = [5]
        self.sorted_list = [1, 2, 3, 4, 5]
        self.unsorted = [4, 1, 3, 2, 5]
        self.duplicates = [3, 1, 2, 3, 2]

    def test_empty_list(self):
        """Tom liste gir tom liste."""
        self.assertEqual(bucket_sort(self.empty), [])

    def test_single_element(self):
        """Enkelt-element forblir uendret."""
        self.assertEqual(bucket_sort(self.single), [5])

    def test_already_sorted(self):
        """Allerede sortert liste forblir uendret."""
        self.assertEqual(bucket_sort(self.sorted_list), self.sorted_list)

    def test_unsorted_list(self):
        """Typisk usortert liste skal sorteres korrekt."""
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(bucket_sort(self.unsorted), expected)

    def test_with_duplicates(self):
        """Sorterer duplikater riktig, bevarer frekvens."""
        expected = [1, 2, 2, 3, 3]
        self.assertEqual(bucket_sort(self.duplicates), expected)

    def test_original_unchanged(self):
        """Input-listen må ikke muteres."""
        original = self.unsorted.copy()
        _ = bucket_sort(self.unsorted)
        self.assertEqual(self.unsorted, original)

if __name__ == '__main__':
    unittest.main()
