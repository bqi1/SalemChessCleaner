import Pieces as pcs
import sys
import tkinter as tk
sys.path.insert(1,'Roles/')
import AllRoles as roles
import random
class GameMaster():
    def __init__(self):
        self.board = [[[] for col in range(8)] for row in range(8)]
        self.turn = random.choice(["WHITE","BLACK"])
        self.last_piece_clicked = [9,9]
        self.whites_blacks_num = [16,16]
        self.ability_tiles = []
        self.move_tiles = []
        self.kill_tiles = []
        self.graveyard = []
        self.keep_playing = True
        self.moveset_active = False
        self.setup_initial_pieces()
    def setup_initial_pieces(self):
        for [row,colour] in [[0,"BLACK"],[7,"WHITE"]]:
            self.board[row][0] = pcs.Rook(colour)
            self.board[row][1] = pcs.Knight(colour)
            self.board[row][2] = pcs.Bishop(colour)
            self.board[row][5] = pcs.Bishop(colour)
            self.board[row][6] = pcs.Knight(colour)
            self.board[row][7] = pcs.Rook(colour)
            for column in range(8):
                if colour == "BLACK":
                    self.board[row+1][column] = pcs.Pawn(colour)
                else:
                    self.board[row-1][column] = pcs.Pawn(colour)
            #temp
            self.board[row][0].update_role(roles.BasicRole())
            self.board[row][1].update_role(roles.BasicRole())
            self.board[row][2].update_role(roles.BasicRole())
            self.board[row][5].update_role(roles.BasicRole())
            self.board[row][6].update_role(roles.BasicRole())
            self.board[row][7].update_role(roles.BasicRole())

        self.board[0][3] = pcs.Queen("BLACK")
        self.board[0][4] = pcs.King("BLACK")
        self.board[7][3] = pcs.King("WHITE")
        self.board[7][4] = pcs.Queen("WHITE")

        #temp 
        self.board[0][3].update_role(roles.BasicRole())
        self.board[0][4].update_role(roles.BasicRole())
        self.board[7][3].update_role(roles.BasicRole())
        self.board[7][4].update_role(roles.BasicRole())
    def get_turn_message(self):
        if self.turn == "WHITE":
            return "It's WHITE's turn!"
        else:
            return "It's BLACK's turn!"
    def next_turn(self):
        self.moveset_active = False
        self.last_piece_clicked = [9,9]
        self.ability_tiles = []
        self.move_tiles = []
        self.kill_tiles = []
        if self.turn == "WHITE":
            self.turn = "BLACK"
        else:
            self.turn = "WHITE"
    def get_moves_and_kills(self,row,col):
        piece = self.board[row][col]
        if isinstance(piece,pcs.Piece):
            move_tiles,kill_tiles = piece.get_moves_and_kills(row,col,self.board)
            return move_tiles,kill_tiles
        else:
            return [],[]
    def tile_click(self,row,col):
        if not self.keep_playing:
            return [],[],[],""
        message = ""
        # If you clicked a tile but no tile is highlighted, or if you click a piece that's not yours, or if tiles are highlighted and you don't click any
        if (isinstance(self.board[row][col],list) and not self.moveset_active)\
            or (isinstance(self.board[row][col],pcs.Piece) and self.turn != self.board[row][col].colour and [row,col] not in self.kill_tiles)\
                or (self.moveset_active and ([row,col] not in self.ability_tiles and [row,col] not in self.move_tiles and [row,col] not in self.kill_tiles)):
            self.ability_tiles,self.move_tiles,self.kill_tiles = [],[],[]
            self.moveset_active = False
            return [],[],[],""
        # Else, highlight them tiles if not already
        if not self.moveset_active:
            self.last_piece_clicked = [row,col]
            self.moveset_active = True
            moveset,killset = self.get_moves_and_kills(row,col)
            ability_set = self.get_ability_selections(row,col)
            self.ability_tiles = ability_set.copy()
            self.move_tiles = moveset.copy()
            self.kill_tiles = killset.copy()
            return moveset,killset,ability_set,message
        # Else, it means a highlighted tile was clicked
        if [row,col] in self.ability_tiles:
            message = self.ability_tile_clicked(row,col)
        elif [row,col] in self.move_tiles or [row,col] in self.kill_tiles:
            self.move(row,col)
            self.moveset_active = False
            message = self.get_turn_message()
        return [],[],self.ability_tiles.copy(),message
    def ability_tile_clicked(self,row,col):
        self.ability_tiles = self.board[row][col].role.get_ability_tiles()
        self.board[row][col].role.activate_ability(row,col,self.board)
        return self.board[row][col].role.ability_message()
    def ability_button_clicked(self):
        if not self.keep_playing: return ""
        if self.last_piece_clicked == [9,9]:
            return ""
        row,col = self.last_piece_clicked
        self.ability_tiles = self.board[row][col].role.get_ability_tiles()
        return self.board[row][col].role.ability_message()
    def move(self,row,col):

        if [row,col] in self.kill_tiles:
            self.kill(row,col)
        self.board[row][col] = self.board[self.last_piece_clicked[0]][self.last_piece_clicked[1]]
        self.board[self.last_piece_clicked[0]][self.last_piece_clicked[1]] = []
        self.next_turn()
    def kill(self,row,col):
        if self.turn == "BLACK":
            self.whites_blacks_num[0]-=1
        else:
            self.whites_blacks_num[1]-=1
        if self.board[row][col].role != None:
            self.graveyard.append("{0}: {1}".format(str(self.board[row][col]),str(self.board[row][col].role)))
    def get_ability_selections(self,row,col):
        piece = self.board[row][col]
        if isinstance(piece,pcs.Piece) and piece.role != None:
            ability_selections = piece.role.get_ability_tiles(row,col,self.board)
            return ability_selections
        else:
            return []
    def get_surrender_message(self):
        self.keep_playing = False
        if self.turn == "WHITE":
            return "WHITE forfeits their career! The champion is BLACK!"
        else:
            return "BLACK chooses the obviously inferior way out! The winner is WHITE!"
    def get_graveyard_victims(self):
        return self.graveyard
    def check_lose_condition(self):
        if self.whites_blacks_num[1] < 1:
            self.keep_playing = False
            return "BLACK has carelessly sacrificed all their soldiers in vain! WHITE dominates!"
        elif self.whites_blacks_num[0] < 1:
            self.keep_playing = False
            return "WHITE has run dry of their valuable warriors like a nerd! BLACK wins!"
