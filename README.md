## Яндекс Практикум
#### Курс "Автоматизатор тестирования на Python"
#### 7 спринт
#### Финальный проект


### Файлы:
- allure_results/ - результаты запуска тестов allure
- conftest.py - фикстуры создания и удаления курьера
- data.py - классы с "ручками" и вспомогательные классы для тестирования
- tests/test_create_courier.py - тесты создания курьера
- tests/test_create_order.py - тест создания заказа
- tests/test_get_order_list.py - тест получения списка заказов
- tests/test_login_courier.py - тесты авторизации курьера

#### установка зависимостей
pip3 install -r requirements.txt
#### Запуск тестов
`pytest tests/ --alluredir=allure_results`
#### Запуск отчетности allure
`allure serve allure_results`
