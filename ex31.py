def main():
    print("""You enter a dark room with two doors.\nDo you go through door "1" or door "2"?""")
    door = input("> ")
    
    if door == "1": return door_1()
    
    elif door == "2": return door_2()
    
    else:
        print("You start to get bored with your indecision. You think that you should really get a move on.\n\n")
        return main()
    
def door_1(): 

    print("There is a giant bear here eating a cheesecake.")
    print("What do you do?")
    print("'1' Take the cake.")
    print("'2' Scream at the bear.\n")
    
    bear = input("> ")
    
    if bear == "1": return bear_1()
        
    elif bear == "2": return bear_2()
       
    else: return bear_3(bear)
      
def bear_1():
    print("The bear is sad and claws your face off in a depressed rage. Good job!\n")
    return death()
 
def bear_2():
    print("The bear is terrified and mauls you in fear. Good job!\n")
    return death()
 
def bear_3(bear):
    print("You quietly sneak to the corner and huddle terrified.")
    print(f"Well, doing {bear} was probably better.")
    print("The bear becomes bored and leaves. You now have some cake. Good job!")
    print("Would you like to finish your cake ('1') or go back and look at door two ('2')?\n")
    
    choice = input("> ")
    
    if choice == "1": return cake()
    
    else: return door_2()
    
 
def door_2(): 

    print("You suddenly discover yourself staring in to the endless infinity of Cthulhu's retina.")
    print("'1' Blue-ish berries")
    print("'2' Yellow jacket clothespins.")
    print("'3' Understanding revolvers yelling melodies.\n")
    
    insanity = input("> ")
    
    if insanity == "1" or insanity == "2": return cthulhu_1_and_2()

    elif insanity == "3": return cthulhu_3()

    else:
        return cthulhu_4()
        
        
def cthulhu_1_and_2(): 
        print("Your body survives powered by a mind of jello.")
        print("Good job!\n")
        return death()

def cthulhu_3(): 

    print("The insanity rots your eyes into a pool of muck.")
    print("Good job!\n")
    return death()

def cthulhu_4():
    print("You snap your eyes shut and flee with the sound of blissful insanity causing you to forget the cute kitten.\n")
    return main()


def cake():
    print("You slowly manage to eventually eat the bear sized cheesecake, when you suddenly hear the bear return with his big brother...\n\n")
    print("They offer you shelter and nourishment and you manage to escape and return to your family in the Nexus.\n")
    return death()

def death():
    print("Would you like to play again? y/n\n")
    again = input("> ")
    
    if again == "y": return main()
    
    else:
        print("Thanks for playing! Good-bye\n")
        quit()

# else:
    # print("You stumble around and fall on a knife and taste metal before darkness...")
    # print("Good job!")
    

main()

# Note(BCL): Maybe make classes for the different rooms