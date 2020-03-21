from abc import ABC, abstractmethod
import Roles as roles
import tkinter as tk
class Piece(ABC):
    def __init__(self,colour):
        pass
    @abstractmethod
    def get_moveset(self,row,column,board):
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
    def get_moveset(self,row,column,board):
        moves = []
        return moves
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
    def get_moveset(self,row,column,board):
        pass
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
    def get_moveset(self,row,column,board):
        pass
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
    def get_moveset(self,row,column,board):
        pass
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
    def get_moveset(self,row,column,board):
        pass
class Pawn(Piece):
    def __init__(self,colour):
        self.colour = colour
        self.role = None
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
    def get_moveset(self,row,column,board):
        pass