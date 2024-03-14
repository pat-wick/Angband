# player.py
# ------------
# By Pat Wick
# This module defines a player agent class. This is intended
# to be used in an implementation of an adventure game but could
# generally be adapted for other player character uses.

from retro.game import Game
from projectile import Projectile

class Player:
    name = "player"
    level = 1
    xp = 0
    direction = (1,0)
    class_ = ""
    speed = 0
    damage = 0
    
    def __init__(self, position, race, class_):
        """Class and race will determine player stats and abilities.
        """
        self.position = position
        self.race = race
        self.class_ = class_
        if class_.capitalize() == "Warrior":
            self.color = "red"
            self.class_ == class_
        elif class_.capitalize() == "Rogue":
            self.color = "green"
            self.class_ == class_
        else:
            self.color = "blue"
            self.class_ == class_

        if race.capitalize() == "Human":
            self.character = "H"
            self.speed = 3
            self.damage = int(2 + (self.level / 3))
        elif race.capitalize() == "Elf":
            self.character = "E"
            self.speed = 1
            self.damage = int(1 + (self.level / 4))
        else:
            self.character = "D"
            self.speed = 6
            self.damage = int(3 + (self.level / 2))

    def attack(self,game):
        """Warrior is a melee character, mage and rogue use ranged attacks.
        """
        # if self.class_ == "Warrior":
        #     if game.turn_number % self.speed == 0:
        #         agent = self.get_agent_in_position((self.position[0] + self.direction[0],self.position[1] + self.direction[1]),game)
        #         if agent:
        #             if agent.deadly:
        #                 agent.hp -= game.get_agent_by_name("player").damage * 2
        # else:
        projectile = Projectile((self.position[0] + self.direction[0],self.position[1] + self.direction[1]), self.direction, self.speed, game)
        game.add_agent(projectile)
        #print("pew pew pew")

    def handle_keystroke(self, keystroke, game):
        x, y = self.position
        if keystroke.name in ("KEY_LEFT", "KEY_RIGHT"):
            if keystroke.name == "KEY_LEFT":
                new_position = (x - 1, y)
                self.direction = (-1,0)
            else:
                new_position = (x + 1, y)
                self.direction = (1,0)
            if game.on_board(new_position):
                self.try_to_move(new_position,game)
                if game.is_empty(new_position):
                    self.position = new_position
        
        if keystroke.name in ("KEY_DOWN", "KEY_UP"):
            if keystroke.name == "KEY_DOWN":
                new_position = (x, y + 1)
                self.direction = (0,1)
            else:
                new_position = (x, y - 1)
                self.direction = (0,-1)
            if game.on_board(new_position):
                self.try_to_move(new_position,game)
                if game.is_empty(new_position):
                    self.position = new_position

        if keystroke == " ":
            self.attack(game)

    def try_to_move(self, position, game):
        """Check if player moved into an enemy and loses.
        """
        agent = self.get_agent_in_position(position,game)
        if agent:
            if agent.deadly:
                game.state['message'] = "Monsters can be deadly..."
                game.end()
        

    def get_agent_in_position(self, position, game):
        """Checks a location for current agents.
        """
        agents = game.get_agents_by_position()[position]
        if agents:
            return agents[0]
        
    def level_up(self):
        """Player levelup is managed by an xp curve.
        """
        xpToLevel = (self.level + self.level - 1) * 20
        if self.xp >= xpToLevel:
            self.xp -= xpToLevel
            self.level += 1
            
    def play_turn(self,game):
        self.level_up()
        game.state["Level"] = self.level
