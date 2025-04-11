from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LOGIN_EMAIL_INPUT, LOGIN_PASSWORD_INPUT, LOGIN_BUTTON_MAIN

# Настройки тестового аккаунта. При необходимости вынесите в отдельный конфиг.
TEST_EMAIL = "your_registered_email@example.com"
TEST_PASSWORD = "your_registered_password"

def wait_for_clickable(driver, locator, timeout=10):
    """
    Ожидает, пока элемент не станет кликабельным.
    :param driver: экземпляр WebDriver
    :param locator: кортеж локатора (например, (By.XPATH, "//button[...]"))
    :param timeout: время ожидания в секундах (по умолчанию 10)
    :return: веб-элемент после того, как он станет кликабельным
    """
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))

def wait_for_visibility(driver, locator, timeout=10):
    """
    Ожидает, пока элемент не станет видимым.
    :param driver: экземпляр WebDriver
    :param locator: кортеж локатора
    :param timeout: время ожидания в секундах
    :return: веб-элемент после того, как он станет видимым
    """
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))

def wait_for_presence(driver, locator, timeout=10):
    """
    Ожидает появления элемента в DOM.
    :param driver: экземпляр WebDriver
    :param locator: кортеж локатора
    :param timeout: время ожидания в секундах
    :return: веб-элемент, как только он появляется
    """
    return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))

def element_has_class(element, class_name):
    """
    Проверяет, содержит ли заданный элемент указанный CSS класс.
    :param element: веб-элемент
    :param class_name: имя класса для проверки
    :return: True, если класс найден, иначе False
    """
    classes = element.get_attribute("class")
    return class_name in classes if classes else False

def login_common(driver):
    """
    Выполняет общий сценарий входа в систему.
    Использует тестовые данные (EMAIL и PASSWORD) и локаторы, определённые в модуле locators.
    """
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(TEST_EMAIL)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(TEST_PASSWORD)
    driver.find_element(*LOGIN_BUTTON_MAIN).click()
    # Если требуется, можно заменить фиксированную задержку на динамическое ожидание
    WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))
