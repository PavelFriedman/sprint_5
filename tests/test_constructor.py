import time
import pytest
from selenium.webdriver.common.by import By
from locators import (
    ACCOUNT_LINK,
    CONSTRUCTOR_LINK,
    LOGO_LINK,
    BUNS_TAB,
    SAUCES_TAB,
    FILLINGS_TAB
)
from generators import generate_email, generate_password

BASE_URL = "http://stellarburgers.com"  # Укажите актуальный URL


def test_transition_to_constructor_from_account(driver):
    driver.get(BASE_URL)

    driver.find_element(*ACCOUNT_LINK).click()
    time.sleep(1)

    # Допустим, после входа переходим в личный кабинет (здесь можно вставить код входа, если требуется)

    driver.find_element(*CONSTRUCTOR_LINK).click()
    time.sleep(1)

    buns_tab = driver.find_element(*BUNS_TAB)
    assert buns_tab.is_displayed(), "Элемент 'Булки' не отображается после перехода в Конструктор"

    driver.find_element(*LOGO_LINK).click()
    time.sleep(1)
    assert driver.current_url == BASE_URL or driver.find_element(
        *BUNS_TAB).is_displayed(), "Переход по логотипу не осуществился корректно"


def test_constructor_sections(driver):
    driver.get(BASE_URL)

    driver.find_element(*CONSTRUCTOR_LINK).click()
    time.sleep(1)

    assert driver.find_element(*BUNS_TAB).is_displayed(), "Вкладка 'Булки' не отображается"
    assert driver.find_element(*SAUCES_TAB).is_displayed(), "Вкладка 'Соусы' не отображается"
    assert driver.find_element(*FILLINGS_TAB).is_displayed(), "Вкладка 'Начинки' не отображается"
