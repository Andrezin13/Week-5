def directions():
    steps = [
      "Move Forward",
      "Move Backward",
      "Turn Left",
      "Turn Right",
    ]
    return steps

def menu()
    print ("Please enter a direction:")
    steps = directions()
    for index, direction in enumerate(steps):
        print(f"{index+1}. {direction}")

def run_task3()
    menu()

run_task3()