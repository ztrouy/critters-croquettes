from swimming import Fish, Turtle, Frog, Starfish, Eel
from walking import Llama, Goat, Sheep, Pig, Horse
from slithering import Snake, Lizard, Gecko, Worm, Skink


def display_animal(animal):
    if hasattr(animal, "shift"):
        print(f"{animal.name} the {animal.species} is available to play during the {animal.shift} shift, and came here on {animal.date_added}")
    else:
        print(f"{animal.name} the {animal.species} is available all day, and came here on {animal.date_added}")


# Creating instances for each class
miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow")

billy = Goat("Billy", "domestic goat", "midday", "Goat Chow")

dolly = Sheep("Dolly", "domestic sheep", "night", "Sheep Chow")

porky = Pig("Porky", "domestic pig", "morning", "Pig Chow")

spirit = Horse("Spirit", "domestic horse", "midday", "Horse Chow")

slither = Snake("Slither", "garden snake", "Snake Chow")

lizzy = Lizard("Lizzy", "gecko lizard", "Lizard Chow")

george = Gecko("George", "leopard gecko", "Gecko Chow")

wiggles = Worm("Wiggles", "earthworm", "Worm Chow")

skittles = Skink("Skittles", "blue-tongued skink", "Skink Chow")

nemo = Fish("Nemo", "clownfish", "Fish Chow")

shelly = Turtle("Shelly", "sea turtle", "Turtle Chow")

hoppy = Frog("Hoppy", "tree frog", "Frog Chow")

patrick = Starfish("Patrick", "common starfish", "Starfish Chow")

electric = Eel("Electric", "electric eel", "Eel Chow")

# Display all initial animals
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

# Feed all initial animals
miss_fuzz.feed()
billy.feed()
dolly.feed()
porky.feed()
spirit.feed()
slither.feed()
lizzy.feed()
george.feed()
wiggles.feed()
skittles.feed()
nemo.feed()
shelly.feed()
hoppy.feed()
patrick.feed()
electric.feed()