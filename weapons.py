
class Weapon:
    def __str__(self):
        return self.name
        

class Wand(Weapon):
    def __init__(self):
        self.name = "Wand"
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