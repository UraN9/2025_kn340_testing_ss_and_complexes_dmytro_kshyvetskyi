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
    invalid_inputs = [50]
    with pytest.raises(ValueError):
        for n in invalid_inputs:
            get_n_random_words(n)
