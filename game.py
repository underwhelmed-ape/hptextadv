# Python Text RPG
# Underwhelmed Ape

import cmd # help use command line
import textwrap # wrap text around the console for overflow
import sys
import os
import time
import random # generate pseudo-random numbers
import math

import player

screen_width = 100


#initilise the player

myPlayer = player.Player()


def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        setup_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            setup_game()
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()


###### Title Screen ######
# will allow player to select menu options
def title_screen():
    os.system('clear')
    print('#############################################')
    print('######## Harry Potter Text Adventure ########') # placeholder game name
    print('#############################################')
    print('')
    print('                   - PLAY -                  ')
    print('                   - HELP -                  ')
    print('                   - QUIT -                  ')
    print('')
    print('        -Created by Underwhelmed Ape-        ')
    title_screen_selections()


def help_menu():
    print('#############################################')
    print('################# Help Menu #################') # placeholder game name
    print('#############################################')
    print('')
    print('- Type "up", "down", "left", "right" to move')
    print('- Use "look" to inspect something')
    print('')
    print('                   - PLAY -                  ')
    print('                   - QUIT -                  ')
    print('- Good luck in the adventure...')
    title_screen_selections()


###### MAP ######
"""
# player starts at b2 (x)
      1   2   3   4
    -----------------
    |   |   |   |   |  a
    -----------------
    |   | x |   |   |  b
    -----------------
    |   |   |   |   |  c
    -----------------
    |   |   |   |   |  d
    -----------------

"""

# constant variables set-up

ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = 'False'
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'a1': False, 'a2': False, 'a3': False, 'a4': False,
                'b1': False, 'b2': False, 'b3': False, 'b4': False,
                'c1': False, 'c2': False, 'c3': False, 'c4': False,
                'd1': False, 'd2': False, 'd3': False, 'd4': False,
                }

zonemap = {
    'a1': {
        ZONENAME: 'Town Market',
        DESCRIPTION: 'A thriving market place where you can find many exotic and magical objects',
        EXAMINATION: 'examine',
        SOLVED: 'False',
        UP: '',
        DOWN: 'b1',
        LEFT: '',
        RIGHT: 'a2'
    },
    'a2': {
        ZONENAME: 'Town Entrance',
        DESCRIPTION: 'This is the main gate to the town',
        EXAMINATION: 'examine',
        SOLVED: 'False',
        UP: '',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3'
    },
    'a3': {
        ZONENAME: 'Town Square',
        DESCRIPTION: 'A great place for a meeting',
        EXAMINATION: 'examine',
        SOLVED: 'False',
        UP: '',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4'
    },
    'a4': {
        ZONENAME: 'Town Hall',
        DESCRIPTION: 'The home of bureaucracy',
        EXAMINATION: 'examine',
        SOLVED: 'False',
        UP: '',
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: ''
    },
    'b1': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: 'False',
        UP: 'a1',
        DOWN: 'c1',
        LEFT: '',
        RIGHT: 'b2'
    },
    'b2': {
        ZONENAME: 'Home',
        DESCRIPTION: 'This is your home',
        EXAMINATION: 'Your home looks as messy as always! You really should clean up.',
        SOLVED: 'False',
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3'
    },
    'b3': {
        ZONENAME: "Forest",
        DESCRIPTION: '',
        EXAMINATION: 'examine',
        SOLVED: 'False',
        UP: 'a3',
        DOWN: 'c3',
        LEFT: 'b2',
        RIGHT: 'b4'
    },
    'b4': {
        ZONENAME: "Empty Shack",
        DESCRIPTION: 'This house inside the forest was abandoned long ago ... it looks dangerous to enter ',
        EXAMINATION: 'examine',
        SOLVED: 'False',
        UP: 'a4',
        DOWN: 'c4',
        LEFT: 'b3',
        RIGHT: ''
    },
    'c1': {
        ZONENAME: "The Dragon Tavern",
        DESCRIPTION: '',
        EXAMINATION: 'examine',
        SOLVED: 'False',
        UP: 'b1',
        DOWN: 'd1',
        LEFT: '',
        RIGHT: 'c2'
    },
    'c2': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: 'False',
        UP: 'b2',
        DOWN: 'd2',
        LEFT: 'c1',
        RIGHT: 'c3'
    },
    'c3': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: 'False',
        UP: 'b3',
        DOWN: 'd3',
        LEFT: 'c2',
        RIGHT: 'c4'
    },
    'c4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: 'False',
        UP: 'b4',
        DOWN: 'd4',
        LEFT: 'c3',
        RIGHT: ''
    },
    'd1': {
        ZONENAME: "The Dragon Tavern",
        DESCRIPTION: 'A popular local haunt. Bring your own glasses!',
        EXAMINATION: 'examine',
        SOLVED: 'False',
        UP: 'c1',
        DOWN: '',
        LEFT: '',
        RIGHT: 'd2'
    },
    'd2': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: 'False',
        UP: 'c2',
        DOWN: '',
        LEFT: 'd1',
        RIGHT: 'd3'
    },
    'd3': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: 'False',
        UP: 'c3',
        DOWN: '',
        LEFT: 'd2',
        RIGHT: 'd4'
    },
    'd4': {
        ZONENAME: "",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: 'False',
        UP: 'c4',
        DOWN: '',
        LEFT: 'd3',
        RIGHT: ''
    }
