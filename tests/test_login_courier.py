import allure
import pytest
import requests

from data import Courier, EndPoints, StatusCodesCourier, NewCourierCreds


class TestLoginCourier:

    @allure.title('Проверка авторизации курьера с валидными данными')
    @allure.description('Авториземся, проверяем ответ и удаляем курьера')
    def test_courier_login_success(self, empty_courier):

        response = Courier().courier_login_and_get_id(empty_courier["data"])
        assert response["status_code"] == StatusCodesCourier.courier_login_successful["status_code"]
        assert "id" in response["response_text"]

    @allure.title('Авторизация без заполнения обязательных полей Login/Password')
    @allure.description('Авторизация заполнения обязательного поля {courier_data}')
    @pytest.mark.parametrize('courier_data', [NewCourierCreds.generate_creds_set("without_login"),
                                              NewCourierCreds.generate_creds_set("without_pass")])
    def test_courier_login_without_parameters_failed(self, courier_data):

        response = requests.post(EndPoints.login_courier, data=courier_data)
        assert response.status_code == StatusCodesCourier.courier_login_one_param_empty["status_code"]
        assert response.text == StatusCodesCourier.courier_login_one_param_empty["response_text"]

    @allure.title('Авторизации курьера с несуществующими данными')
    @allure.description('Авторизация с несуществующими данными')
    def test_courier_login_without_null_login_failed(self):
        courier_data = NewCourierCreds.generate_creds_set("incorrect")
        response = requests.post(EndPoints.login_courier, data=courier_data)
        assert response.status_code == StatusCodesCourier.courier_login_incorrect_creds["status_code"]
        assert response.text == StatusCodesCourier.courier_login_incorrect_creds["response_text"]
