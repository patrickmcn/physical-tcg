import os
from tkinter import *
import random
import time
import detect_color
from CardEffects import EnergyDrink, Caltrops, Disarm, Debilitate, Booster, Invigorate
class Cards:
    def __init__(self, name = "test", power = 0, type = "monster", color = None, effect = 0):
        self.name = name
        self.power = power
        self.imagefile = f"physical-tcg/images/{name}.png"
        self.type = type
        self.effect = effect 
        if color is None:
            self.color = "red" if type == "monster" else "blue"
        else:
            self.color = color

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
            self._imagefile = "physical-tcg/images/default.png"
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value):
        self._color = value
    @property
    def effect(self):
        return self._effect
    @effect.setter
    def effect(self, effect):
        self._effect = effect

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
    
    def __add__(self, other):
        combinedPower = self.power + other.power
        return combinedPower
    
    def applyEffect(self, target, currentLane, currentPlayer, lanes):
        if self.effect == "EnergyDrink":
            EnergyDrink(target)
        elif self.effect == "Caltrops":
            Caltrops(target)
        elif self.effect == "Booster":
            Booster(target)
        elif self.effect == "Disarm":
            Disarm(target) 
        elif self.effect == "Debilitate":
            Debilitate(target) 
        elif self.effect == "Invigorate":
            Invigorate(target) 


class Deck:
    def __init__(self):
        self.cards = []
        cards = [1, 2, 3, 4, 5] 
        self.cards.append(Cards("test", 2, "spell", "blue"))
        for num in range(11):
            power = random.choice(cards)
            self.cards.append(Cards(f"test{power}", power, "monster", "red"))

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

class Deck2(Deck):
    def __init__(self):
        super().__init__()
        self.cards = []
        cards = [1, 2, 3, 4, 5] 
        #self.cards.append(Cards("test", 2, "spell"))
        self.cards.append(Cards("spell06", 0, "spell", "blue", "EnergyDrink"))
        self.cards.append(Cards("spell01", 0, "spell", "blue", "Caltrops"))
        self.cards.append(Cards("spell04", 0, "spell", "blue", "Booster"))
        self.cards.append(Cards("spell05", 0, "spell", "blue", "Invigorate"))
        self.cards.append(Cards("spell03", 0, "spell", "blue", "Disarm"))
        self.cards.append(Cards("spell02", 0, "spell", "blue", "Debilitate"))
        self.cards.append(Cards("monster01", 2,  "monster", "red"))
        self.cards.append(Cards("monster02", 3,  "monster", "red"))
        self.cards.append(Cards("monster03", 3,  "monster", "red"))
        self.cards.append(Cards("monster04", 5,  "monster", "red"))
        self.cards.append(Cards("monster05", 4,  "monster", "red"))
        self.cards.append(Cards("monster06", 3,  "monster", "red"))
        self.cards.append(Cards("monster07", 4,  "monster", "red"))
        self.cards.append(Cards("monster08", 4,  "monster", "red"))
        self.cards.append(Cards("monster09", 4,  "monster", "red"))
        self.cards.append(Cards("monster10", 4,  "monster", "red"))
        self.cards.append(Cards("monster11", 2,  "monster", "red"))
        self.cards.append(Cards("monster12", 2,  "monster", "red"))
        self.cards.append(Cards("monster13", 4,  "monster", "red"))
        self.cards.append(Cards("monster14", 2,  "monster", "red"))
        self.cards.append(Cards("monster15", 4,  "monster", "red"))
        
        for num in range(11):
            power = random.choice(cards)
            self.cards.append(Cards(f"test{power}", power, "monster", "red"))


