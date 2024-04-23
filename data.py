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
