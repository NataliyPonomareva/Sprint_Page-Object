import allure

from data import Urls
from pages.base_page import BasePage


class TestConvertion:
    @allure.title('Тест перехода на главную страницу "Самокат" по клику на логотип "Самоката"')
    def test_convertion_page_scooter(self, driver): #
        order_button_top = BasePage(driver)
        order_button_top.open_page(Urls.DRIVER)
        order_button_top.convertion_scooter()
        assert driver.current_url == Urls.DRIVER # Проверка, что страница была перенаправлена на URL сервиса "Самокат"

    @allure.title('Тест открытия  в новом окне главной страницы Дзена по клику на логотип Яндекса"')
    def test_convertion_page_dzen(self, driver):
        page_scooter = BasePage(driver)
        page_scooter.open_page(Urls.DRIVER)
        page_scooter.convertion_dzen()
        assert driver.current_url == Urls.DZEN_URL # Проверка URL
