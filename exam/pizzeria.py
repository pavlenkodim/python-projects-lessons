class Pizza:
    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.status = ('preparing', 'done')


    def preparing(self):
        self.status = 'preparing'

        t = Timer(300.0, self.done())
        t.start()

    def done(self):
        self.status = 'done'

class Peperoni (Pizza):
    def __init__(self):
        super().__init__('piperoni', 2.00, ['', ''])

    def free_meat(self):
        self.status = 'free_meat'

piperoni = Pizza('piperoni', 1.00, [])

piperoni_2 = Peperoni()

piperoni_2.preparing()