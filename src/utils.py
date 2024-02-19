import json


class Category:
    quantity_category = 0
    quantity_unique_products = 0

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.__product = product
        Category.quantity_category += 1
        Category.quantity_unique_products = len(self.__product)

    def add_products(self, data):
        list(self.__product).append({
            "name": data[0],
            "description": data[1],
            "price": data[2],
            "quantity": data[3]
        })

    @property
    def print_product(self):
        lists = []
        for item in self.__product:
            lists.append(f"{item['name']}, {item['price']} руб. Остаток: {item['quantity']} шт.")
        return '\n'.join(lists)


class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @classmethod
    def create_products(cls, new_product):
        name, description, price, quantity = (new_product[0], new_product[1], new_product[2], new_product[3])
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):

        float(new_price)
        if new_price <= 0.0:
            print('Цена введена не корректно!')
        elif new_price < self._price:
            while True:
                answer = input('Цена ниже преждней. Вы хотите изменить цену (y/n):\n').lower()
                if answer == 'y':
                    self._price = new_price
                    break
                else:
                    break
        else:
            self._price = new_price


def connection_file(f):
    with open(f, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def filling_classes_Category(file):
    category = []
    for item in file:
        category.append(Category(item['name'], item['description'], item['products']))
    return category


def filling_classes_Product(file):
    products = []
    for item in file:
        for items in item['products']:
            products.append(Product(items['name'], items['description'], items['price'], items['quantity']))
    return products
