import random
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

    #########################################################################################################################
    # Тут має бути новий метод - тільки перша буква буде зараховуватись
    # Можна вводити більше однієї букви
    # Вводити можна тільки латинські букви
    ########################################################################################################################

class TestCheckLettersInWord(unittest.TestCase):
    def setUp(self):
        print("Приготуємо дані для тестів")
        letters_to_guess = set(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

        self.test_word = "".join(random.choices(list(letters_to_guess), k = random.randint(3, 8)))
        self.guess_letters = letters_to_guess
        # Сетапимо пусті значення для тестів які перевіряють на порожні дані
        self.empty_test_word = ""
        self.no_letters = set()
        return super().setUp()

    def test_user_entered_cyrillic_letter(self):
        """
        Перевіряємо чи користувач ввів кириличну букву
        1. Якщо ввів кириличну букву, то функція має впасти з помилкою ValueError
        2. Якщо ввів латинську букву, то функція має працювати і повернути щось
        >>>Цей тест готовий<<<
        """
        with self.assertRaises(ValueError):
            check_letters_in_word({'а', 'б', 'в'}, self.test_word)
        self.assertTrue(len(check_letters_in_word({'a', 'b', 'c'}, self.test_word)) > 0)

    def test_all_letters_guessed(self):
        """
        Даний тест є валідний"""
        test_word = 'apple'
        self.assertEqual(
            check_letters_in_word (set(test_word), test_word),
            test_word
        )

    # def test_no_letters_guessed(self):
    #     self.assertEqual(check_letters_in_word(set(), 'banana'), '******')

    def test_some_letters_guessed(self):
        self.assertEqual(check_letters_in_word({'a', 'n'}, 'banana'), '*anana')

    def test_repeated_letters(self):
        self.assertEqual(check_letters_in_word({'b', 'a'}, 'banana'), 'ba*a*a')

#################################################################################################################################
    def test_valid_interface_arguments(self):
        """
        Перевіряємо чи функція працює з валідними аргументами
        Перевіряємо чи справді передаються слова і букви вірного типу
        1. Якщо ми передаємо неправильні типи то функція має впасти
        2. Якщо ми передаємо правильні типи то функція має працювати
        """

        # Ми виносимо ці змінні у setUp щоб не дублювати код
        # test_word = "ValideWord"
        # guess_letters = set(["a", "b", "c"])
        # Переприсвоювати змінні не потрібно, бо вони є в setUp
        test_word = self.test_word
        guess_letters = self.guess_letters
        print(f"test_word: {test_word}, guess_letters: {guess_letters}")
        # Не валідні типи
        for arg in [123, 12.5, None,]:
            with self.assertRaises(TypeError):
                check_letters_in_word(guess_letters, arg)

        #Це бага, тут неправильна поведінка, бо функція приймає список замість рядка
        # Тому ми переписали функцію щоб вона ловила цю помилку і не працювала з неправильними типами
        with self.assertRaises(TypeError):
            check_letters_in_word(guess_letters, ["a", "p", "p", "l", "e"])
        # Валідні типи
        self.assertIsInstance(test_word, str) 
        self.assertIsInstance(guess_letters, set)

    def test_empty_word(self):
        """
        Перевіряємо чи вгадане слово є порожнім
        1. Передаємо порожне слово, виловлюємо помилку 
        2. Передаємо слово і очікуємо що функція щось поверне
        >>>Цей тест готовий<<<
        """
        guess_letters = set(["a", "b"])

        with self.assertRaises(ValueError):
            check_letters_in_word(self.guess_letters, self.empty_test_word)
        self.assertGreater(len(check_letters_in_word(self.guess_letters, self.test_word)), 0)

    def test_empty_letters(self):
        """
        Перевірка на порожню букву.
        В даному тесті ми перевіряємо коли слово є а буква яка вгадується є порожньою
        >>>Цей тест готовий<<<
        """

        # Виловлюємо Помилку
        with self.assertRaises(ValueError):
            check_letters_in_word(self.no_letters, self.test_word)
        # Перевіряємо текст помилки, що це саме наша помилка яку ми написали
        with self.assertRaises(ValueError) as context:
            check_letters_in_word(self.no_letters, self.test_word)
            self.assertEqual(str(context.exception), "Слово не має бути порожнім")
        # Для контрольної перевірки передаємо букву і тут має бути повернутись значення
        # Якшо буква буде (при правильних даних) то функція щось поверне
        self.assertTrue(len(check_letters_in_word({'a'}, self.test_word)) > 0)

    # def test_letters_not_in_word(self):
    #     word = "НеПустеСлово"
    #     self.assertEqual(len(check_letters_in_word({'a'}, word)))

if __name__ == "__main__":
    unittest.main(verbosity=2)