from money_exchange import wizard_money




class Item:
    def __init__(self):
        raise NotImplementedError('Do not create raw Item objects')

    def __str__(self):
        return self.name

class Purse(Item):
    def __init__(self):
        self.name = "Standard Purse"
        self.description = "A standard sized purse with all your money.\nThis purse only holds 15 Galleons"
        self.value = 670
    
    def purse_contents(self):
        return wizard_money(self.value)

    def __str__(self):
        return f'{self.name} \n{self.purse_contents()}'




class Pocket_Knife(Item):
    def __init__(self):
        self.name = "A small Pocket Knife"
        self.description = "This looks ordinary but looks can be deceiving"
        self.value = 200


class Sneakoscope(Item):
    def __init__(self):
        self.name = "A basic Sneakoscope"
        self.description = "Useful for detecting untrustworthy people around you"
        self.cost = 800
        self.enabled = False

class BasicPotionsKit(Item):
    def __init__(self):
        self.name = "Basic Potions Kit"
        self.description = "This lightweight kit is useful for whipping up emergency antidotes and poisons"
        self.cost = 1200





if __name__ == "__main__":
    from items import Purse

    purse = Purse()
    purse.value = 200
    print(purse.purse_contents())

    purse.value += -60
    print(purse.purse_contents())

    print(purse)