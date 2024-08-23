import allure

from pages.base_page import BasePage
from locators.window_confirm_registration_locator import WindowConfirmRegistrationLocator


class WindowConfirmRegistration(BasePage):

    @allure.step('Нажимаем кнопку "Да"')
    def click_button_yes(self):
        button_yes = self.wait_and_find_element(WindowConfirmRegistrationLocator.BUTTON_YES)
        button_yes.click()
