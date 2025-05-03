from tkinter import *
from gameplayBasics import *

class StartGUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg = "white")
        self.setUpGUI()

    def setUpGUI(self):
        for row in range(2):
            Grid.rowconfigure(self, row, weight = 1)
            
            for col in range(2):
                Grid.rowconfigure(self, col, weight = 1)
         

        self.startButton = Button(self, text= "Start Game", command= self.startGame, font=("TkDefaultFont",20))
        self.startButton.grid(row= 1, column= 1 )

        self.test = Label(self, text= "Test", bg = "black", font=("TkDefaultFont",20))
        self.test.grid(row = 2, column = 2 )
        
        self.pack(side = "bottom",fill = BOTH, expand = 1)   
    def startGame(self):
        self.quit()
        gameScreen()

#create window
window2 = Tk()
#set window title 
window2.title("Start Screen")
#generate the GUI
p = StartGUI(window2)
#display the gut and wait for user interaction
window2.mainloop()