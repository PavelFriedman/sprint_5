import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    # Используем Google Chrome. Убедитесь, что chromedriver установлен и находится в PATH.
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()  # Завершаем работу драйвера в конце каждого теста
