class Weapon:
    def__init__(self):
        raise NotImplementedError("Do not create raw Weapon objects.")

    def__str__(self):
        return self.player_name

class Rock(Weapon):
    def__init__(self):
        self.name = "Rock"
        self.description = "A fist-sized rock, for bludgeoning"
        self.damage = 5

class HealingPotion(Consumable):
    def__init__(self):
        self.name = "A basic Healing Potion"
        self.healing_value = 50
        self.value = 986 # 2G 0S 0K
