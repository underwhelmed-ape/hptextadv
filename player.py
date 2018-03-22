import items



###### Player Setup ######

# establishing state of main character
# this is a class used to store and initilise values of the player

class Player:
    def __init__(self):
        self.inventory = [#items.Wand(),
                          #items.Pocket_Knife(),
                          #items.Rock(),
                          'Money(50)',
                          'KB_ticket(0)']
        self.name = '' # string of player's name
        self.house = '' # string of player's house in game
        self.subject = ''
        self.hp = 0 # int of hitpoints
        self.mp = 0 # int of magic points/energy
        self.status_effects = [] #array
        self.location = 'b2' # string of where player is at the time
        self.game_over = False


    def print_inventory(self):
        print("Inventory: ")
        for item in self.inventory:
            print("* " + str(item))
        best_weapon = self.most_important_weapon()
        print("Your best weapon in your {}".format
        (best_weapon))

    def most_important_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item_damage
            except AttributeError:
                pass

        return best_weapon
