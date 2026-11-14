from functools import total_ordering
from urllib import response


def directions():
    steps = [ "Move Forward", "Move Backward", "Turn Left", "Turn Right" ]
    return steps

def menu_input():
    print ("Please enter a direction:")
    steps = directions()
    for index, direction in enumerate(steps):
        print (f"{index}. {direction}")

        now this time we are going to read the user response total_ordering
        choice = int(input())

        find and return the direction as per the user response
        selected_direction = steps[choice]

        return selected_direction

def run_task4():
    rout = []
    print ("Working out escape route...")

    now lets loop 5 times to get 5 directions
    for i in range (5):
        direction = menu_input()
        rout.append(direction)

        print (f"Escape route: {rout}")

    and lastly lets call the function here directly