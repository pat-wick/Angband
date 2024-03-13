from retro.game import Game
from random import sample
from player import Player
from wall import Wall
from random import randint

def board_edges(board_size):
    """The outline of the generated board. Used in angband to surround
    the level with immovable objects to keep the enemies and player inside
    """
    x,y = board_size
    positions = []
    top = [(i,0) for i in range(x)]
    bottom = [(i,y-1) for i in range(x)]
    left = [(0,j) for j in range(1,y-1)]
    right = [(x-1,j) for j in range(1,y-1)]
    return top + bottom + left + right

def inner_board(board_size):
    x,y = board_size
    positions = []
    for i in range(1,x-1):
        for j in range(1,y-1):
            positions.append((i,j))
    return positions
    
def random_empty_position(game):
    """Returns a random empty position.
    """
    agents_by_position = game.get_agents_by_position()
    while True:
        x, y = game.board_size
        i = randint(1, x-2)
        j = randint(1, y-2)
        if not agents_by_position[(i,j)]:
            return (i,j)

def level_one(board_size):
    x,y = board_size
    positions = []
    for i in range(1,x-1):
        for j in range(1,y//4):
            if i <= x // 4 or i >= x - (x // 4):
                positions.append((i,j))
    for i in range(1,x//4):
        for j in range((y - (y // 4)), y-1):
            positions.append((i,j))

    # Introduce randomness within predefined pattern
    for _ in range(10):  # Example: Add 10 random obstacles
        rand_i = randint(1, x - 2)
        rand_j = randint(1, y - 2)
        positions.append((rand_i, rand_j))

    # for i in range(1,x-1):
    #     for j in range(1,y-1):
    #         if i >=4 and i <= 7 or i >= 13 and i <= 16:
    #             if j >= 4 and j <= 7 or j >= 13 and j <= 16:
    #                 positions.append((i,j))
    return positions

def level_two(board_size):
    x,y = board_size
    positions = []
    for i in range(1,x-1):
        for j in range(1,y-1):
            if i >=4 and i <= 7 or i >= 13 and i <= 16:
                if j >= 4 and j <= 7 or j >= 13 and j <= 16:
                    positions.append((i,j))
    return positions