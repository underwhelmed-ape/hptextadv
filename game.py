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
