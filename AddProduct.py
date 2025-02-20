class AddProduct:
    def __init__(self):
        self.products = {}

    def add(self, name, price):
        self.products[name] = price
        print(f"Added {name} with price {price}")

    def get_products(self):
        return self.products
