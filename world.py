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
This is where you work. \n'''


class Fireplace(MapTile):
    def intro_text(self):
        return '''
You can use Floo Powder here to get to Diagon Alley'''


class DiagonAlleyBottom(MapTile):
    def intro_text(self):
        return '''
This is the bottom end of Diagon Alley. \n'''

class DiagonAlleyTop(MapTile):
    def intro_text(self):
        return '''
This is the top end of Diagon Alley. \n'''


class KnockturnAlley(MapTile):
    def intro_text(self):
        return '''
This is the crime scene.'''


class SecretRoom(MapTile):
    def intro_text(self):
        return '''
Congratulations you have solved the crime'''


class PopupPotions(MapTile):
    def __init__(self, x, y):
        self.trader = Trader()
        super().__init__(x,y)
    
    def intro_text(self):
        print('''Trader: \n
Welcome to Pop-up Potions, \n
Your one stop shop for all your magical needs''')

    def trade(self, player):
        print(f'\nHere are my wares! \n')
        for i, item in enumerate(self.trader.inventory, 1):
            print(f'{i}. {item.name}: \n{wizard_money(item.value)}')
        while True:
            user_input = input("Choose an item number you wish to buy, or press 'Q' to exit my shop \n> ")
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
            print(f"You only have {player.inventory[2].value} knuts")
            return
        else:
            self.trader.inventory.remove(item)
            player.exchange_money(-item.value) # as buying, value needs to be negative
            print(f'Thank you for buying {item}')
            print(f'\nHere are my new wares! \n')
            for i, item in enumerate(self.trader.inventory, 1):
                print(f'{i}. {item.name}: \n{wizard_money(item.value)}')

# CREATING THE WORLD MAP

# xxxx|xxxx|.pot|shop|
#     |fire|DA-1|DA-2|
# xxxx|Home|xxxx|KTA |Vict|

#  00 | 10 | 20 | 30 |
#  01 | 11 | 21 | 31 |
#  02 | 12 | 22 | 32 | 42 |

world_map = [
    [None, None, PopupPotions(2,0), None, None],
    [None, Fireplace(1,1), DiagonAlleyTop(2,1), DiagonAlleyBottom(3,1), None],
    [None, StartTile(1,2), None, KnockturnAlley(3,2), SecretRoom(4,2)]
]

def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except:
        return None


if __name__ == "__main__":
    from player import Player

    my_player = Player()
    print(my_player.inventory[2]) #purse

    shop = PopupPotions(1,2)
    shop.intro_text()
    shop.trade(my_player)
