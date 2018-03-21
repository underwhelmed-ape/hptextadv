class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def __str__(self):
        return self.player_name

class Rock(Weapon):
    def __init__(self):
        self.name = "Rock"
        self.description = "A fist-sized rock, for bludgeoning"
        self.damage = 5

#class HealingPotion(Consumable):
#    def __init__(self):
#        self.name = "A basic Healing Potion"
#        self.healing_value = 50
#        self.value = 986 # 2G 0S 0K
