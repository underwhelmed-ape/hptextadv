# Adding in Non-playable Characters (npc)

import items
import consumables
from game_visuals import narrate


# Trader character
class NonPlayableCharacter():
    def __init__(self):
        raise NotImplementedError('Do not create raw NPC objects')

    def __str__(self):
        return self.name




class Trader(NonPlayableCharacter):
    def __init__(self):
        self.name = "Trader"
        self.Money = 10000
        self.inventory = [
            consumables.BasicHealingPotion(),
            consumables.BasicHealingPotion(),
            items.Sneakoscope(),
            items.BasicPotionsKit()]


class Perkins(NonPlayableCharacter):
    def __init__(self):
        self.name = "Perkins"
        self.times_spoken = 0


    def talk(self, player):
        if True: # placeholder for non puzzle completion
            if self.times_spoken == 0:
                speech = f'''
    Perkins: 
    Hi {player.name}, we've been have a lot of trouble lately with a series of muggle baiting attacks. 
    We need your help catching this individual before they do any more harm. 

    We've received an owl about a bewitched item for sale in Knockturn Alley, it's currently attacking anyone who approaches it. 
    We need you to stop this and see what you can find in the area.'''
                self.times_spoken += 1
                return narrate(speech, 0.05)
            else:
                speech = '''
    Well, what are you waiting for? 
    You need to find Knockturn alley and find a way to stop the incident before it hurts any Witches or Wizards.'''
                return narrate(speech, 0.05)
        
        else:
            if self.times_spoken == 1:
                speech = '''
    Well done. I got the owl saying you had fixed the enchanted item. 
    A teapot this time? This sounds like the guy we are chasing. Maybe he was selling it before he was disturbed.
    You should have a look around the area and see what clues you can find. He can't have gotten far!
    If you need any items to help you on the mission, you can probably find them in Diagon Alley. 
    The Ministry of Magic will reinburse you of course.
    '''
                self.times_spoken += 1
                return narrate(speech, 0.05)
            else:
                speech = '''
    You should have a look around the area and see what clues you can find. He can't have gotten far!
    If you need any items to help you on the mission, you can probably find them in Diagon Alley. 
    The Ministry of Magic will reinburse you of course. If you submit your expenses in time that is!'''
                return narrate(speech, 0.05)
