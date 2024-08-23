from selenium.webdriver.common.by import By



class ConfirmingOrderLocator:
    WINDOW_CONFIRM_ORDER = (By.XPATH, "//div[text() = 'Заказ оформлен']")  # Окно 'Заказ оформлен'
    BUTTON_VIEW_STATUS = (By.XPATH, '//button[text()="Посмотреть статус"]')  # кнопка "Посмотреть статус"
    BUTTON_ORDER_STATUS = (By.XPATH, '//button[text()="Статус заказа"]')  # кнопка "Статус заказа"
