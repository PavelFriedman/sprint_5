from selenium.webdriver.common.by import By

# =================== Регистрация ===================
REGISTRATION_NAME_INPUT = (By.XPATH, "//input[@name='name']")
# Поле для ввода имени при регистрации

REGISTRATION_EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
# Поле для ввода email при регистрации

REGISTRATION_PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
# Поле для ввода пароля при регистрации

REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
# Кнопка "Зарегистрироваться"

PASSWORD_ERROR_MESSAGE = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")
# Сообщение об ошибке при некорректном пароле

# =================== Вход ===================
LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
# Кнопка "Войти в аккаунт" на главной странице

LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@name='email']")
# Поле ввода email в форме входа

LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")
# Поле ввода пароля в форме входа

LOGIN_BUTTON_PERSONAL = (By.XPATH, "//a[contains(@href, '/account')]")
# Ссылка или кнопка, ведущая к форме входа (например, "Личный кабинет")

ACCOUNT_LINK = (By.XPATH, "//a[contains(@href, '/account')]")
# Элемент "Личный кабинет", появляющийся после успешного входа

# =================== Раздел "Конструктор" ===================
CONSTRUCTOR_LINK = (By.XPATH, "//a[text()='Конструктор']")
# Ссылка "Конструктор"

LOGO_LINK = (By.XPATH, "//a[contains(@class, 'AppHeader_header__logo')]")
# Логотип, ведущий на главную страницу

BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
# Вкладка "Булки"

SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
# Вкладка "Соусы"

FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
# Вкладка "Начинки"

# =================== Выход ===================
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")
# Кнопка "Выйти" в личном кабинете
