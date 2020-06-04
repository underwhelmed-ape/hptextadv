class Spell:
    def __init__(self):
        raise NotImplementedError("Do not create raw Spell objects")
    
    def __str__(self):
        return self.name


class Anteoculatia(Spell):
    def __init__(self):
        self.name = 'Anteoculatia'
        self.pronounce = 'an-tee-oh-kyoo-LAY-chee-ah'
        self.effect = 'Causes the target to grow antlers'
        self.damage = 0
        self.blockability = 0.2

class Expelliarmus(Spell):
    def __init__(self):
        self.name = 'Expelliarmus'
        self.pronounce = ' ex-PELL-ee-ARE-muss '
        self.effect = 'Disarming Charm'
        self.damage = None
        self.blockability = 0.8

class AvadaKedavra(Spell):
    def __init__(self):
        self.name = 'Avada Kedavra'
        self.pronounce = 'ah-VAH-dah keh-DAV-rah'
        self.effect = 'Death'
        self.damage = 1000
        self.blockability = 0


class Aguamenti(Spell):
    def __init__(self):
        self.name = 'Aguamenti'
        self.pronounce = 'AH-gwah-MEN-tee'
        self.effect = 'Produces a clean, drinkable jet of water from the wand tip.'
        self.damage = 0
        self.blockability = 0.2