class MainGUI(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg = "white")
        self.p1deck = Deck()
        self.p2deck = Deck2()
        self.p1hand = []
        self.p2hand = []
        self.p1Lane1 = []
        self.p1Lane2 = []
        self.p1Lane3 = []
        self.p2Lane1 = []
        self.p2Lane2 = []
        self.p2Lane3 = []
        self.phase = 0
        self.p1Turn = True
        self.turnCount = 1
        self.playedMonster = False
        self.listofP1Locations = [self.p1Lane1, self.p1Lane2, self.p1Lane3]
        self.listofP2Locations = [self.p2Lane1, self.p2Lane2, self.p2Lane3]
        self.round = 1
        self.winners = []
        self.winsNeeded = 2
        self.roundResults = "Round Results:"
        self.setUpGUI()

    def putInHand(self, whoseturn):
        if(whoseturn == 1):
            card = self.p1deck.draw()
            self.p1hand.append(card)
        elif(whoseturn == 2):
            card = self.p2deck.draw()
            self.p2hand.append(card)
    
    def setUpGUI(self):
        for i in range(5):
            self.putInHand(1)
            self.putInHand(2)
        #print(self.p1hand)
        #print(self.p2hand)
        for row in range(5):
            Grid.rowconfigure(self, row, weight = 1)
            
            for col in range(4):
                Grid.rowconfigure(self, col, weight =1)
        
        p2c1 = self.p2hand[0].imagefile
        img = PhotoImage(file = p2c1)
        self.p2Card1 = Menubutton(self, image= img, bg = "black")
        self.p2Card1.image = img
        self.p2Card1.grid(row = 0, column = 0)

        self.p2Card1.menu =Menu(self.p2Card1, tearoff=0)
        self.p2Card1["menu"] = self.p2Card1.menu

        buttonFrame = Frame(self)
        buttonFrame.grid(row=1, column=0)

        self.p2Card1.menu.add_command(label= " Lane 1", command= lambda: self.playLane(self.p1Turn, 0, 1, 2) )
        self.p2Card1.menu.add_command(label= " Lane 2", command= lambda: self.playLane(self.p1Turn, 0, 2, 2) )
        self.p2Card1.menu.add_command(label= " Lane 3", command= lambda: self.playLane(self.p1Turn, 0, 3, 2) )
        scanP1Button = Button(buttonFrame, text="Scan P1 Card", command=lambda: self.openScanDialog(1), font=("TkDefaultFont", 18))
        scanP1Button.pack(padx=5, pady=5)
    
        scanP2Button = Button(buttonFrame, text="Scan P2 Card", command=lambda: self.openScanDialog(2), font=("TkDefaultFont", 18))
        scanP2Button.pack(padx=5, pady=5)
        

        p2c2 = self.p2hand[1].imagefile
        img = PhotoImage(file = p2c2)
        self.p2Card2 = Menubutton(self, image= img, bg = "black")
        self.p2Card2.image = img
        self.p2Card2.grid(row = 0, column = 1)

        self.p2Card2.menu = Menu(self.p2Card2, tearoff= 0)
        self.p2Card2["menu"] = self.p2Card2.menu

        self.p2Card2.menu.add_command(label= " Lane 1", command= lambda: self.playLane(self.p1Turn, 1, 1, 2) )
        self.p2Card2.menu.add_command(label= " Lane 2", command= lambda: self.playLane(self.p1Turn, 1, 2, 2) )
        self.p2Card2.menu.add_command(label= " Lane 3", command= lambda: self.playLane(self.p1Turn, 1, 3, 2) )

        p2c3 = self.p2hand[2].imagefile
        img = PhotoImage(file = p2c3)
        self.p2Card3 = Menubutton(self, image= img, bg = "black")
        self.p2Card3.image = img
        self.p2Card3.grid(row = 0, column = 2)

        self.p2Card3.menu =Menu(self.p2Card3, tearoff=0)
        self.p2Card3["menu"] = self.p2Card3.menu

        self.p2Card3.menu.add_command(label= " Lane 1", command= lambda: self.playLane(self.p1Turn, 2, 1, 2) )
        self.p2Card3.menu.add_command(label= " Lane 2", command= lambda: self.playLane(self.p1Turn, 2, 2, 2) )
        self.p2Card3.menu.add_command(label= " Lane 3", command= lambda: self.playLane(self.p1Turn, 2, 3, 2) )

        p2c4 = self.p2hand[3].imagefile
        img = PhotoImage(file = p2c4)
        self.p2Card4 = Menubutton(self, image= img, bg = "black")
        self.p2Card4.image = img
        self.p2Card4.grid(row = 0, column = 3)

        self.p2Card4.menu =Menu(self.p2Card4, tearoff=0)
        self.p2Card4["menu"] = self.p2Card4.menu

        self.p2Card4.menu.add_command(label= " Lane 1", command= lambda: self.playLane(self.p1Turn, 3, 1, 2) )
        self.p2Card4.menu.add_command(label= " Lane 2", command= lambda: self.playLane(self.p1Turn, 3, 2, 2) )
        self.p2Card4.menu.add_command(label= " Lane 3", command= lambda: self.playLane(self.p1Turn, 3, 3, 2) )

        p2c5 = self.p2hand[4].imagefile
        img = PhotoImage(file = p2c5)
        self.p2Card5 = Menubutton(self, image= img, bg = "black")
        self.p2Card5.image = img
        self.p2Card5.grid(row = 0, column = 4)

        self.p2Card5.menu =Menu(self.p2Card5, tearoff=0)
        self.p2Card5["menu"] = self.p2Card5.menu

        self.p2Card5.menu.add_command(label= " Lane 1", command= lambda: self.playLane(self.p1Turn, 4, 1, 2) )
        self.p2Card5.menu.add_command(label= " Lane 2", command= lambda: self.playLane(self.p1Turn, 4, 2, 2) )
        self.p2Card5.menu.add_command(label= " Lane 3", command= lambda: self.playLane(self.p1Turn, 4, 3, 2) )

        p2l1 = "physical-tcg/images/p2l1.png"
        img = PhotoImage(file= p2l1)
        self.player2Lane1 = Label(self, image= img, bg = "black")
        self.player2Lane1.image = img
        self.player2Lane1.grid(row = 1,column = 1 )

        p2l2 = "physical-tcg/images/p2l2.png"
        img = PhotoImage(file= p2l2)
        self.player2Lane2 = Label(self, image= img)
        self.player2Lane2.image = img
        self.player2Lane2.grid(row = 1,column = 2 )

        p2l3 = "physical-tcg/images/p2l3.png"
        img = PhotoImage(file= p2l3)
        self.player2Lane3 = Label(self, image= img)
        self.player2Lane3.image = img
        self.player2Lane3.grid(row = 1,column = 3 )

        self.winnersSoFar = Label(self, text = self.roundResults)
        self.winnersSoFar.grid(row = 1, column = 4)

        self.turnNum= Label(self, text = f"{"Player 1" if self.p1Turn else "Player 2"}\nTurn {self.turnCount}")
        self.turnNum.grid(row = 2, column = 0)
        
        lane1 = Label(self, text = "Lane 1", font=("TkDefaultFont",40))
        lane1.grid(row = 2, column = 1 )

        lane2 = Label(self, text = "Lane 2", font=("TkDefaultFont",40))
        lane2.grid(row = 2, column = 2 )

        lane3 = Label(self, text = "Lane 3", font=("TkDefaultFont",40))
        lane3.grid(row = 2, column = 3 )

        nextButton = Button(self, text = "Next Phase", command = lambda: self.turnProgression(), font=("TkDefaultFont",20))
        nextButton.grid(row = 2, column = 4)

        p1l1 = "physical-tcg/images/p1l1.png"
        img = PhotoImage(file= p1l1)
        self.player1Lane1 = Label(self, image= img, bg = "black")
        self.player1Lane1.image = img
        self.player1Lane1.grid(row = 3,column = 1 )

        p1l2 = "physical-tcg/images/p1l2.png"
        img = PhotoImage(file= p1l2)
        self.player1Lane2 = Label(self, image= img)
        self.player1Lane2.image = img
        self.player1Lane2.grid(row = 3,column = 2)

        p1l3 = "physical-tcg/images/p1l3.png"
        img = PhotoImage(file= p1l3)
        self.player1Lane3 = Label(self, image= img)
        self.player1Lane3.image = img
        self.player1Lane3.grid(row = 3,column = 3)

        self.roundLabel = Label(self, text = f"Best of {self.winsNeeded + 1}\nRound {self.round}")
        self.roundLabel.grid(row = 3, column = 4 )

        p1c1 = self.p1hand[0].imagefile
        img = PhotoImage(file = p1c1)
        self.p1Card1 = Menubutton(self, image= img, bg = "black")
        self.p1Card1.image = img
        self.p1Card1.grid(row = 4, column = 0)

        self.p1Card1.menu =Menu(self.p1Card1, tearoff=0)
        self.p1Card1["menu"] = self.p1Card1.menu

        self.p1Card1.menu.add_command(label= " Lane 1", command= lambda: self.playLane(self.p1Turn, 0, 1, 1) )
        self.p1Card1.menu.add_command(label= " Lane 2", command= lambda: self.playLane(self.p1Turn, 0, 2, 1) )
        self.p1Card1.menu.add_command(label= " Lane 3", command= lambda: self.playLane(self.p1Turn, 0, 3, 1) )

        p1c2 = self.p1hand[1].imagefile
        img = PhotoImage(file = p1c2)
        self.p1Card2 = Menubutton(self, image= img, bg = "black")
        self.p1Card2.image = img
        self.p1Card2.grid(row = 4, column = 1)

        self.p1Card2.menu =Menu(self.p1Card2, tearoff=0)
        self.p1Card2["menu"] = self.p1Card2.menu

        self.p1Card2.menu.add_command(label= " Lane 1", command= lambda: self.playLane(self.p1Turn, 1, 1, 1) )
        self.p1Card2.menu.add_command(label= " Lane 2", command= lambda: self.playLane(self.p1Turn, 1, 2, 1) )
        self.p1Card2.menu.add_command(label= " Lane 3", command= lambda: self.playLane(self.p1Turn, 1, 3, 1) )

        p1c3 = self.p1hand[2].imagefile
        img = PhotoImage(file = p1c3)
        self.p1Card3 = Menubutton(self, image= img, bg = "black")
        self.p1Card3.image = img
        self.p1Card3.grid(row = 4, column = 2)

        self.p1Card3.menu =Menu(self.p1Card3, tearoff=0)
        self.p1Card3["menu"] = self.p1Card3.menu

        self.p1Card3.menu.add_command(label= " Lane 1", command= lambda: self.playLane(self.p1Turn, 2, 1, 1) )
        self.p1Card3.menu.add_command(label= " Lane 2", command= lambda: self.playLane(self.p1Turn, 2, 2, 1) )
        self.p1Card3.menu.add_command(label= " Lane 3", command= lambda: self.playLane(self.p1Turn, 2, 3, 1) )

        p1c4 = self.p1hand[3].imagefile
        img = PhotoImage(file = p1c4)
        self.p1Card4 = Menubutton(self, image= img, bg = "black")
        self.p1Card4.image = img
        self.p1Card4.grid(row = 4, column = 3)

        self.p1Card4.menu =Menu(self.p1Card4, tearoff=0)
        self.p1Card4["menu"] = self.p1Card4.menu

        self.p1Card4.menu.add_command(label= " Lane 1", command= lambda: self.playLane(self.p1Turn, 3, 1, 1) )
        self.p1Card4.menu.add_command(label= " Lane 2", command= lambda: self.playLane(self.p1Turn, 3, 2, 1) )
        self.p1Card4.menu.add_command(label= " Lane 3", command= lambda: self.playLane(self.p1Turn, 3, 3, 1) )

        p1c5 = self.p1hand[4].imagefile
        img = PhotoImage(file = p1c5)
        self.p1Card5 = Menubutton(self, image= img, bg = "black")
        self.p1Card5.image = img
        self.p1Card5.grid(row = 4, column = 4)

        self.p1Card5.menu =Menu(self.p1Card5, tearoff=0)
        self.p1Card5["menu"] = self.p1Card5.menu

        self.p1Card5.menu.add_command(label= " Lane 1", command= lambda: self.playLane(self.p1Turn, 4, 1, 1) )
        self.p1Card5.menu.add_command(label= " Lane 2", command= lambda: self.playLane(self.p1Turn, 4, 2, 1) )
        self.p1Card5.menu.add_command(label= " Lane 3", command= lambda: self.playLane(self.p1Turn, 4, 3, 1) )

        self.display = Label(self, text = "blank", anchor = "center")
        self.display.grid(row = 3, column = 0 )

        self.pack(side = "bottom",fill = BOTH, expand = 1)
    
    def drawPhase(self):
        self.playedMonster = False
        if (self.p1Turn):
            for i in range(len(self.p1hand)):
                if(self.p1hand[i].name == "default"):
                    self.p1hand.pop(i)
                    card = self.p1deck.draw()
                    self.p1hand.insert(i, card)
                    img = PhotoImage(file = self.p1hand[i].imagefile)
                    if(i == 0):
                        self.p1Card1.configure(image =img)
                        self.p1Card1.image = img
                    if(i == 1):
                        self.p1Card2.configure(image =img)
                        self.p1Card2.image = img
                    if(i == 2):
                        self.p1Card3.configure(image =img)
                        self.p1Card3.image = img
                    if(i == 3):
                        self.p1Card4.configure(image =img)
                        self.p1Card4.image = img
                    if(i == 4):
                        self.p1Card5.configure(image =img)
                        self.p1Card5.image = img
        if (self.p1Turn == False):
            for i in range(len(self.p2hand)):
                if(self.p2hand[i].name == "default"):
                    self.p2hand.pop(i)
                    card = self.p2deck.draw()
                    self.p2hand.insert(i, card)
                    img = PhotoImage(file = self.p2hand[i].imagefile)
                    if(i == 0):
                        self.p2Card1.configure(image =img)
                        self.p2Card1.image = img
                    if(i == 1):
                        self.p2Card2.configure(image =img)
                        self.p2Card2.image = img
                    if(i == 2):
                        self.p2Card3.configure(image =img)
                        self.p2Card3.image = img
                    if(i == 3):
                        self.p2Card4.configure(image =img)
                        self.p2Card4.image = img
                    if(i == 4):
                        self.p2Card5.configure(image =img)
                        self.p2Card5.image = img



    def turnProgression(self):
        if(self.turnCount > 5):
            #print("end")
            self.endGame()
            return ""
        if (self.turnCount >= 1):
            self.drawPhase()
        if ( self.p1Turn == True):
            self.p1Turn = False
            self.turnCount += 1
            self.turnNum.configure(text = f"{"Player 1" if self.p1Turn else "Player 2"}\nTurn {self.turnCount}")
        elif(self.p1Turn == False):
            self.p1Turn = True
            self.turnCount += 1
            self.turnNum.configure(text = f"{"Player 1" if self.p1Turn else "Player 2"}\nTurn {self.turnCount}")
           

    def handManager(self, isP1Turn, handslot):
        img = PhotoImage(file = "physical-tcg/images/default.png")
        if (isP1Turn == True):
            if(handslot == 0):
                self.p1Card1.configure(image =img)
                self.p1Card1.image = img
            if(handslot == 1):
                self.p1Card2.configure(image =img)
                self.p1Card2.image = img
            if(handslot == 2):
                self.p1Card3.configure(image =img)
                self.p1Card3.image = img
            if(handslot == 3):
                self.p1Card4.configure(image =img)
                self.p1Card4.image = img
            if(handslot == 4):
                self.p1Card5.configure(image =img)
                self.p1Card5.image = img
        if (isP1Turn == False):
            if(handslot == 0):
                self.p2Card1.configure(image =img)
                self.p2Card1.image = img
            if(handslot == 1):
                self.p2Card2.configure(image =img)
                self.p2Card2.image = img
            if(handslot == 2):
                self.p2Card3.configure(image =img)
                self.p2Card3.image = img
            if(handslot == 3):
                self.p2Card4.configure(image =img)
                self.p2Card4.image = img
            if(handslot == 4):
                self.p2Card5.configure(image =img)
                self.p2Card5.image = img

    def playSpell(self,isP1Turn, handslot, lane):
        if(isP1Turn):
            if(lane == 1):
                try:
                    self.p1Lane1[0].power += self.p1hand[handslot].power
                    self.p1hand.pop(handslot)
                    self.p1hand.insert(handslot, Cards("default"))
                    self.handManager(isP1Turn, handslot)
                except:
                    print("no monster card here")
                    self.display.configure(text = "no monster card here")
            if(lane == 2):
                try:
                    self.p1Lane2[0].power += self.p1hand[handslot].power
                    self.p1hand.pop(handslot)
                    self.p1hand.insert(handslot, Cards("default"))
                    self.handManager(isP1Turn, handslot)
                except:
                    print("no monster card here")
                    self.display.configure(text = "no monster card here")
            if(lane == 3):
                try:
                    self.p1Lane3[0].power += self.p1hand[handslot].power
                    self.p1hand.pop(handslot)
                    self.p1hand.insert(handslot, Cards("default"))
                    self.handManager(isP1Turn, handslot)
                except:
                    print("no monster card here")
                    self.display.configure(text = "no monster card here")
        if(isP1Turn == False):
            if(lane == 1):
                try:
                    self.p2Lane1[0].power += self.p1hand[handslot].power
                    self.p2hand.pop(handslot)
                    self.p2hand.insert(handslot, Cards("default"))
                    self.handManager(isP1Turn, handslot)
                except:
                    print("no monster card here")
                    self.display.configure(text = "no monster card here")
            if(lane == 2):
                try:
                    self.p2Lane2[0].power += self.p1hand[handslot].power
                    self.p2hand.pop(handslot)
                    self.p2hand.insert(handslot, Cards("default"))
                    self.handManager(isP1Turn, handslot)
                except:
                    print("no monster card here")
                    self.display.configure(text = "no monster card here")
            if(lane == 3):
                try:
                    self.p2Lane3[0].power += self.p1hand[handslot].power
                    self.p2hand.pop(handslot)
                    self.p2hand.insert(handslot, Cards("default"))
                    self.handManager(isP1Turn, handslot)
                except:
                    print("no monster card here")
                    self.display.configure(text = "no monster card here")
        return ""
        
    def playLane(self,isP1Turn, handslot, lane, turnCheck):
        if (turnCheck == 2 and isP1Turn == True):
            self.display.configure(text = "you cant play P2 cards on P1's turn")
            return ""
        
        elif(turnCheck == 1 and isP1Turn == False):
            self.display.configure(text = "you cant play P1 cards on P2's turn")
            return ""
        
        if (self.p1hand[handslot].name == "default" and isP1Turn == True):
            print("no card here")
            self.display.configure(text = "no card here")
            return ""
        
        if (self.p2hand[handslot].name == "default" and isP1Turn == False):
            print("no card here")
            self.display.configure(text = "no card here")
            return ""
        
        if(self.p1hand[handslot].type == "spell" and turnCheck == 1):
            self.playSpell(isP1Turn, handslot, lane)
            return ""
        
        if(len(self.listofP1Locations[lane - 1]) >= 1 and turnCheck == 1):
            self.display.configure(text = "There is already a card here play somewhere else")
            return ""
        
        if(len(self.listofP2Locations[lane - 1]) >= 1 and turnCheck == 2):
            self.display.configure(text = "There is already a card here play somewhere else")
            print(len(self.listofP2Locations[lane - 1]))
            print(self.listofP2Locations[lane - 1])
            return ""
        
        if(self.playedMonster == True):
            print("already played a monster this turn")
            self.display.configure(text = "already played a monster this turn")
            return ""
        
        self.playedMonster = True
        if(lane == 1):
            if (isP1Turn == True and len(self.p1Lane1) < 1):
                self.p1Lane1.append(self.p1hand[handslot])
                self.p1hand.pop(handslot)
                self.p1hand.insert(handslot, Cards("default"))
                self.handManager(isP1Turn, handslot)
                img = PhotoImage(file = self.p1Lane1[0].imagefile)
                self.player1Lane1.configure(image =img)
                self.player1Lane1.image = img
            if (isP1Turn == False and len(self.p2Lane1) < 1):
                self.p2Lane1.append(self.p2hand[handslot])
                self.p2hand.pop(handslot)
                self.p2hand.insert(handslot, Cards("default"))
                self.handManager(isP1Turn, handslot)
                img = PhotoImage(file = self.p2Lane1[0].imagefile)
                self.player2Lane1.configure(image =img)
                self.player2Lane1.image = img
        elif(lane == 2):
            if (isP1Turn == True and len(self.p1Lane2) < 1):
                self.p1Lane2.append(self.p1hand[handslot])
                self.p1hand.pop(handslot)
                self.p1hand.insert(handslot, Cards("default"))
                self.handManager(isP1Turn, handslot)
                img = PhotoImage(file = self.p1Lane2[0].imagefile)
                self.player1Lane2.configure(image =img)
                self.player1Lane2.image = img
            if (isP1Turn == False and len(self.p2Lane2) < 1):
                self.p2Lane2.append(self.p2hand[handslot])
                self.p2hand.pop(handslot)
                self.p2hand.insert(handslot, Cards("default"))
                self.handManager(isP1Turn, handslot)
                img = PhotoImage(file = self.p2Lane2[0].imagefile)
                self.player2Lane2.configure(image =img)
                self.player2Lane2.image = img
        elif(lane ==3):    
            if (isP1Turn == True and len(self.p1Lane3) < 1):
                self.p1Lane3.append(self.p1hand[handslot])
                self.p1hand.pop(handslot)
                self.p1hand.insert(handslot, Cards("default"))
                self.handManager(isP1Turn, handslot)
                img = PhotoImage(file = self.p1Lane3[0].imagefile)
                self.player1Lane3.configure(image =img)
                self.player1Lane3.image = img
            if (isP1Turn == False and len(self.p2Lane3) < 1):
                self.p2Lane3.append(self.p2hand[handslot])
                self.p2hand.pop(handslot)
                self.p2hand.insert(handslot, Cards("default"))
                self.handManager(isP1Turn, handslot)
                img = PhotoImage(file = self.p2Lane3[0].imagefile)
                self.player2Lane3.configure(image =img)
                self.player2Lane3.image = img
    
    def scanCard(self, player, handPosition):
        cardColor = detect_color.detectColor()
        deck = self.p1deck if player == 1 else self.p2deck
        hand = self.p1hand if player == 1 else self.p2hand
        cardType = "monster" if cardColor == "red" else "spell"
        match = [card for card in deck.cards if card.color == cardColor]
        if match:
            scannedCard = match[0]
            deck.cards.remove(scannedCard)
            oldCard = hand[handPosition]
            hand[handPosition] = scannedCard
            self.updateHandDisplay(player == 1, handPosition)
            self.display.configure(text = f"Scanned {cardColor} {cardType} card: {scannedCard.name}")
        else:
            self.display.configure(text = f"No {cardColor} cards remaining in deck")

    def updateHandDisplay(self, isP1Turn, handslot):
        if isP1Turn:
            card = self.p1hand[handslot]
            img = PhotoImage(file=card.imagefile)
            if handslot == 0:
                self.p1Card1.configure(image=img)
                self.p1Card1.image = img
            elif handslot == 1:
                self.p1Card2.configure(image=img)
                self.p1Card2.image = img
            elif handslot == 2:
                self.p1Card3.configure(image=img)
                self.p1Card3.image = img
            elif handslot == 3:
                self.p1Card4.configure(image=img)
                self.p1Card4.image = img
            elif handslot == 4:
                self.p1Card5.configure(image=img)
                self.p1Card5.image = img
        else:
            card = self.p2hand[handslot]
            img = PhotoImage(file=card.imagefile)
            if handslot == 0:
                self.p2Card1.configure(image=img)
                self.p2Card1.image = img
            elif handslot == 1:
                self.p2Card2.configure(image=img)
                self.p2Card2.image = img
            elif handslot == 2:
                self.p2Card3.configure(image=img)
                self.p2Card3.image = img
            elif handslot == 3:
                self.p2Card4.configure(image=img)
                self.p2Card4.image = img
            elif handslot == 4:
                self.p2Card5.configure(image=img)
                self.p2Card5.image = img

    def openScanDialog(self, player):
        dialog = Toplevel(self)
        dialog.title(f"Scan Card")
        Label(dialog, text = "Choose position to place scanned card:").pack(pady=5)

        for i in range(5):
            Button(dialog, text = f"Position {i + 1}", command = lambda pos = i: [self.scanCard(player, pos), dialog.destroy()]).pack(pady=2)
        Button(dialog, text = "Cancel", command = dialog.destroy).pack(pady=5)

    def resetLanes(self):
        listOfLanes = [self.player1Lane1, self.player1Lane2, self.player1Lane3, self.player2Lane1, self.player2Lane2, self.player2Lane3]
        listOfLaneImages = []
        for player in range(1,3):
            for i in range(1,4):
                listOfLaneImages.append(f"physical-tcg/images/p{player}l{i}.png")
        for i in range(0,6):
            img = PhotoImage(file = listOfLaneImages[i])
            listOfLanes[i].configure(image = img)
            listOfLanes[i].image = img

    def resetHand(self):
        for i in range(5):
            self.putInHand(1)
            self.putInHand(2)
        listOfP1Hand = [self.p1Card1, self.p1Card2, self.p1Card3, self.p1Card4, self.p1Card5]
        listOfP2Hand = [self.p2Card1, self.p2Card2, self.p2Card3, self.p2Card4, self.p2Card5]
        for i in range (5):
            img = PhotoImage(file = self.p1hand[i].imagefile )
            listOfP1Hand[i].configure(image = img)
            listOfP1Hand[i].image = img
            img = PhotoImage(file = self.p2hand[i].imagefile )
            listOfP2Hand[i].configure(image = img)
            listOfP2Hand[i].image = img
        

    def roundReset(self):
        self.round += 1
        self.p1deck = Deck()
        self.p2deck = Deck2()
        self.p1hand = []
        self.p2hand = []
        self.p1Lane1.pop()
        self.p1Lane2.pop()
        self.p1Lane3.pop()
        self.p2Lane1.pop()
        self.p2Lane2.pop()
        self.p2Lane3.pop()
        self.phase = 0
        self.p1Turn = True
        self.turnCount = 1
        self.playedMonster = False
        self.roundLabel.configure(text = f"Best of {self.winsNeeded + 1}\nRound {self.round}")
        self.turnNum.configure(text = f"{"Player 1" if self.p1Turn else "Player 2"}\nTurn {self.turnCount}")
        self.resetLanes()
        self.resetHand()




    def endGame(self):
        listOfP1Power = []
        try:
            listOfP1Power.append(self.p1Lane1[0].power)
        except:
            pass
        try:
            listOfP1Power.append(self.p1Lane2[0].power)
        except:
            pass
        try:
            listOfP1Power.append(self.p1Lane3[0].power)
        except:
            pass
        
        #print(listOfP1Power)
        p1Points = sum(listOfP1Power)

        listOfP2Power = []
        try:
            listOfP2Power.append(self.p2Lane1[0].power)
        except:
            pass
        try:
            listOfP2Power.append(self.p2Lane2[0].power)
        except:
            pass
        try:
            listOfP2Power.append(self.p2Lane3[0].power)
        except:
            pass
        
        #print(listOfP2Power)
        p2Points = sum(listOfP2Power)    
            
        if(p1Points > p2Points):
            print(f"Player 1 won round {self.round} {p1Points} to {p2Points}")
            self.display.configure(text = f"Player 1 won round {self.round} {p1Points} to {p2Points}")
            self.winners.append("P1win")
            self.roundResults += f"\nRound {self.round}: P1"
            self.winnersSoFar.configure(text = self.roundResults)
            
        elif(p1Points < p2Points):
            print(f"Player 2 won round {self.round} {p2Points} to {p1Points}")
            self.display.configure(text = f"Player 2 won round {self.round} {p2Points} to {p1Points}")
            self.winners.append("P2win")
            self.roundResults += f"\nRound {self.round}: P2"
            self.winnersSoFar.configure(text = self.roundResults)
            
        else:
            print(f"You Tied round {self.round} with {p1Points} points")
            self.display.configure(text = f"You Tied round {self.round} with {p1Points} points")
            self.winners.append("Tie")
            self.roundResults += f"\nRound {self.round}: Tie"
            self.winnersSoFar.configure(text = self.roundResults)
        #self.display.configure(text=)
        #time.sleep(2)
        if(self.winners.count("P1win") == self.winsNeeded ):
            print("P1 wins the game")
            self.display.configure(text = "P1 wins the game")
            self.quit()
        if(self.winners.count("P2win") == self.winsNeeded ):
            print("P2 wins the game")
            self.display.configure(text = "P2 wins the game")
            self.quit()
        if(self.round > ((self.round * 2) - 1)):
            print("Game ended in a tie")
            self.display.configure(text = "Game ended in a tie")
            self.quit()
        self.roundReset()
   

        

def gameScreen():
    #create window
    window = Tk()
    #set window title 
    window.title("Card Test")
    #generate the GUI
    p = MainGUI(window)
    #display the gut and wait for user interaction
    window.mainloop()
