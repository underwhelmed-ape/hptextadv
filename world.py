from npc import Trader
from money_exchange import wizard_money

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError('Create a subclass instead')

class StartTile(MapTile):
    def intro_text(self):
        return '''
        Welcome to the Ministry of Magic. \n
        This is where you work. \n
        '''

class DiagonAlleyBottom(MapTile):
    def intro_text(self):
        return '''
        This is the bottom end of Diagon Alley. \n
        '''

class DiagonAlleyTop(MapTile):
    def intro_text(self):
        return '''
        This is the top end of Diagon Alley. \n
        '''

class PopupPotions(MapTile):
    def __init__(self, x, y):
        self.trader = Trader()
        super().__init__(x,y)
    
    def intro_text(self):
        print('''
Trader: \n
Welcome to Pop-up Potions, \n
Your one stop shop for all your magical needs
        ''')

    def trade(self, player):
        print(f'\nHere are my wares! \n')
        for i, item in enumerate(self.trader.inventory, 1):
            print(f'{i}. {item.name}: \n{wizard_money(item.value)}')
        while True:
            user_input = input("Choose an item number you wish to buy, or press 'Q' to exit my shop \n>")
            if user_input.lower() == 'q':
                print('Thank you for visting my shop!')
                return
            else:
                try:
                    choice = int(user_input)
                    if choice == 0:
                        print('Invalid number\n')
                    else:
                        to_swap = self.trader.inventory[choice - 1]
                        print(f'you chose: {to_swap}')
                        self.swap(to_swap, player)
                except ValueError:
                    print('Just tell me the number of the item you want to purchace!\n')
                except:
                    print('Invalid number\n')
    
    def swap(self, item, player):
        if item.value > player.inventory[2].value:
            print("You don't have enough Gold")
            return
        else:
            self.trader.inventory.remove(item)
            player.inventory[2].value -= item.value
            print(f'Thank you for buying {item}')
            print(f'\nHere are my new wares! \n')
            for i, item in enumerate(self.trader.inventory, 1):
                print(f'{i}. {item.name}: \n{wizard_money(item.value)}')




if __name__ == "__main__":
    from player import Player

    my_player = Player()
    print(my_player.inventory[2]) #purse

    shop = PopupPotions(1,2)
    shop.intro_text()
    shop.trade(my_player)
