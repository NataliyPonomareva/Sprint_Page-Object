import allure
import pytest

from data import Urls
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage


value = [
    {"question":'Сколько это стоит? И как оплатить?', "answer": 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'},
    {"question":'Хочу сразу несколько самокатов! Так можно?', "answer": 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'},
    {"question":'Как рассчитывается время аренды?', "answer": 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'},
    {"question":'Можно ли заказать самокат прямо на сегодня?', "answer": 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'},
    {"question":'Можно ли продлить заказ или вернуть самокат раньше?', "answer": 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'},
    {"question":'Вы привозите зарядку вместе с самокатом?', "answer": 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'},
    {"question":'Можно ли отменить заказ?', "answer": 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'},
    {"question":'Я жизу за МКАДом, привезёте?', "answer": 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'}
    ]

class TestQuestionAnswer:
    @allure.description('Тестирование выпадающего списка в разделе «Вопросы о важном»')
    @pytest.mark.parametrize("index", list(range(len(value))))
    def test_questions_and_answers(self, driver, index):
        page = BasePage(driver)
        page.open_page(Urls.DRIVER)
        page.scroll_to_question(index)
        page.click_by_element(BasePageLocators.COOKIE)
        page.click_question(index)
        answer_text = page.get_answer_text(index)

        assert answer_text == value[index]["answer"]
