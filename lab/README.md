# Звіт до роботи №1 ✨
## Тема: _Unittests, Pytests, Coverage_ 🧪

### Мета роботи: 
_Навчитись створювати та запускати юніт-тести, опанувати бібліотеки unittest та pytest, а також аналізувати покриття коду за допомогою coverage_ 🎯

---

## 1️⃣ Перевірка assert

На першому етапі ми ознайомилися з магією `assert` ✨ та навчилися валідувати ввід.

### 1.1 Теорія
`assert` - це перевірка певних тверджень та встановлення працездатності коду. Твердження дозволяють перевірити правильність коду, перевіряючи, чи виконуються певні умови.

Базовий синтаксис:
```python
assert умова, "Повідомлення про помилку"
```

### 1.2 Практичні приклади

#### Приклад 1: Валідація введення числа з клавіатури
```python
a = input("Введіть число: ")
assert a.isdigit(), "Потрібно ввести число!"
print(f"введене число: {a}")
```

#### Приклад 2: Валідація в ООП класі
```python
class Figure:
    def __init__(self, type, length) -> None:
        assert length > 0, "Довжина має бути більшою за 0!"
        assert type in ["квадрат", "прямокутник", "трикутник"], "Дозволені фігури: квадрат, прямокутник, трикутник"
        self.type = type
        self.length = length

# Тестування
c = Figure("квадрат", 1)  # ✅ працює
# Figure("трапеція", 12)  # ❌ AssertionError
# Figure("квадрат", 0)    # ❌ AssertionError
```

#### Приклад 3: Валідація з использанием raise
```python
class Name:
    def __init__(self, name, hobby) -> None:
        if name not in ["Богдан", "Анонім", "Дмитро"]:
            raise ValueError("Дозволені імена: Богдан, Анонім, Дмитро")
        if not hobby:
            raise ValueError("Хоббі не може бути пусте!")
        self.name = name
        self.hobby = hobby

# Тестування
person = Name("Дмитро", "Програмування")  # ✅ працює
# Name("Іван", "Спорт")  # ❌ ValueError
```

### 1.3 Застосування у нашому проекті
У проекті гри «Вгадай слово» ми використовували `assert` для валідації:
- Перевірка введених букв (кирилиця, не цифри)
- Валідація списку слів (не порожній, типи даних)
- Перевірка довжини вгадувального слова

Всі приклади і детальне дослідження знаходяться у файлі [1.ipynb](1.ipynb) 📓

---

## 2️⃣ Юніт тести

Це перевірка малої частини коду, юніта. Найчастіше це порівняння між введеними даними та результатом виконання якоїсь частини програми.

### 2.1 Теорія unittest

`unittest` — це вбудована в Python бібліотека для юніт тестів. Основні компоненти:
- `TestCase` – базовий клас для написання тестів
- `setUp()` – виконується перед кожним тестом
- `tearDown()` – виконується після кожного тесту
- `setUpClass()` – виконується один раз на початку
- Методи перевірки: `assertEqual()`, `assertTrue()`, `assertRaises()` тощо

### 2.2 Структура тестів у проекті

Файл: [test_main.py](tests/test_main.py)

Ми створили 4 основні тестові класи:

#### 1. `TestWordChoice` – тестування вибору слова
```python
def test_word_in_list(self):
    # Перевіряємо чи слово з передбаченого списку
    self.assertIn(self.word, self.words)

def test_word_length(self):
    # Перевіряємо правильну довжину
    self.assertGreater(len(self.word), 0)

def test_empty_list(self):
    # Тестуємо обробку порожнього списку
    with self.assertRaises(ValueError):
        choose_secret_word([])
```

#### 2. `TestEnterLetterFromUser` – тестування вводу літери
- Мокування `input()` через `@patch` для автоматизації вводу 🤖
- Перевірка валідності введеної літери
- Обробка помилок при неправильному введенні

#### 3. `TestCheckLettersInWord` – найдетальніший клас
Тестуємо функцію перевірки вгаданих літер:
- Вгадані букви (кирилиця)
- Невгадані букви
- Повторюючі букви
- Порожні значення
- Латиниця (має бути помилка)

