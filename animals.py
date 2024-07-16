# import the python datetime module to help us create a timestamp
from datetime import date

def display_animal(animal):
    print(f"{animal.name} is a {animal.species}, and they came here on {animal.date_added}")

class Llama:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()

class Goat:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()

class Sheep:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()

class Pig:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()

class Horse:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.walking = True
        self.date_added = date.today()

class Snake:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

class Lizard:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

class Gecko:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

class Worm:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

class Skink:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.slithering = True
        self.date_added = date.today()

class Fish:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

class Turtle:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

class Frog:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

class Starfish:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()

class Eel:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.swimming = True
        self.date_added = date.today()


# Creating instances for each class
miss_fuzz = Llama("Miss Fuzz", "domestic llama")

billy = Goat("Billy", "domestic goat")

dolly = Sheep("Dolly", "domestic sheep")

porky = Pig("Porky", "domestic pig")

spirit = Horse("Spirit", "domestic horse")

slither = Snake("Slither", "garden snake")

lizzy = Lizard("Lizzy", "gecko lizard")

george = Gecko("George", "leopard gecko")

wiggles = Worm("Wiggles", "earthworm")

skittles = Skink("Skittles", "blue-tongued skink")

nemo = Fish("Nemo", "clownfish")

shelly = Turtle("Shelly", "sea turtle")

hoppy = Frog("Hoppy", "tree frog")

patrick = Starfish("Patrick", "common starfish")

electric = Eel("Electric", "electric eel")