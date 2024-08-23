import allure

from data import Urls
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage


class TestConvertion:
    @allure.description('Тест перехода на главную страницу "Самокат" по клику на логотип "Самоката"')
    def test_convertion_page_scooter(self, driver): #
        order_button_top = BasePage(driver)
        order_button_top.open_page(Urls.DRIVER)
        order_button_top.wait_and_find_element(BasePageLocators.ORDER_BUTTON_TOP)
        order_button_top.click_by_element(BasePageLocators.ORDER_BUTTON_TOP)
        logo_scooter = order_button_top.wait_and_find_element(BasePageLocators.LOGO_SCOOTER)
        logo_scooter.click()
        assert driver.current_url == Urls.DRIVER # Проверка, что страница была перенаправлена на URL сервиса "Самокат"


