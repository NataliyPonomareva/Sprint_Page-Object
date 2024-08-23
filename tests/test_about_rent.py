import allure
import pytest
from data import Urls
from locators.about_rent_locators import AboutRentLocator
from locators.base_page_locators import BasePageLocators
from locators.for_who_scooter_locator import ForWhoScooterLocator
from locators.window_confirm_registration_locator import WindowConfirmRegistrationLocator
from pages.about_rent_page import AboutRent
from pages.base_page import BasePage
from pages.for_who_scooter_page import ForWhoScooter



class TestAboutRent:

    @allure.description('Тест на открытие Окна подтверждения заказа после заполнения формы "Про аренду"')

    @pytest.mark.parametrize(
        "name, surname, address, metro, telephone, when, period, colour, comment",
        [
            ("Ирина", "Смирнова", "Высотная", "Кузьминки", "+79856457822", "01.10.2024", "сутки", "black", "Позвоните при доставке"),
            ("Петр", "Красилов", "ул. Усачева, 21, 2", "Спортивная", "+87985645782", "20.10.2024", "трое суток", "grey", "позвонить за час"),
        ]
    )
    def test_about_rent(self, driver, name, surname, address, metro, telephone, when, period, colour, comment):
        order_button_top = BasePage(driver)
        order_button_top.open_page(Urls.DRIVER)
        order_button_top.wait_and_find_element(BasePageLocators.ORDER_BUTTON_TOP)
        order_button_top.click_by_element(BasePageLocators.ORDER_BUTTON_TOP)
        order_button_top.wait_and_find_element(ForWhoScooterLocator.HEADER_FOR_WHO)
        complete_for_who = ForWhoScooter(driver)
        complete_for_who.input_form_for_who_scooter(name, surname, address, metro, telephone)

        complete_for_who.wait_and_find_element(AboutRentLocator.HEADER_ABOUT_RENT)
        complete_about_rent = AboutRent(driver)
        complete_about_rent.fill_rent_form(when, period, colour, comment)

        assert BasePage(driver).is_displayed(WindowConfirmRegistrationLocator.WINDOW_CONFIRM_REGISTRATION), "Окно подтверждения заказа не появилось"
