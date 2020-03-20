try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
from functools import partial
from GameMaster import GameMaster
import Roles as Roles
import Pieces as Pieces
import random

class MainWindow(tk.Frame):
    def __init__(self,parent,*args,**kwargs):
        tk.Frame.__init__(self,parent,*args,**kwargs)
        self.parent = parent
        self.pictures={"Peek":tk.PhotoImage(file="Icons/Peek.png")}

        new_window = tk.Toplevel(self.parent)
        self.dictionary_window = DictionaryWindow(new_window)
        self.setupWindow()
        self.gamemaster = GameMaster()
        
        self.chessboard = ChessboardFrame(self)
        self.message_board = MessageBoard(self)
        self.chessboard.grid_propagate(False)
        self.chessboard.grid(row=0,column=0,columnspan=8,rowspan=8)
        self.message_board.grid(row=7,column=8,columnspan=3,rowspan=3)
        self.setupButtons()        
    def setupWindow(self):
        # Set up screen width, height, placement of windows. Create dictionary window
        screen_width = self.parent.winfo_screenwidth()
        screen_height = self.parent.winfo_screenheight()*5//4
        x = screen_width//20
        y = screen_height//25
        self.parent.geometry('{}x{}+{}+{}'.format(screen_width*2//3,screen_height*2//3,x,y))
        self.parent.title("Salem Chess")
    def setupButtons(self):
        surrender_button = tk.Button(self,bg="red",\
            command=partial(self.toggle_surrender),text="Surrender",\
                height=1,width=10,font=("Courier",10))
        surrender_button.grid(row=0,column=10,columnspan=3,sticky="N")

        peek_button = tk.Button(self,bg="dark green",\
            command=partial(self.toggle_peek),\
                height=28,width=50,image=self.pictures["Peek"])
        peek_button.grid(row=0,column=8,columnspan=3,sticky="SW")

        ability_button = tk.Button(self,bg="yellow",\
            command=partial(self.toggle_ability),text="Ability",\
                height=1,width=10,font=("Courier",15))
        ability_button.grid(row=6,column=8,columnspan=3,sticky="N")

        graveyard_button = tk.Button(self,bg="purple3",\
            command=partial(self.toggle_graveyard),text="Graveyard",\
                height=1,width=10,font=("Courier",13))
        graveyard_button.grid(row=0,column=8,columnspan=3,sticky="S")
    def toggle_surrender(self):
        self.message_board.change_message(self.gamemaster.get_surrender_message())
    def toggle_graveyard(self):
        pass
    def toggle_peek(self):
        pass
    def toggle_ability(self):
        pass
class DictionaryWindow(tk.Frame):
    def __init__(self,parent,*args,**kwargs):
        tk.Frame.__init__(self,parent,*args,**kwargs)
        self.parent = parent
        self.setupWindow()
    def setupWindow(self):
        screen_width = self.parent.winfo_screenwidth()//3
        screen_height = self.parent.winfo_screenheight()*2//3
        x = screen_width*2 + screen_width//4
        y = screen_height//2
        self.parent.geometry('{}x{}+{}+{}'.format(screen_width*2//3,screen_height*2//3,x,y))
        self.parent.title("Dictionary")
class ChessboardFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self,parent,*args,**kwargs)
        self.parent = parent
        self.pictures = {"Rook":tk.PhotoImage(file="Icons/rook.png"),\
            "RookFilled":tk.PhotoImage(file="Icons/rook-filled.png"),\
            "KnightFilled":tk.PhotoImage(file="Icons/knight-filled.png"),\
            "BishopFilled":tk.PhotoImage(file="Icons/bishop-filled.png"),\
            "QueenFilled":tk.PhotoImage(file="Icons/queen-filled.png"),\
            "KingFilled":tk.PhotoImage(file="Icons/king-filled.png"),\
            "PawnFilled":tk.PhotoImage(file="Icons/pawn-filled.png"),\
            "Knight":tk.PhotoImage(file="Icons/knight.png"),\
            "Bishop":tk.PhotoImage(file="Icons/bishop.png"),\
            "Queen":tk.PhotoImage(file="Icons/queen.png"),\
            "King":tk.PhotoImage(file="Icons/king.png"),\
            "Pawn":tk.PhotoImage(file="Icons/pawn.png"),\
            "Empty":tk.PhotoImage(file="Icons/Empty.png")}
        self.tiles = [[[] for col in range(8)] for row in range(8)]
        self.initialize_board()
    def initialize_board(self):
        for row in range(8):
            for col in range(8):
                if (row%2==0)==(col%2==0):
                    tileColour="#4f3325"
                else:
                    tileColour="white"
                button = tk.Button(self.parent,bg=tileColour,\
                    command=partial(self.tile_click,row,col),\
                        width=9,height=4)
                button.grid(row=row,column=col,sticky="sewn")
                self.tiles[row][col] = button
    def tile_click(self,row,column):
        print(row,column)
class MessageBoard(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self,parent,*args,**kwargs)
        self.parent = parent
        self.label = tk.Label(self,text="",bg="white",height=5,width=38,\
            font=("Comic Sans",9),justify=tk.LEFT,anchor="nw")
        self.label.grid(row=0,rowspan=3)
    def change_message(self,string):
        self.label.config(text=string)
if __name__ == "__main__":
    root = tk.Tk()
    MainWindow(root).grid()
    root.mainloop()