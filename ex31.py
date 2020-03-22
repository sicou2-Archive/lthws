print("""You enter a dark room with two doors.\nDo you go through door "1" or door "2"?""")


door = input("> ")

if door == "1":
    print("There is a giant bear here eating a cheesecake.")
    print("What do you do?")
    print("'1' Take the cake.")
    print("'2' Scream at the bear.")
    
    bear = input("> ")
    
    if bear == "1":
        print("The bear is sad and claws your face off in a depressed rage. Good job!")
    elif bear == "2":
        print("The bear is terrified and mauls you in fear. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("The bear becomes bored and leaves. You now have some cake. Good job!")
        
elif door == "2":
    print("You suddenly discover yourself staring in to the endless infinity of Cthulhu's retina.")
    print("'1' Blue-ish berries")
    print("'2' Yellow jacket clothespins.")
    print("'3' Understanding revolvers yelling melodies.")
    
    insanity = input("> ")
    
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
        
else:
    print("You stumble around and fall on a knife and taste metal before darkness...")
    print("Good job!")
    
#Note(BCL): stopped just after writing and testing code