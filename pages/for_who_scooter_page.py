import allure

from locators.for_who_scooter_locator import ForWhoScooterLocator
from pages.base_page import BasePage




class ForWhoScooter(BasePage):

    @allure.step('Заполнение поля "Имя"')
    def complete_name(self, name): # Заполняем поле "Имя"
        self.wait_and_find_element(ForWhoScooterLocator.NAME).send_keys(name)

    @allure.step('Заполнение поля "Фамилия"')
    def complete_surname(self, surname): # Заполняем поле "Фамилия"
        self.wait_and_find_element(ForWhoScooterLocator.SURNAME).send_keys(surname)

    @allure.step('Заполнение поля "Адрес доставки"')
    def complete_address(self, address): # Заполняем поле "Адрес: куда привезти заказ"
        self.wait_and_find_element(ForWhoScooterLocator.ADDRESS).send_keys(address)

    @allure.step('Выбор станции метро')
    def complete_metro_station(self, metro): # Заполняем поле "Станция метро"
        metro_input = self.wait_and_find_element(ForWhoScooterLocator.METRO_STATION_INPUT)
        metro_input.click()
        metro_input.send_keys(metro)
        self.select_from_dropdown_list(ForWhoScooterLocator.METRO_STATION_SEARCH)

    @allure.step('Заполнение поля "Номер телефона"')
    def complete_telephone(self, telephone): # Заполняем поле "Телефон: на него позвонит курьер"
        self.wait_and_find_element(ForWhoScooterLocator.TELEPHONE).send_keys(telephone)

    @allure.step('Нажимаем кнопку "Далее"')
    def click_button_then(self): # Нажимаем кнопку "Далее"
        self.wait_and_find_element(ForWhoScooterLocator.BUTTON_THEN).click()

    @allure.step('Заполнение формы "Для кого самокат"')
    def input_form_for_who_scooter(self, name, surname, address, metro, telephone): # Заполненяем форму "Для кого самокат"
        self.complete_name(name)
        self.complete_surname(surname)
        self.complete_address(address)
        self.complete_metro_station(metro)
        self.complete_telephone(telephone)
        self.click_button_then()
