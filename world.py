from npc import Trader, Perkins
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

    def examine(self):
        raise NotImplementedError('Create a subclass instead')

    def __str__(self):
         return self.name




class StartTile(MapTile):
    def __init__(self, x, y, player):
        self.name = 'Ministry of Magic Entrance Hall'
        self.perkins = Perkins()
        
    
    def intro_text(self):
        return '''
You are in the Ministry of Magic.
It is a huge ornate corridor with a golden statue visible in the distance'''

    def talk(self, player):
        return f'''
Perkins: 
Hi {player.name}, we've been have a lot of trouble lately with a series of muggle baiting attacks. 
We need your help catching this individual before they do any more harm. 

We've received an owl about a bewitched item for sale in Knockturn Alley, it's currently attacking anyone who approaches it. 
We need you to stop this and see what you can find in the area.'''


class Fireplace(MapTile):
    def __init__(self, x, y, player):
        if player.x == 1 and player.y == 2:
            self.name = 'Entrance Hall Fireplace'
        if player.x == 2 and player.y == 1:
            self.name = 'Diagon Alley Fireplace'

    def intro_text(self):
        return '''Fireplace Transport. All users must provide their own Floo Powder.'''
        

    def transport(self, player):
        if self.name == 'Entrance Hall Fireplace':
            print('This fireplace will take you to Diagon Alley \nWould you like to go? [y/n]')
            user_decision = input('> ')
            try:
                if user_decision.lower() in ['no', 'n']:
                    print('OK, nevermind')
                    return
                elif user_decision.lower() in ['yes', 'y']:
                    player.x = 2
                    player.y = 1
                    print('Welcome to Diagon Alley')
            except:
                print('Just say yes[y] or no[n]!!')
        
        elif self.name == 'Entrance Hall Fireplace':
            print('This fireplace will take you back to the Ministry of Magic. \nWould you like to go? [y/n]')
            user_decision = input('> ')
            try:
                if user_decision.lower() in ['no', 'n']:
                    return
                elif user_decision.lower() in ['yes', 'y']:
                    player.x = 1
                    player.y = 2
                    print('The familar tiled walls of the Ministry greet you as you return')
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
    def __init__(self, x, y, player):
        self.final_boss = FinalBoss()

    def intro_text(self): 
        return f'''
You have found the culprit. \n
It is {self.final_boss.name}, a well known muggle baiter. \n
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


class ClosedMapTile:
    def __init__(self, x, y, player):
        self.x = x
        self.y = y
        self.player = player
    
    def description(self):
        return None

    def __str__(self):
         return self.description()


class MinistryWall(ClosedMapTile):
    def description(self):
        return '''
There is only a dour tiled wall in front of you, you cannot go any further'''

class MinistryStatue(ClosedMapTile):
    def description(self):
        return '''
You look down the corridor. 
In the distance you can see a golden statue. 
You cannot complete your job there. 
You turn back'''

class MinistryPerkins(ClosedMapTile):
    def description(self):
        return '''
You just see Perkins in front of you.
He is blocking the way forward'''


if __name__ == "__main__":
    from player import Player

    player = Player()

    room = SecretRoom(4,2,player)
    print(room.intro_text())

