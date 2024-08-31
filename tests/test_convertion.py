import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import Urls
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage


class TestConvertion:
    @allure.title('Тест перехода на главную страницу "Самокат" по клику на логотип "Самоката"')
    def test_convertion_page_scooter(self, driver): #
        order_button_top = BasePage(driver)
        order_button_top.open_page(Urls.DRIVER)
        order_button_top.wait_and_find_element(BasePageLocators.ORDER_BUTTON_TOP)
        order_button_top.click_by_element(BasePageLocators.ORDER_BUTTON_TOP)
        logo_scooter = order_button_top.wait_and_find_element(BasePageLocators.LOGO_SCOOTER)
        logo_scooter.click()
        assert driver.current_url == Urls.DRIVER # Проверка, что страница была перенаправлена на URL сервиса "Самокат"

    @allure.title('Тест открытия  в новом окне главной страницы Дзена по клику на логотип Яндекса"')
    def test_convertion_page_scooter(self, driver):
        page_scooter = BasePage(driver)
        page_scooter.open_page(Urls.DRIVER)
        logo_yandex = page_scooter.wait_and_find_element(BasePageLocators.LOGO_YANDEX)
        logo_yandex.click()

        # Получение дескрипторов окон
        original_window = driver.current_window_handle
        WebDriverWait(driver, 10).until(expected_conditions.new_window_is_opened)

        # Переключение на новое окно
        new_window = [window for window in driver.window_handles if window != original_window][0]
        driver.switch_to.window(new_window)

        # Ожидание загрузки страницы Дзена
        WebDriverWait(driver, 10).until(expected_conditions.url_to_be(Urls.DZEN_URL))

        # Проверка URL
        assert driver.current_url == Urls.DZEN_URL
