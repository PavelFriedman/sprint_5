from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
from conftest import driver, login


class TestSwitchBlocksOnConstructor:
    # Проверка перехода из раздела "Булки" в раздел "Начинки", с логином
    def test_navigate_to_fillings_block_from_buns_on_constructor_success(self, driver, login):
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(
            TestLocators.button_make_the_order))
        driver.find_element(*TestLocators.fillings_block).click()
        assert driver.find_element(*TestLocators.selected_button).text == "Начинки"

    # Проверка перехода из раздела "Соусы" в раздел "Начинки", без логина
    def test_navigate_to_fillings_block_from_sauces_on_constructor_success(self, driver):
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(
            TestLocators.button_login_in_main))
        driver.find_element(*TestLocators.sauces_block).click()
        driver.find_element(*TestLocators.fillings_block).click()
        assert driver.find_element(*TestLocators.selected_button).text == "Начинки"

    # Проверка перехода из раздела "Булки" в раздел "Соусы", с логином
    def test_navigate_to_sauces_block_from_buns_on_constructor_success(self, driver, login):
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(
            TestLocators.button_make_the_order))
        driver.find_element(*TestLocators.sauces_block).click()
        assert driver.find_element(*TestLocators.selected_button).text == "Соусы"

    # Проверка перехода из раздела "Начинки" в раздел "Соусы", без логина
    def test_navigate_to_sauces_block_from_fillings_on_constructor_success(self, driver):
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(
            TestLocators.button_login_in_main))
        driver.find_element(*TestLocators.fillings_block).click()
        driver.find_element(*TestLocators.sauces_block).click()
        assert driver.find_element(*TestLocators.selected_button).text == "Соусы"

    # Проверка перехода из раздела "Соусы" в раздел "Булки", с логином
    def test_navigate_to_buns_block_from_sauces_on_constructor_success(self, driver, login):
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(
            TestLocators.button_make_the_order))
        driver.find_element(*TestLocators.sauces_block).click()
        driver.find_element(*TestLocators.buns_block).click()
        assert driver.find_element(*TestLocators.selected_button).text == "Булки"

    # Проверка перехода из раздела "Начинки" в раздел "Булки", без логина
    def test_navigate_to_buns_block_from_fillings_on_constructor_success(self, driver):
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(
            TestLocators.button_login_in_main))
        driver.find_element(*TestLocators.fillings_block).click()
        driver.find_element(*TestLocators.buns_block).click()
        assert driver.find_element(*TestLocators.selected_button).text == "Булки"