import unittest
from phonebook import PhoneBook

class PhoneBookTest(unittest.TestCase):
    def setUp(self):
        self.pb = PhoneBook()

    def test_add_and_get(self):
        self.pb.add_contact("Alice", "1234")
        self.assertEqual(self.pb.get_number("Alice"), "1234")

    def test_update_contact(self):
        self.pb.add_contact("Bob", "0000")
        self.pb.update_contact("Bob", "1111")
        self.assertEqual(self.pb.get_number("Bob"), "1111")

    def test_remove_contact(self):
        self.pb.add_contact("Charlie", "2222")
        self.pb.remove_contact("Charlie")
        with self.assertRaises(KeyError):
            _ = self.pb.get_number("Charlie")

    def test_has_contact(self):
        self.pb.add_contact("Dana", "3333")
        self.assertTrue(self.pb.has_contact("Dana"))
        self.assertFalse(self.pb.has_contact("Eve"))

    def test_all_contacts(self):
        names = ["Fay", "Gus", "Hank"]
        for i, name in enumerate(names):
            self.pb.add_contact(name, f"{i:04d}")
        self.assertCountEqual(self.pb.all_contacts(), names)

    def test_add_duplicate_raises(self):
        self.pb.add_contact("Ivy", "4444")
        with self.assertRaises(KeyError):
            self.pb.add_contact("Ivy", "5555")

    def test_update_nonexistent_raises(self):
        with self.assertRaises(KeyError):
            self.pb.update_contact("Jack", "6666")

    def test_remove_nonexistent_raises(self):
        with self.assertRaises(KeyError):
            self.pb.remove_contact("Kim")

if __name__ == '__main__':
    unittest.main()
