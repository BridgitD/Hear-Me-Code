# Peanut Butter Jelly Time!

from sys import exit
import os

# Welcome Screen
welcome1 = "LUNCH TIME!!!"

# Can you make a peanut butter and jelly sandwich?
def the_kitchen():
    start = raw_input("Are you hungry for some PB&J? (Y/N) ")
    if start[0].upper() == "Y":
        print "Awesome! Let's get started!"
        bread()
    elif start[0].upper() == "N":
        print "More for me!"
        print "Bye!"
        exit(0)
    else:
        print "I'm not sure you answered the question..."
        the_kitchen()

# Do you have enough bread?
def bread():
    global bread, bread_per_sandwich, leftover_bread
    bread = int(raw_input("How many pieces of bread can you find? "))
    if bread <= 0:
        print "Well, you can't get very far without bread..."
        print "Guess we need to go shopping"
        exit(0)
        #shopping()
    elif bread > 0:
        bread_per_sandwich = bread / 2
        leftover_bread = bread % 2
        peanut_butter()
    else:
        print "I don't think you entered a number. Try again."
        bread()

# Do you have peanut butter and jelly?
def peanut_butter():
    global peanut_butter
    peanut_butter = int(raw_input("How many sandwiches worth of peanut butter do you have? "))
    if peanut_butter <= 0:
        print "NO PEANUT BUTTER!?"
        print "Shopping time!"
        exit(0)
        #shopping()
    else:
        jelly()

def jelly():
    global jelly
    jelly = int(raw_input("How many sandwiches worth of jelly do you have? "))
    if jelly <= 0:
        print "What's PB&J without the J!?"
        print "Time to go shopping"
        exit(0)
        #shopping()
    else:
        making_sandwiches()

# How many sandwiches can you make?
def making_sandwiches():
    global bread_per_sandwich, peanut_butter, jelly, sandwiches_possible, bread
    sandwiches_possible = min(bread_per_sandwich, peanut_butter, jelly)
    
    if sandwiches_possible > 1:
        print "You can make {0} sandwiches! Find friends and share!".format(sandwiches_possible)
        peanut_butter -= sandwiches_possible
        jelly -= sandwiches_possible
        bread -= (sandwiches_possible * 2)
        still_hungry()
    elif sandwiches_possible == 1:
        print "You can make {0} sandwich!".format(sandwiches_possible)
        peanut_butter -= sandwiches_possible
        jelly -= sandwiches_possible
        bread -= (sandwiches_possible * 2)
        still_hungry()
    else:
        print "Hmm, it seems we have more shopping to do..."
        exit(0)
        #shopping()

# Are you still hungry?
def still_hungry():
    give_me_more = raw_input("Are you still hungry? (Y/N)" )
    if give_me_more[0].upper() == "Y":
        open_face()
    elif give_me_more[0].upper() == "N":
        print "Ok! Until next time!"
        exit(0)
    else:
        "I'm not sure you answered the question..."
        still_hungry()

# Can you still make some open face sandwiches?
def open_face():
    global leftover_bread, peanut_butter, jelly, bread
    openface_possible = min(leftover_bread, peanut_butter, jelly)
    if openface_possible > 0:
        print "Okay! Lucky for you, there's still enough for an openface PB&J!"
        leftover_bread -= openface_possible
        peanut_butter -= openface_possible
        jelly -= openface_possible
        bread -= openface_possible
        still_hungry()
    else:
        print "Grocery store time then!"
        exit(0)
        #shopping()
    
#Clear Screen
def clear_screen():
    if clear:
        os.system('clear')
    else:
        print "and..."

# New Game
def start_game():
    clear_screen()
    print welcome1
    the_kitchen()

# Start
clear = True
start_game()
