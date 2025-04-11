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
        """
        Тест проверяет переход в раздел "Конструктор" из личного кабинета,
        а также переход по логотипу, который либо возвращает на главную,
        либо оставляет активной вкладку "Булки".
        """
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)

        # Переход в раздел личного кабинета
        wait.until(EC.element_to_be_clickable(ACCOUNT_LINK)).click()
        # Переход в раздел "Конструктор"
        wait.until(EC.element_to_be_clickable(CONSTRUCTOR_LINK)).click()

        # Ожидаем появления вкладки "Булки" и проверяем активное состояние по атрибуту aria-selected
        buns_tab = wait.until(EC.presence_of_element_located(BUNS_TAB))
        buns_selected = buns_tab.get_attribute("aria-selected")
        assert buns_selected == "true", "Изначально активная вкладка не 'Булки'"

        # Переход по логотипу
        wait.until(EC.element_to_be_clickable(LOGO_LINK)).click()
        # Ждем, пока либо изменится URL, либо вкладка "Булки" останется активной
        wait.until(EC.or_(EC.url_to_be(BASE_URL), EC.presence_of_element_located(BUNS_TAB)))
        current_url = driver.current_url
        buns_selected_after = buns_tab.get_attribute("aria-selected")
        assert current_url == BASE_URL or buns_selected_after == "true", \
            "Переход по логотипу не осуществился корректно"

    def test_buns_tab_active(self, driver):
        """
        Тест проверяет, что вкладка "Булки" является активной при переходе в раздел "Конструктор".
        """
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)

        # Переход в раздел "Конструктор"
        wait.until(EC.element_to_be_clickable(CONSTRUCTOR_LINK)).click()
        buns_tab = wait.until(EC.presence_of_element_located(BUNS_TAB))

        # Проверка: атрибут aria-selected у вкладки "Булки" должен равняться "true"
        buns_selected = buns_tab.get_attribute("aria-selected")
        assert buns_selected == "true", "Вкладка 'Булки' не активна"

    def test_sauces_tab_active(self, driver):
        """
        Тест проверяет, что после клика вкладка "Соусы" становится активной.
        """
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(CONSTRUCTOR_LINK)).click()
        sauces_tab = wait.until(EC.presence_of_element_located(SAUCES_TAB))

        # Клик по вкладке "Соусы"
        sauces_tab.click()
        sauces_selected = sauces_tab.get_attribute("aria-selected")
        assert sauces_selected == "true", "Вкладка 'Соусы' не активна после клика"

    def test_fillings_tab_active(self, driver):
        """
        Тест проверяет, что после клика вкладка "Начинки" становится активной.
        """
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable(CONSTRUCTOR_LINK)).click()
        fillings_tab = wait.until(EC.presence_of_element_located(FILLINGS_TAB))

        # Клик по вкладке "Начинки"
        fillings_tab.click()
        fillings_selected = fillings_tab.get_attribute("aria-selected")
        assert fillings_selected == "true", "Вкладка 'Начинки' не активна после клика"
