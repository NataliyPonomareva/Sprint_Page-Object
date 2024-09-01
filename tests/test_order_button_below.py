import allure

from data import Urls
from pages.order_page import OrderPage


class TestOrderBelow:
    @allure.title('Тест перехода в форму бронирования через кнопку "Заказать" внизу страницы')
    def test_order_button_below(self, driver):
        order_button_below = OrderPage(driver)
        order_button_below.open_page(Urls.DRIVER)
        header = order_button_below.open_order_form_button_below()
        assert header.is_displayed(), "Заголовок 'Для кого самокат' не отображается"