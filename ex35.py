from sys import exit
def gold_room():
    print("this room is full of gold. how much do you take?")

    choice = input(">")
    if int(choice) > 0:
        how_much = int(choice)
    else:
        dead("man, learn to type a number.")
    
    if how_much < 50:
        print("nice! you are not greedy, you win!")
        exit(0)

    else:
        dead("you greedy bastard!")

def bear_room():
    print("there is a bear here")
    print("the bear has a bunch of honey")
    print("the fat bear is in front of another door")
    print("how are you going to move the bear")
    bear_move = False

    while True:
        choice = input(">")

        if choice == "take honey":
            dead("the bear look at you then slaps your face")
        elif choice == "taunt bear" and not bear_move:
            print("the bear has moved from the door")
            print("you can get throught it now")
            bear_move = True
        elif choice == "taunt bear" and bear_move:
            print("the bear get pissed off and chew your legs")
        elif choice == "open door" and bear_move:
            gold_room()
        else:
            print("i got no idea what that means")

def cth_room():
    print("here you see the great evil Cthulhu")
    print("he, it, whatever stares at you and you go insane.")
    print("do you flee for your life or eat your head?")

    choice = input(">")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "good job!")
    exit(0)

#初始房間
def start():
    print("you are in a dark room")
    print("there is a door to your right and left")
    print("which one do you take?")

    choice = input(">")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cth_room()
    else:
        dead("you stumble around the room until you starve")

start()