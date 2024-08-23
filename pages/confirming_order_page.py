import allure

from locators.confirming_order_locators import ConfirmingOrderLocator
from pages.base_page import BasePage


class ConfirmingOrder(BasePage):

    @allure.step('Нажимаем кнопку "Посмотреть статус"')
    def click_button_view_status(self): # Нажимаем кнопку "Посмотреть статус"
        button_view_status = self.wait_and_find_element(ConfirmingOrderLocator.BUTTON_VIEW_STATUS)
        button_view_status.click()
