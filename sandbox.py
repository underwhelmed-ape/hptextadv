import math

# 29 knuts in sickle
# 17 sickles in galleon
# 493 knuts in galleon
def wizard_money(knuts):
    if knuts == 0:
        print("You have no money in your pouch")
    elif knuts < 29:
        print("Knuts: " + str(knuts))
    elif knuts < 493:
        sickles = math.floor(knuts / 29)
        remaining = knuts % 29
        print("Sickles: " + str(sickles))
        print("Knuts: " + str(remaining))
    elif knuts >= 493:
        galleons = math.floor(knuts / 493)
        remaining_knuts = knuts % 493
        sickles = math.floor(remaining_knuts / 29)
        remaining = remaining_knuts % 29
        print("Galleons: " + str(galleons))
        print("Sickles: " + str(sickles))
        print("Knuts: " + str(remaining))

wizard_money(21)
wizard_money(200)
wizard_money(600)
wizard_money(0)
