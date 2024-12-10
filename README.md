# Design and Analysis of Algorithms

## Тиждень 1

- [Chapter 01](./Chapter_01/) - Тема 1. Аналіз алгоритмів. Стратегія «розділяй і володарюй»
- [Chapter 02](./Chapter_02/) - Тема 2. Жадібні алгоритми та динамічне програмування

## Тиждень 2

- [Chapter 03](./Chapter_03/) - Тема 3. Графи та дерева
- [Chapter 04](./Chapter_04/) - Тема 4. Префіксні дерева

## Тиждень 3

- [Chapter 05](./Chapter_05/) - Тема 5. Алгоритми роботи з великими даними
- [Chapter 06](./Chapter_06/) - Тема 6. Основи паралельних обчислень і модель MapReduce

## Тиждень 4

- [Chapter 07](./Chapter_07/) - Тема 7. Алгоритми керування кешем
- [Chapter 08](./Chapter_08/) - Тема 8. Алгоритми контролю потоку та обмеження швидкості

## Тиждень 5

- [Chapter 09](./Chapter_09/) - Тема 9. Локальний пошук, евристики та імітація відпалу
- [Chapter 10](./Chapter_10/) - Тема 10. Алгоритмічна складність, наближені та рандомізовані алгоритми

### Інструкція з встановлення залежностей

Щоб встановити всі пакети з файлу `requirements.txt` і налаштувати середовище для запуску прикладів з нашого репозиторію, виконайте наступні кроки.

#### 1. Перевірка встановлення Python і pip

Спочатку переконайтеся, що Python встановлено. Відкрийте термінал (або командний рядок) і виконайте команду:

```bash
python --version
```

або, якщо у вашій системі використовується Python 3:

```bash
python3 --version
```

У відповідь має з'явитися номер версії Python, наприклад `Python 3.10.9`. Якщо Python не встановлено, завантажте його з [офіційного сайту](https://www.python.org/) і встановіть.

Перевірте наявність `pip`:

```bash
pip --version
```

або:

```bash
pip3 --version
```

Якщо `pip` відсутній, встановіть його командою:

```bash
python -m ensurepip --upgrade
```

#### 2. Створення віртуального середовища

Рекомендується створити віртуальне середовище для ізоляції залежностей проєкту. Для цього виконайте:

```bash
python -m venv .venv
```

Ця команда створить папку `.venv` у корені вашого репозиторію, де зберігатимуться всі залежності.

#### 3. Активація віртуального середовища

Щоб почати працювати у створеному середовищі, активуйте його:

- **На Windows**:

    ```bash
    .venv\Scripts\activate
    ```

- **На macOS або Linux**:

    ```bash
    source .venv/bin/activate
    ```

Після активації перед вашим запитом у терміналі з'явиться префікс `(.venv)`.

#### 4. Встановлення залежностей

Для встановлення залежностей виконайте:

```bash
pip install -r requirements.txt
```

Ця команда автоматично завантажить і встановить усі зазначені у файлі пакети.

#### 5. Запуск прикладів

Тепер ви можете запускати скрипти чи приклади з репозиторію. Наприклад:

```bash
python your_script.py
```

#### 6. Деактивація віртуального середовища

Після завершення роботи деактивуйте віртуальне середовище командою:

```bash
deactivate
```

##### Команда розробки

Автор курсу - Юрій Кучма

Методолог - Дар’я Турко

Проджект-менеджер - Юлія Садова
