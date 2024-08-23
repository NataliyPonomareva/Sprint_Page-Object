from selenium.webdriver.common.by import By


class ForWhoScooterLocator:

    HEADER_FOR_WHO = (By.CLASS_NAME, "Order_Header__BZXOb") # заголовок "Для кого самокат"
    NAME = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[1]/input") # поле "Имя"
    SURNAME = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[2]/input") # поле "Фамилия"
    ADDRESS = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[3]/input") # поле "Адрес: куда привезти заказ"
    ORDER_METRO = "//input[@placeholder = '* Станция метро']"

    METRO_STATION_INPUT= (By.XPATH, "//input[@placeholder = '* Станция метро']") # поле "Станция метро"
    METRO_STATION_SEARCH = (By.XPATH, "//li[@class ='select-search__row']") # выпадающий список станций метро

    TELEPHONE = (By.XPATH, "/html/body/div/div/div[2]/div[2]/div[5]/input") # поле "Телефон: на него позвонит курьер"
    BUTTON_THEN = (By.XPATH, "//button[text() = 'Далее']") # кнопка "Далее"