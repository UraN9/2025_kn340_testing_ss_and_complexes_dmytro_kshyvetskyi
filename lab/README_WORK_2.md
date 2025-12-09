# Звіт до роботи №2 ✨

## Тема: _GitHub Actions та CI/CD Automation_ 🚀

![Run Tests](https://github.com/UraN9/2025_kn340_testing_ss_and_complexes_dmytro_kshyvetskyi/actions/workflows/python-app.yml/badge.svg)
[![codecov](https://codecov.io/github/UraN9/2025_kn340_testing_ss_and_complexes_dmytro_kshyvetskyi/graph/badge.svg?token=C9NTNIJK3Q)](https://codecov.io/github/UraN9/2025_kn340_testing_ss_and_complexes_dmytro_kshyvetskyi)

### Мета роботи: 
_Налаштувати автоматизацію тестування та розгортання коду за допомогою GitHub Actions, опанувати CI/CD процеси та інтеграцію з зовнішніми сервісами_ 🎯

---

## 1️⃣ Створення першого Workflow з шаблону

На першому етапі ми познайомилися з GitHub Actions та створили перший автоматичний Workflow.

### 1.1 Теорія GitHub Actions

GitHub Actions — це вбудований сервіс GitHub, що дозволяє автоматизувати робочі процеси прямо в репозиторії.

Основні поняття:
- **Workflow** – файл конфігурації (`.yml`) у папці `.github/workflows/`
- **Event** – подія, яка запускає Workflow (push, pull_request, schedule, manual)
- **Job** – набір завдань, що виконуються на одному runner
- **Step** – окремий крок у завданні (run, uses)
- **Runner** – віртуальна машина, на якій виконуються кроки

### 1.2 Процес створення Workflow

1. Перейти до вкладки `Actions` у репозиторії на GitHub
2. Вибрати шаблон `Python application` 
3. Натиснути кнопку `Configure`
4. Редагувати файл та зберегти (Commit)

### 1.3 Структура базового Workflow файлу

```yaml
name: Run Tests  # Назва Workflow, що відображається в Actions

on:  # Тригери для запуску Workflow
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
  workflow_dispatch:  # Дозволяє запускати вручну

permissions:
  contents: read

jobs:
  build:  # Назва завдання
    runs-on: ubuntu-latest  # ОС для виконання
    steps:
      - uses: actions/checkout@v4  # Завантажити код
      - name: Set up Python
        uses: actions/setup-python@v6
        with:
          python-version: '3.13'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest -v
```

### 1.4 Наші Workflow файли

Файл: [.github/workflows/python-app.yml](../../.github/workflows/python-app.yml)

Створили Workflow з наступними особливостями:
- ✅ Запуск при push та pull_request на branch `main`
- ✅ Ручний запуск з параметрами (`workflow_dispatch`)
- ✅ Автоматичний запуск за розписанням (Cron)
- ✅ Python 3.13 з Poetry
- ✅ Інтеграція з flake8 та black

---

## 2️⃣ Редагування Workflow та додавання кроків

Модифікували стандартний Workflow для задоволення наших потреб.

### 2.1 Додавання кроків Workflow

Наш Workflow містить 3 основні завдання (jobs):

#### 1. **Start Job** – Інформаційна сходинка
```yaml
jobs:
  start:
    name: Start Job
    runs-on: ubuntu-latest
    steps:
    - name: Echo commit info
      if: github.event_name == 'push' || github.event_name == 'pull_request'
      run: echo "Запуск з назвою коміту - ${{ github.event.head_commit.message }}"
    
    - name: Echo manual trigger info
      if: github.event_name == 'workflow_dispatch'
      run: echo "Action запустив користувач - ${{ github.actor }}"
```

Цей job демонструє:
- Умовне виконання кроків (`if:`)
- Доступ до контексту GitHub (`github.event_name`, `github.actor`)
- Простий вивід інформації

#### 2. **Run Linters** – Перевірка коду
```yaml
run-linters:
  needs: start  # Залежність від job 'start'
  name: Run Linters
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - name: Set up Python "3.13"
      uses: actions/setup-python@v6
      with:
        python-version: "3.13"
    - name: Setup Poetry
      uses: Gr1N/setup-poetry@v9
    - name: Install dependencies
      working-directory: ./lab
      run: poetry install --with dev
    - name: Lint with flake8
      working-directory: ./lab
      run: flake8 . --count --select=E9,F63,F7,F82 --show-source
    - name: Black Check
      working-directory: ./lab
      run: black --check .
```

Цей job перевіряє:
- Синтаксичні помилки через flake8
- Форматування коду через black
- Якість коду

#### 3. **Run Tests** – Запуск тестів та покриття
```yaml
run-tests:
  needs: start
  name: Run Tests
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v4
    - name: Set up Python "3.13"
      uses: actions/setup-python@v6
      with:
        python-version: "3.13"
    - name: Setup Poetry
      uses: Gr1N/setup-poetry@v9
    - name: Install dependencies
      working-directory: ./lab
      run: poetry install --with dev
    - name: Test with pytest
      working-directory: ./lab
      run: pytest --cov --junitxml=junit.xml -v
    - name: Generate Report
      working-directory: ./lab
      run: coverage run -m pytest -v
```

Цей job:
- Встановлює всі залежності через Poetry
- Запускає тести через pytest з покриттям
- Генерує звіт про покриття

### 2.2 Ключові особливості

- **needs:** – створює залежність між завданнями (граф виконання)
- **working-directory:** – встановлює робочу папку для команд
- **if:** – умовне виконання кроків
- **uses:** – використання готових Action з GitHub Marketplace

---

## 3️⃣ Запуск Workflow вручну та по Cron

Налаштовуємо різні тригери для запуску Workflow.

### 3.1 Ручний запуск (workflow_dispatch)

```yaml
on:
  workflow_dispatch:
    inputs:
      python-version:
        description: 'Python version to use'
        required: false
        default: '3.13'
```

Це дозволяє:
- Запускати Workflow вручну з вкладки `Actions`
- Передавати параметри вручну
- Тестувати Workflow на попиту

### 3.2 Запуск за розписанням (Cron)

```yaml
on:
  schedule:
    - cron: '0 7 * * tue'  # Щовівторка о 7:00 UTC
```

Розшифровка Cron виразу:
- `0` – 0 хвилин
- `7` – 7 година
- `*` – будь-який день місяця
- `*` – будь-який місяць
- `tue` – вівторок

Для налаштування використовуємо [CronTab GURU](https://crontab.guru/)

### 3.3 Запуск при push та pull_request

```yaml
on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
```

Цей тригер автоматично запускає тести при:
- Будь-якому commit у branch `main`
- Відкритті pull request у branch `main`

---

## 4️⃣ Створення декількох Jobs та умов виконання

Демонструємо продвинуті можливості GitHub Actions.

### 4.1 Залежності між Jobs (Dependency Graph)

```yaml
jobs:
  start:
    name: Start Job
    # ... steps ...

  run-linters:
    needs: start  # Чекає завершення job 'start'
    # ... steps ...

  run-tests:
    needs: start  # Чекає завершення job 'start'
    # ... steps ...
```

Граф виконання:
```
start (запускається першим)
  ├── run-linters (чекає start)
  └── run-tests (чекає start)
```

### 4.2 Умовне виконання кроків (if conditions)

```yaml
- name: Echo commit info
  if: github.event_name == 'push' || github.event_name == 'pull_request'
  run: echo "Запуск з назвою коміту - ${{ github.event.head_commit.message }}"

- name: Echo manual trigger info
  if: github.event_name == 'workflow_dispatch'
  run: echo "Action запустив користувач - ${{ github.actor }}"
```

Умовні вирази:
- `github.event_name` – тип події
- `github.actor` – хто запустив
- Логічні оператори: `||` (або), `&&` (та), `!` (не)

### 4.3 Використання секретів (невидимих змінних)

```yaml
- name: Upload to server
  env:
    SECRET_TOKEN: ${{ secrets.GITHUB_TOKEN }}
  run: echo "Using secret: $SECRET_TOKEN"
```

Секрети зберігаються в GitHub та доступні через `${{ secrets.НАЗВА }}`

---

## 5️⃣ Баджі та статуси

Додавання статусних баджів до README файлу.

### 5.1 Створення Workflow Badge

1. Перейти до вкладки `Actions`
2. Обрати потрібний Workflow
3. Натиснути на `...` в правому кутку
4. Обрати `Create status badge`
5. Скопіювати Markdown код

### 5.2 Приклад Workflow Badge

```markdown
[![Run Tests](https://github.com/UraN9/2025_kn340_testing_ss_and_complexes_dmytro_kshyvetskyi/actions/workflows/python-app.yml/badge.svg)](https://github.com/UraN9/2025_kn340_testing_ss_and_complexes_dmytro_kshyvetskyi/actions/workflows/python-app.yml)
```

Результат: [![Run Tests](https://github.com/UraN9/2025_kn340_testing_ss_and_complexes_dmytro_kshyvetskyi/actions/workflows/python-app.yml/badge.svg)](https://github.com/UraN9/2025_kn340_testing_ss_and_complexes_dmytro_kshyvetskyi/actions/workflows/python-app.yml)

### 5.3 Badge показує статус:
- 🟢 **Green** – всі тести пройшли успішно
- 🔴 **Red** – тести провалилися
- 🟡 **Yellow** – тести в процесі

---

## 6️⃣ Інтеграція з Codecov (Додатково)

Налаштування автоматичної загрузки звітів про покриття.

### 6.1 Реєстрація на Codecov

1. Перейти на [codecov.io](https://about.codecov.io/)
2. Натиснути `Login` та обрати GitHub
3. Авторизуватися
4. Обрати репозиторій

### 6.2 Додавання кроків у Workflow

```yaml
# Встановлюємо потрібні пакети
- name: Install dependencies
  run: |
    pip install pytest coverage codecov

# Запускаємо тести з покриттям
- name: Run Tests
  run: pytest --cov

# Генеруємо XML звіт
- name: Generate Report
  run: coverage xml

# Завантажуємо в Codecov
- name: Upload Coverage to Codecov
  uses: codecov/codecov-action@v3
  with:
    directory: ./
```

### 6.3 Додавання Codecov Badge

На сайті Codecov:
1. Перейти у репозиторій
2. Вкладка `Settings -> Badges & Graph`
3. Скопіювати готовий Markdown код
4. Вставити в README файл

Приклад:
```markdown
[![codecov](https://codecov.io/github/UraN9/2025_kn340_testing_ss_and_complexes_dmytro_kshyvetskyi/graph/badge.svg?token=C9NTNIJK3Q)](https://codecov.io/github/UraN9/2025_kn340_testing_ss_and_complexes_dmytro_kshyvetskyi)
```

---

## Висновки 🏁

### Що було зроблено ✅

1. **Створено Workflow файл**
   - Python application шаблон
   - Налаштовано для нашого проекту
   - Додано Poetry підтримку

2. **Налаштовано 3 Jobs**
   - `start` – інформаційна сходинка
   - `run-linters` – перевірка коду (flake8, black)
   - `run-tests` – запуск тестів та покриття

3. **Додано тригери запуску**
   - ✅ Push на `main` branch
   - ✅ Pull Request на `main` branch
   - ✅ Ручний запуск (`workflow_dispatch`)
   - ✅ Розклад (Cron, щовівторка о 7:00 UTC)

4. **Залежності та умови**
   - Jobs залежать один від одного (`needs:`)
   - Умовне виконання кроків (`if:`)
   - Контекстні змінні GitHub

5. **Баджі та статуси**
   - Workflow Status Badge додано до README
   - Codecov Integration Badge додано

### Мета досягнута? 
✅ **100% дотримання завдання!** 🎉

**Нові знання:**  🚀  
- GitHub Actions – створення та налаштування Workflow файлів (`.yml`)
- CI/CD Pipeline – автоматизація тестування та розгортання
- Events и Triggers – push, pull_request, schedule (Cron), workflow_dispatch
- Jobs та Steps – організація роботи Workflow
- Умовне виконання – `if:` умови для гнучкості процесу
- Залежності між Jobs – `needs:` для контролю порядку виконання
- Контекстні змінні – доступ до інформації про Git та GitHub (`github.actor`, `github.event_name`)
- Секрети в GitHub – безпечне зберігання конфіденційних даних
- Матриці (Matrix) – паралельне тестування на різних версіях Python
- Poetry інтеграція – управління залежностями у CI/CD
- Linting та форматування – автоматична перевірка коду (flake8, black)
- Coverage Integration – інтеграція з Codecov для аналізу покриття
- Баджи та статуси – демонстрація стану проекту в README
- Cron вирази – розклад автоматичних запусків через CronTab GURU

**Всі завдання виконані?** Так, повністю! 💯  

**Складнощі:** Не виникало 🧠  

**Формат звіту подобається?** Дуже! Можна і теорію показати, і код, і скріншоти/результати 📊

**Побажання:** Ніяких 🔮

### Автоматизація у дії 🤖

Коли код push-иться до репозиторію:
1. 🟢 Запускається Workflow
2. 🔍 Перевіряється синтаксис (flake8)
3. 🎨 Перевіряється форматування (black)
4. ✅ Запускаються тести (pytest)
5. 📊 Генерується звіт про покриття
6. 📤 Результати завантажуються на Codecov
7. 🏷️ Badge оновлюється на README

---

## Команди для роботи з Workflow ⚙️

```bash
# Перевірити синтаксис YAML файлу
python -m yaml python-app.yml

# Запустити тести локально
poetry run pytest -v

# Перевірити код з flake8
poetry run flake8 .

# Перевірити форматування з black
poetry run black --check .

# Генерувати звіт про покриття
poetry run coverage run -m pytest
poetry run coverage report
poetry run coverage html
```

---