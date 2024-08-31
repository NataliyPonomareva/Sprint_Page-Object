import allure
from selenium.webdriver.common.by import By

from data import Urls
from locators.base_page_locators import BasePageLocators
from locators.order_page_locator import OrderPageLocator
from pages.base_page import BasePage
from pages.order_page import OrderPage


class TestOrderBelow:
    @allure.title('Тест перехода в форму бронирования через кнопку "Заказать" внизу страницы')
    def test_order_button_below(self, driver):
        order_button_below = BasePage(driver)
        order_button_below.open_page(Urls.DRIVER)
        order_button_below.scroll_and_find_element(BasePageLocators.ORDER_BUTTON_DOWN)
        header_for_who = order_button_below.wait_and_find_element(OrderPageLocator.HEADER_FOR_WHO)
        assert header_for_who.is_displayed()