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
        self.name = ''
        self.house = ''
        self.subject = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.x = 1
        self.y = 2
        self.game_over = False


    def print_inventory(self):
        print("Inventory: ")
        for item in self.inventory:
            print(f'* {item}')

    
    def exchange_money(self, knuts):
        '''add or subtract money when receiving or spending money'''
        self.inventory[2].value += knuts
        print(f'You now have: \n{wizard_money(self.inventory[2].value)} \nin your wallet.')

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
    
    def move_north(self):
        self.move(0,-1)

    def move_south(self):
        self.move(0,1)

    def move_east(self):
        self.move(-1,0)

    def move_west(self):
        self.move(1,0)
        


if __name__ == "__main__":
    from player import Player

    player = Player()

    #player.print_inventory()
    print(player.inventory[2])
    
    player.exchange_money(600)