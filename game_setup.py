def setup_game():
    os.system('clear')

    ### get player's name
    question_name = "Hello, what's your name? \n"
    narrate(question_name)
    player_name = input("> ").strip()
    player.name = player_name
    os.system('clear')

    ### get player's house
    question_house = "Select your House \nAre you a (G)ryffindor, (S)lytherin, (H)ufflepuff or (R)avenclaw? \n"
    narrate(question_house)

    
    player_house = input("> ").strip()
    os.system('clear')
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
    

    welcome_statement_1 = '''The path in front of you has been blocked. 
You peer at the brick wall, it is aging and lightly discoloured, but is otherwise 
unremarkable from the surrounding London townhouses.
You have been to Diagon Alley many times though.

Tap the brick with your Wand.\n
'''
    
    narrate(welcome_statement_1)
    brick_options = ['(1) Three up and two across', '(2) One up and four across']
    for option in brick_options:
        print(option)
    brick_answer = input('> ')
    while brick_answer != '1':
        narrate('Not quite. Have you forgotten already?\n')
        brick_answer = input('> ')
    
    os.system('clear')
    time.sleep(1)
    welcome_statement_2 = f'''Welcome {player.name} to the Wizarding World.

        "Let us step into the night and pursue that flighty temptress...
        adventure" - Albus Dumbledore
    '''
    narrate(welcome_statement_2)
    time.sleep(2)
    player.player_stats()