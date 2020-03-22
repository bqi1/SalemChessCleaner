from abc import ABC, abstractmethod
import tkinter as tk
class Piece(ABC):
    def __init__(self,colour):
        pass
    @abstractmethod
    def get_moves_and_kills(self,row,column,board):
        pass
    @abstractmethod
    def update_role(self,role):
        pass
    @abstractmethod
    def append_status(self,status):
        pass
    @abstractmethod
    def remove_status(self,status):
        pass
    @abstractmethod
    def __str__(self):
        pass
class Rook(Piece):
    def __init__(self,colour):
        self.colour = colour
        self.role = None
        self.statuses = []
        if(self.colour == "BLACK"):
            self.picture = tk.PhotoImage(file="Icons/rook-filled.png")
        else:
            self.picture = tk.PhotoImage(file="Icons/rook.png")
    def update_role(self,role):
        self.role = role
    def append_status(self,status):
        self.statuses.append(status)
    def remove_status(self,status):
        try:
            self.statuses.remove(role)
        except:
            return
    def get_moves_and_kills(self,row,column,board):
        moves = []
        direction_boundary = [[-1,-1],[1,8]]
        for [direction,boundary] in direction_boundary:
            for row1 in range(row+direction,boundary,direction):
                if 0<=row1<8:
                    if board[row1][column] == []:
                        moves.append([row1,column])
                    elif isinstance(board[row1][column],Piece):
                        moves.append([row1,column])
                        break
            for col1 in range(column+direction,boundary,direction):
                if 0<=col1<8:
                    if board[row][col1] == []:
                        moves.append([row,col1])
                    elif isinstance(board[row][col1],Piece):
                        moves.append([row,col1])
                        break
        moveset,killset=self.role.filter_moves_and_kills(self.colour,moves,row,column,board)
        return moveset,killset
    def __str__(self):
        return self.colour+" Rook"
class Knight(Piece):
    def __init__(self,colour):
        self.colour = colour
        self.role = None
        self.statuses = []
        if(self.colour == "BLACK"):
            self.picture = tk.PhotoImage(file="Icons/knight-filled.png")
        else:
            self.picture = tk.PhotoImage(file="Icons/knight.png")
    def update_role(self,role):
        self.role = role
    def append_status(self,status):
        self.statuses.append(status)
    def remove_status(self,status):
        try:
            self.statuses.remove(role)
        except:
            return
    def get_moves_and_kills(self,row,column,board):
        moves = []
        directions = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]
        for [row1,col1] in directions:
            if 0<=row+row1<8 and 0<=column+col1<8:
                if board[row+row1][column+col1] == []:
                    moves.append([row+row1,column+col1])
                elif isinstance(board[row+row1][column+col1],Piece):
                    moves.append([row+row1,column+col1])
        moveset,killset=self.role.filter_moves_and_kills(self.colour,moves,row,column,board)
        return moveset,killset
    def __str__(self):
        return self.colour+" Knight"
class Bishop(Piece):
    def __init__(self,colour):
        self.colour = colour
        self.role = None
        self.statuses = []
        if(self.colour == "BLACK"):
            self.picture = tk.PhotoImage(file="Icons/bishop-filled.png")
        else:
            self.picture = tk.PhotoImage(file="Icons/bishop.png")
    def update_role(self,role):
        self.role = role
    def append_status(self,status):
        self.statuses.append(status)
    def remove_status(self,status):
        try:
            self.statuses.remove(role)
        except:
            return
    def get_moves_and_kills(self,row,column,board):
        moves = []
        for row1 in [1,-1]:
            for col1 in [1,-1]:
                row_direction = row1
                col_direction = col1
                while True:
                    if row_direction+row<0 or row_direction+row>7 or col_direction+column<0 or col_direction+column>7:
                        break
                    if board[row_direction+row][col_direction+column] == []:
                        moves.append([row_direction+row,col_direction+column])

                    elif isinstance(board[row_direction+row][col_direction+column],Piece):
                        if board[row_direction+row][col_direction+column].colour != self.colour:
                            moves.append([row_direction+row,col_direction+column])
                        break

                    row_direction = row_direction+row1
                    col_direction = col_direction+col1


        moveset,killset=self.role.filter_moves_and_kills(self.colour,moves,row,column,board)
        return moveset,killset
    def __str__(self):
        return self.colour+" Bishop"
