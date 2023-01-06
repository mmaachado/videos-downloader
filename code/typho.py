import time
import sys
import random


def typing(message: str) -> str:
    """
    Method to create a typing effect on console.

    :param message: (Required) The output message that should be displayed.
    
    :return: str
    """

    print("")
    for word in message:
        time.sleep(random.choice(
            [0.3, 0.1, 0.8, 0.7,   0.7, 0.07, 0.06, 0.06, 0.05, 0.01]))
        sys.stdout.write(word)
        sys.stdout.flush()
    time.sleep(.1)
    return ""
