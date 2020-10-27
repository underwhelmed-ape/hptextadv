# Python Text RPG
# Underwhelmed Ape

import cmd # help use command line
import textwrap # wrap text around the console for overflow
import sys
import os
import random # generate pseudo-random numbers
import math
from collections import OrderedDict
from functools import partial
from title_screens import title_screen, help_menu, about_menu, title_screen_selections
from game_setup import setup_game
from game_visuals import narrate
from player import Player
import world

screen_width = 100

player = Player()

## MAP ##

# CREATING THE WORLD MAP


#     |FWal|    |FWal|.pot|shop|
# FWal|fire|FWal|fire|DA-1|DA-2|Grin
# Stat|Home|Perk|FWal|AWal|KTA |Hag 
#     |Wall|    |    |    |Vict|

#  00 | 10 | 20 | 30 | 40 | 50 |
#  01 | 11 | 21 | 31 | 41 | 51 | 61
#  02 | 12 | 22 | 32 | 42 | 52 | 62
#  03 | 13 | 23 | 33 | 43 | 53 |

# make shops with no move functionality. Player is transported back out after transaction
# AWal is alley wall, will change output according to player's location
# Hag is npc. Talking suggests that there is hidden magic to those who know how to find it

home = world.StartTile(1,2,player)

world_map = [
    [None, world.FireplaceWall(1,0), None, world.FireplaceWall(3,0), world.PopupPotions(4,0,player), None],
    [world.FireplaceWall(0,1), world.Fireplace(1,1,player), world.FireplaceWall(2,1), world.DiagonAlleyTop(3,1,player), world.DiagonAlleyBottom(4,1, player)],
    [world.MinistryStatue(0,2), home, world.MinistryPerkins(2,2), world.KnockturnAlley(3,2,player), None],
    [None, world.MinistryWall(1,3), None, world.SecretRoom(3,3,player), None]
]

def tile_at(world_map, x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None

###### GAME FUNCTIONALITY ######

def play():

    title_screen()

    setup_game(player)

    while player.victory == False:
        if player.is_alive:
            room = tile_at(world_map, player.x, player.y)
            choose_action(room, player)
        else:
            os.system('clear')
            narrate('You died, bad luck', 0.1)
            sys.exit()



###### GAME INTERACTIVITY ######

def player_move():
    ask = "Where would you like to go?\n"
    dest = input(ask)
    print(f'current room is: {tile_at(world_map, player.x, player.y)}')
    if dest.lower() in ['up', 'north', 'n']:
        new_room = tile_at(world_map, player.x, player.y - 1)
        if isinstance(new_room, world.MapTile):
            print('room is a MapTile')
            print(f'new room is: {new_room}')
            player.move_north()
        elif isinstance(new_room, world.BlockedTile):
            print('room is a ClosedMapTile')
            print(new_room)
            return

    elif dest.lower() in ['d', 'down', 's', 'south']:
        new_room = tile_at(world_map, player.x, player.y + 1)
        if isinstance(new_room, world.MapTile):
            print('room is a MapTile')
            print(f'new room is: {new_room}')
            player.move_south()
        elif isinstance(new_room, world.BlockedTile):
            print(f'new room is: {new_room}')
            print(new_room)
            return

    elif dest in ['left', 'west', 'w', 'W']:
        new_room = tile_at(world_map, player.x - 1, player.y)
        if isinstance(new_room, world.MapTile):
            print('room is a MapTile')
            print(f'new room is: {new_room}')
            player.move_west()
        elif isinstance(new_room, world.BlockedTile):
            print('room is a ClosedMapTile')
            print(new_room)
            return

    elif dest in ['right', 'east', 'e', 'E']:
        new_room = tile_at(world_map, player.x + 1, player.y)
        if isinstance(new_room, world.MapTile):
            print('room is a MapTile')
            print(f'new room is: {new_room}')
            player.move_east()
        elif isinstance(new_room, world.BlockedTile):
            print('room is a ClosedMapTile')
            print(new_room)
            return
    print(f'new current room is: {tile_at(world_map, player.x, player.y)}')



def player_examine(room):
    if room[player.location]['SOLVED'] == True:
        print("You have already completed this job")
    else:
        print("trigger puzzle here")





def action_adder(action_dict, visible_hotkey, hotkeys, action, name):
    for hotkey in hotkeys:
        action_dict[hotkey.lower()] = action
        action_dict[hotkey.upper()] = action
    print(f'{visible_hotkey} -> {name}')

def get_available_actions(room, player):
    '''adds the actions a player can make to a dict'''
    actions = OrderedDict()

    action_adder(actions, '(Q)uit', ['q', 'quit'], sys.exit, "Exit Game")
    action_adder(actions, '(S)tats', ['s', 'stats'], player.player_stats, "Show your stats")
    action_adder(actions, '(I)nventory', ['i', 'inventory'], player.print_inventory, "Show your inventory")
    action_adder(actions, '(M)ove', ['m', 'move'], player_move, "Move")
    
    for action in room.actions:
        action_adder(
            actions, 
            action['visible_hotkey'], 
            action['hotkeys'], 
            action['action'] if action['args'] is None else partial(action['action'], action['args']), 
            action['name']
        )


    return actions


def choose_action(room, player):
    ''' Prompt player to give action command'''
    print('\n' + '===============================================================')
    print('What would like to do?')
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input('\n> ')
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print('Unknown action, please enter another.\n')



play()




