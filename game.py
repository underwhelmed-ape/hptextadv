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

# xxxx|xxxx|xxxx|.pot|shop|
#     |fire|xxxx|DA-1|DA-2|
# Stat|Home|Perk|KTA |xxxx|
# xxxx|Wall|xxxx|Vict|xxxx|

#  00 | 10 | 20 | 30 | 40 |
#  01 | 11 | 21 | 31 | 41 |
#  02 | 12 | 22 | 32 | 42 |
#  03 | 13 | 23 | 33 | 43 |

world_map = [
    [None, None, None, world.PopupPotions(3,0,player), None],
    [None, world.Fireplace(1,1,player), None, world.DiagonAlleyTop(3,1,player), world.DiagonAlleyBottom(4,1, player)],
    [world.MinistryStatue(0,2,player), world.StartTile(1,2,player), world.MinistryPerkins(2,2,player), world.KnockturnAlley(3,2,player), None],
    [None, world.MinistryWall(1,3,player), None, world.SecretRoom(3,3,player), None]
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
            print('You died, bad luck')
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
        elif isinstance(new_room, world.ClosedMapTile):
            print('room is a ClosedMapTile')
            print(new_room)
            return

    elif dest in ['down', 'south', 's', 'S']:
        new_room = tile_at(world_map, player.x, player.y + 1)
        if isinstance(new_room, world.MapTile):
            print('room is a MapTile')
            print(f'new room is: {new_room}')
            player.move_south()
        elif isinstance(new_room, world.ClosedMapTile):
            print('room is a ClosedMapTile')
            print(new_room)
            return

    elif dest in ['left', 'west', 'w', 'W']:
        new_room = tile_at(world_map, player.x - 1, player.y)
        if isinstance(new_room, world.MapTile):
            print('room is a MapTile')
            print(f'new room is: {new_room}')
            player.move_west()
        elif isinstance(new_room, world.ClosedMapTile):
            print('room is a ClosedMapTile')
            print(new_room)
            return

    elif dest in ['right', 'east', 'e', 'E']:
        new_room = tile_at(world_map, player.x + 1, player.y)
        if isinstance(new_room, world.MapTile):
            print('room is a MapTile')
            print(f'new room is: {new_room}')
            player.move_east()
        elif isinstance(new_room, world.ClosedMapTile):
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


    # elif isinstance(room, world.DiagonAlleyTop):
    #     action_adder(actions, 'look', partial(room.transport, player), "Talk to person in tile")    
    # elif isinstance(room, world.DiagonAlleyBottom):
    #     action_adder(actions, 'look', partial(room.transport, player), "Talk to person in tile")    

    return actions


def choose_action(room, player):
    ''' Prompt player to give action command'''
    print('\n' + '=============================================')
    print('What would like to do?')
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input('\n> ')
        action = available_actions.get(action_input)
        if action:
            print(action())
        else:
            print('Unknown action, please enter another.\n')



play()




