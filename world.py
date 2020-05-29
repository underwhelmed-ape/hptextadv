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


class Fireplace(MapTile):
    def intro_text(self):
        return '''
        You can use Floo Powder here to get to Diagon Alley'''


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


class KnockturnAlley(MapTile):
    def intro_text(self):
        return '''
        This is the crime scene. '''


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
    print(tile_at(1,2))

    from player import Player

    my_player = Player()
    print(my_player.inventory[2]) #purse

    shop = PopupPotions(1,2)
    shop.intro_text()
    shop.trade(my_player)



# ###### MAP ######
# """
# # player starts at b2 (x)
#       1   2   3   4
#     -----------------
#     |   |   |   |   |  a
#     -----------------
#     |   | x |   |   |  b
#     -----------------
#     |   |   |   |   |  c
#     -----------------
#     |   |   |   |   |  d
#     -----------------

# """

# # constant variables set-up

# ZONENAME = ''
# DESCRIPTION = 'description'
# EXAMINATION = 'examine'
# SOLVED = 'False'
# UP = 'up', 'north'
# DOWN = 'down', 'south'
# LEFT = 'left', 'west'
# RIGHT = 'right', 'east'

# solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
#                 'b1': False, 'b2': False, 'b3': False, 'b4': False,
#                 'c1': False, 'c2': False, 'c3': False, 'c4': False,
#                 'd1': False, 'd2': False, 'd3': False, 'd4': False,
#                 }

# zonemap = {
#     'a1': {
#         ZONENAME: 'Town Market',
#         DESCRIPTION: 'A thriving market place where you can find many exotic and magical objects',
#         EXAMINATION: 'examine',
#         SOLVED: 'False',
#         UP: '',
#         DOWN: 'b1',
#         LEFT: '',
#         RIGHT: 'a2'
#     },
#     'a2': {
#         ZONENAME: 'Town Entrance',
#         DESCRIPTION: 'This is the main gate to the town',
#         EXAMINATION: 'examine',
#         SOLVED: 'False',
#         UP: '',
#         DOWN: 'b2',
#         LEFT: 'a1',
#         RIGHT: 'a3'
#     },
#     'a3': {
#         ZONENAME: 'Town Square',
#         DESCRIPTION: 'A great place for a meeting',
#         EXAMINATION: 'examine',
#         SOLVED: 'False',
#         UP: '',
#         DOWN: 'b3',
#         LEFT: 'a2',
#         RIGHT: 'a4'
#     },
#     'a4': {
#         ZONENAME: 'Town Hall',
#         DESCRIPTION: 'The home of bureaucracy',
#         EXAMINATION: 'examine',
#         SOLVED: 'False',
#         UP: '',
#         DOWN: 'b4',
#         LEFT: 'a3',
#         RIGHT: ''
#     },
#     'b1': {
#         ZONENAME: "",
#         DESCRIPTION: 'description',
#         EXAMINATION: 'examine',
#         SOLVED: 'False',
#         UP: 'a1',
#         DOWN: 'c1',
#         LEFT: '',
#         RIGHT: 'b2'
#     },
#     'b2': {
#         ZONENAME: 'Home',
#         DESCRIPTION: 'This is your home',
#         EXAMINATION: 'Your home looks as messy as always! You really should clean up.',
#         SOLVED: 'False',
#         UP: 'a2',
#         DOWN: 'c2',
#         LEFT: 'b1',
#         RIGHT: 'b3'
#     },
#     'b3': {
#         ZONENAME: "Forest",
#         DESCRIPTION: '',
#         EXAMINATION: 'examine',
#         SOLVED: 'False',
#         UP: 'a3',
#         DOWN: 'c3',
#         LEFT: 'b2',
#         RIGHT: 'b4'
#     },
#     'b4': {
#         ZONENAME: "Empty Shack",
#         DESCRIPTION: 'This house inside the forest was abandoned long ago ... it looks dangerous to enter ',
#         EXAMINATION: 'examine',
#         SOLVED: 'False',
#         UP: 'a4',
#         DOWN: 'c4',
#         LEFT: 'b3',
#         RIGHT: ''
#     },
#     'c1': {
#         ZONENAME: "The Dragon Tavern",
#         DESCRIPTION: '',
#         EXAMINATION: 'examine',
#         SOLVED: 'False',
#         UP: 'b1',
#         DOWN: 'd1',
#         LEFT: '',
#         RIGHT: 'c2'
#     },
#     'c2': {
#         ZONENAME: "",
#         DESCRIPTION: 'description',
#         EXAMINATION: 'examine',
#         SOLVED: 'False',
#         UP: 'b2',
#         DOWN: 'd2',
#         LEFT: 'c1',
#         RIGHT: 'c3'
#     },
#     'c3': {
#         ZONENAME: "",
#         DESCRIPTION: 'description',
#         EXAMINATION: 'examine',
#         SOLVED: 'False',
#         UP: 'b3',
#         DOWN: 'd3',
#         LEFT: 'c2',
#         RIGHT: 'c4'
#     },
#     'c4': {
#         ZONENAME: "",
#         DESCRIPTION: 'description',
#         EXAMINATION: 'examine',
#         SOLVED: 'False',
#         UP: 'b4',
#         DOWN: 'd4',
#         LEFT: 'c3',
#         RIGHT: ''
#     },
#     'd1': {
#         ZONENAME: "The Dragon Tavern",
#         DESCRIPTION: 'A popular local haunt. Bring your own glasses!',
#         EXAMINATION: 'examine',
#         SOLVED: 'False',
#         UP: 'c1',
#         DOWN: '',
#         LEFT: '',
#         RIGHT: 'd2'
#     },
#     'd2': {
#         ZONENAME: "",
#         DESCRIPTION: 'description',
#         EXAMINATION: 'examine',
#         SOLVED: 'False',
#         UP: 'c2',
#         DOWN: '',
#         LEFT: 'd1',
#         RIGHT: 'd3'
#     },
#     'd3': {
#         ZONENAME: "",
#         DESCRIPTION: 'description',
#         EXAMINATION: 'examine',
#         SOLVED: 'False',
#         UP: 'c3',
#         DOWN: '',
#         LEFT: 'd2',
#         RIGHT: 'd4'
#     },
#     'd4': {
#         ZONENAME: "",
#         DESCRIPTION: 'description',
#         EXAMINATION: 'examine',
#         SOLVED: 'False',
#         UP: 'c4',
#         DOWN: '',
#         LEFT: 'd3',
#         RIGHT: ''
#     }
# #    'd4': {
# #        ZONENAME: "",
# #        DESCRIPTION: 'description',
# #        EXAMINATION: 'examine',
# #        SOLVED: 'False',
# #        UP: 'up', 'north',
# #        DOWN: '',
# #        LEFT: 'left', 'west',
# #        RIGHT: 'right', 'east'
# #    }
# }