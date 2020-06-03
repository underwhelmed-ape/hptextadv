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

from player import Player
import world

screen_width = 100

#initilise the player

player = Player()

###### Title Screen ######
# will allow player to select menu options

def title_screen():
    os.system('clear')
    print('##############################################')
    print('######## Harry Potter Text Adventure #########') # placeholder game name
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
    print('##############################################')
    print('################# Help Menu ##################')
    print('##############################################')
    print('')
    print('- Type "up", "down", "left", "right" to move')
    print('- Use "look" to inspect something')
    print('- Type "i" to view inventory')
    print('')
    print('                  -  PLAY  -                  ')
    print('                  -  ABOUT -                  ')
    print('                  -  QUIT  -                  ')
    print('- Good luck in the adventure...')
    title_screen_selections()

def about_menu():
    print('##############################################')
    print('################# About Menu #################')
    print('##############################################')
    print('This is the about screen')
    print('This will be filled in later')
    print('')
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
        setup_game()
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
            setup_game()
        elif option.lower() in ['help', 'h']:
            help_menu()
        elif option.lower() in ['about', 'a']:
            about_menu()
        elif option.lower() in ['quit', 'q']:
            sys.exit()



###### GAME INTERACTIVITY ######
# handle printing locations, moving, examining, puzzles, triggered-events etc

#show current location
# def print_location():
#     print('\n' + ('#' * (4 + len(player.location)))) # add to new lines
#     print('# ' + player.location.upper() + ' #')
#     print('# ' + zonemap[player.location][DESCRIPTION] + ' #')
#     print('\n' + ('#' * (4 + len(player.location))))

def prompt(): # where we will promt player to do everything, can add fighting etc
    print('\n' + '===============================')
    print('What would like to do?')
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit',  'inspect', 'interact', 'look', 'examine', 'inventory', 'inv', 'i']
    while action.lower() not in acceptable_actions:
        print("Unknown action, please try again. \n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['inspect', 'interact', 'look', 'examine']:
        player_examine(action.lower())
    elif action.lower() in ['inventory', 'inv', 'i']:
        player.print_inventory()


def player_move(myAction):
    ask = "Where would you like to go?\n"
    dest = input(ask)
    if dest in ['up', 'north', 'n', 'N']:
        player.move_north()
        #destination = zonemap[player.location][UP] # accessing where going to move to
        movement_handler()
    if dest in ['down', 'south', 's', 'S']:
        player.move_south()
        #destination = zonemap[player.location][DOWN] # accessing where going to move to
        movement_handler()
    if dest in ['left', 'west', 'w', 'W']:
        player.move_west()
        #destination = zonemap[player.location][LEFT] # accessing where going to move to
        movement_handler()
    if dest in ['right', 'east', 'e', 'E']:
        player.move_east()
        #destination = zonemap[player.location][RIGHT] # accessing where going to move to
        movement_handler()

def movement_handler():
    X = player.x
    Y = player.y
    print(f'\nYou have moved to {world.tile_at(X, Y)}.')
    #player.location = destination
    #print_location()


def player_examine(action):
    if zonemap[player.location][SOLVED] == True:
        print("You have already completed this job")
    else:
        print("trigger puzzle here")

## LIMITING ACTIONS



def get_available_actions(room, player):
    actions = OrderedDict()
    print('Choose an action: ')

    if player.inventory:
        action_adder(actions, 'i', player.print_inventory, 'Print Inventory')





def action_adder():
        actions['i'] = player.print_inventory
        actions['I'] = player.print_inventory
        actions['inventory'] = player.print_inventory
        actions['inv'] = player.print_inventory
        print('i: View Inventory')


###### GAME FUNCTIONALITY ######

def main_game_loop():
    while player.victory == False:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        prompt()
        #here handle if puzzles have been solved, boss defeated etc
        # keeps game promting until game is completed

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

    ### name collecting
    question_subject = "What was your favourite subject? \n"
    question_subject_additional = "[Charms, DADA]. \n"
    for character in question_subject:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_subject = input("> ").strip()
    player.subject = player_name

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

        print("You are now a " + player.house + "! \n")
    else:
        while player_house.lower() not in valid_houses:
            print("Please select a valid House for this adventure!")
            player_house = input("> ").strip()
        if player_house.lower() in valid_houses:
            player.house = player_house
            print("You are now a " + player.house + "! \n")

        ###### Player stats #######

        if player.house == 'Gryffindor':
            self.hp = 100 # hitpoints - int
            self.mp = 100 # magic strength - int
        elif player.house == 'Slytherin':
            self.hp = 100
            self.mp = 120
        elif player.house == 'Hufflepuff':
            self.hp = 100
            self.mp = 60
        elif player.house == 'Ravenclaw':
            self.hp = 100
            self.mp = 60

    ### Introduction
    question3 = f'Welcome {player.name} from {player.house} to the Ministry of Magic. \n' 

    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player.name = input("> ").strip()

# amending types of speech
# gets more ominous as time gets longer

    # speech1 = "Welcome to the magical world! \n"
    # speech2 = "I hope it finds you well \n"
    # speech3 = "Don't get too lost \n"
    # speech4 = "hehehe... \n"
    # for character in speech1:
    #     sys.stdout.write(character)
    #     sys.stdout.flush()
    #     time.sleep(0.03)
    # for character in speech2:
    #     sys.stdout.write(character)
    #     sys.stdout.flush()
    #     time.sleep(0.03)
    # for character in speech3:
    #     sys.stdout.write(character)
    #     sys.stdout.flush()
    #     time.sleep(0.1)
    # for character in speech4:
    #     sys.stdout.write(character)
    #     sys.stdout.flush()
    #     time.sleep(0.2)

    os.system('clear')
    print("###################################")
    print("#        Let's start now          #")
    print("###################################")

    main_game_loop()

title_screen()
