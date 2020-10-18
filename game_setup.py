import os
from game_visuals import narrate
import time

def setup_game(player):
    os.system('clear')

    ### get player's name
    question_name = "Hello, what's your name? \n"
    narrate(question_name, 0.05)
    player_name = input("> ").strip()
    player.name = player_name
    os.system('clear')

    ### get player's house
    question_house = "Select your House \nAre you a (G)ryffindor, (S)lytherin, (H)ufflepuff or (R)avenclaw? \n"
    narrate(question_house, 0.05)     
    set_player_house(player)

    ###### Player stats #######
    set_player_stats(player)

    ### Introduction

    time.sleep(0.5)    

    welcome_statement_1 = '''The path in front of you has been blocked. 
You peer at the brick wall, it is aging and lightly discoloured, but is otherwise 
unremarkable from the surrounding London townhouses.
You have been through here many times though.

Tap the correct brick with your wand to enter Diagon Alley.\n
'''
    
    narrate(welcome_statement_1, 0.05)
    brick_options = ['(1) Three up and two across', '(2) One up and four across']
    for option in brick_options:
        print(option)
    
    enter_diagon_alley()
    
    os.system('clear')
    time.sleep(1)
    narrate(f'''Welcome {player.name} to the Wizarding World.\n''', 0.05)
    narrate('''          "Let us step into the night and pursue that flighty temptress...\n''', 0.05)
    narrate('''           adventure"\n''', 0.05)
    narrate('''          - Albus Dumbledore''', 0.05)
        
    time.sleep(2)



def set_player_house(player):

    player_house = input("> ").strip()
    os.system('clear')
    
    if player_house.lower() in ['g', 'gryffindor']:
        player.house = 'Gryffindor'
    elif player_house.lower() in ['s', 'slytherin']:
        player.house = 'Slytherin'    
    elif player_house.lower() in ['h', 'hufflepuff']:
        player.house = 'Hufflepuff'    
    elif player_house.lower() in ['r', 'ravenclaw']:
        player.house = 'Ravenclaw'
    else:
        print("Please select a valid House for this adventure!")
        set_player_house(player)
        
    

def enter_diagon_alley():
    brick_answer = input('> ')
    if brick_answer != '1':
        narrate('Not quite. Have you forgotten already?\n', 0.05)
        enter_diagon_alley()

def set_player_stats(player):
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