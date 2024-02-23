class Category:
    quantity_category = 0
    quantity_unique_products = 0

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.__product = product
        Category.quantity_category += 1
        Category.quantity_unique_products += len(self.__product)

    def add_product(self, products):
        return self.__product.append(products)

    @property
    def products(self):
        prod = []
        for product in self.__product:
            prod.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return prod

