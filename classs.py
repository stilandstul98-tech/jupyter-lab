class Phone:
    def __init__(self, brand, color, model = None, price = None):
        self.brand = brand
        self.color = color
        self.model = model
        self.price = price
        
    def describe(self):
        if self.price is None and self.model is None:
            print(f"This is {self.brand}, {self.color} color")
        else:
            print(f"This is {self.brand}, {self.color} color, {self.model}, {self.price}")


phone1 = Phone("Apple", "red")

phone1.describe()

phone2 = Phone("Pixel", "black", "7A", "44$")

phone2.describe()