import allure
import pytest

from data import Urls, Answers
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage



class TestQuestionAnswer:
    @allure.title('Тестирование выпадающего списка в разделе «Вопросы о важном»')
    @pytest.mark.parametrize("index", list(range(len(Answers.value))))
    def test_questions_and_answers(self, driver, index):
        page = BasePage(driver)
        page.open_page(Urls.DRIVER)
        page.scroll_to_question(index)
        page.click_by_element(BasePageLocators.COOKIE)
        page.click_question(index)
        answer_text = page.get_answer_text(index)

        assert answer_text == Answers.value[index]["answer"]
