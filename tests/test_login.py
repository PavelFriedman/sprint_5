import time
import pytest
from selenium.webdriver.common.by import By
from locators import (
    LOGIN_BUTTON_MAIN,
    LOGIN_BUTTON_PERSONAL,
    LOGIN_EMAIL_INPUT,
    LOGIN_PASSWORD_INPUT,
    LOGIN_BUTTON_REGISTRATION_FORM,
    LOGIN_BUTTON_RECOVERY_FORM
)
from generators import generate_email, generate_password

BASE_URL = "http://stellarburgers.com"  # Укажите актуальный URL

# Предполагается, что тестовый аккаунт уже создан
TEST_EMAIL = "your_registered_email@example.com"
TEST_PASSWORD = "your_registered_password"


def login_common(driver):
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(TEST_EMAIL)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(TEST_PASSWORD)
    driver.find_element(*LOGIN_BUTTON_MAIN).click()
    time.sleep(2)


def test_login_from_main_page(driver):
    driver.get(BASE_URL)

    driver.find_element(*LOGIN_BUTTON_MAIN).click()
    time.sleep(1)

    login_common(driver)

    account_elements = driver.find_elements(By.XPATH, "//a[contains(@href, '/account')]")
    assert len(account_elements) > 0, "Вход не выполнен через кнопку 'Войти в аккаунт' на главной"


def test_login_from_personal_cabinet(driver):
    driver.get(BASE_URL)

    driver.find_element(*LOGIN_BUTTON_PERSONAL).click()
    time.sleep(1)

    login_common(driver)

    account_elements = driver.find_elements(By.XPATH, "//a[contains(@href, '/account')]")
    assert len(account_elements) > 0, "Вход не выполнен через кнопку 'Личный кабинет'"
