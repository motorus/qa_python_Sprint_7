import requests
import json
from faker import Faker


class NewCourierCreds:

    @staticmethod
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

    # Регистрация нового курьера
    @staticmethod
    def courier_registration_and_get_data():
        data = NewCourierCreds.generate_creds_set()
        response = requests.post(EndPoints.create_courier, data=data)
        return {"response_text": response.text,
                "status_code": response.status_code,
                "data": data}

    def courier_double_registration(self):
        double_data = self.courier_registration_and_get_data()["data"]
        response = requests.post(EndPoints.create_courier, data=double_data)
        return {"response_text": response.text,
                "status_code": response.status_code,
                "data": double_data}

    # Логин и возврат идентификатора
    @staticmethod
    def courier_login_and_get_id(data):
        response = requests.post(EndPoints.login_courier, data=data)
        try:
            courier_id = str(response.json()["id"])
        except AttributeError:
            courier_id = ""

        return {"id": courier_id,
                "response_text": response.text,
                "status_code": response.status_code}

    # удаление курьера по идентификатору
    @staticmethod
    def courier_delete(courier_id):
        response = requests.delete(EndPoints.delete_courier + str(courier_id))
        return {"response_text": response.text, "status_code": response.status_code}


class StatusCodesCourier:
    courier_created = {"status_code": 201,
                       "response_text": '{"ok":true}'}
    login_is_busy = {"status_code": 409,
                     "response_text": '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'}
    empty_value = {"status_code": 400,
                   "response_text": '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'}

    delete_courier = {"status_code": 200,
                      "response_text": '{"ok":true}'}
    delete_courier_without_id = {"status_code": 400,
                                 "response_text": '{"message":  "Недостаточно данных для удаления курьера"}'}
    delete_courier_wrong_id = {"status_code": 404,
                               "response_text": '{"code":404,"message":"Курьера с таким id нет."}'}
    courier_login_successful = {"status_code": 200,
                                "response_text": ''}
    courier_login_one_param_empty = {"status_code": 400,
                                     "response_text": '{"code":400,"message":"Недостаточно данных для входа"}'}

    courier_login_incorrect_creds = {"status_code": 404,
                                     "response_text": '{"code":404,"message":"Учетная запись не найдена"}'}

    order_create = {"status_code": 201,
                    "response_text": '{"code":201,track: }'}
    order_get_list = {"status_code": 200,
                    "response_text": ''}


class EndPoints:
    test_url = 'https://qa-scooter.praktikum-services.ru'
    login_courier = test_url + '/api/v1/courier/login'  # post
    create_courier = test_url + '/api/v1/courier'  # post
    delete_courier = test_url + '/api/v1/courier/'  # delete

    get_order_count = test_url + '/api/v1/courier/:id/ordersCount'  # get
    finish_oder = test_url + '/api/v1/orders/finish/:id'  # put
    cancel_oder = test_url + '/api/v1/orders/cancel'  # put
    get_orders = test_url + '/api/v1/orders'  # get
    get_order_by_number = test_url + '/api/v1/orders/track'  # get
    accept_order = test_url + '/api/v1/orders/accept/:id'  # put
    create_order = test_url + '/api/v1/orders'  # post


class Order:
    @staticmethod
    def create_order(color):
        headers = {"Content-type": "application/json"}
        data = OrderData.data
        data.update(color)
        json_data = json.dumps(data)
        response = requests.post(EndPoints.create_order, headers=headers, data=json_data)
        return response


class OrderData:
    # Данные для создания ордера
    data = {
        "firstName": "Имя",
        "lastName": "Фамильевич",
        "address": "г.Москва",
        "metroStation": 1,
        "phone": "+7 123456789",
        "rentTime": 4,
        "deliveryDate": "2024-12-31",
        "comment": "comment",
    }
