# Цей модуль буде відповідати за генерацію слів які потрібно вгадати
import random

INITIAL_WORDS = ["apple", "banana", "cherry", "orange", "Python", "testing", "module", "function", "variable", "exception", "Developer"]
def get_n_random_words(n: int) -> list[str]:
    if n > len(INITIAL_WORDS):
        raise ValueError("Запитуване число слів перевищує доступну кількість слів.")
    return [w.lower() for w in random.sample(INITIAL_WORDS, n)]