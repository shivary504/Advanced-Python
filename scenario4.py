class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def category(self):
        if self.price >= 50000:
            return "Premium"
        elif self.price >= 20000:
            return "Mid-range"
        else:
            return "Budget"

class Store:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self, mobile):
        self.mobiles.append(mobile)

    def display(self):
        for m in self.mobiles:
            print(f"Brand: {m.brand}, Model: {m.model}, Price: ₹{m.price}, Category: {m.category()}")

store = Store()

store.add_mobile(Mobile("Apple", "iPhone 16", 80000))
store.add_mobile(Mobile("Samsung", "Galaxy A35", 30000))
store.add_mobile(Mobile("Redmi", "Note 14", 15000))

store.display()
