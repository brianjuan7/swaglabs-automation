from random import randrange


class Product:
    TAX = 0.08
    items = [
        {"label": "Sauce Labs Bike Light",
         "price": 9.99,
         "description": "A red light isn't the desired state in testing but it sure helps when riding your bike at "
                        "night. Water-resistant with 3 lighting modes, 1 AAA battery included."},
        {"label": "Test.allTheThings() T-Shirt (Red)",
         "price": 15.99,
         "description": "This classic Sauce Labs t-shirt is perfect to wear when cozying up to your keyboard to "
                        "automate a few tests. Super-soft and comfy ringspun combed cotton."},
        {"label": "Sauce Labs Backpack",
         "price": 29.99,
         "description": "carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with"
                        " unequaled laptop and tablet protection."}
    ]

    def __init__(self):
        self.index = None
        self.random_index = randrange(0, len(self.items))

    def get_random_item(self):
        return self.items[self.random_index]

    def get_an_item(self, index):
        self.index = index
        return self.items[self.index]
