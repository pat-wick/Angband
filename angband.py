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

from retro.game import Game
from player import Player
from dungeon import Dungeon
from random import sample
from wall import Wall
from map import (
    board_edges,
    inner_board,
    level_one,
    random_empty_position
)
from monster_spawner import MonsterSpawner

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

board_size = (50,25)
x,y = board_size

walls = [Wall(position) for position in board_edges(board_size)]
level = [Wall(position) for position in level_one(board_size)]
game = Game(walls + level, {"Race":race, "Class":class_,"CharLevel":1,"Floor":1}, board_size = board_size)
game.add_agent(MonsterSpawner())
game.add_agent(Player((x//2,y//2),race,class_))

game.play()