import pytest
from selenium import webdriver

import data

@pytest.fixture(scope='function')
def driver():
    firefox = webdriver.Firefox()  # запуск Firefox
    firefox.maximize_window()  # открытие приложения в окне

    yield firefox

    firefox.quit()