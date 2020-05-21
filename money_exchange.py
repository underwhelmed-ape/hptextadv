import math

# 29 knuts in sickle
# 17 sickles in galleon
# 493 knuts in galleon
# requires import math

def wizard_money(knuts):
    if knuts == 0:
        print("You have no money in your purse")
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


if __name__ == "__main__":
    k = 600
    wizard_money(k)