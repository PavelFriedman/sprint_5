from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ACCOUNT_LINK, LOGOUT_BUTTON, LOGIN_BUTTON_MAIN

BASE_URL = "http://stellarburgers.com"  # Укажите актуальный URL


class TestLogout:
    def test_logout(self, driver):
        """
        Тест проверяет, что после выполнения процедуры выхода из аккаунта отображается
        кнопка "Войти в аккаунт", что свидетельствует о корректном выходе пользователя.
        """
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)

        # Переход в раздел "Личный кабинет"
        wait.until(EC.element_to_be_clickable(ACCOUNT_LINK)).click()

        # Ожидание и клик по кнопке "Выйти"
        wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()

        # Ожидание появления кнопки "Войти в аккаунт" как признака успешного выхода
        login_button = wait.until(EC.visibility_of_element_located(LOGIN_BUTTON_MAIN))
        assert login_button.is_displayed(), "После выхода кнопка 'Войти в аккаунт' не отображается, выход не выполнен"
