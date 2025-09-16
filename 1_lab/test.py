import unittest
from unittest.mock import patch
from main import choose_secret_word, enter_letter_from_user, WORDS

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

if __name__ == "__main__":
    unittest.main(verbosity=2)