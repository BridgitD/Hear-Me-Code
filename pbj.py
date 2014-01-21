# Peanut Butter Jelly Time!

### IMPORTS AND GLOBALS
from sys import exit
import os

bread = 0
peanut_butter = 0
jelly = 0

# Welcome Screen
welcome1 = "LUNCH TIME!!!"

# Can you make a peanut butter and jelly sandwich?
def the_kitchen():
    print "Okay, we're in the kitchen."
    start = raw_input("Are you hungry for some PB&J? (Y/N) ")
    if start[0].upper() == "Y":
        print "Awesome! Let's get started!"
        ingredients()
    elif start[0].upper() == "N":
        print "More for me!"
        print "Bye!"
        exit(0)
    else:
        print "I'm not sure you answered the question..."
        the_kitchen()

### MAKING SANDWICHES ###

# Do you have the materials for a PB&J?
def ingredients():
    global bread, peanut_butter, jelly
    bread = int(raw_input("How many pieces of bread can you find? "))
    peanut_butter = int(raw_input("How many sandwiches worth of peanut butter do you have? "))
    jelly = int(raw_input("How many sandwiches worth of jelly do you have? "))
    if min(bread, peanut_butter, jelly) <= 0:
        print "Uh oh, looks like you're missing some ingredients."
        print "Shopping time!"
        shopping()
    elif min(bread, peanut_butter, jelly) > 0:
        print "Ok, let's make some sandwiches!"
        clear_screen()
        sandwiches()
    else:
        print "Hmm, I think you may have mistyped something..."
        print "Let's try again"
        ingredients()

# How many sandwiches can you make?
def sandwiches():
    global bread, peanut_butter, jelly
    sandwiches_possible = min((bread / 2), peanut_butter, jelly)
    openface_possible = min((bread % 2), peanut_butter, jelly)
    
    print "Let's see here..."
    print "..."
    
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
    elif sandwiches_possible == 0 and openface_possible > 0:
        print "You can't make a full sandwich, but..."
        openface()
    elif bread >= 1 and peanut_butter >= 1:
        print "You can't make a full PB&J, but..."
        pb_only()
    else:
        print "Looks like we're short some ingredients. Shopping time!"
        shopping()
        
# Can you make an open-face PB&J?
def openface():
    global bread, peanut_butter, jelly
    print "Lucky for you, we can make an open-face PB&J!"
    bread -= 1
    peanut_butter -= 1
    jelly -= 1
    still_hungry()

# Can you make an peanut butter sandwich?
def pb_only():
    global bread, peanut_butter
    pb_possible = min((bread / 2), peanut_butter)
    pb_open_possible = min((bread % 2), peanut_butter)
    
    if pb_possible > 0:
        print "You could have {0} peanut butter-only sandwich(es)...".format(pb_possible)
        choice = raw_input("Want one? (Y/N)")
        if choice[0].upper() == "Y":
            print "I mean, if you really insist..."
            still_hungry()
        elif choice[0].upper() == "N":
            print "Good choice. Peanut butter only sandwiches aren't as good as PB&J."
            print "Let's go shopping instead."
            shopping()
    elif pb_open_possible > 0:
        print "You could have {0} peanut butter-only open-face sandwich...".format(pb_open_possible)
        choice = raw_input("Want it? (Y/N)")
        if choice[0].upper() == "Y":
            print "Ugh, I suppose that's a lunch..."
            still_hungry()
        elif choice[0].upper() == "N":
            print "Good choice. Peanut butter only sandwiches just aren't as good as PB&J."
            print "Let's go shopping instead."
            shopping()

# Are you still hungry?
def still_hungry():
    give_me_more = raw_input("Are you still hungry? (Y/N)" )
    if give_me_more[0].upper() == "Y":
        sandwiches()
    elif give_me_more[0].upper() == "N":
        print "Ok! Until next time!"
        exit(0)
    else:
        "I'm not sure you answered the question..."
        still_hungry()

### SHOPPING ###

# Shopping Time!
def shopping():
    clear_screen()
    print "Welcome to the grocery store!"
    what_to_buy()

def what_to_buy():
    global bread, peanut_butter, jelly
    if min(bread, peanut_butter, jelly) <= 0:
    
        # Do you need bread?
        if bread < 1:
            print "You need to buy some bread."
        elif bread < 2:
            print "If you want more than just an open-face sandwich, you should buy bread."
        else:
            print "We're good on bread."

        # Do you need peanut butter?
        if peanut_butter < 1:
            print "You need to buy some peanut butter."
        else:
            print "We're good on peanut butter."
    
        # Do you need jelly?
        if jelly < 1:
            print "You need to buy some jelly."
        else:
            print "We're good on jelly."
    
        # What do you want to buy?
        buying()
    
    else:
        print "I think you bought enough. Let's go back to the kitchen."
        sandwiches()
    
def buying():
    global bread, peanut_butter, jelly
    choice = raw_input("What should we pick up first? (Bread/Peanut Butter/Jelly) ")
    if choice[0].upper() == "B":
        new_bread = int(raw_input("How many slices should we buy?"))
        bread += new_bread
        clear_screen()
        print "Great, you bought some bread."
        what_to_buy()
    elif choice[0].upper() == "P":
        new_pb = int(raw_input("How much peanut butter should we buy?"))
        peanut_butter += new_pb
        clear_screen()
        print "Great, you bought some peanut butter."
        what_to_buy()
    elif choice[0].upper() == "J":
        new_jelly = int(raw_input("How much jelly should we buy?"))
        jelly += new_jelly
        clear_screen()
        print "Greay, you bought some jelly."
        what_to_buy()
    
### SETUP ###

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
