<h1><p align="center"><strong>Екзаменаційна робота</strong></p>
<p align="center"><strong>З дисципліни «Тестування програмних систем та комплексів»</strong></p>
<p align="center"><strong>Студента групи КН-340</strong></p>
<p align="center"><strong>Кшивецький Дмитро</strong></p></h1>

# Білет №9

## 1. Що таке граничні значення (Boundary Values) і чому помилки часто трапляються саме там?

**Граничні значення (Boundary Values)** — це значення, які знаходяться на межах допустимого діапазону вхідних даних. 
Граничні значення можуть бути як мінімальними (нижня межа), так і максимальними (верхня межа). Наприклад, якщо функція приймає дані в діапазоні від 0 до 100, граничними значеннями будуть -1, 0, 100, 101.

**Чому помилки трапляються саме там?**
1. **Проблеми з логікою обробки країв діапазону.** Розробники можуть не враховувати поведінку програми на межі через помилкові припущення.
2. **Недостатнє тестування.** Тестування часто зосереджене на середніх значеннях, а не на екстремальних.
3. **Перехід між діапазонами.** Межі є місцями, де виконується переключення логіки розрахунків або вироблення іншої поведінки.

Тестування граничних значень допомагає виявити помилки, які можуть виникати у таких екстремальних випадках.

---

## 2. Опишіть методи класу `unittest.TestCase`: `assertEqual`, `assertTrue`, `assertRaises`.

### **`assertEqual(a, b)`**
- **Опис**: Перевіряє, чи значення `a` дорівнює `b`.
- **Приклад**:
    ```python
    self.assertEqual(5 + 5, 10)  # Тест проходить
    self.assertEqual("hello", "world")  # Тест не проходить
    ```

### **`assertTrue(expr)`**
- **Опис**: Перевіряє, чи вираз `expr` є `True` (істинним).
- **Приклад**:
    ```python
    self.assertTrue(5 > 3)  # Тест проходить
    self.assertTrue(2 == 3)  # Тест не проходить
    ```

### **`assertRaises(expected_exception, callable, *args, **kwargs)`**
- **Опис**: Перевіряє, чи виклик функції `callable(*args, **kwargs)` призводить до виникнення помилки `expected_exception`.
- **Приклад**:
    ```python
    with self.assertRaises(ValueError):
        int("not a number")  # Тест проходить, бо викликається ValueError
    ```

---

## 3. Яка роль QA-інженера в команді розробки Agile/Scrum?

У команді Agile/Scrum QA-інженер відповідає за забезпечення якості продукту, співпрацюючи з усією командою на кожному етапі розробки. Основні завдання QA-інженера:
1. **Аналіз вимог.** Перевірка, чи вимоги достатньо зрозумілі та тестовані.
2. **Написання та запуск тестів.** QA-інженери створюють автоматичні та ручні тести, що перевіряють відповідність продукту специфікації.
3. **Інтеграція тестів у CI/CD.** Автоматизовані тести інтегруються в процеси Continuous Integration та Continuous Deployment, що дає змогу виявляти помилки ще під час розробки.
4. **Навчання команди важливості якості.** QA допомагає забезпечити культуру якості всередині команди.
5. **Координація спринтів.** Забезпечує, щоб усі тестування були завершені до кінця кожного спринту.

---

## 4. **Завдання:** 
У файлі `main.py` напишіть функцію `get_grade(score: int)`, яка повертає оцінку (A, B, C, D, F) залежно від балу. Якщо бал < 0 або > 100, викликати помилку.
**Тест:** У файлі `test.py` протестуйте граничні значення (наприклад, 59 і 60, 89 і 90) та некоректні вхідні дані.

---

### Файл [`main.py`](./main.py)
```python
def get_grade(score: int) -> str:
    """
    Функція повертає оцінку залежно від балу.
    :param score: Бал студента (діапазон 0–100).
    :return: Оцінка (A, B, C, D, F).
    """
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"
```

---

### Файл [`test.py`](./test.py)
```python
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
```

### Рузультат:
```bash
Dima@HOME-PC MINGW64 ~/2025_kn340_testing_ss_and_complexes_dmytro_kshyvetskyi/exam (main)
$ python -m unittest test.py
...
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK

```

---

## Як запустити

#### Запустіть тести командою:

```bash
cd exam/
python -m unittest test.py
```
