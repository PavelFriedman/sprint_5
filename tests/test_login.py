from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import (
    REGISTRATION_NAME_INPUT,
    REGISTRATION_EMAIL_INPUT,
    REGISTRATION_PASSWORD_INPUT,
    REGISTRATION_BUTTON,
    PASSWORD_ERROR_MESSAGE,
    ACCOUNT_LINK
)
from helpers import generate_email, generate_password  # Вспомогательные функции для генерации данных

BASE_URL = "http://stellarburgers.com"  # Укажите актуальный URL

class TestRegistration:
    def test_successful_registration(self, driver):
        """
        Тест проверяет успешную регистрацию.
        После регистрации ожидается появление элемента, свидетельствующего
        об успешном создании аккаунта (например, ссылка на личный кабинет).
        """
        driver.get(BASE_URL + "/register")
        wait = WebDriverWait(driver, 10)

        # Заполнение полей регистрации
        name_input = wait.until(EC.visibility_of_element_located(REGISTRATION_NAME_INPUT))
        name_input.send_keys("Test Name")

        email = generate_email(name="test", surname="testov", cohort="1999")
        email_input = wait.until(EC.visibility_of_element_located(REGISTRATION_EMAIL_INPUT))
        email_input.send_keys(email)

        password = generate_password(8)
        password_input = wait.until(EC.visibility_of_element_located(REGISTRATION_PASSWORD_INPUT))
        password_input.send_keys(password)

        # Клик по кнопке регистрации
        reg_button = wait.until(EC.element_to_be_clickable(REGISTRATION_BUTTON))
        reg_button.click()

        # Ожидание появления элемента "Личный кабинет" как признака успешной регистрации
        account_elem = wait.until(EC.visibility_of_element_located(ACCOUNT_LINK))
        assert account_elem.is_displayed(), "Элемент 'Личный кабинет' не найден – регистрация не выполнена успешно"

    def test_registration_with_invalid_password(self, driver):
        """
        Тест проверяет, что при попытке регистрации с некорректным паролем
        (менее 6 символов) отображается сообщение об ошибке.
        """
        driver.get(BASE_URL + "/register")
        wait = WebDriverWait(driver,
