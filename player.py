from items import Pocket_Knife, Purse
from weapons import Wand
from money_exchange import wizard_money


###### Player Setup ######

# establishing state of main character
# this is a class used to store and initilise values of the player

class Player:
    def __init__(self):
        self.inventory = [Wand(),
                          Pocket_Knife(),
                          Purse()]
        self.name = '' # string of player's name
        self.house = '' # string of player's house in game
        self.subject = ''
        self.hp = 0 # int of hitpoints
        self.mp = 0 # int of magic points/energy
        self.status_effects = []
        self.location = 'b2'
        self.game_over = False


    def print_inventory(self):
        print("Inventory: ")
        for item in self.inventory:
            print(f'* {item}')

    
    def exchange_money(self, knuts):
        '''add or subtract money when receiving or spending money'''
        self.inventory[2].value += knuts
        print(f'You now have: \n{wizard_money(self.inventory[2].value)} \nin your wallet.')


if __name__ == "__main__":
    from player import Player

    player = Player()

    #player.print_inventory()
    print(player.inventory[2])
    
    player.exchange_money(600)