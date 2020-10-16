# Python Text RPG
# Underwhelmed Ape

import cmd # help use command line
import textwrap # wrap text around the console for overflow
import sys
import os
import time
import random # generate pseudo-random numbers
import math
from collections import OrderedDict
from functools import partial


from player import Player
import world

screen_width = 100

player = Player()

## MAP ##

# CREATING THE WORLD MAP

# xxxx|xxxx|.pot|shop|
#     |fire|DA-1|DA-2|
# Stat|Home|Perk|KTA |Vict|
# xxxx|Wall|xxxx|xxxx|xxxx|

#  00 | 10 | 20 | 30 |
#  01 | 11 | 21 | 31 |
#  02 | 12 | 22 | 32 | 42 |
#  03 | 13 | 23 | 33 | 43 |
world_map = [
    [None, None, world.PopupPotions(2,0,player), None, None],
    [None, world.Fireplace(1,1,player), world.DiagonAlleyTop(2,1,player), world.DiagonAlleyBottom(3,1, player), None],
    [world.MinistryStatue(0,2,player), world.StartTile(1,2,player), world.MinistryPerkins(2,2,player), world.KnockturnAlley(3,2,player), world.SecretRoom(4,2,player)],
    [None, world.MinistryWall(1,3,player), None, None, None]
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

    setup_game()

    while player.victory == False:
        room = tile_at(world_map, player.x, player.y)
        #if isinstance(room, MinistryWall):
        print(room)
        choose_action(room, player)
        #prompt()



###### Title Screen ######
# will allow player to select menu options

def title_screen():
    os.system('clear')
    print('##############################################')
    print('######## Harry Potter Text Adventure #########')
    print('##############################################')
    print('')
    print('                  -  PLAY  -                  ')
    print('                  -  HELP  -                  ')
    print('                  -  ABOUT -                  ')
    print('                  -  QUIT  -                  ')
    print('')
    print('        -Created by Underwhelmed Ape-        ')
    title_screen_selections()

def help_menu():
    os.system('clear')
    print('##############################################')
    print('################# Help Menu ##################')
    print('##############################################')
    print('')
    print('- Type "up", "down", "left", "right" when moving')
    print('- Use "look" to inspect something')
    print('- Use "talk" to interact with people')
    print('- Type "i" to view inventory')
    print('')
    print('                  -  PLAY  -                  ')
    print('                  -  ABOUT -                  ')
    print('                  -  QUIT  -                  ')
    print('- Good luck in the adventure...')
    title_screen_selections()

def about_menu():
    os.system('clear')
    print('##############################################')
    print('################# About Menu #################')
    print('##############################################')
    print('This is a text adventure game based in the')
    print('Harry Potter universe')
    print('')
    print('A young worker in the Ministry of Magic finds')
    print('themselves at the heart of an investigation')
    print('')
    print('Explore the Magical world and solve the mystery')
    print('')
    print('')
    print('                  -  PLAY  -                  ')
    print('                  -  HELP  -                  ')
    print('                  -  QUIT  -                  ')
    print('- Good luck in the adventure...')
    title_screen_selections()

def title_screen_selections():
    option = input("> ")
    if option.lower() in ['play', 'p']:
        return
    elif option.lower() in ['help', 'h']:
        help_menu()
    elif option.lower() in ['about', 'a']:
        about_menu()
    elif option.lower() in ['quit', 'q']:
        sys.exit()
    while option.lower() not in ['play', 'help', 'about', 'quit', 'p', 'h', 'a', 'q']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() in ['play', 'p']:
            return
        elif option.lower() in ['help', 'h']:
            help_menu()
        elif option.lower() in ['about', 'a']:
            about_menu()
        elif option.lower() in ['quit', 'q']:
            sys.exit()


###### GAME INTERACTIVITY ######

def player_move():
    ask = "Where would you like to go?\n"
    dest = input(ask)
    print(f'current room is: {tile_at(world_map, player.x, player.y)}')
    if dest in ['up', 'north', 'n', 'N']:
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

# def movement_handler():
#     X = player.x
#     Y = player.y
#     print(f'\nYou have moved to {world.tile_at(X, Y)}.')
    #player.location = destination
    #print_location()



def player_examine():
    if room[player.location][SOLVED] == True:
        print("You have already completed this job")
    else:
        print("trigger puzzle here")



def setup_game():
    os.system('clear')

    ### name collecting
    question_name = "Hello, what's your name? \n"
    for character in question_name:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ").strip()
    player.name = player_name

    ### subject collecting
    # question_subject = "What was your favourite subject? \n"
    # question_subject_additional = "[Charms, DADA]. \n"
    # for character in question_subject:
    #     sys.stdout.write(character)
    #     sys.stdout.flush()
    #     time.sleep(0.05)
    # player_subject = input("> ").strip()
    # player.subject = player_subject

    ### Hogwarts House
    question_house = "What House do you belong to? \n"
    question_house_additional = "You can be a (G)ryffindor, (S)lytherin, (H)ufflepuff or (R)avenclaw. \n"
    for character in question_house:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question_house_additional:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.005)
    player_house = input("> ").strip()
    valid_houses = ['gryffindor', 'slytherin', 'hufflepuff', 'ravenclaw', 'g', 's', 'h', 'r']
    if player_house.lower() in valid_houses:

        if player_house.lower() in ['g', 'gryffindor']:
            player.house = 'Gryffindor'
        if player_house.lower() in ['s', 'slytherin']:
            player.house = 'Slytherin'    
        if player_house.lower() in ['h', 'hufflepuff']:
            player.house = 'Hufflepuff'    
        if player_house.lower() in ['r', 'ravenclaw']:
            player.house = 'Ravenclaw'
    else:
        while player_house.lower() not in valid_houses:
            print("Please select a valid House for this adventure!")
            player_house = input("> ").strip()
        if player_house.lower() in valid_houses:
            if player_house.lower() in ['g', 'gryffindor']:
                player.house = 'Gryffindor'
            if player_house.lower() in ['s', 'slytherin']:
                player.house = 'Slytherin'    
            if player_house.lower() in ['h', 'hufflepuff']:
                player.house = 'Hufflepuff'    
            if player_house.lower() in ['r', 'ravenclaw']:
                player.house = 'Ravenclaw'
            

    ###### Player stats #######
    #can merge with above

    if player.house == 'Gryffindor':
        player.hp = 100 # hitpoints - int
        player.mp = 100 # magic strength - int
        player.mp = 100 # magic strength - int
        player.house_description = 'Nerve and Bravery'
    elif player.house == 'Slytherin':
        player.hp = 100
        player.mp = 120
        player.house_description = 'Cunning and Ambition'
    elif player.house == 'Hufflepuff':
        player.hp = 120
        player.mp = 60
        player.house_description = 'Hard Work and loyalty'
    elif player.house == 'Ravenclaw':
        player.hp = 100
        player.mp = 60
        player.house_description = 'Wisdom and Wit'

    ### Introduction


    time.sleep(0.5)
    print("####################################")
    print("#       Let's begin the game       #")
    print("####################################")
    

    welcome_statement = f'''Welcome {player.name} to the Ministry of Magic.
We welcome people from all houses here. 
As a {player.house}, you value {player.house_description}.\n'''
    
    for character in welcome_statement:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
   
    player.player_stats()

