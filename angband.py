# angband.py
# ------------
# By Pat Wick
# This game is a redevelopment of the retro game "Angband". Named after
# the stronghold of Morgoth, the Sauron before Sauron in the Lord of the Rings,
# the game is a dungeon-crawler adventure game where the player is tasked with
# delving into Angband to confront Morgoth. Defeating monsters earns the player
# experience points (xp) which allow for more power as the player levels up.
# In this, v0.2, a general movement and combat system exists, but level
# generation, items, and monster spawning won't happen until future versions.

import pyxel
from player import Player

class App:
    def __init__(self):
        pyxel.init(320, 240)
        print("Welcome to AngBAD (a poor representation of Angband)!\n")
    
        race = input("Choose your race (Human, Elf, Dwarf): ").capitalize()
        while race not in ["Human", "Elf", "Dwarf"]:
            print("Invalid race. Please choose Human, Elf, or Dwarf.")
            race = input("Choose your race (Human, Elf, Dwarf): ").capitalize()

        class_ = input("Choose your class (Warrior, Mage, Rogue): ").capitalize()
        while class_ not in ["Warrior", "Mage", "Rogue"]:
            print("Invalid class. Please choose Warrior, Mage, or Rogue.")
            class_ = input("Choose your class (Warrior, Mage, Rogue): ").capitalize()

        print(f"\nYou've chosen to play as a {race} {class_}.")
        input("Press Enter to continue. Good luck!")
        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)
        

App()