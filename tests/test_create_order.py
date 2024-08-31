import allure
import pytest
from data import Urls
from locators.base_page_locators import BasePageLocators
from locators.order_page_locator import OrderPageLocator
from pages.base_page import BasePage
from pages.order_page import OrderPage



class TestCreateOrder:
    @allure.title('Тест открытия Окна подтверждения заказа после заполнения формы "Про аренду"')
    @pytest.mark.parametrize(
        "name, surname, address, metro, telephone, when, period, colour, comment",
        [
            ("Ирина", "Смирнова", "Высотная", "Кузьминки", "+79856457822", "01.10.2024", "сутки", "black", "Позвоните при доставке"),
            ("Петр", "Красилов", "ул. Усачева, 21, 2", "Спортивная", "+87985645782", "20.10.2024", "трое суток", "grey", "позвонить за час"),
        ]
    )
    def test_create_order(self, driver, name, surname, address, metro, telephone, when, period, colour, comment):
        create_order = OrderPage(driver)
        create_order.open_page(Urls.DRIVER)
        create_order.wait_and_find_element(BasePageLocators.ORDER_BUTTON_TOP)
        create_order.click_by_element(BasePageLocators.ORDER_BUTTON_TOP)
        create_order.wait_and_find_element(OrderPageLocator.HEADER_FOR_WHO)
        create_order.input_form_for_who_scooter(name, surname, address, metro, telephone)

        create_order.wait_and_find_element(OrderPageLocator.HEADER_ABOUT_RENT)
        create_order.fill_rent_form(when, period, colour, comment)
        create_order.order_confirmation()
        create_order.wait_and_find_element(OrderPageLocator.BUTTON_ORDER_STATUS)

        assert create_order.is_displayed(OrderPageLocator.BUTTON_ORDER_STATUS)
