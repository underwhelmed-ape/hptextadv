# Python Text RPG
# Underwhelmed Ape

import cmd # help use command line
import textwrap # wrap text around the console for overflow
import sys
import os
import time
import random # generate pseudo-random numbers

screen_width = 100

###### Player Setup ######

# establishing state of main character
# this is a class used to store and initilise values of the player
class player:
    def __init__(self):
        self.name = '' # string of player's name
        self.hp = 0 # int of hitpoints
        self.mp = 0 # int of magic points/energy
        self.status_effects = [] #array
        self.location = 'start' # string of where player is at the time

#initilise the player

myPlayer = player()

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

title_screen()

def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game() #placeholder
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("> ")
        if option.lower() == ("play"):
            start_game() #placeholder
        elif option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()



title_screen_selections()



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
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit',  'inspect', 'interact', 'look', 'examine']
    while action.lower() not in acceptable_actions:
        print("Unknown action, please try again. \n")
        action = input("> ")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player.move(action.lower())
    elif action.lower() in ['inspect', 'interact', 'look', 'examine']:
        player.examine(action.lower())

def player.move(myAction):
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


def player.examine(action):
    if zonemap[myPlayer.location][SOLVED] == True:
        print("You have already completed this job")
    else:
        print("trigger puzzle here")     


###### GAME FUNCTIONALITY ######
def start_game():
    return
