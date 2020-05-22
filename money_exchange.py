import math

# 29 knuts in sickle
# 17 sickles in galleon
# 493 knuts in galleon
# requires import math

def wizard_money(knuts):
    if knuts == 0:
        return 'You have no money in your purse'
    elif knuts < 29:
        return f'Knuts: {knuts}'
    elif knuts < 493:
        sickles = math.floor(knuts / 29)
        remaining = knuts % 29
        return f'Sickles: {sickles} \nKnuts: {remaining}'
        
    elif knuts >= 493:
        galleons = math.floor(knuts / 493)
        remaining_knuts = knuts % 493
        sickles = math.floor(remaining_knuts / 29)
        remaining = remaining_knuts % 29
        return f'  * Galleons: {galleons} \n  * Sickles: {sickles} \n  * Knuts: {remaining}'






if __name__ == "__main__":
    k = 600
    print(wizard_money(k))