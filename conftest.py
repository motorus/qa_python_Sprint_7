import pytest
from helps import Courier


@pytest.fixture(scope='function')
def empty_courier():
    new_courier = Courier.courier_registration_and_get_data()
    courier_login = Courier.courier_login_and_get_id(new_courier["data"])
    yield new_courier
    Courier().courier_delete(courier_login["id"])


@pytest.fixture(scope='function')
def courier_for_delete():
    new_courier = Courier.courier_registration_and_get_data()
    courier_login = Courier.courier_login_and_get_id(new_courier["data"])
    yield courier_login
