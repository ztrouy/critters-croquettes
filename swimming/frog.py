from datetime import date

class Frog:
    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
