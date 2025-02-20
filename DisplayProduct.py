class DisplayProduct:
    def show(self, products):
        print("\nProduct List:")
        for name, price in products.items():
            print(f"{name}: {price}")