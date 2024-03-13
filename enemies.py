from strategy import (
    random_move,
    move_toward_player,
)

class Orc:
    """Scary.
    """
    character = "O"
    maxHp = 20
    hp = maxHp
    deadly = True
    speed = 25

    def __init__(self,position):
        self.position = position

    def play_turn(self, game):
        if game.turn_number % self.speed == 0:
            move = move_toward_player(self.position, game)
            if move:
                x, y = self.position
                dx, dy = move
                self.position = (x + dx, y + dy)
                if self.position == game.get_agent_by_name("player").position:
                    game.state['message'] = "Yum."
                    game.end()

        if self.hp <= 0:
            game.remove_agent(self)
            game.get_agent_by_name("player").xp += self.maxHp

class Rat:
    """Not so scary.
    """
    character = "R"
    maxHp = 2
    hp = maxHp
    deadly = True
    speed = 15

    def __init__(self, position):
        self.position = position

    def play_turn(self, game):
        if game.turn_number % self.speed == 0:
            move = random_move(self.position, game)
            if move:
                x, y = self.position
                dx, dy = move
                self.position = (x + dx, y + dy)
                if self.position == game.get_agent_by_name("player").position:
                    game.state['message'] = "Eep."
                    game.end()

        if self.hp <= 0:
            game.remove_agent(self)
            game.get_agent_by_name("player").xp += self.maxHp

class Spider:
    """Creepy-crawly.
    """
    character = "S"
    maxHp = 5
    hp = maxHp
    deadly = True
    speed = 5

    def __init__(self,position):
        self.position = position

    def play_turn(self, game):
        if game.turn_number % self.speed == 0:
            move = random_move(self.position, game)
            if move:
                x, y = self.position
                dx, dy = move
                self.position = (x + dx, y + dy)
                if self.position == game.get_agent_by_name("player").position:
                    game.state['message'] = "Hsssss."
                    game.end()
        
        if self.hp <= 0:
            game.remove_agent(self)
            game.get_agent_by_name("player").xp += self.maxHp