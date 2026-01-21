import unittest
from main import get_grade

class TestGetGrade(unittest.TestCase):
    def test_valid_boundary_values(self):
        # Тестуємо граничні значення
        self.assertEqual(get_grade(59), "F")
        self.assertEqual(get_grade(60), "D")
        self.assertEqual(get_grade(89), "B")
        self.assertEqual(get_grade(90), "A")
        self.assertEqual(get_grade(100), "A")

    def test_invalid_values(self):
        # Тестуємо некоректні дані
        with self.assertRaises(ValueError):
            get_grade(-1)
        with self.assertRaises(ValueError):
            get_grade(101)

    def test_other_valid_values(self):
        # Тестуємо середній діапазон
        self.assertEqual(get_grade(75), "C")
        self.assertEqual(get_grade(85), "B")

if __name__ == "__main__":
    unittest.main()