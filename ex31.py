print(" you enter a dark room with two doors. \n do you go through door #1 or door #2? ")
door = input("door")
if door == "1":
    print("there is a giant bear here eating a cheese cake.")
    print("what do you do?")
    print("1. Take the cake.")
    print("2. scream at the bear")

    bear = input(">")

    if bear == "1":
        print("the bear eat your face off. Good job!")
    elif bear == "2":
        print("the bear eats your leg off. Good job!")
    else:
        print(f"well, doing {bear} is probably better.")
        print("bear ran away")

elif door == "2":
    print("you stare into the endless abyss at Cthulhu's rest")
    print("1. Blueberries")
    print("2. yellow jacket clothespines")
    print("3. Understanding revolovers yelling melodies")
    insanty = input(">")

    if insanty == "1" or insanty == "2":
        print("your body survives powered by a mind of jello)")
        print("good jobs!")
    else:
        print("the insanity rots your eyes into a pool of muse")
        print("good job!")

else:
    print("you stumble around and fall on a knife and die. Good job!")