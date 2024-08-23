import allure

from data import Urls
from locators.base_page_locators import BasePageLocators
from locators.for_who_scooter_locator import ForWhoScooterLocator
from pages.base_page import BasePage


class TestOrder:

    @allure.description('Тест перехода в форму бронирования через кнопку "Заказать" вверху страницы')
    def test_order_button_top(self, driver):
        order_button_top = BasePage(driver)
        order_button_top.open_page(Urls.DRIVER)
        order_button_top.wait_and_find_element(BasePageLocators.ORDER_BUTTON_TOP)
        order_button_top.click_by_element(BasePageLocators.ORDER_BUTTON_TOP)
        header_for_who = order_button_top.wait_and_find_element(ForWhoScooterLocator.HEADER_FOR_WHO)
        assert header_for_who.is_displayed()
