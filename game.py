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
    print('################# Help Menu #################')
    print('#############################################')
    print('')
    print('- Type "up", "down", "left", "right" to move')
    print('- Use "look" to inspect something')
    print('- Type "i" to view inventory')
    print('')
    print('                   - PLAY -                  ')
    print('                   - QUIT -                  ')
    print('- Good luck in the adventure...')
    title_screen_selections()





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
        myPlayer.print_inventory()


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
        time.sleep(0.005)
    player_house = input("> ").strip()
    valid_houses = ['gryffindor', 'slytherin', 'hufflepuff', 'ravenclaw', 'g', 's', 'h', 'r']
    if player_house.lower() in valid_houses:

        if player_house.lower() in ['g', 'gryffindor']:
            myPlayer.house = 'Gryffindor'
        if player_house.lower() in ['s', 'slytherin']:
            myPlayer.house = 'Slytherin'    
        if player_house.lower() in ['h', 'hufflepuff']:
            myPlayer.house = 'Hufflepuff'    
        if player_house.lower() in ['r', 'ravenclaw']:
            myPlayer.house = 'Ravenclaw'    

        print("You are now a " + myPlayer.house + "! \n")
    else:
        while player_house.lower() not in valid_houses:
            print("Please select a valid House for this adventure!")
            player_house = input("> ").strip()
        if player_house.lower() in valid_houses:
            myPlayer.house = player_house
            print("You are now a " + myPlayer.house + "! \n")

        ###### Player stats #######

        if myPlayer.house == 'Gryffindor':
            self.hp = 120 # hitpoints - int
            self.mp = 20 # magic strength - int
        elif myPlayer.house == 'Slytherin':
            self.hp = 40
            self.mp = 120
        elif myPlayer.house == 'Hufflepuff':
            self.hp = 60
            self.mp = 60
        elif myPlayer.house == 'Ravenclaw':
            self.hp = 60
            self.mp = 60

    ### Introduction
    question3 = f'Welcome {myPlayer.name} from {myPlayer.house} to the Ministry of Magic. \n' 

    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    myPlayer.name = input("> ").strip()

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
