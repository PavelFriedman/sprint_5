import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators import TestLocators
from conftest import driver
from helpers import create_random_email, create_random_password, create_email_base
from data import UsersTestData


class TestRegistration:
    # Регистрация аккаунта пользователя с валидными значениями инпутов
    def test_registration_new_account_success_submit(self, driver):
        random_email = create_random_email()
        random_password = create_random_password()
        driver.find_element(*TestLocators.button_login_in_main).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.button_register))
        driver.find_element(*TestLocators.button_register).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.button_submit))
        driver.find_element(*TestLocators.input_name).send_keys(UsersTestData.username)
        driver.find_element(*TestLocators.input_email).send_keys(random_email)
        driver.find_element(*TestLocators.input_password).send_keys(random_password)
        driver.find_element(*TestLocators.button_submit).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.button_login))
        assert driver.find_element(*TestLocators.button_register).is_displayed()

    # Регистрация аккаунта при пустом поле "Имя"
    def test_registration_name_is_empty_failed_submit(self, driver):
        random_email = create_random_email()
        random_password = create_random_password()
        driver.find_element(*TestLocators.button_login_in_main).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.button_register))
        driver.find_element(*TestLocators.button_register).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.button_submit))
        driver.find_element(*TestLocators.input_name).send_keys('')
        driver.find_element(*TestLocators.input_email).send_keys(random_email)
        driver.find_element(*TestLocators.input_password).send_keys(random_password)
        driver.find_element(*TestLocators.button_submit).click()
        assert driver.find_element(*TestLocators.button_submit).is_displayed()

    # Регистрация аккаунта при вводе невалидного значения в поле Email — отсутствует @
    def test_registration_invalid_email_format_without_at_failed_submit(self, driver):
        email_base = create_email_base()
        random_password = create_random_password()
        driver.find_element(*TestLocators.button_login_in_main).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.button_register))
        driver.find_element(*TestLocators.button_register).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.button_submit))
        driver.find_element(*TestLocators.input_name).send_keys(UsersTestData.username)
        driver.find_element(*TestLocators.input_email).send_keys(f'{email_base}yandex.ru')
        driver.find_element(*TestLocators.input_password).send_keys(random_password)
        driver.find_element(*TestLocators.button_submit).click()
        assert driver.find_element(*TestLocators.button_submit).is_displayed()

    # Регистрация аккаунта при вводе невалидного значения в поле Email — отсутствует домен первого уровня
    def test_registration_invalid_mail_format_with_invalid_domain_failed_submit(self, driver):
        email_base = create_email_base()
        random_password = create_random_password()
        driver.find_element(*TestLocators.button_login_in_main).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.button_register))
        driver.find_element(*TestLocators.button_register).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.button_submit))
        driver.find_element(*TestLocators.input_name).send_keys(UsersTestData.username)
        driver.find_element(*TestLocators.input_email).send_keys(f'{email_base}@ya.')
        driver.find_element(*TestLocators.input_password).send_keys(random_password)
        driver.find_element(*TestLocators.button_submit).click()
        assert driver.find_element(*TestLocators.button_submit).is_displayed()

    # Регистрация аккаунта при вводе валидного по длине значения в поле "Пароль"
    @pytest.mark.parametrize('valid_password', ['123456', '1234567', '123456789012'])
    def test_registration_valid_length_password_success_submit(self, driver, valid_password):
        random_email = create_random_email()
        driver.find_element(*TestLocators.button_login_in_main).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.button_register))
        driver.find_element(*TestLocators.button_register).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.button_submit))
        driver.find_element(*TestLocators.input_name).send_keys(UsersTestData.username)
        driver.find_element(*TestLocators.input_email).send_keys(random_email)
        driver.find_element(*TestLocators.input_password).send_keys(valid_password)
        driver.find_element(*TestLocators.button_submit).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.button_login))
        assert driver.find_element(*TestLocators.button_register).is_displayed()

    # Регистрация аккаунта при вводе НЕвалидного по длине значения в поле "Пароль"
    @pytest.mark.parametrize('wrong_password', ['12345', '1234', '1', ''])
    def test_registration_invalid_length_password_failed_submit(self, driver, wrong_password):
        random_email = create_random_email()
        driver.find_element(*TestLocators.button_login_in_main).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.button_register))
        driver.find_element(*TestLocators.button_register).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.button_submit))
        driver.find_element(*TestLocators.input_name).send_keys(UsersTestData.username)
        driver.find_element(*TestLocators.input_email).send_keys(random_email)
        driver.find_element(*TestLocators.input_password).send_keys(wrong_password)
        driver.find_element(*TestLocators.button_submit).click()
        assert driver.find_element(*TestLocators.button_submit).is_displayed()

    # Проверка появления подсказки при вводе НЕвалидного по длине значения в поле "Пароль"
    @pytest.mark.parametrize('wrong_password', ['12345', '1234', '1',])
    def test_registration_invalid_length_password_notification_incorrect_password(self, driver, wrong_password):
        random_email = create_random_email()
        driver.find_element(*TestLocators.button_login_in_main).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.button_register))
        driver.find_element(*TestLocators.button_register).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(TestLocators.button_submit))
        driver.find_element(*TestLocators.input_name).send_keys(UsersTestData.username)
        driver.find_element(*TestLocators.input_email).send_keys(random_email)
        driver.find_element(*TestLocators.input_password).send_keys(wrong_password)
        driver.find_element(*TestLocators.button_submit).click()
        assert driver.find_element(*TestLocators.notification_incorrect_password).text == 'Некорректный пароль'