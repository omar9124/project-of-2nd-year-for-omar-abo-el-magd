import time
import random

# Clean input validator
def valid_input(prompt, options):
    while True:
        response = input(prompt).strip().lower()
        if response in options:
            return response
        print("Invalid input. Try again.")

# Introduce the game setting and initial scene
def start(enemy):
    print("Defeat the enemy or collect enough points to win!")
    time.sleep(1)
    print("You find yourself in an open field filled with grass and wildflowers.")
    time.sleep(1)
    print(f"You must defeat a {enemy}.")
    time.sleep(1)
    print("In front of you is a house.")
    time.sleep(1)
    print("To your right is a dark cave.")
    time.sleep(1)
    print("In your hand, you hold a trusty dagger.")
    time.sleep(1)

# Logic for entering and exploring the house
def explore_house(x, score, enemy):
    print(f"You approach the house... A {enemy} jumps out.")
    time.sleep(1)

    choice = valid_input("Do you want to fight or run? (fight/run): ", ["fight", "run"])
    if choice == 'fight':
        if 'sword' in x:
            print(f"You slay the {enemy} with your sword.")
            score += 5
            print("You win!")
            return score, True
        else:
            print("You fight with your dagger... It's not enough.")
            print("You are defeated.")
            return score, True
    else:  # run
        print("You run back to the field.")
        return score, False

# Logic for entering and exploring the cave
def explore_cave(x, score):
    print("You peer into the cave...")
    time.sleep(1)

    if 'sword' not in x:
        print("You see a shiny magical sword.")
        choice = valid_input("Do you want to take it or run? (take/run): ", ["take", "run"])
        if choice == 'take':
            print("You take the sword.")
            x.append('sword')
            score += 5
        else:
            print("You run back to the field.")

    else:
        print("The cave is empty.")
        time.sleep(1)

    return x, score

# Main game loop function
def adventure_game():
    score = 0
    x = []
    enemy = random.choice(['pirate', 'fairy', 'dragon'])
    max_turns = 5
    turns = 0
    game_over = False

    start(enemy)

    while not game_over and turns < max_turns:
        print(f"\nTurn {turns + 1} of {max_turns}")
        print(f"Score: {score}")
        print("1. Knock on the house door")
        print("2. Peer into the cave")

        choice = valid_input("What will you do? (1 or 2): ", ["1", "2"])
        if choice == '1':
            score, game_over = explore_house(x, score, enemy)
        elif choice == '2':
            x, score = explore_cave(x, score)

        # Hero win condition
        if score >= 10 and not game_over:
            print("You have become the hero of the land!")
            game_over = True

        turns += 1

    # Game result if not ended by game_over
    if not game_over:
        print("\nThe journey has ended. Let's see how you did...")
        if score >= 10:
            print("You are victorious. Your courage led to success.")
        elif score >= 5:
            print("You survived, but challenges remain.")
        else:
            print("You failed to make your mark this time.")

    print(f"Final score: {score}")
    print(f"Total turns taken: {turns}")

    # Ask if the player wants to play again
    again = valid_input("Play again? (y/n): ", ["y", "n"])
    if again == 'y':
        print("Restarting game...\n")
        time.sleep(1)
        adventure_game()
    else:
        print("Thanks for playing!")

# Start the game
adventure_game()
