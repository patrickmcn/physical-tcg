import os
from tkinter import *
import random
class Cards:
    def __init__(self, name = "default", power = 0):
        self.name = name
        self.power = power
        self.imagefile = f"physical-tcg/images/{name}.png"

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

class Deck:
    def __init__(self):
        self.cards = []
        for num in range(0,10):
            self.cards.append(Cards())
    @property
    def cards (self):
        return self._cards
    
    @cards.setter
    def cards (self, value):
        self._cards = value
    
    # functions for the Deck class
    def shuffle (self):
        random.shuffle(self.cards)
    
    def draw (self):
        try:
            topCard = self.cards[0]
        except IndexError:
            return None
        self.cards.pop(0)
        return topCard

class MainGUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg = "white")
        self.p1deck = Deck()
        self.p2deck = Deck()
        self.p1hand = []
        self.p2hand = []
        self.setUpGUI()

    def putInHand(self):
        card = self.p1deck.draw()
        self.p1hand.append(card)
    
    def setUpGUI(self):
        for i in range(0,6):
            self.putInHand()
        for row in range(5):
            Grid.rowconfigure(self, row, weight = 1)
            
            for col in range(7):
                Grid.rowconfigure(self, col, weight =1)
        
        testOpp1 = "physical-tcg/images/3PowerCardSmall.png"
        img = PhotoImage(file = testOpp1)
        testCard = Button(self, image= img, bg = "black")
        testCard.image = img
        testCard.grid(row = 0, column = 0)

        lane1 = Label(self, text = "Lane 1")
        lane1.grid(row = 3, column = 2 )

        lane2 = Label(self, text = "Lane 2")
        lane2.grid(row = 3, column = 4 )

        lane3 = Label(self, text = "Lane 3")
        lane3.grid(row = 3, column = 6 )

        nextButton = Button(self, text = "Next Phase", command = print(self.p1deck.cards[1]))
        nextButton.grid(row =3, column = 7)

        testDraw = self.p1hand[0].imagefile
        img = PhotoImage(file = testDraw)
        testCard2 = Button(self, image= img, bg = "black")
        testCard2.image = img
        testCard2.grid(row = 5, column = 0)

        testDraw = self.p1hand[1].imagefile
        img = PhotoImage(file = testDraw)
        testCard2 = Button(self, image= img, bg = "black")
        testCard2.image = img
        testCard2.grid(row = 5, column = 4)
        
        testDraw = self.p1hand[2].imagefile
        img = PhotoImage(file = testDraw)
        testCard2 = Button(self, image= img, bg = "black")
        testCard2.image = img
        testCard2.grid(row = 5, column = 7)

        self.pack(side = "bottom",fill = BOTH, expand = 1)
    
    def play():
        pass


        
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