#    'd4': {
#        ZONENAME: "",
#        DESCRIPTION: 'description',
#        EXAMINATION: 'examine',
#        SOLVED: 'False',
#        UP: 'up', 'north',
#        DOWN: '',
#        LEFT: 'left', 'west',
#        RIGHT: 'right', 'east'
#    }
}



###### GAME INTERACTIVITY ######
# handle printing locations, moving, examining, puzzles, triggered-events etc

#show current location
def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location)))) # add to new lines
    print('# ' + myPlayer.location.upper() + ' #')
    print('# ' + zonemap[myPlayer.location][DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(myPlayer.location))))

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
        print("INVENTORY: \n")
        pretty_print_unordered(myPlayer.inventory)

# for printing inventory in easy to read manner
def pretty_print_unordered(list):
    for item in list:
        print("* " + str(item))


# 29 knuts in sickle
# 17 sickles in galleon
# 493 knuts in galleon
# requires import math
def wizard_money(knuts):
    if knuts == 0:
        print("You have no money in your pouch")
    elif knuts < 29:
        print("Knuts: " + str(knuts))
    elif knuts < 493:
        sickles = math.floor(knuts / 29)
        remaining = knuts % 29
        print("Sickles: " + str(sickles))
        print("Knuts: " + str(remaining))
    elif knuts >= 493:
        galleons = math.floor(knuts / 493)
        remaining_knuts = knuts % 493
        sickles = math.floor(remaining_knuts / 29)
        remaining = remaining_knuts % 29
        print("Galleons: " + str(galleons))
        print("Sickles: " + str(sickles))
        print("Knuts: " + str(remaining))


def player_move(myAction):
    ask = "Where would you like to go?\n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP] # accessing where going to move to
        movement_handler(destination)
    if dest in ['down', 'south']:
        destination = zonemap[myPlayer.location][DOWN] # accessing where going to move to
        movement_handler(destination)
    if dest in ['left', 'west']:
        destination = zonemap[myPlayer.location][LEFT] # accessing where going to move to
        movement_handler(destination)
    if dest in ['right', 'east']:
        destination = zonemap[myPlayer.location][RIGHT] # accessing where going to move to
        movement_handler(destination)

def movement_handler(destination):
    print("\n" + "You have moved to " + destination + ".")
    myPlayer.location = destination
    print_location()


def player_examine(action):
    if zonemap[myPlayer.location][SOLVED] == True:
        print("You have already completed this job")
    else:
        print("trigger puzzle here")


###### GAME FUNCTIONALITY ######

def main_game_loop():
    while myPlayer.game_over == False:
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
    myPlayer.name = player_name

    ### name collecting
    question_subject = "What was your favourite subject? \n"
    for character in question_subject:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_subject = input("> ").strip()
    myPlayer.subject = player_name

    ### Hogwarts House
    question_house = "What House do you belong to? \n"
    question_house_additional = "You can be a Gryffindor, Slytherin, Hufflepuff or Ravenclaw. \n"
    for character in question_house:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question_house_additional:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_house = input("> ").strip()
    valid_houses = ['gryffindor', 'slytherin', 'hufflepuff', 'ravenclaw', 'g', 's', 'h', 'r']
    if player_house.lower() in valid_houses:
        myPlayer.house = player_house
        print("You are now a " + myPlayer.house + "! \n")
    else:
        while player_house.lower() not in valid_houses:
            print("Please select a valid House for this adventure!")
            player_house = input("> ").strip()
        if player_house.lower() in valid_houses:
            myPlayer.house = player_house
            print("You are now a " + myPlayer.house + "! \n")

        ###### Player stats #######

        if myPlayer.house is 'Gryffindor':
            self.hp = 120 # int of hitpoints
            self.mp = 20 # int of magic points/energy
        elif myPlayer.house is 'Slytherin':
            self.hp = 40 # int of hitpoints
            self.mp = 120 # int of magic points/energy
        elif myPlayer.house is 'Hufflepuff':
            self.hp = 60 # int of hitpoints
            self.mp = 60 # int of magic points/energy
        elif myPlayer.house is 'Ravenclaw':
            self.hp = 60 # int of hitpoints
            self.mp = 60 # int of magic points/energy

    ### Introduction
    question3 = "Welcome, " + player_name + " from " + player_house + ".\n"
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ").strip()
    myPlayer.name = player_name

# amending types of speech
# gets more ominous as time gets longer

    speech1 = "Welcome to the magical world! \n"
    speech2 = "I hope it finds you well \n"
    speech3 = "Don't get too lost \n"
    speech4 = "hehehe... \n"
    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)

    os.system('clear')
    print("###################################")
    print("#        Let's start now          #")
    print("###################################")

    main_game_loop()

title_screen()
