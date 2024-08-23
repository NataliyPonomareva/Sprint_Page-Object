from selenium.webdriver.common.by import By


class BasePageLocators:
    ORDER_BUTTON_TOP = (By.CLASS_NAME, "Button_Button__ra12g") # кнопка "Войти" вверху страницы
    ORDER_BUTTON_DOWN = (By.XPATH, '//div[contains(@class, "Home_FinishButton")]/button[text()="Заказать"]') # кнопка "Войти" внизу страницы
    LOGO_SCOOTER = (By.XPATH, '//img[@alt = "Scooter"]') # Лого "Самокат"
    LOGO_YANDEX = (By.XPATH, '//img[@alt = "Yandex"]') # Лого "Яндекс"
    COOKIE = (By.XPATH, '//button[text() = "да все привыкли"]')  # Кнопка принятия куков

    @staticmethod
    def question_locator(index):
        return f"accordion__heading-{index}"

    @staticmethod
    def answer_locator(index):
        return f"accordion__panel-{index}"