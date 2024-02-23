import pytest
import src.utils as utils
from src.Product import Product
from src.Category import Category

# file = '../products.json'
# conect = utils.filling_classes(utils.connection_file(file))
#
# @pytest.fixture
# def category():
#     return conect
#
#
# @pytest.fixture
# def product():
#     return utils.filling_classes(utils.connection_file(file))[0].products


prod = [
    {
        "name": "Samsung Galaxy C23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    },
    {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8
    }
]

cat = {
    "name": "Смартфоны",
    "description": "Многофункциональное устройство",
    "products": [
        Product(prod[0].get("name"), prod[0].get("description"), prod[0].get("price"),
                prod[0].get("quantity")),
        Product(prod[1].get("name"), prod[1].get("description"), prod[1].get("price"),
                prod[1].get("quantity"))
    ]
}


@pytest.fixture
def product_all():
    return cat.get('products')


@pytest.fixture
def category():
    return Category(cat.get("name"), cat.get("description"), cat.get("products"))


def test_price(product_all):
    assert product_all[0].price == 180000.0
    product_all[0].price = 183000.0
    assert product_all[0].price == 183000.0
    product_all[0].price = 0
    assert product_all[0].price == 183000.0


def test_create_products(category, product_all):
    category.add_product(Product.create_products({"name": "Xiaomi Redmi Note 11",
                                                  "description": "1024GB, Синий",
                                                  "price": 31000.0,
                                                  "quantity": 14
                                                  }))
    assert category.products[2] == 'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.'
