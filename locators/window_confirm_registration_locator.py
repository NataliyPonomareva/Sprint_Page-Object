from selenium.webdriver.common.by import By


class WindowConfirmRegistrationLocator:
    WINDOW_CONFIRM_REGISTRATION = (By.XPATH, "//div[text() = 'Хотите оформить заказ?']")  # Окно подтверждения бронирования
    BUTTON_YES = (By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/div[2]/button[2]')  # кнопка "Да"


