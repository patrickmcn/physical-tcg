def EnergyDrink(target, amount = 2):
    if target and hasattr(target, 'power'):
        target.power += amount
        print(f"{target.name}'s power increased by {amount} to {target.power}")
        
def Caltrops(target, amount = 2):
    if target and hasattr(target, 'power'):
        target.power -= amount
        print(f"{target.name}'s power decreased by {amount} to {target.power}")
def Booster(target, amount = 1):
    if target and hasattr(target, 'power'):
        target.power += amount
        print(f"{target.name}'s power increased by {amount} to {target.power}")
def Disarm(target, amount = 1):
    if target and hasattr(target, 'power'):
        target.power -= amount
        print(f"{target.name}'s power decreased by {amount} to {target.power}")
def Debilitate(target, amount = 3):
    if target and hasattr(target, 'power'):
        target.power -= amount
        print(f"{target.name}'s power decreased by {amount} to {target.power}")
def Invigorate(target, amount = 3):
    if target and hasattr(target, 'power'):
        target.power += amount
        print(f"{target.name}'s power increased by {amount} to {target.power}")
    