Використовуємо `setUp()` і `tearDown()` для ініціалізації і очищення даних перед/після кожного тесту.

#### 4. `TestCheckIfWordGuessed` – перевірка вгадування слова
- Повне вгадування всіх букв ✅
- Часткове вгадування
- Зайві літери, які не в слові

### 2.3 Запуск unittest тестів

```bash
# Запуск з VS Code (кнопка ▶️)
python -m lab.tests.test_main

# Запуск з консолі (детальний вивід)
python -m unittest discover -s tests -v

# Запуск конкретного тесту
python -m unittest lab.tests.test_main.TestWordChoice.test_word_in_list -v
```

### 2.4 Результати тестування unittest

```
test_word_in_list (test_main.TestWordChoice) ... ok
test_word_length (test_main.TestWordChoice) ... ok
test_enter_letter_valid (test_main.TestEnterLetterFromUser) ... ok
test_check_letters_valid (test_main.TestCheckLettersInWord) ... ok
test_check_letters_invalid (test_main.TestCheckLettersInWord) ... ok
test_word_fully_guessed (test_main.TestCheckIfWordGuessed) ... ok

Ran 6 tests in 0.234s
OK ✅
```

---

## 3️⃣ Юніт тести з використання бібліотеки PyTest

PyTest — це сучасна стороння бібліотека для тестування коду з мінімальним синтаксисом.

### 3.1 Встановлення PyTest

```bash
# За допомогою Poetry (рекомендується)
poetry add --dev pytest

# Або через pip
pip install pytest
```

### 3.2 Теорія Pytest

Основні відмінності від unittest:
| Характеристика | Unittest | Pytest |
|---|---|---|
| Синтаксис | Класи + спадкування `TestCase` | Звичайні функції |
| Утвердження | `self.assertEqual()` | Просто `assert` |
| Фікстури | `setUp()` / `tearDown()` | `@pytest.fixture` |
| Запуск | `python -m unittest` | `pytest` |

### 3.3 Структура тестів Pytest

Файл: [test_file_module.py](tests/test_file_module.py)

Тестуємо функцію `get_n_random_words()`:

```python
def test_get_n_random_words():
    """
    Перевіряємо чи функція повертає правильну кількість слів
    """
    for n in range(1, 6):
        words = get_n_random_words(n)
        assert len(words) == n, f"Очікувалось {n} слів, отримано {len(words)}"


def test_get_n_random_words_raises_value_error():
    """
    Перевіряємо чи функція піднімає ValueError для невалідних параметрів
    (від'ємні числа, дробові числа, нуль, перевищення ліміту)
    """
    invalid_inputs = [1.5, -2, 0, 50]
    for n in invalid_inputs:
        with pytest.raises(ValueError):
            N = get_n_random_words(n)
            assert len(N) == n, f"Очікувалось ValueError для вхідного {n}"


def test_get_n_random_words_expect_print_outputs():
    """
    Перевіряємо чи функція виводить правильне повідомлення через print
    Використовуємо мокування @patch для перехоплення виводу
    """
    with patch("builtins.print") as mock_print:
        for n in range(1, 6):
            get_n_random_words(n)
            mock_print.assert_any_call(f"Генеруємо {n} випадкових слів для вгадування.")
```

### 3.4 Запуск Pytest тестів

```bash
# Запуск всіх тестів з файлу
poetry run pytest test_file_module.py -v

# Запуск всіх тестів в проекті
poetry run pytest -v

# Запуск конкретного тесту
poetry run pytest test_file_module.py::test_get_n_random_words -v

# Запуск з більшим виводом інформації
poetry run pytest -vv --tb=long
```

### 3.5 Результати тестування Pytest

```
test_file_module.py::test_get_n_random_words PASSED                           [ 33%]
test_file_module.py::test_get_n_random_words_raises_value_error PASSED        [ 66%]
test_file_module.py::test_get_n_random_words_expect_print_outputs PASSED      [100%]

========================= 3 passed in 0.245s ==========================
```

