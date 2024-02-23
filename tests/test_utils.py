import src.utils as utils

file = './products.json'


def test_filling_classes():
    assert type(utils.filling_classes(utils.connection_file(file))) == list
