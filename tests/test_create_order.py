import json
import allure
import pytest
import requests

from data import Order, StatusCodesCourier


class TestOrderCreate:

    @allure.title('Создание заказа с разными цветами')
    @allure.description('Создание заказа с разными цветами. Цвет - {color}')
    @pytest.mark.parametrize('color', [{"color": ["BLACK"]},
                                       {"color": ["GREY"]},
                                       {"color": ["BLACK", "GRAY"]},
                                       {"color": [""]}])
    def test_create_order_success(self, color):
        response = Order().create_order(color)
        assert response.status_code == StatusCodesCourier.order_create["status_code"]
        assert "track" in response.text
