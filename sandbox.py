import math

# 29 knuts in sickle
# 17 sickles in galleon
# 493 knuts in galleon
def wizard_money(knuts):
    if knuts < 29:
        print("Knuts: " + str(knuts))
    elif knuts >= 493:
        galleons = math.floor(knuts / 493)
        remaining = knuts % 493
        print("Galleons: " + str(galleons))
    else:
        print("dnfvkndv")

wizard_money(21)
wizard_money(200)
wizard_money(600)
