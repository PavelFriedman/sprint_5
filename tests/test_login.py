import pytest
from locators import (
    LOGIN_BUTTON_MAIN,
    LOGIN_BUTTON_PERSONAL,
    ACCOUNT_LINK
)
from helpers import login_common

BASE_URL = "http://stellarburgers.com"  # Укажите актуальный URL

class TestLogin:
    def test_login_from_main_page(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*LOGIN_BUTTON_MAIN).click()
        login_common(driver)
        account_elements = driver.find_elements(*ACCOUNT_LINK)
        assert len(account_elements) > 0, "Вход не выполнен через кнопку 'Войти в аккаунт' на главной"

    def test_login_from_personal_cabinet(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*LOGIN_BUTTON_PERSONAL).click()
        login_common(driver)
        account_elements = driver.find_elements(*ACCOUNT_LINK)
        assert len(account_elements) > 0, "Вход не выполнен через кнопку 'Личный кабинет'"