def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print(f'{hotkey}: {name}')

def get_available_actions(room, player):
    actions = OrderedDict()
    print('choose your action: ')

    action_adder(actions, 'quit', sys.exit, "Exit Game")
    action_adder(actions, 'stats', player.player_stats, "Show player stats")
    action_adder(actions, 'move', player_move, "Move")
    if player.inventory:
        action_adder(actions, 'i', player.print_inventory, "Prints player's inventory")
    if isinstance(room, world.StartTile):
        action_adder(actions, 'talk', partial(room.talk, player), "Talk to person in tile")
    elif isinstance(room, world.Fireplace):
        action_adder(actions, 'look', partial(room.transport, player), "Examine your location")
    elif isinstance(room, world.DiagonAlleyTop):
        action_adder(actions, 'look', partial(room.transport, player), "Talk to person in tile")    
    elif isinstance(room, world.DiagonAlleyBottom):
        action_adder(actions, 'look', partial(room.transport, player), "Talk to person in tile")    

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


'''
Welcome {player.name} to your first day, here at the Ministry of Magic. 
We have assigned you to the Department of Magical Law Enforcement. 
Specifically, the Misuse of Muggle Artifacts Office. I'll leave you with Perkins, 
he will be able to tell you what you will be doing for your first job here. 

Perkins:
1. Initial conversation with Perkins - mandatory
Hi {player.name}, we've been have a lot of trouble lately with a series of muggle baiting attacks. 
We need your help catching this individual before they do permanent damage. 

We've just had a call about a bewitched item for sale in Knockturn Alley, it's currently attacking anyone who approaches it. 
We need you to stop this and see what you can find in the area.

2. If player talk to Perkins before solving puzzle
Well, what are you waiting for? You need to find Knockturn alley and find a way to stop the teapot before it hurts any Witches or Wizards.  

3. After solving first puzzle.
Well done. I got the owl saying you had fixed the enchanted item. 
A teapot this time? This sounds like the guy we are chasing. Maybe he was selling it before he was disturbed.
You should have a look around the area and see what clues you can find. He can't have gotten far!
If you need any items to help you on the mission, you can probably find them in Diagon Alley. 
The Ministry of Magic will reinburse you of course.  

4. If talk again: 
You should have a look around the area and see what clues you can find. He can't have gotten far!
If you need any items to help you on the mission, you can probably find them in Diagon Alley. 
The Ministry of Magic will reinburse you of course. If you submit your expenses in time that is!
'''
