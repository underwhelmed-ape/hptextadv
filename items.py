class Weapon:
    def __str__(self):
        return self.name

class Wand(Weapon):
    def __init__(self):
        self.name = "This is your wand, it chose you."
        self.description = "This is your most important tool, look after it!! You cannot do magic without it"

class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A fist-sized rock, for bludgeoning"
        self.damage = 5

class Dagger(Weapon):
    def __init__(self):
        self.name = "Dagger"
        self.description = "A worn looking dagger"
        self.damage = 10

#class HealingPotion(Consumable):
#    def __init__(self):
#        self.name = "A basic Healing Potion"
#        self.healing_value = 50
#        self.value = 986 # 2G 0S 0K



class Item:
    def __str__(self):
        return self.name


class Purse(Item):
    def __init__(self):
        self.name = "A standard sized purse with all your money"
        self.description = "This purse only holds 15 Galleons"
        self.value = 0


class Pocket_Knife(Item):
    def __init__(self):
        self.name = "A small Pocket Knife"
        self.description = "This looks ordinary but looks can be deceiving"
        self.value = 200


class Sneakoscope(Item):
    def __init__(self):
        self.name = "A basic Sneakoscope"
        self.description = "Useful for detecting untrustworthy people around you"
        self.value = 800

class Potions_kit(Item):
    def __init__(self):
        self.name = "A portable potions kit for on the go antidotes"
        self.description = "This kit is useful for whipping up emergency antidotes and poisons"
        self.value = 1200
