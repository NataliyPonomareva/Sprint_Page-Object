from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPageLocators(BasePage):
    @staticmethod
    def get_question_answer(question):
        return By.CLASS_NAME, f'//accordion__button[text() = "{question}"]'

    @staticmethod
    def answer_to_question(answer):
        return By.CLASS_NAME, f'//accordion__panel[text() = "{answer}"]'

