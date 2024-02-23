import pytest
import src.utils as utils
from src.Product import Product
from src.Category import Category

file = './products.json'


@pytest.fixture
def category():
    return utils.filling_classes(utils.connection_file(file))


def test_add_product(category):
    assert category[0].add_product(Product('Iphone 13', '512GB, Gray space', 150000, 10)) is None


def test_proucts(category):
    assert category[0].products[0] == 'Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.'
    assert category[0].products[2] == 'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.'
