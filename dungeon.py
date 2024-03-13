# dungeon.py
# ------------
# By Pat Wick
# This module defines a dungeon generation algorithm. I
# still need to figure out what that might actually mean

class Dungeon:
    board_size = (10,10)
    board_width = 10
    board_height = 10
    position = (0,0)
    dungeon_map = [["."] * board_width] * board_height
    
    
    for row in range(board_height):
        for col in range(board_width):
            if row == 0 or row == board_height-1:
                dungeon_map[row][col] = "#"
            else:
                if col == 0 or col == board_width-1:
                    dungeon_map[row][col] = "#"
                else:
                    dungeon_map[row][col] = "."

    def __init__(self, position):
        self.position = position
        self.name = "dungeon"