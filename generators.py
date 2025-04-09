Файл с функциями для генерации email и пароля:

```python
import random
import string

def generate_email(name="test", surname="testov", cohort="1999", domain="yandex.ru"):
    """
    Генерирует уникальный email в формате:
    имя_фамилия_номер когорты_3 случайных цифры@домен
    Пример: test_testov_1999_123@yandex.ru
    """
    random_digits = ''.join(random.choices(string.digits, k=3))
    email = f"{name}_{surname}_{cohort}_{random_digits}@{domain}"
    return email

def generate_password(length=8):
    """
    Генерирует случайный пароль, состоящий из букв и цифр.
    Минимальное требование — не менее 6 символов, рекомендуется 8 и более.
    """
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))
