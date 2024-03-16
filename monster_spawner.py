# monster_spawner.py
# -------------------
# By Pat Wick
# This module defines a MonsterSpawner agent class.

from random import (
    randint,
    choices,
)
from enemies import *
from map import random_empty_position
from stairs import Stairs

class MonsterSpawner:
    display = False
    floor = 0

    def __init__(self):
        pass

    def play_turn(self, game):
        """Places each of the monsters on the board for that level.
        """
        toSpawn = self.should_spawn_monsters(game.state["Floor"])

        for i in range(toSpawn):
            monster = self.choose_monster()(random_empty_position(game))
            game.add_agent(monster)
            if i == 0:
                if game.state["Floor"] != 1:
                    game.remove_agent_by_name("stairs")
                game.add_agent(Stairs(random_empty_position(game)))


    def should_spawn_monsters(self, floor_number):
        """Returns the number of monsters to spawn, given the player
        advanced a floor.
        """
        numMonsters = 0
        if floor_number != self.floor:
            numMonsters = randint(1, floor_number // 10 + 3)
            self.floor = floor_number
        return numMonsters
    
    def choose_monster(self):
        """Picks a random monster out of a weighted list of monsters.
        """
        monsters = [Orc, Rat, Spider]
        monster = choices(monsters, weights = (10, 30, 60))
        monster = monster[0]
        return monster
