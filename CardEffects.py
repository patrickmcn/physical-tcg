def EnergyDrink(targetCard, amount = 2):
    if targetCard and hasattr(targetCard, 'power'):
        targetCard.power += amount
        print(f"{targetCard.name}'s power increased by {amount} to {targetCard.power}")
        
