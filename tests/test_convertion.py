import allure

from data import Urls
from pages.main_page import MainPage


class TestConvertion:
    @allure.title('Тест перехода на главную страницу "Самокат" по клику на логотип "Самоката"')
    def test_convertion_page_scooter(self, driver): #
        order_button_top = MainPage(driver)
        order_button_top.open_page(Urls.DRIVER)
        order_button_top.convertion_scooter()
        assert order_button_top.get_current_url() == Urls.DRIVER # Проверка, что страница была перенаправлена на URL сервиса "Самокат"

    @allure.title('Тест открытия  в новом окне главной страницы Дзена по клику на логотип Яндекса"')
    def test_convertion_page_dzen(self, driver):
        page_scooter = MainPage(driver)
        page_scooter.open_page(Urls.DRIVER)
        page_scooter.convertion_dzen()
        assert page_scooter.get_current_url() == Urls.DZEN_URL # Проверка URL
