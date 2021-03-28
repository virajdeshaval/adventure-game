#
# Project: Adventure game
#
# A text-based adventure game in an Open Field, filled with grass and yellow wildflowers.
#
# Author: Viraj Deshaval
# Created on 15th Feb. 2021
#
import time
import random

# Function created to add pauses
def print_pause(prompt, seconds=2):
    print(prompt)
    time.sleep(seconds)

# Introduction function to show the intro.
def intro(monster):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {monster} is somewhere around here, "
                "and has been terrifying the nearby village.", 3)
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective) dagger.\n")

# Fight with monster or run away from monster
def fight_run(monster, sword):
    if sword == "dagger":
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny dagger.")
        response = input("Would you like to (1) fight or (2) run away?\n> ")
        if response == "1":
            print_pause("You do your best...")
            print_pause(f"but your dagger is no match for the {monster}.")
            print_pause("You have been defeated!", 1)
            play_again()
        elif response == "2":
            field(monster, sword)
        else:
            fight_run(monster, sword)
    elif sword == "magical sword":
        response = input("Would you like to (1) fight or (2) run away?\n> ")
        print("")
        if response == "1":
            print_pause(f"As the {monster} moves to attack, "
                        "you unsheath your new sword.")
            print_pause("The Sword of Ogoroth shines brightly "
                        "in your hand as you brace yourself "
                        "for the attack.")
            print_pause(f"But the {monster} takes one look at "
                        "your shiny new toy and runs away!")
            print_pause(f"You have rid the town of the {monster}. "
                        "You are victorious!")
            play_again()
        elif response == "2":
            field(monster, sword)
        else:
            fight_run(monster, sword)

# Kick starts the game
def play_again():
    response = input("Would you like to play again? (y/n)\n> ").lower()
    print("")
    if response == "y":
        adventure_game()
    elif response == "n":
        print_pause("Thanks for playing! See you next time.")
        print("exiting ", end="", flush=True)
        for n in range(3):
            time.sleep(1)
            print(".", end="", flush=True)
    else:
        play_again()


def house(monster, sword):
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door "
                f"opens and out steps a {monster}")
    print_pause(f"Eep! This is the {monster}'s house!")
    print_pause(f"The {monster} attacks you!")
    fight_run(monster, sword)


def cave(monster, sword):
    print_pause("You peer cautiously into the cave.")
    if sword == "dagger":
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger "
                    "and take the sword with you.")
        sword = "magical sword"
    elif sword == "magical sword":
        print_pause("You've been here before, and gotten "
                    "all the good stuff. It's just an empty cave now.")
    print_pause("You walk back out to the field.\n")
    field(monster, sword)


def choices(monster, sword):
    choice = input("(Please enter 1 or 2.)\n> ")
    print("")
    if choice == "1":
        house(monster, sword)
    elif choice == "2":
        cave(monster, sword)
    else:
        choices(monster, sword)


def field(monster, sword):
    print_pause("Enter 1 to knock on the door of the house.", 1)
    print_pause("Enter 2 to peer into the cave.", 1)
    print_pause("What would you like to do?", 1)
    choices(monster, sword)


def adventure_game():
    monsters = ['troll', 'wicked fairie', 'pirate', 'gorgon', 'dragon']
    monster = random.choice(monsters)
    sword = "dagger"

    intro(monster)
    field(monster, sword)


adventure_game()