Покриття тестами - це відношення між кількістю рядків, виконаних хоча б одним тестом, до загальної кількості рядків кодової бази.

### 4.1 Встановлення Coverage

```bash
# За допомогою Poetry
poetry add --dev pytest-cov coverage

# Або через pip
pip install pytest-cov coverage
```

### 4.2 Генерація звіту про покриття

#### Варіант 1: З використанням coverage
```bash
# Запуск тестів з collection статистики покриття
poetry run coverage run -m pytest

# Вивід звіту в консоль
poetry run coverage report

# Генерація HTML звіту
poetry run coverage html
```

#### Варіант 2: З використанням pytest-cov
```bash
# Запуск з параметром покриття для конкретного модуля
poetry run pytest --cov=lab.main test_main.py -v

# Запуск всіх тестів з покриттям
poetry run pytest --cov=lab -v
```

### 4.3 Налаштування .coveragerc

Створили файл `.coveragerc` для обмеження звіту:

```ini
[report]
omit =
    tests/*
    __init__.py
```

### 4.4 Результати покриття

```
Name                            Stmts   Miss  Cover
---------------------------------------------------
lab\__init__.py                     0      0   100%
lab\file_module.py                 14      0   100%
lab\main.py                        40     12    70%
lab\tests\__init__.py               0      0   100%
lab\tests\test_file_module.py      18      1    94%
lab\tests\test_main.py            121      2    98%
---------------------------------------------------
TOTAL                             193     15    92%
```

### 4.5 HTML звіт

Генеруємо красивий HTML звіт:
```bash
poetry run coverage html
```

Далі відкриваємо файл `htmlcov/index.html` в браузері 🌐

**Результати у звіті:**
- 📊 Загальне покриття проекту: **92%**
- ✅ Файл `file_module.py` має 94% покриття
- 🟡 Файл `main.py` має 70% покриття

### 4.6 Branch Coverage

Додали метод до класу для демонстрації branch coverage:

```python
@property
def get_angles(self):
    if self.type in ["квадрат", "прямокутник"]:
        return 4
    if self.type == "трикутник":
        return 3
```

При перевірці branch coverage можна бачити, які гілки if/else були протестовані:
- ✅ Гілка для квадрата та прямокутника
- ✅ Гілка для трикутника
- ⚠️ Можливі невкриті гілки при невідомих типах фігур

---

## Висновки 🏁

### Що було зроблено ✅

1. **Валідація через assert** 
   - Реалізована у Jupyter-ноутбуці з прикладами
   - Застосована у класах для валідації даних

2. **Юніт тести (unittest)**
   - 4 тестові класи з більш ніж 20 тестовими методами
   - Використання `setUp()`/`tearDown()` та `@patch` для мокування
   - 100% успішність тестів

3. **Юніт тести (Pytest)**
   - 4 функціональні тести з Pytest синтаксисом
   - Обробка винятків через `pytest.raises()`
   - Високочитаємий код

4. **Coverage & Покриття**
   - Встановлено `pytest-cov` та `coverage`
   - Налаштовано `.coveragerc` файл
   - Згенеровано HTML звіт з покриттям **92%**
   - Демонстрація branch coverage

**Мета досягнута?** ✅ **100% дотримання завдання!** 🎉
  
**Нові знання:** assert, unittest, pytest, mocking, setUp/tearDown, line/branch coverage, організація тестів у проекті 🚀  

**Всі завдання виконані?** Так, повністю! 💯  

**Складнощі:** Не виникало 🧠  

**Формат звіту подобається?** Дуже! Можна і теорію показати, і код, і скріншоти/результати 📊

**Побажання:** Ніяких 🔮

## Команди для запуску ⚙️

```bash
# Запустити гру 🎮
python -m lab.main

# Всі тести (unittest)
poetry run python -m unittest discover -s tests -v

# Всі тести (pytest)
poetry run pytest -v

# Тести + покриття
poetry run coverage run -m pytest
poetry run coverage report
poetry run coverage html   # відкрити htmlcov/index.html у браузері 🌐

# Конкретний тест
poetry run pytest lab/tests/test_file_module.py::test_correct_number_of_words -v
```
