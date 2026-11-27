
import unittest

from lessons import ANIMALS, TRANSPORT, NUMBERS, get_lesson


class TestLessons(unittest.TestCase):

    def test_animals_count(self):
        self.assertEqual(len(ANIMALS), 8)

    def test_transport_count(self):
        self.assertEqual(len(TRANSPORT), 8)

    def test_numbers_count(self):
        self.assertEqual(len(NUMBERS), 10)

    def test_animal_names_exist(self):
        for animal in ANIMALS:
            self.assertIn("name", animal)
            self.assertIn("emoji", animal)
            self.assertIn("sound", animal)

    def test_transport_names_exist(self):
        for vehicle in TRANSPORT:
            self.assertIn("name", vehicle)
            self.assertIn("emoji", vehicle)

    def test_get_lesson(self):
        self.assertEqual(len(get_lesson("animals")), 8)
        self.assertEqual(len(get_lesson("transport")), 8)
        self.assertEqual(len(get_lesson("numbers")), 10)

    def test_invalid_lesson(self):
        self.assertEqual(get_lesson("unknown"), [])


if __name__ == "__main__":
    unittest.main()
