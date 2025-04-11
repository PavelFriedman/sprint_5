import time
import pytest
from selenium.webdriver.common.by import By
from locators import (
    REGISTRATION_NAME_INPUT,
    REGISTRATION_EMAIL_INPUT,
    REGISTRATION_PASSWORD_INPUT,
    REGISTRATION_BUTTON,
    PASSWORD_ERROR_MESSAGE
)
from generators import generate_email, generate_password

BASE_URL = "http://stellarburgers.com"  # Укажите актуальный URL тестового приложения


def test_successful_registration(driver):
    driver.get(f"{BASE_URL}/register")

    # Заполняем форму регистрации
    driver.find_element(*REGISTRATION_NAME_INPUT).send_keys("Test Name")
    email = generate_email(name="test", surname="testov", cohort="1999")
    driver.find_element(*REGISTRATION_EMAIL_INPUT).send_keys(email)
    password = generate_password(8)
    driver.find_element(*REGISTRATION_PASSWORD_INPUT).send_keys(password)

    driver.find_element(*REGISTRATION_BUTTON).click()
    time.sleep(2)  # Лучше использовать WebDriverWait для ожидания элементов

    # Проверяем наличие ссылки в личном кабинете как сигнал об успешной регистрации
    account_elements = driver.find_elements(By.XPATH, "//a[contains(@href, '/account')]")
    assert len(account_elements) > 0, "Личный кабинет не найден — регистрация, возможно, не прошла успешно"


def test_registration_with_invalid_password(driver):
    driver.get(f"{BASE_URL}/register")

    driver.find_element(*REGISTRATION_NAME_INPUT).send_keys("Test Name")
    email = generate_email(name="test", surname="testov", cohort="1999")
    driver.find_element(*REGISTRATION_EMAIL_INPUT).send_keys(email)
    driver.find_element(*REGISTRATION_PASSWORD_INPUT).send_keys("123")  # Некорректный пароль

    driver.find_element(*REGISTRATION_BUTTON).click()
    time.sleep(2)

    error_element = driver.find_element(*PASSWORD_ERROR_MESSAGE)
    assert error_element.is_displayed(), "Сообщение об ошибке не отображается при некорректном пароле"
