from selenium.webdriver.common.by import By


class OrderPageLocator:

# Форма "Для кого самокат"
    HEADER_FOR_WHO = (By.CLASS_NAME, "Order_Header__BZXOb") # заголовок "Для кого самокат"
    NAME = (By.XPATH, '//*[@placeholder="* Имя"]') # поле "Имя"
    SURNAME = (By.XPATH, '//*[@placeholder="* Фамилия"]') # поле "Фамилия"
    ADDRESS = (By.XPATH, '//*[@placeholder="* Адрес: куда привезти заказ"]') # поле "Адрес: куда привезти заказ"
    ORDER_METRO = "//input[@placeholder = '* Станция метро']"

    METRO_STATION_INPUT= (By.XPATH, "//input[@placeholder = '* Станция метро']") # поле "Станция метро"
    METRO_STATION_SEARCH = (By.XPATH, "//li[@class ='select-search__row']") # выпадающий список станций метро

    TELEPHONE = (By.XPATH, '//*[@placeholder="* Телефон: на него позвонит курьер"]') # поле "Телефон: на него позвонит курьер"
    BUTTON_THEN = (By.XPATH, "//button[text() = 'Далее']") # кнопка "Далее"

# Форма "Про аренду"
    HEADER_ABOUT_RENT = (By.XPATH, '//*[text()="Про аренду"]') # заголовок "Про аренду"
    WHEN = (By.XPATH, '//*[@placeholder="* Когда привезти самокат"]') # поле "Когда привезти самокат"

    PERIOD_INPUT = (By.XPATH, '//div[@class="Dropdown-control"]') # стрелка в поле "Срок аренды"
    PERIOD_SEARCH = (By.XPATH, '//div[@class="Dropdown-option"]') # Выпадающий список "Срок аренды"

    @staticmethod
    def period_value(period):
        return (By.XPATH, f"//div[@class='Dropdown-option' and text()='{period}']")

    @staticmethod  # "Цвет самоката"
    def colour_checkbox(colour):
        return (By.ID, f"{colour}")

    COMMENT = (By.XPATH, '//*[@placeholder="Комментарий для курьера"]') # комментарий для курьера
    BUTTON_ORDER = (By.XPATH, '//button[contains(@class,"Button_Middle") and text()="Заказать"]' ) # кнопка "Заказать"


# Окно подтверждения бронирования
    WINDOW_CONFIRM_REGISTRATION = (By.XPATH, "//div[text() = 'Хотите оформить заказ?']")
    BUTTON_YES = (By.XPATH, '//button[text()="Да"]')  # кнопка "Да"


# Окно 'Заказ оформлен'
    WINDOW_CONFIRM_ORDER = (By.XPATH, "//div[text() = 'Заказ оформлен']")  # заголовок окна 'Заказ оформлен'
    BUTTON_VIEW_STATUS = (By.XPATH, '//button[text()="Посмотреть статус"]')  # кнопка "Посмотреть статус"
    BUTTON_ORDER_STATUS = (By.XPATH, '//button[text()="Статус заказа"]')  # кнопка "Статус заказа"