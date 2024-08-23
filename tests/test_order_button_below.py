import allure
from selenium.webdriver.common.by import By

from data import Urls
from locators.base_page_locators import BasePageLocators
from locators.for_who_scooter_locator import ForWhoScooterLocator
from pages.base_page import BasePage


class TestOrderBelow:
    @allure.description('Тест перехода в форму бронирования через кнопку "Заказать" внизу страницы')
    def test_order_button_below(self, driver):
        order_button_below = BasePage(driver)
        order_button_below.open_page(Urls.DRIVER)
        order_button_below.scroll_and_find_element(BasePageLocators.ORDER_BUTTON_DOWN)
        header_for_who = order_button_below.wait_and_find_element(ForWhoScooterLocator.HEADER_FOR_WHO)
        assert header_for_who.is_displayed()
