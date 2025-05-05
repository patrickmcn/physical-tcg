from tkinter import *
from gameplayBasics import *

class StartGUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg = "white" )
        self.setUpGUI()
        self.roundsNeededToWin = 2

    def setUpGUI(self):
        for row in range(2):
            Grid.rowconfigure(self, row, weight = 1)
            
            for col in range(2):
                Grid.rowconfigure(self, col, weight = 1)
         

        self.startButton = Button(self, text= "Start Game", command = lambda: self.startGame(self.roundsNeededToWin), font=("TkDefaultFont",20))
        self.startButton.grid(row= 0, column= 1 )

        self.optionButton = Menubutton(self, text= "Settings", font=("TkDefaultFont",20))
        self.optionButton.grid(row = 1, column = 1 )

        self.optionButton.menu = Menu(self.optionButton, tearoff=0)
        self.optionButton["menu"] = self.optionButton.menu

        self.optionButton.menu.add_command(label = "Best of 1", command = lambda: self.setRoundNumber(1))
        self.optionButton.menu.add_command(label = "Best of 3", command = lambda: self.setRoundNumber(2))
        self.optionButton.menu.add_command(label = "Best of 5", command = lambda: self.setRoundNumber(3))



        self.quitGame = Button(self, text ="Quit Game", font=("TkDefaultFont",20), command = lambda: self.quit() )
        self.quitGame.grid(row = 2, column = 1 )
        
        self.pack(side = "bottom",fill = BOTH, expand = 1)   
    def startGame(self, rounds):
        gameScreen(rounds)

    def setRoundNumber(self, numOfRounds):
        self.roundsNeededToWin = numOfRounds


#create window
window2 = Tk()
#set window title 
window2.title("Start Screen")
#generate the GUI
p2 = StartGUI(window2)
#display the gut and wait for user interaction
window2.mainloop()