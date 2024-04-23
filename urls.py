
class EndPoints:
    test_url = 'https://qa-scooter.praktikum-services.ru'
    login_courier   = test_url + '/api/v1/courier/login'  # post
    create_courier  = test_url + '/api/v1/courier'  # post
    delete_courier  = test_url + '/api/v1/courier/'  # delete
    get_order_count = test_url + '/api/v1/courier/:id/ordersCount'  # get
    finish_oder     = test_url + '/api/v1/orders/finish/:id'  # put
    cancel_oder     = test_url + '/api/v1/orders/cancel'  # put
    get_orders      = test_url + '/api/v1/orders'  # get
    get_order_by_number = test_url + '/api/v1/orders/track'  # get
    accept_order    = test_url + '/api/v1/orders/accept/:id'  # put
    create_order    = test_url + '/api/v1/orders'  # post
