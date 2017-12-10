# Python Text RPG
# Underwhelmed Ape

import cmd # help use command line
import textwrap # wrap text around the console for overflow
import sys
import os
import time
import random

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

#initilise the player

myPlayer = player()

###### Title Screen ######
#will allow player to select menu options
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

def title_screen():
    os.system('clear')
    print('################################')
    print('# Ministry of Magic Mayham RPG #')
    print('################################')
    print('            - PLAY -            ')
    print('            - HELP -            ')
    print('            - QUIT -            ')
    print(' -Created by Underwhelmed Ape-  ')

title_screen_selections()

def help_menu:
    print('################################')
    print('# Ministry of Magic Mayham RPG #')
    print('################################')
    print('- Type "up", "down", "left", "right" to move')
    print('- Use "look" to inspect something')
    print('- Good luck in the adventure')

title_screen_selections()
