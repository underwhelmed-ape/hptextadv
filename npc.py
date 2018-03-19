# Adding in Non-playable Characters (npc)

import items

# Trader character
class NonPlayableCharacter():
    def__init__(self):
        raise NotImplementedError("Do not create raw NPC objects.")

    def__str__(self):
        return self.player_name

class Trader(NonPlayableCharacter):
    def__init__(self):
        self.name = "Trader"
        self.Money = 10000
        self.inventory = [items.HealingPotion()]
