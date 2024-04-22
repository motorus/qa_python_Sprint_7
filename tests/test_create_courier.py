import allure
import pytest
import requests
from data import Courier, StatusCodesCourier, NewCourierCreds, EndPoints


class TestCreateCourier:

    @allure.title('Создание нового курьера')
    @allure.description('Создаем нового курьера, проверяем статус код и текст ответа')
    def test_create_courier_success(self, empty_courier):
        assert empty_courier["status_code"] == StatusCodesCourier.courier_created["status_code"]
        assert empty_courier["response_text"] == StatusCodesCourier.courier_created["response_text"]

    @allure.title('Регистрация существующего курьера')
    @allure.description('Проверяем ожидаемую ошибку, удаляем курьера')
    def test_registration_double_courier_failed(self):
        courier = Courier()
        result = courier.courier_double_registration()
        assert result["status_code"] == StatusCodesCourier.login_is_busy["status_code"]
        assert result["response_text"] == StatusCodesCourier.login_is_busy["response_text"]

    @allure.title('Создание курьера без обязательных полей Login/Password')
    @allure.description('Создание курьера без обязательных полей Login/Password')
    @pytest.mark.parametrize("courier_data", [NewCourierCreds.generate_creds_set("without_login"),
                                              NewCourierCreds.generate_creds_set("without_pass")])
    def test_courier_registration_without_parameters_failed(self, courier_data):
        response = requests.post(EndPoints.create_courier, data=courier_data)
        assert response.status_code == StatusCodesCourier.empty_value["status_code"]
        assert response.text == StatusCodesCourier.empty_value["response_text"]

