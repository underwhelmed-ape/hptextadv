import items

class Player:
    def__init__(self):
        self.inventory = [items.Wand(),
                          items.Pocket_Knife(),
                          'Money(50)',
                          'KB_ticket(0)']

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
