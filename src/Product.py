class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @classmethod
    def create_products(cls, number):
        # for prod in product:
        #     if prod[0] == number['name']:
        #         prod[2] = max(prod[2], number['price'])
        #         prod[3] += number['quantity']
        #         print('Данный товар существует, количество товара увеличина, цена выбрана наибольщая')
        #         return
        return cls(**number)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        float(new_price)
        if new_price <= 0.0:
            print('Цена введена не корректно!')
        elif new_price < self._price:
            answer = input('Цена ниже преждней. Вы хотите изменить цену (y/n):\n').lower()
            if answer == 'y':
                self._price = new_price
        else:
            self._price = new_price
