
class Consumable:
    def __str__(self):
        return self.name

class BasicHealingPotion(Consumable):
   def __init__(self):
       self.name = "A basic Healing Potion"
       self.healing_value = 50
       self.cost = 986

class KnightsBusTicket(Consumable):
    def __init__(self):
       self.name = "One ticket for the Knight's Bus"
       self.healing_value = 50
       self.cost = 319