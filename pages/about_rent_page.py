import allure

from locators.about_rent_locators import AboutRentLocator
from pages.base_page import BasePage


class AboutRent(BasePage):
    @allure.step('Выбираем дату доставки самоката')
    def complete_when_bring(self, when): # Заполняем поле "Когда привезти самокат"
        self.wait_and_find_element(AboutRentLocator.WHEN).send_keys(when)

    @allure.step('Выбираем срок аренды самоката')
    def complete_period(self, period): # Заполняем поле "Срок аренды"
        self.wait_and_find_element(AboutRentLocator.PERIOD_INPUT).click()
        period_option_locator = AboutRentLocator.period_value(period)
        self.wait_and_find_element(period_option_locator).click()

    @allure.step('Выбор цвета самоката')
    def complete_colour(self, colour): # Выбираем "Цвет самоката"
        self.wait_and_find_element(AboutRentLocator.colour_checkbox(colour)).click()

    @allure.step('Заполнение поля "Комментарий"')
    def complete_comment(self, comment): # Заполняем поле "Комментарий для курьера"
        self.wait_and_find_element(AboutRentLocator.COMMENT).send_keys(comment)

    @allure.step('Нажимаем кнопку "Заказать"')
    def click_button_order(self): # Нажимаем кнопку "Заказать"
        self.wait_and_find_element(AboutRentLocator.BUTTON_ORDER).click()

    @allure.step('Заполнение формы "Про аренду"')
    def fill_rent_form(self, when, period, colour, comment):
        self.complete_when_bring(when)
        self.click_by_element(AboutRentLocator.HEADER_ABOUT_RENT)
        self.complete_period(period)
        self.complete_colour(colour)
        self.complete_comment(comment)
        self.click_button_order()