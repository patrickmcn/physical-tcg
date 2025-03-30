import os
from tkinter import *
class Cards:
    def __init__(self, name = "default", power = 0):
        self.name = name
        self.power = power
        self.imagefile = f"images/{name}.png"

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if(isinstance(value, str)):
            self._name = value
        else:
            self._name = "default"

    @property
    def power(self):
        return self._power
    
    @power.setter
    def power(self, value):
        if(isinstance(value, int)):
            self._power = value
        else:
            self._power = 0

    @property
    def imagefile(self):
        return self._imagefile
    
    @imagefile.setter
    def imagefile(self, value):
        if(os.path.isfile(value)):
            self._imagefile = value
        else:
            self._imagefile = "images/default.png"

    def __str__(self):
        return f"{self.name} has {self.power} power"
    
    def __gt__(self, other):
        card1 = self.power
        card2 = other.power
        if (card1 > card2):
            return True
        return False
    
    def __lt__(self, other):
        card1 = self.power
        card2 = other.power
        if (card1 < card2):
            return True
        return False
    
    def __eq__(self, other):
        card1 = self.power
        card2 = other.power
        if(card1 == card2):
            return True
        return False

class MainGUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg = "white")
        self.setUpGUI()

    def setUpGUI(self):
        for row in range(3):
            Grid.rowconfigure(self, row, weight = 1)
            
            for col in range(5):
                Grid.rowconfigure(self, col, weight =1)
        
        testOpp1 = "physical-tcg/images/3PowerCard.png"
        img = PhotoImage(file = testOpp1)
        testCard = Label(self, image= img, bg = "black")
        testCard.image = img
        testCard.grid(row = 0, column = 1)

        self.pack(side = "bottom",fill = BOTH, expand = 1)

        
#create window
window = Tk()
#set window title 
window.title("Card Test")
#generate the GUI
p = MainGUI(window)
#display the gut and wait for user interaction
window.mainloop()

#c1 = Cards()
#c2 = Cards("guy", 7)
#print(c1) 
#print(c2)
#print (c1 > c2)
#c1.power = 4
#print(c1)