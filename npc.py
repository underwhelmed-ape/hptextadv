# Adding in Non-playable Characters (npc)

import items

class Person:
    age = 21
    name = "Name"

    def birth_year():
        return 2018 - age

people = [Person(), Person(), Person()]

people[0].name = "Ed"

# Trader character
class NonPlayableCharacter():
    def__init__(self):
        raise NotImplementedError("Do not create raw NPC objects.")

    def__str__(self):
        return self.player_name

class Trader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Trader"
        self.Money = 10000
        self.inventory = [items.HealingPotion()]
