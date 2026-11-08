
class Product:
    VAT_RATE = 0.17
    created_count = 0
    def __init__(self, name, price):
        Product.created_count += 1
        self.name = name
        self.price = price

    def price_with_vat(self):
        return self.price + self.price * self.VAT_RATE



#tar5

