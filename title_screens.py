###### Title Screen ######

import os
import sys

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
    print('')
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
    else:
        print("Please enter a valid command.")
        title_screen_selections()
