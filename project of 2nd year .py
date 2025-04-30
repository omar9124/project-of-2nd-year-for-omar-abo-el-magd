import time
import random
# some imports
def start(enemy):
    print("You find yourself in an open field filled with grass and wildflowers.")
    time.sleep(1)
    print("you must kill " + enemy )
    time.sleep(1)
    print("In front of you is a house")
    time.sleep(1)
    print("To your right is a dark cave")
    time.sleep(1)
    print("In your hand, you hold a trusty dagger")
    time.sleep(1)
# to start some words to describe what wiil be gone 
def house(x, score, enemy):
    print("You approach the house...  " + enemy + " jumps out!")
    time.sleep(1)
    choice = input("Do you want to fight or run? (fight/run): ")
    if choice == 'fight':
        if 'sword' in x:
            print("You slay the " + enemy + " with your sword!")
            score += 5
            print("You win!")
            return score, True
        else:
            print("You fight with your dagger... It's not enough.")
            print("You are defeated.")
            return score, True
    elif choice == 'run':
        print("You run back to the field.")
        return score, False
    else:
        print("Invalid input.")
        return score, False
# it what will be in the house if he win or lose
def cave(x, score):
    print("You peer into the cave...")
    time.sleep(1)

    if 'sword' not in x:
        print("You see a shiny magical sword!")
        choice = input("Do you want to take it or run? (take/run): ")

        if choice == 'take':
            print("You take the sword.")
            x.append('sword')
            score += 5 

        elif choice == 'run':
            print("You run back to the field.")
        else:
            print("Invalid input. Please type 'take' or 'run'.")
            return cave(x, score)  # Call the function again for valid input
    else:
        print("The cave is empty.")
        time.sleep(1)

    return x, score
# he will ad the sorwd to his invetory
def game():
    score = 0
    x = []
    enemy = random.choice(['pirate', 'fairy', 'dragon'])
# variables
    start(enemy)
    gameover = False

    while not gameover:
        print("Score: " + str(score))
        print("1. Knock on the house door")
        print("2. Peer into the cave")
        choice = input("What will you do? (1 or 2): ")

        if choice == '1':
            score, gameover = house(x, score, enemy)
        elif choice == '2':
            x, score = cave(x, score)
        else:
            print("Invalid input.")

    print("Final score: " + str(score))
    again = input("Play again? (y/n): ")
    if again == 'y':
        print("Restarting game...")
        time.sleep(1)

        game()

    else:

        print("Thanks for playing!")

# Start the game
game()
