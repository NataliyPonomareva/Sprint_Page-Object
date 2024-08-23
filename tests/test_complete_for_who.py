import allure
import pytest
from data import Urls
from locators.about_rent_locators import AboutRentLocator
from locators.base_page_locators import BasePageLocators
from locators.for_who_scooter_locator import ForWhoScooterLocator
from pages.base_page import BasePage
from pages.for_who_scooter_page import ForWhoScooter



class TestCompleteForWho:
    @allure.description('Тест открытия формы "Про аренду" после заполнения формы "Для кого самокат"')
    @pytest.mark.parametrize(
        "name, surname, address, metro, telephone",
        [
            ("Ирина", "Смирнова", "Высотная", "Кузьминки", "+79856457822"),
            ("Петр", "Красилов", "ул. Усачева, 21, 2", "Спортивная", "+87985645782"),
        ]
    )
    def test_complete_for_who(self, driver, name, surname, address, metro, telephone):
        order_button_top = BasePage(driver)
        order_button_top.open_page(Urls.DRIVER)
        order_button_top.wait_and_find_element(BasePageLocators.ORDER_BUTTON_TOP)
        order_button_top.click_by_element(BasePageLocators.ORDER_BUTTON_TOP)
        order_button_top.wait_and_find_element(ForWhoScooterLocator.HEADER_FOR_WHO)
        complete_for_who = ForWhoScooter(driver)
        complete_for_who.input_form_for_who_scooter(name, surname, address, metro, telephone)
        header_about_rent = complete_for_who.wait_and_find_element(AboutRentLocator.HEADER_ABOUT_RENT)
        assert header_about_rent.is_displayed()