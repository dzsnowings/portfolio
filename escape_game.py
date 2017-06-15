start = '''
You wake up and find yourself in a dark room. Your hands are tied, and the lights are off.
Choose your answers by typing a choice enclosed in ''.
'''

def giveUp():
    print('''You've decided to accept your fate or being trapped in this room forever.
    You rethink your life decisions for the next 5 minutes until a bomb in the room explodes and kills you.
    Whoops, what a tragic accident.''')

def bombBlack():
    print('''There are now 3 colored wires left on the bomb. Which wire would you like to cut?
    Choose 'red', 'brown', or 'white'.''')
    user_input = input().lower()
    if user_input == "red":
        bombRed()
    elif user_input == "brown":
        print('''You cut the correct wire! The countdown timer has stopped. However, you have not found the key to the door yet.
        Would you like to search the 'carpet' or 'give up'?''')
        user_input = input().lower()
        if user_input == "carpet":
            carpet()
        elif user_input == "give up":
            giveUp()
    elif user_input=="white":
        print ('''The white wire did not do anything the timer is still ticking. You have 3 minutes left.
        Would you like to cut another wire? Type 'yes' or 'no'.''')
        user_input = input().lower()
        if user_input == "yes":
            print("There are now only 2 wires left on the bomb. Which wire would you like to cut? Choose 'red' or 'brown'.")
            user_input = input().lower()
            if user_input == "red":
                bombRed()
            elif user_input == "brown":
                bombBrown()
        elif user_input == "no":
            print("Would you like to search the 'carpet' or 'give up'?")
            user_input = input().lower()
            if user_input == "carpet":
                carpet()
            elif user_input == "give up":
                giveUp()

def bombWhite():
    print('''There are now 3 colored wires left on the bomb. Which wire would you like to cut?
    Choose 'red', 'black', or 'brown'.''')
    user_input = input().lower()
    if user_input == "red":
        print("You cut the wrong wire. The bomb immediately displayed 00:00:00 and exploded. YOU HAVE DIED. Sorry. My, what a tragic accident.")
    elif user_input == "brown":
        bombBrown()
    elif user_input == "black":
        print ('''You cut the wrong wire. The bomb subtracted 2 minutes from the timer. It now displays 00:01:00. You only have 1 minute to escape.
        Would you like to cut another wire? Type 'yes' or 'no'.''')
        user_input = input().lower()
        if user_input == "yes":
            print('''There are now only 2 wires left on the bomb. Which wire would you like to cut?
            Choose 'red' or 'brown'.''')
            user_input = input().lower()
            if user_input == "red":
                bombRed()
            elif user_input == "brown":
                bombBrown()
        elif user_input == "no":
            print("Would you like to search the 'carpet' or 'give up'?")
            user_input = input().lower()
            if user_input == "carpet":
                carpet()
            elif user_input == "give up":
                giveUp()

def bombRed():
    print('''You cut the wrong wire. The bomb immediately displayed 00:00:00 and exploded.
    YOU HAVE DIED.
    Sorry.
    My, what a tragic accident.''')

def bombBrown():
    print('''You cut the correct wire! The countdown timer has stopped. However, you have not found the key to the door yet.
    Would you like to search the 'carpet' or 'give up'?''')
    user_input = input().lower()
    if user_input == "carpet":
        carpet()
    elif user_input == "give up":
        giveUp()

def bomb():
    print('''There are 4 colored wires on the bomb. Which wire would you like to cut with your wirecutter?
    Choose 'red', 'black', 'brown', or 'white'.''')
    user_input = input().lower()
    if user_input == "red":
        bombRed()
    elif user_input == "black":
        print('''You cut the wrong wire. The bomb subtracted 2 minutes from the timer. It now displays 00:01:00. You only have 1 minute to escape.
        Would you like to cut another wire? Type 'yes' or 'no'.''')
        user_input = input().lower()
        if user_input == "yes":
            bombBlack()
        elif user_input == "no":
            print("Would you like to search the 'carpet' or 'give up'?")
            user_input = input().lower()
            if user_input == "carpet":
                carpet()
            elif user_input == "give up":
                giveUp()
    elif user_input == "brown":
        bombBrown()
    elif user_input=="white":
        print ('''The white wire did not do anything the timer is still ticking. It now displays 00:03:00. You have 3 minutes to escape.
        would you like to cut another wire? Type 'yes' or 'no'.''')
        user_input = input().lower()
        if user_input == "yes":
            bombWhite()
        elif user_input == "no":
            print("Would you like to search the 'carpet' or 'give up'?")
            user_input = input().lower()
            if user_input == "carpet":
                carpet()
            elif user_input == "give up":
                giveUp()

