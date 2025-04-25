def EnergyDrink(target, amount = 2):
    if target and hasattr(target, 'power'):
        target.power += amount
        print(f"{target.name}'s power increased by {amount} to {target.power}")
        
def Caltrops(target, amount = 2):
    if target and hasattr(target, 'power'):
        target.power -= amount
        print(f"{target.name}'s power decreased by {amount} to {target.power}")
def AndresEffect(currentLane, currentPlayer, lanes, card, Buff= 3):
    emptyLanes= all(lane[currentPlayer] is None or laneIndex == currentLane for laneIndex, lane in enumerate(lanes) if laneIndex != currentLane)
    if emptyLanes:
        card.power += Buff
        print(f"{card.name} is alone, he gains {Buff} power and is ever stronger at {card.power}")
