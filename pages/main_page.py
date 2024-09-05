import allure

from data import Urls
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step('Загрузка драйвера')
    def __init__(self, driver):
        super().__init__(driver)  # Вызов конструктора родительского класса


    @allure.step('Клик на вопрос')
    def click_question(self, index):
        question_locator = (By.ID, MainPageLocators.question_locator(index))
        self.click_by_element(question_locator)

    @allure.step('Открытие ответа')
    def get_answer_text(self, index):
        answer_locator = (By.ID, MainPageLocators.answer_locator(index))
        return self.get_text(answer_locator)

    @allure.step('Скролл страницы до ID вопроса')
    def scroll_to_question(self, index):
        question_locator = (By.ID, MainPageLocators.question_locator(index))
        self.scroll_and_find_element(question_locator)
        self.click_by_element(MainPageLocators.COOKIE)  # Согласиться с куками, для закрытия предупреждающего окна

    @allure.step('Перехода на главную страницу "Самокат"')
    def convertion_scooter(self):
        self.click_by_element(MainPageLocators.ORDER_BUTTON_TOP)  # Клик по кнопке "Заказать"
        self.click_by_element(MainPageLocators.LOGO_SCOOTER)  # Клик по лого "Самокат"

    @allure.step('Перехода на страницу "Дзен"')
    def convertion_dzen(self):
        self.click_by_element(MainPageLocators.LOGO_YANDEX)  # Клик по лого "Яндекс"
        original_window = self.get_current_window_handle() # Получение дескрипторов окон
        self.switch_to_new_window(original_window) # Переключение на новое окно
        self.wait_for_url(Urls.DZEN_URL) # Ожидание загрузки страницы Дзена
