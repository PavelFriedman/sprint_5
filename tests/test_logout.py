from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators
from conftest import driver, login


class TestLogout:
    # вход по кнопке «Войти в аккаунт» на главной
    def test_logout_of_personal_account_success(self, driver, login):
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(
            TestLocators.button_make_the_order))
        driver.find_element(*TestLocators.button_personal_account).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.profile))
        driver.find_element(*TestLocators.button_logout).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.button_login))
        assert driver.find_element(*TestLocators.button_login).is_displayed()