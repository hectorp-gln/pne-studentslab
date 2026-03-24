class Products:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_information(self):
        return f"Name: {self.name} | Price: {self.price}"

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.s_cart = []

    def add_to_cart(self, product):
        self.s_cart.append(product)

    def compute_total(self):
        total = 0
        for item in self.s_cart:
            z = Products()
            total += z.price
        return total

