import os
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
    
c1 = Cards()
c2 = Cards("guy", 7)
print(c1) 
print(c2)
print (c1 > c2)
c1.power = 4
print(c1)