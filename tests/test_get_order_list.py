import allure
import requests
from data import EndPoints, StatusCodesCourier


class TestOrdersList:

    @allure.title('Получение списка заказов')
    @allure.description('Получаем список заказов и проверяем ответ(track в ответе)')
    def test_get_orders_list_success(self):
        response = requests.get(EndPoints.get_orders)
        assert response.status_code == StatusCodesCourier.order_get_list["status_code"]
        assert "track" in response.text
