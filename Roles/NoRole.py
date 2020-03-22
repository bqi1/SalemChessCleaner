import sys
sys.path.insert(1,"../")
from Pieces import Piece
class BasicRole():
    def __init__(self):
        pass
    def filter_moves_and_kills(self,my_colour,moves,row,column,board):
        move_list = []
        kill_list = []
        for [row1,col1] in moves:
            if board[row1][col1] == []:
                move_list.append([row1,col1])
            elif isinstance(board[row1][col1],Piece) and board[row1][col1].colour != my_colour:
                kill_list.append([row1,col1])
        return move_list,kill_list
    def get_ability_tiles(self,row,col,board):
        # Highlights tiles for player to choose
        return []
    def __str__(self):
        return "Basic"
    def get_description(self):
        return "No special abilities. Basically a loser."
    def ability_message(self):
        return ""
    def activate_ability(self,row,col,board):
        pass