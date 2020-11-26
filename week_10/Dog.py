from week_10.Pet import Pet


class Dog(Pet):

    def __init__(self, name, haired):
        super().__init__(name)
        self.haired = haired

    def get_haired(self):
        return self.haired

    def __str__(self):
        return "I'm a dog and my name is " + self.name
