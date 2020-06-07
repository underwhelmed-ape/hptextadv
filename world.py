from npc import Trader
from enemies import FinalBoss
from money_exchange import wizard_money
from spells import Anteoculatia, AvadaKedavra, Expelliarmus, Aguamenti



class MapTile:
    def __init__(self, x, y, player):
        self.x = x
        self.y = y
        self.player = player
        self.times_visited = 0

    def intro_text(self):
        raise NotImplementedError('Create a subclass instead')


class StartTile(MapTile):
    def intro_text(self):
        return '''
You are in the Ministry of Magic.
There is a grand fireplace in front of you'''


class Fireplace(MapTile):
    def intro_text(self, player):
        print()
        return self.transport()

    def transport(self):
        print('This fireplace will take you to Diagon Alley \nWould you like to go? [y/n]')
        user_decision = input('> ')
        try:
            if user_decision.lower() == 'n':
                return
            elif user_decision.lower() == 'y':
                player.x = 2
                player.y = 1
        except:
            print('Just say yes[y] or no[n]!!')
            


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
    def __init__(self, x, y):
        self.final_boss = FinalBoss()
        self.spell_options = []

        super().__init__(x,y)

    def intro_text(self): 
        return f'''
You have found the culprit. \n
It is {final_boss.name}, a well known muggle baiter. \n
But it looks like he won't come quietly!!\n'''

    def fight(self, player):
        print("WW: You'll have to defeat me in a wizard's duel.")
        spell_options = []



class PopupPotions(MapTile):
    def __init__(self, x, y, player):
        self.trader = Trader()
        super().__init__(x, y, player)
    
    def intro_text(self):
        return '''Trader:
    Welcome to Pop-up Potions,
    Your one stop shop for all your magical needs.
    How can I help you today?'''

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
            print(f"You only have \n{player.inventory[2]}")
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

def world_map(player):
    return [
        [None, None, PopupPotions(2,0,player), None, None],
        [None, Fireplace(1,1,player), DiagonAlleyTop(2,1,player), DiagonAlleyBottom(3,1, player), None],
        [None, StartTile(1,2,player), None, KnockturnAlley(3,2,player), SecretRoom(4,2,player)]
    ]

# Locates a tile at a location
# This returns the location in the world, when the player moves
def tile_at(world_map, x, y):
    if x < 0 or y < 0:
        return None
    try:
        map = world_map()
        return map[y][x]
    except IndexError:
        return None


if __name__ == "__main__":
    #from player import Player

    print(tile_at(2,0))

    # my_player = Player()
    # print(my_player.inventory[2]) #purse

    # shop = PopupPotions(1,2)
    # shop.intro_text()
    # shop.trade(my_player)
