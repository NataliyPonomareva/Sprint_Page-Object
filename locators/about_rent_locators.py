from selenium.webdriver.common.by import By



class AboutRentLocator:
    HEADER_ABOUT_RENT = (By.XPATH, '//*[@id="root"]/div/div[2]/div[1]') # заголовок "Про аренду"
    WHEN = (By.XPATH, '//*[@placeholder="* Когда привезти самокат"]') # поле "Когда привезти самокат"

    PERIOD_INPUT = (By.XPATH, '//div[@class="Dropdown-control"]') # стрелка в поле "Срок аренды"
    PERIOD_SEARCH = (By.XPATH, '//div[@class="Dropdown-option"]') # Выпадающий список "Срок аренды"

    @staticmethod
    def period_value(period):
        return (By.XPATH, f"//div[@class='Dropdown-option' and text()='{period}']")


    @staticmethod  # "Цвет самоката"
    def colour_checkbox(colour):
        return (By.ID, f"{colour}")

    COMMENT = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[4]/input') # комментарий для курьера
    BUTTON_ORDER = (By.XPATH, '//button[contains(@class,"Button_Middle") and text()="Заказать"]' ) # кнопка "Заказать"
