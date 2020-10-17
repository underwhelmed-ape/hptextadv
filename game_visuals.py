import sys
import time


def narrate(phrase, delay):
    for character in phrase:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)

