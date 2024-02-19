import pytest
import src.utils as utils

file = './products.json'


@pytest.fixture
def category_1():
    return utils.Category('Конфеты', 'Вкусные',
                          [{
                              "name": "Аленка",
                              "description": "Сладкая",
                              "price": 50.0,
                              "quantity": 10
                          }])


def test_init_(category_1):
    assert category_1.name == 'Конфеты'
    assert category_1.description == 'Вкусные'


def test_add_products(category_1):
    category_1.add_products(("Iphone 15", "512GB, Gray space", 210000.0, 8))


@pytest.fixture
def category():
    return utils.filling_classes_Category(utils.connection_file(file))


def test_filling_classes_Category(category):
    assert category[0].name == 'Смартфоны'
    assert category[0].description == ('Смартфоны, как средство не только коммуникации, но и получение дополнительных '
                                       'функций для удобства жизни')


def test_print_product(category):
    assert category[0].print_product == ('Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
                                         'Iphone 15, 210000.0 руб. Остаток: 8 шт.\n'
                                         'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.')

@pytest.fixture
def product():
    return utils.Product('Аленка', 'Сладкая', 50.0, 10)


def test_init_product(product):
    assert product.name == 'Аленка'
    assert product.description == 'Сладкая'
    assert product._price == 50.0
    assert product.quantity == 10


def test_create_product(product):
    assert product.create_products(('Alpen Gold', 'Шоколад молочный', 100.0, 15))


def test_price(product):
    product.price = 55.0
    assert product.price == 55.0

@pytest.fixture
def classes_Product():
    return utils.filling_classes_Product(utils.connection_file(file))


def test_filling_classes_Product(classes_Product):
    assert classes_Product[0].name == 'Samsung Galaxy C23 Ultra'
