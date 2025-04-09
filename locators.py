from selenium.webdriver.common.by import By

# === Регистрация ===
REGISTRATION_NAME_INPUT = (By.XPATH, "//input[@name='name']")              # Поле ввода имени при регистрации
REGISTRATION_EMAIL_INPUT = (By.XPATH, "//input[@name='email']")            # Поле ввода email при регистрации
REGISTRATION_PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")      # Поле ввода пароля при регистрации
REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка «Зарегистрироваться»

# Сообщения об ошибках при регистрации
PASSWORD_ERROR_MESSAGE = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")  # Ошибка для некорректного пароля

# === Вход в систему ===
LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")       # Кнопка «Войти в аккаунт» на главной странице
LOGIN_BUTTON_PERSONAL = (By.XPATH, "//a[contains(@href, '/account')]")      # Кнопка «Личный кабинет»
# Дополнительно для форм:
LOGIN_BUTTON_REGISTRATION_FORM = (By.XPATH, "//button[text()='Войти']")    # Кнопка входа в форме регистрации
LOGIN_BUTTON_RECOVERY_FORM = (By.XPATH, "//button[text()='Войти']")        # Кнопка входа в форме восстановления пароля

# Поля ввода для входа
LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@name='email']")                 # Поле ввода email при входе
LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@name='password']")             # Поле ввода пароля при входе

# === Личный кабинет и переходы ===
ACCOUNT_LINK = (By.XPATH, "//a[contains(@href, '/account')]")             # Ссылка «Личный кабинет»
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выйти']")                     # Кнопка «Выйти» в личном кабинете

# Переход из личного кабинета в конструктор
CONSTRUCTOR_LINK = (By.XPATH, "//a[text()='Конструктор']")                # Кнопка «Конструктор»
LOGO_LINK = (By.XPATH, "//a[contains(@class, 'AppHeader_header__logo')]")   # Логотип Stellar Burgers

# === Раздел «Конструктор» ===
BUNS_TAB = (By.XPATH, "//span[text()='Булки']")                           # Вкладка «Булки»
SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")                          # Вкладка «Соусы»
FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")                      # Вкладка «Начинки»
