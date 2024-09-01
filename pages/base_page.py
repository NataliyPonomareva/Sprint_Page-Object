import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.base_page_locators import BasePageLocators
from selenium.webdriver.common.by import By
from data import Urls



class BasePage:
    @allure.step('Загрузка драйвера')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Загружаем страницу')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Проверка отражения элемента на странице')
    def is_displayed(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except NoSuchElementException:
            return False

    @allure.step('Выбор элемента из дропдауна листа')
    def select_from_dropdown_list(self, locator):
        dropdown = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator))
        dropdown.click()

    @allure.step('Поиск элемента на страницы и ожидание загрузки')
    def wait_and_find_element(self, locator) -> WebElement:
        WebDriverWait(self.driver, 50).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Заполнение поля')
    def send_keys(self, locator, val=None) -> WebElement:
        self.wait_and_find_element(locator).send_keys(val)
        
    @allure.step('Скролл страницы до нужного элемента')
    def scroll_and_find_element(self, locator) -> WebElement: # Скролл страницы до элемента и клик по нему
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Скролл страницы до ID вопроса')
    def scroll_to_question(self, index):
        question = self.driver.find_element(By.ID, BasePageLocators.question_locator(index))
        self.driver.execute_script("arguments[0].scrollIntoView();", question)
        self.click_by_element(BasePageLocators.COOKIE) # Согласиться с куками, для закрытие предупреждающего окна

    @allure.step('Клик на элемент')
    def click_by_element(self, button): # Найти элемент и кликнуть по нему
        button_top = self.wait_and_find_element(button)
        button_top.click()

    @allure.step('Клик на вопрос')
    def click_question(self, index):
        question = self.driver.find_element(By.ID, BasePageLocators.question_locator(index))
        question.click()

    @allure.step('Открытие ответа')
    def get_answer_text(self, index):
        answer = self.wait_and_find_element((By.ID, BasePageLocators.answer_locator(index)))
        return answer.text

    @allure.step('Перехода на главную страницу "Самокат"')
    def convertion_scooter(self):
        self.wait_and_find_element(BasePageLocators.ORDER_BUTTON_TOP).click() # Клик по кнопке "Заказать" (чтобы уйти с главной страницы)
        self.wait_and_find_element(BasePageLocators.LOGO_SCOOTER).click() # Клик по лого "Самокат"

    @allure.step('Перехода на страницу "Дзен"')
    def convertion_dzen(self):
        self.wait_and_find_element(BasePageLocators.LOGO_YANDEX).click() # Клик по лого "Яндекс"

        # Получение дескрипторов окон
        original_window = self.driver.current_window_handle
        WebDriverWait(self.driver, 10).until(expected_conditions.new_window_is_opened)

        # Переключение на новое окно
        new_window = [window for window in self.driver.window_handles if window != original_window][0]
        self.driver.switch_to.window(new_window)

        # Ожидание загрузки страницы Дзена
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(Urls.DZEN_URL))
