import unittest
from unittest.mock import patch
from main import *

class TestWordChoice(unittest.TestCase):
    def test_word_in_list(self):
        word = choose_secret_word(WORDS)
        self.assertIn(word, WORDS, f"Слово {word} має бути у списку {WORDS}")

    def test_word_is_string(self):
        word = choose_secret_word(WORDS)
        self.assertIsInstance(word, str, f"Слово {word} має бути рядком")

    def test_word_length(self):
        word = choose_secret_word(WORDS)
        self.assertGreater(len(word), 0, "Слово має бути не порожнім")
        self.assertLessEqual(len(word), 20, "Слово має бути не довшим за 20 символів")

    def test_word_not_numeric(self):
        word = choose_secret_word(WORDS)
        self.assertFalse(word.isdigit(), f"Слово {word} не має бути числом")

    def test_word_not_empty(self):
        word = choose_secret_word(WORDS)
        self.assertNotEqual(word, "", "Слово не має бути порожнім")

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            choose_secret_word([])

class TestEnterLetterFromUser(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', 'a'])
    def test_enter_letter_from_user(self, mock_input):
        self.assertEqual(enter_letter_from_user(), '1')
        self.assertEqual(enter_letter_from_user(), 'a')

        # __builtins__.input = mock_input
        # try:
        #     self.assertEqual(enter_letter_from_user(), 'a')
        # finally:
        #     __builtins__.input = original_input

class TestCheckLettersInWord(unittest.TestCase):
    def test_all_letters_guessed(self):
        """
        Даний тест є валідний"""
        test_word = 'apple'
        self.assertEqual(
            check_letters_in_word (set(test_word), test_word),
            test_word
        )

    def test_no_letters_guessed(self):
        self.assertEqual(check_letters_in_word(set(), 'banana'), '******')

    def test_some_letters_guessed(self):
        self.assertEqual(check_letters_in_word({'a', 'n'}, 'banana'), '*anana')

    def test_repeated_letters(self):
        self.assertEqual(check_letters_in_word({'b', 'a'}, 'banana'), 'ba*a*a')

    def test_empty_letters(self):
        """
        Даний тест ми також залишимо та трішки модифікуємо"""
        test_word = 'test'
        guess_letters = set("")
        with self.assertRaises(ValueError):
            check_letters_in_word(guess_letters, "")

    def test_empty_word(self):
        guess_letters = set("")
        # Виловлюємо Помилку
        with self.assertRaises(ValueError):
            check_letters_in_word(guess_letters, "")
        # Перевіряємо текст помилки, що це саме наша помилка яку ми написали
        with self.assertRaises(ValueError) as context:
            check_letters_in_word(guess_letters, "")
            self.assertEqual(str(context.exception), "Слово не має бути порожнім")

    def test_letters_not_in_word(self):
        self.assertEqual(check_letters_in_word({'x', 'y', 'z'}, 'orange'), '******')

if __name__ == "__main__":
    unittest.main(verbosity=2)