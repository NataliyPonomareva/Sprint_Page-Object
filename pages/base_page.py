import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions



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

    @allure.step('Клик на элемент')
    def click_by_element(self, button): # Найти элемент и кликнуть по нему
        button_top = self.wait_and_find_element(button)
        button_top.click()

    @allure.step('Открытие ответа')
    def get_text(self, locator):
        element  = self.wait_and_find_element(locator)
        return element .text

    @allure.step('Получение url страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Получение дескрипторов окон')
    def get_current_window_handle(self):
        return self.driver.current_window_handle

    @allure.step('Переключение на новое окно')
    def switch_to_new_window(self, original_window):
        WebDriverWait(self.driver, 10).until(expected_conditions.new_window_is_opened)
        new_window = [window for window in self.driver.window_handles if window != original_window][0]
        self.driver.switch_to.window(new_window)

    @allure.step('Ожидание загрузки URL')
    def wait_for_url(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_to_be(url))
