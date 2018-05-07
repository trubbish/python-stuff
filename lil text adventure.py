import random
import time

def displayIntro():
    print()
    print("You're hiking in the woods, and you come across")
    print("a fork in the road. One path will kill you while the")
    print("other path with lead to treasure beyond your wildest")
    print("dreams. Good luck!")
    print()

def choosePath():
    path = ""
    while path != "1" and path != "2":
        path = input("Which path will you choose? (1 or 2): ")

    return path

def checkPath(chosenPath):
    print("You head down the path cautiously.")
    time.sleep(2)
    print("You don't see anything deadly, so you keep going.")
    print()
    time.sleep(2)

    correctPath = random.randint(1, 2)

    if chosenPath == str(correctPath):
        print("You find a pile of gold resting next to a priceless artifact.")
        print("You're rich!")
        time.sleep(10)
    else:
        print("You step on a plate that sinks into the ground.")
        print("Dart traps go off in every direction and you")
        print("are hit repeatedly. Your body is never found.")
        time.sleep(10)

playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    choice = choosePath()
    checkPath(choice)