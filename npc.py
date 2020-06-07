# Adding in Non-playable Characters (npc)

import items
import consumables


# Trader character
class NonPlayableCharacter():
    def __init__(self):
        raise NotImplementedError('Do not create raw NPC objects')

    def __str__(self):
        return self.name




class Trader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Trader"
        self.Money = 10000
        self.inventory = [
            consumables.BasicHealingPotion(),
            consumables.BasicHealingPotion(),
            items.Sneakoscope(),
            items.BasicPotionsKit()]


class Perkins(NonPlayableCharacter):
    def __init__(self):
        self.name = "Perkins"
