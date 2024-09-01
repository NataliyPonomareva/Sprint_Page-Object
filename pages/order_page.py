import allure

from locators.base_page_locators import BasePageLocators
from locators.order_page_locator import OrderPageLocator
from pages.base_page import BasePage



class OrderPage(BasePage):

    @allure.step('Открытие формы бронирование через кнопку "Заказать" внизу страницы')
    def opening_order_form(self, heaber):
        self.scroll_and_find_element(BasePageLocators.ORDER_BUTTON_DOWN)
        self.wait_and_find_element(OrderPageLocator.HEADER_FOR_WHO)

    @allure.step('Выбор станции метро')
    def complete_metro_station(self, metro):
        metro_input = self.wait_and_find_element(OrderPageLocator.METRO_STATION_INPUT)
        metro_input.click()
        metro_input.send_keys(metro)
        self.select_from_dropdown_list(OrderPageLocator.METRO_STATION_SEARCH)

    @allure.step('Заполнение формы "Для кого самокат"')
    def input_form_for_who_scooter(self, name, surname, address, metro, telephone): # Заполненяем форму "Для кого самокат"
        self.send_keys(OrderPageLocator.NAME, name) # Заполняем поле "Имя"
        self.send_keys(OrderPageLocator.SURNAME, surname) # Заполняем поле "Фамилия"
        self.send_keys(OrderPageLocator.ADDRESS, address) # Заполняем поле "Адрес: куда привезти заказ"
        self.complete_metro_station(metro) # Заполняем поле "Станция метро"
        self.send_keys(OrderPageLocator.TELEPHONE, telephone) # Заполняем поле "Телефон: на него позвонит курьер"
        self.click_by_element(OrderPageLocator.BUTTON_THEN) # Нажимаем кнопку "Далее"


    @allure.step('Выбираем срок аренды самоката')
    def complete_period(self, period): # Заполняем поле "Срок аренды"
        self.wait_and_find_element(OrderPageLocator.PERIOD_INPUT).click()
        period_option_locator = OrderPageLocator.period_value(period)
        self.wait_and_find_element(period_option_locator).click()

    @allure.step('Выбор цвета самоката')
    def complete_colour(self, colour): # Выбираем "Цвет самоката"
        self.wait_and_find_element(OrderPageLocator.colour_checkbox(colour)).click()


    @allure.step('Заполнение формы "Про аренду"')
    def fill_rent_form(self, when, period, colour, comment):
        self.wait_and_find_element(OrderPageLocator.HEADER_ABOUT_RENT)
        self.send_keys(OrderPageLocator.WHEN, when) # Заполняем поле "Когда привезти самокат"
        self.click_by_element(OrderPageLocator.HEADER_ABOUT_RENT)  # Клик по заголовку "Про аренду", чтобы закрылся календарь
        self.complete_period(period) # Заполняем поле "Срок аренды"
        self.complete_colour(colour) # Выбираем "Цвет самоката"
        self.send_keys(OrderPageLocator.COMMENT, comment) # Заполняем поле "Комментарий для курьера"
        self.click_by_element(OrderPageLocator.BUTTON_ORDER) # Нажимаем кнопку "Заказать"


    @allure.step('Подтверждение заказа')
    def order_confirmation(self):
        self.click_by_element(OrderPageLocator.BUTTON_YES) # Нажимаем кнопку "Да"
        self.click_by_element(OrderPageLocator.BUTTON_VIEW_STATUS) # Нажимаем кнопку "Посмотреть статус"
        button = self.wait_and_find_element(OrderPageLocator.BUTTON_ORDER_STATUS)  # Поиск кнопки "Статус заказа"
        return button

    @allure.step('Открытие формы бронирования через кнопку "Заказать", расположенную вверху страницы')
    def open_order_form(self):
        self.wait_and_find_element(BasePageLocators.ORDER_BUTTON_TOP).click()
        self.wait_and_find_element(OrderPageLocator.HEADER_FOR_WHO)

    @allure.step('Открытие формы бронирования через кнопку "Заказать", расположенную внизу страницы')
    def open_order_form_button_below(self):
        self.scroll_and_find_element(BasePageLocators.ORDER_BUTTON_DOWN)
        header = self.wait_and_find_element(OrderPageLocator.HEADER_FOR_WHO)
        return header
