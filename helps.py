import allure
from faker import Faker
import requests
from data import OrderData
from urls import EndPoints
import json


class NewCourierCreds:

    @staticmethod
    @allure.step("Генерация фековых кредов для регистрации курьера")
    def generate_creds_set(param="valid"):
        creds = {}
        fake = Faker("ru_RU")

        login = fake.user_name() if param != "without_login" else ""
        password = fake.password() if param != "without_pass" else ""
        firstname = fake.first_name()
        creds = {"login": login,
                 "firstName": firstname,
                 "password": password}
        if param == "incorrect":
            creds = {"login": "123123123",
                     "firstName": "123123123",
                     "password": "123123123"}

        return creds


class Courier:

    @staticmethod
    @allure.step("Регистрация нового курьера и возврат данных регистрации")
    def courier_registration_and_get_data():
        data = NewCourierCreds.generate_creds_set()
        response = requests.post(EndPoints.create_courier, data=data)
        return {"response_text": response.text,
                "status_code": response.status_code,
                "data": data}

    @allure.step("Проверка повторной регистрации")
    def courier_double_registration(self):
        double_data = self.courier_registration_and_get_data()["data"]
        response = requests.post(EndPoints.create_courier, data=double_data)
        return {"response_text": response.text,
                "status_code": response.status_code,
                "data": double_data}

    @staticmethod
    @allure.step("Авторизация и возврат ID курьера и результата авторизации")
    def courier_login_and_get_id(data):
        response = requests.post(EndPoints.login_courier, data=data)
        try:
            courier_id = str(response.json()["id"])
        except AttributeError:
            courier_id = ""

        return {"id": courier_id,
                "response_text": response.text,
                "status_code": response.status_code}

    @staticmethod
    @allure.step("Удаление курьера")
    def courier_delete(courier_id):
        response = requests.delete(EndPoints.delete_courier + str(courier_id))
        return {"response_text": response.text, "status_code": response.status_code}


class Order:
    @staticmethod
    @allure.step("Создание заказа")
    def create_order(color):
        headers = {"Content-type": "application/json"}
        data = OrderData.data
        data.update(color)
        json_data = json.dumps(data)
        response = requests.post(EndPoints.create_order, headers=headers, data=json_data)
        return response