class King(Piece):
    def __init__(self,colour):
        self.colour = colour
        self.role = None
        self.statuses = []
        if(self.colour == "BLACK"):
            self.picture = tk.PhotoImage(file="Icons/king-filled.png")
        else:
            self.picture = tk.PhotoImage(file="Icons/king.png")
    def update_role(self,role):
        self.role = role
    def append_status(self,status):
        self.statuses.append(status)
    def remove_status(self,status):
        try:
            self.statuses.remove(role)
        except:
            return
    def get_moves_and_kills(self,row,column,board):
        moves = []
        for row_change in [-1,0,1]:
            for col_change in [-1,0,1]:
                if row_change == col_change == 0:
                    continue
                if 0<=row+row_change<8 and 0<=column+col_change<8 and board[row+row_change][column+col_change] == []:
                    moves.append([row+row_change,column+col_change])
                elif 0<=row+row_change<8 and 0<=column+col_change<8 and isinstance(board[row+row_change][column+col_change],Piece):
                    moves.append([row+row_change,column+col_change])
        moveset,killset=self.role.filter_moves_and_kills(self.colour,moves,row,column,board)
        return moveset,killset
    def __str__(self):
        return self.colour+" King"
class Queen(Piece):
    def __init__(self,colour):
        self.colour = colour
        self.role = None
        self.statuses = []
        if(self.colour == "BLACK"):
            self.picture = tk.PhotoImage(file="Icons/queen-filled.png")
        else:
            self.picture = tk.PhotoImage(file="Icons/queen.png")
    def update_role(self,role):
        self.role = role
    def append_status(self,status):
        self.statuses.append(status)
    def remove_status(self,status):
        try:
            self.statuses.remove(role)
        except:
            return
    def get_moves_and_kills(self,row,column,board):
        moves = []
        direction_boundary = [[-1,-1],[1,8]]
        for [direction,boundary] in direction_boundary:
            for row1 in range(row+direction,boundary,direction):
                if 0<=row1<8 and board[row1][column] == []:
                    moves.append([row1,column])
                elif 0<=row1<8 and isinstance(board[row1][column],Piece):
                    moves.append([row1,column])
                    break
            for col1 in range(column+direction,boundary,direction):
                if 0<=col1<8 and board[row][col1] == []:
                    moves.append([row,col1])
                elif 0<=col1<8 and isinstance(board[row][col1],Piece):
                    moves.append([row,col1])
                    break
        for row1 in [1,-1]:
            for col1 in [1,-1]:
                row_direction = row1
                col_direction = col1
                while True:
                    if row_direction+row<0 or row_direction+row>7 or col_direction+column<0 or col_direction+column>7:
                        break
                    if board[row_direction+row][col_direction+column] == []:
                        moves.append([row_direction+row,col_direction+column])
                    elif isinstance(board[row_direction+row][col_direction+column],Piece):
                        if board[row_direction+row][col_direction+column].colour != self.colour:
                            moves.append([row_direction+row,col_direction+column])
                        break
                    row_direction = row_direction+row1
                    col_direction = col_direction+col1
        moveset,killset=self.role.filter_moves_and_kills(self.colour,moves,row,column,board)
        return moveset,killset
    def __str__(self):
        return self.colour+" Queen"
class Pawn(Piece):
    def __init__(self,colour):
        self.colour = colour
        self.role = None
        self.start = True
        self.statuses = []
        if(self.colour == "BLACK"):
            self.picture = tk.PhotoImage(file="Icons/pawn-filled.png")
        else:
            self.picture = tk.PhotoImage(file="Icons/pawn.png")
    def update_role(self,role):
        self.role = role
    def append_status(self,status):
        self.statuses.append(status)
    def remove_status(self,status):
        try:
            self.statuses.remove(role)
        except:
            return
    def get_moves_and_kills(self,row,column,board):
        moves = []
        killset = []
        if self.colour == "WHITE":
            increment = -1
        else:
            increment = 1
        if 0<=row+increment<8 and board[row+increment][column] == []:
            moves.append([row+increment,column])
        if self.start and 0<=row+increment*2<8 and board[row+increment*2][column] == []:
            moves.append([row+increment*2,column])
        for col_change in [1,-1]:
            if self.colour == "WHITE":
                row_change = -1
            else:
                row_change = 1
            if 0<=row+row_change<8 and 0<=column+col_change<8 and isinstance(board[row+row_change][column+col_change],Piece)\
                and board[row+row_change][column+col_change].colour != self.colour:
                killset.append([row+row_change,column+col_change])
        return moves,killset
    def __str__(self):
        return self.colour+" Pawn"


