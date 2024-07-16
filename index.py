from swimming import Fish, Turtle, Frog, Starfish, Eel
from walking import Llama, Goat, Sheep, Pig, Horse
from slithering import Snake, Lizard, Gecko, Worm, Skink


def display_animal(animal):
    print(f"This {animal.species} is named {animal.name}, and they came here on {animal.date_added}")


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

display_animal(miss_fuzz)
display_animal(billy)
display_animal(dolly)
display_animal(porky)
display_animal(spirit)
display_animal(slither)
display_animal(lizzy)
display_animal(george)
display_animal(wiggles)
display_animal(skittles)
display_animal(nemo)
display_animal(shelly)
display_animal(hoppy)
display_animal(patrick)
display_animal(electric)