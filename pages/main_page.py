import allure

from data import Urls
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class MainPage(BasePage):
    @allure.step('Загрузка драйвера')
    def __init__(self, driver):
        super().__init__(driver)  # Вызов конструктора родительского класса


    @allure.step('Клик на вопрос')
    def click_question(self, index):
        question = self.driver.find_element(By.ID, MainPageLocators.question_locator(index))
        question.click()


    @allure.step('Открытие ответа')
    def get_answer_text(self, index):
        answer = self.wait_and_find_element((By.ID, MainPageLocators.answer_locator(index)))
        return answer.text

    @allure.step('Скролл страницы до ID вопроса')
    def scroll_to_question(self, index):
        question = self.driver.find_element(By.ID, MainPageLocators.question_locator(index))
        self.driver.execute_script("arguments[0].scrollIntoView();", question)
        self.click_by_element(MainPageLocators.COOKIE) # Согласиться с куками, для закрытие предупреждающего окна

    @allure.step('Перехода на главную страницу "Самокат"')
    def convertion_scooter(self):
        self.wait_and_find_element(MainPageLocators.ORDER_BUTTON_TOP).click() # Клик по кнопке "Заказать" (чтобы уйти с главной страницы)
        self.wait_and_find_element(MainPageLocators.LOGO_SCOOTER).click() # Клик по лого "Самокат"

    @allure.step('Перехода на страницу "Дзен"')
    def convertion_dzen(self):
        self.wait_and_find_element(MainPageLocators.LOGO_YANDEX).click() # Клик по лого "Яндекс"

        # Получение дескрипторов окон
        original_window = self.driver.current_window_handle
        WebDriverWait(self.driver, 10).until(expected_conditions.new_window_is_opened)

        # Переключение на новое окно
        new_window = [window for window in self.driver.window_handles if window != original_window][0]
        self.driver.switch_to.window(new_window)

        # Ожидание загрузки страницы Дзена
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(Urls.DZEN_URL))
