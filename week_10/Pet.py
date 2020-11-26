class Pet:

    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return "I'm a pet and my name is " + self.name