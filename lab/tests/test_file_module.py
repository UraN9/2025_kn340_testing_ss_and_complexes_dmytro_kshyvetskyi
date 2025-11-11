from unittest.mock import patch
import pytest
from lab.file_module import get_n_random_words

def test_get_n_random_words():
    """
    Перевіряємо чи функція повертає правильну кількість слів"""
    for n in range(1, 6):
        words = get_n_random_words(n)
        assert len(words) == n, f"Очікувалось {n} слів, отримано {len(words)}"

def test_get_n_random_words_raises_value_error():
    """
    Перевіряємо чи функція піднімає ValueError коли ми перевищуємо доступну кількість слів
    """
    invalid_inputs = [1.5, -2, 0, 50]
    for n in invalid_inputs:
        with pytest.raises(ValueError):
            N = get_n_random_words(n)
            assert len(N) == n, f"Очікувалось ValueError для вхідного {n}"
            

def test_get_n_random_words_expect_print_outputs():
    with patch('builtins.print') as mock_print:
        for n in range(1, 6):
            get_n_random_words(n)
            mock_print.assert_any_call(f"Генеруємо {n} випадкових слів для вгадування.")