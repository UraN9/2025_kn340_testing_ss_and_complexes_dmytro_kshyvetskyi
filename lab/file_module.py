# Цей модуль буде відповідати за генерацію слів які потрібно вгадати
import random

INITIAL_WORDS = ["apple", "banana", "cherry", "orange", "Python", "testing", "module", "function", "variable", "exception", "Developer"]
def get_n_random_words(n: int) -> list[str]:
    if n > len(INITIAL_WORDS):
        print("Неможливо згенерувати запитувану кількість слів.")
        raise ValueError("Запитуване число слів перевищує доступну кількість слів.")
    elif n != int(n):
        print("Кількість слів має бути цілим числом.")
        raise ValueError("Кількість слів має бути цілим числом.")
    elif n <= 0:
        print("Кількість слів не може бути від'ємною.")
        raise ValueError("Кількість слів не може бути від'ємною.")
    else:
        print(f"Генеруємо {n} випадкових слів для вгадування.")
    return [w.lower() for w in random.sample(INITIAL_WORDS, n)]