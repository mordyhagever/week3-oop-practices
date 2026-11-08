class Product:
    def __init__(self, name, price, quantity=0):
        if price < 0:
            raise ValueError("price can't be negative")
        self.name = name
        self.price = price
        self.quantity = quantity

