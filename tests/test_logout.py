import time
import pytest
from selenium.webdriver.common.by import By
from locators import ACCOUNT_LINK, LOGOUT_BUTTON, LOGIN_BUTTON_MAIN

BASE_URL = "http://stellarburgers.com"


def test_logout(driver):
    driver.get(BASE_URL)

    # Переход в Личный кабинет и выполнение входа (при необходимости добавьте код входа)
    driver.find_element(*ACCOUNT_LINK).click()
    time.sleep(1)
    # ... (код входа, если требуется)

    driver.find_element(*LOGOUT_BUTTON).click()
    time.sleep(1)

    login_button = driver.find_element(*LOGIN_BUTTON_MAIN)
    assert login_button.is_displayed(), "После выхода кнопка 'Войти в аккаунт' не отображается, выход не выполнен"
