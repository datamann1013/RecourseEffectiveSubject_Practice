import unittest
from counting_sort import counting_sort

class CountingSortTest(unittest.TestCase):
    def setUp(self):
        self.empty = []
        self.single = [42]
        self.sorted_list = [1, 2, 3, 4, 5]
        self.unsorted = [4, 1, 3, 2, 5]
        self.duplicates = [3, 1, 2, 3, 2]
        self.negative = [0, -1, 5, -1, 3]  # tester negative verdier

    def test_empty_list(self):
        """Tom liste skal returnere tom liste."""
        self.assertEqual(counting_sort(self.empty), [])

    def test_single_element(self):
        """Liste med ett element forblir uendret."""
        self.assertEqual(counting_sort(self.single), [42])

    def test_already_sorted(self):
        """Allerede sortert liste forblir uendret."""
        self.assertEqual(counting_sort(self.sorted_list), self.sorted_list)

    def test_unsorted_list(self):
        """Typisk usortert liste skal sorteres korrekt."""
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(counting_sort(self.unsorted), expected)

    def test_with_duplicates(self):
        """Bevarer riktige antall av duplikate verdier."""
        expected = [1, 2, 2, 3, 3]
        self.assertEqual(counting_sort(self.duplicates), expected)

    def test_negative_values(self):
        """Håndterer negative tall korrekt ved offset med min_val."""
        expected = [-1, -1, 0, 3, 5]
        self.assertEqual(counting_sort(self.negative), expected)

    def test_original_unchanged(self):
        """Input-listen må ikke muteres."""
        original = self.unsorted.copy()
        _ = counting_sort(self.unsorted)
        self.assertEqual(self.unsorted, original)

if __name__ == '__main__':
    unittest.main()
