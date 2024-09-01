import allure
import pytest
from data import Urls
from pages.order_page import OrderPage



class TestCreateOrder:
    @allure.title('Тест открытия Окна подтверждения заказа после заполнения формы "Про аренду"')
    @pytest.mark.parametrize(
        "name, surname, address, metro, telephone, when, period, colour, comment",
        [
            ("Ирина", "Смирнова", "Высотная", "Кузьминки", "+79856457822", "01.10.2024", "сутки", "black", "Позвоните при доставке"),
            ("Петр", "Красилов", "ул. Усачева, 21, 2", "Спортивная", "+87985645782", "20.10.2024", "трое суток", "grey", "позвонить за час"),
        ]
    )
    def test_create_order(self, driver, name, surname, address, metro, telephone, when, period, colour, comment):
        create_order = OrderPage(driver)
        create_order.open_page(Urls.DRIVER) # переход на хост
        create_order.open_order_form()  # открытие формы бронирования
        create_order.input_form_for_who_scooter(name, surname, address, metro, telephone) # заполнение формы "Для кого самокат
        create_order.fill_rent_form(when, period, colour, comment) # заполнение формы "Про аренду"
        button = create_order.order_confirmation()
        assert button.is_displayed(), "Кнопка 'Статус заказа' не отображается"
