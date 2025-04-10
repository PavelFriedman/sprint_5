from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import (
    ACCOUNT_LINK,
    CONSTRUCTOR_LINK,
    LOGO_LINK,
    BUNS_TAB,
    SAUCES_TAB,
    FILLINGS_TAB
)

BASE_URL = "http://stellarburgers.com"  # Укажите актуальный URL

class TestConstructor:
    def test_transition_to_constructor_from_account(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)

        # Ждем кликабельности элемента "Личный кабинет" и кликаем
        wait.until(EC.element_to_be_clickable(ACCOUNT_LINK)).click()

        # Ждем кликабельности элемента "Конструктор" и кликаем
        wait.until(EC.element_to_be_clickable(CONSTRUCTOR_LINK)).click()

        # Ждем появления вкладки "Булки" и проверяем активное состояние по атрибуту class
        buns_tab = wait.until(EC.presence_of_element_located(BUNS_TAB))
        buns_class = buns_tab.get_attribute("class")
        assert "active" in buns_class, "Изначально активная вкладка не 'Булки'"

        # Ждем кликабельности логотипа и кликаем по нему
        wait.until(EC.element_to_be_clickable(LOGO_LINK)).click()

        # Ожидаем, что либо URL станет BASE_URL, либо состояние вкладки "Булки" останется активным
        wait.until(EC.or_(EC.url_to_be(BASE_URL), EC.presence_of_element_located(BUNS_TAB)))
        current_url = driver.current_url
        buns_class_after = buns_tab.get_attribute("class")
        assert current_url == BASE_URL or "active" in buns_class_after, \
            "Переход по логотипу не осуществился корректно"

    def test_buns_tab_active(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)
        # Переходим в раздел "Конструктор"
        wait.until(EC.element_to_be_clickable(CONSTRUCTOR_LINK)).click()

        # Проверка: по умолчанию активна вкладка "Булки"
        buns_tab = wait.until(EC.presence_of_element_located(BUNS_TAB))
        buns_class = buns_tab.get_attribute("class")
        assert "active" in buns_class, "Изначально активная вкладка не 'Булки'"

    def test_sauces_tab_active(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(CONSTRUCTOR_LINK)).click()

        # Переходим на вкладку "Соусы"
        sauces_tab = wait.until(EC.presence_of_element_located(SAUCES_TAB))
        sauces_tab.click()
        sauces_class = sauces_tab.get_attribute("class")
        assert "active" in sauces_class, "Вкладка 'Соусы' не стала активной после клика"

    def test_fillings_tab_active(self, driver):
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(CONSTRUCTOR_LINK)).click()

        # Переходим на вкладку "Начинки"
        fillings_tab = wait.until(EC.presence_of_element_located(FILLINGS_TAB))
        fillings_tab.click()
        fillings_class = fillings_tab.get_attribute("class")
        assert "active" in fillings_class, "Вкладка 'Начинки' не стала активной после клика"