def carpet():
    print('''You look under the carpet and find a key. You try it on the door, and the door unlocks.
    Congratulations, you have escaped the room!
    You open the door and find a long corridor with 12 colored doors. 
    To be continued...''')

def nightstand():
    print('''The nighstand opened! Inside it is a bomb displaying 00:05:00. You have 5 minutes to escape before it explodes.
    You freak out and panic for a full minute and are now left with only 4 minutes.
    Would you like to disarm the 'bomb', search the 'carpet', or 'give up'?''')
    user_input = input().lower()
    if user_input == "bomb":
        bomb()
    elif user_input == "carpet":
        carpet()
    elif user_input == "give up":
        giveUp()

def cabinet():
    print('''The cabinet opened! Inside it is a box that is nailed shut. You look around the cabinet and find a crowbar behind it.
    You pry the box open and find a key. Would you like to try the key on the 'door' or 'nightstand'?''')
    user_input = input().lower()
    if user_input == "door":
        doorKey2()
    elif user_input == "nightstand":
        nightstand()

def doorKey1():
    print ("The key did not work on the door. Would you like to try the key on the 'cabinet' or 'nightstand'?")
    user_input = input().lower()
    if user_input == "cabinet":
        cabinet()
    elif user_input == "nightstand":
        print("The key did not work for the nightstand. Would you like to try the key on the 'cabinet' or give up'?")
        user_input = input().lower()
        if user_input == "cabinet":
            cabinet()
        elif user_input == "give up":
            giveUp()

def doorKey2():
    print("The key once again did not work on the door. Would you like to try the key on the 'nightstand' or 'give up'?")
    user_input = input().lower()
    if user_input == "nightstand":
        nightstand()
    elif user_input == "give up":
        giveUp()

def bed():
    print('''You look under the bed and find a key and a wire cutter. You put the wire cutter in the middle of the room for later use.
    Would you like to test the key on the 'nightstand', 'cabinet', or 'door'?''')
    user_input = input().lower()
    if user_input == "cabinet":
        cabinet()
    elif user_input == "nightstand":
        print("The key did not work for the nightstand. Would you like to try the key on the 'cabinet' or the 'door'?")
        user_input = input().lower()
        if user_input == "cabinet":
            cabinet()
        elif user_input == "door":
            doorKey1()
    elif user_input =="door":
        doorKey1()

def findFlashlight():
    print('''You crawl around the room and find a flashlight. Lucky for you, it works! You see a cabinet and a bed in the room.
    Would you like to search the 'cabinet' or the 'bed'?''')
    user_input = input().lower()
    if user_input == "cabinet":
        print("To your dismay, the cabinet is locked. :( Would you like to go back and search the 'bed' or 'give up'?")
        user_input = input().lower()
        if user_input == "bed":
            bed()
        elif user_input == "give up":
            giveUp()
    elif user_input == "bed":
        bed()

def untieHands():
    print('''You successfully untie your hands after a few minutes of struggling.
    Do you want to find another light source or find the door? Type 'find flashlight' or 'door'.''')
    user_input = input().lower()
    if user_input == "find flashlight":
        findFlashlight()
    elif user_input == "door":
        print("The door is locked. Would you like to find a flashlight'or give up? Type 'find flashlight' or 'give up'.")
        user_input = input().lower()
        if user_input == "find flashlight":
            findFlashlight()
        elif user_input == "give up":
            giveUp()
















print(start)
print("Would you like to untie your hands or find a light switch? Type 'untie hands' or 'find light switch'.")
user_input = input().lower()
if user_input == "find light switch":
    print('''You feel around the walls and find the light switch. You turn it on and off, but it doesn't work.
    Would you like to try to untie your hands or give up? Type 'untie hands' or 'give up'.''')
    user_input = input().lower()
    if user_input == "untie hands":
        untieHands()
    elif user_input == "give up":
        giveUp()
elif user_input == "untie hands":
    untieHands()
