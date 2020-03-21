import Pieces as pcs
class GameMaster():
    def __init__(self):
        self.board = [[[] for col in range(8)] for row in range(8)]

    def get_moves_and_kills(self,row,col):
        move_tiles = []
        kill_tiles = []
        piece = self.board[row][col]
        piece_colour = piece.colour
        piece_moves = piece.get_moveset(row,col,self.board)
        for [p_row,p_col] in piece_moves:
            if pcs.Piece in self.board[p_row][p_col] and self.board[p_row][p_col].colour != piece_colour:
                kill_tiles.append([p_row,p_col])
            elif pcs.Piece not in self.board[p_row][p_col]:
                move_tiles.append([p_row,p_col])
        return move_tiles,kill_tiles

    def get_surrender_message(self):
        return "Loser"
    def get_graveyard_victims(self):
        return ["Dead dude"]