# projectile.py
# ------------
# By Pat Wick
# This module defines a "casted" projectile. This is the basis
# for ranged character types' attacks.

from retro.game import Game

class Projectile:
    character = "*"
    deadly = False
        
    def __init__(self, position, direction, speed, game):
        self.position = position
        self.direction = direction
        self.speed = speed
        if game.get_agent_by_name("player").class_ == "Rogue":
            if self.direction in [(1,0), (-1,0)]:
                self.character = "-"
            elif self.direction in [(0,1), (0,-1)]:
                self.character = "|"
        if game.get_agent_by_name("player").class_ == "Warrior":
            if self.direction in [(0,1), (0,-1)]:
                self.character = "|"
            elif self.direction == (1,0):
                self.character = "/"
            else:
                self.character = "\\"

    def move(self, game):
        """Try to move in direction set by player when launched. If blocked,
        disappear. If projectile hits an enemy, lower hp by damage.
        """
        dx, dy = self.direction
        new_position = (self.position[0] + dx, self.position[1] + dy)
        if game.on_board(new_position):
            if game.is_empty(new_position):
                self.position = new_position
            else:
                agent = self.get_agent_in_position(new_position,game)
                if agent:
                    if agent.deadly:
                        agent.hp -= game.get_agent_by_name("player").damage
                        game.remove_agent(self)
                    else:
                        game.remove_agent(self)
        else:
            game.remove_agent(self)

    def play_turn(self,game):
        """Speed of projectiles depends on character race.
        """
        if game.turn_number % self.speed == 0:
            self.move(game)
            try:
                if game.get_agent_by_name("player").class_ == "Warrior":
                    game.remove_agent(self)
            except:
                pass
            

    def get_agent_in_position(self, position, game):
        """Returns an agent at the position, or returns None. 
        game.get_agents_by_position always returns a list, which may
        contain zero, one, or multiple agents at the given position. 
        In the Beast game, we never allow more than one agent to be in 
        a position.
        """
        agents = game.get_agents_by_position()[position]
        if agents:
            return agents[0]

    def handle_collision(self, game):
        # need to fix this at some point
        pass