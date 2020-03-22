import Pieces as pcs
import sys
import tkinter as tk
sys.path.insert(1,'Roles/')
import AllRoles as roles
class GameMaster():
    def __init__(self):
        self.board = [[[] for col in range(8)] for row in range(8)]

    def get_moves_and_kills(self,row,col):
        piece = self.board[row][col]
        move_tiles,kill_tiles = piece.get_moves_and_kills(row,col,self.board)
        return move_tiles,kill_tiles

    def get_surrender_message(self):
        return "Loser"
    def get_graveyard_victims(self):
        return ["Dead dude"]

if __name__ == "__main__":
    root = tk.Tk()
    rook = pcs.Pawn("BLACK")
    board = [[[] for c in range(8)] for r in range(8)]
    board[0][6] = pcs.Rook("BLACK")
    board[5][5] = pcs.Rook("BLACK")
    board[4][4] = pcs.Rook("WHITE")
    board[3][3] = rook
    rook.update_role(roles.BasicRole())
    print(rook.get_moves_and_kills(3,3,board))