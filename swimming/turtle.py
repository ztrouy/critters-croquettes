from datetime import date

class Turtle:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()
        self.food = food

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')