# # import list
from random import randrange

# # map creation

# # character

# # enemy

# # items

# def main(): 

    # hero = character()
    
    # room()
    # return print(hero)
    
# def room():
    # print("A goblin guard stands in front of you.\n1 Fight him!\n2 Run for help.)")
    # action = int(input("Please enter number:\n> "))
    # #tell them what they do

# def character():

    # hitpoints = 0
    # hitpoints = randrange(0,10)
    
    # attack = 1

    # stats = [randrange(0,10), attack]
    # print(stats)
    
 # #   stats[0] = stats[0].randrange(0,10)
    





# stats = randrange(



# #main()

def main(): room_antichamber()


# NOTE(BCL): Consider looking up classes and using them for rooms, characters, maybe items
def room_antichamber():
    print('A goblin is here and attacks. 1 Fight 2 Run')
    action = input('> ')

# NOTE(BCL): After fight give chance to rest after fighting module is given
    
    if action == '1': 
        print ('Goblin dies, see three rooms. 1 Left, 2 Center, 3 Right')
        room_choice = input('> ')
        
        if room_choice == '1': return room_chest() #LEFT ROOM CHEST ROOM
        
        elif room_choice == '2': return room_slime() #CENTER ROOM SLIME ROOM
        
        elif room_choice == '3': return room_orc #RIGHT ROOM ORC ROOM
        
        else: pass #NEED TO CONSIDER OTHER ACTION WITH A WHILE LOOP TO GIVE ANOTHER CHANCE AT ACTION
    else:
        print('You run from the room and go looking for help to continue the fight.')
        return 0 # DEATH ENDING METHOD NEEDED
      
    
def room_chest(): 
    print('You see a chest. 1 Pick lock or 2 Leave alone')
    action = input('> ')
    
    if action == "1":
        print('You attempt to pick the lock...')
        lock_test = randrange(1,10)
        print(lock_test)
        lock_test = randrange(1,10)
        print(lock_test)
        lock_test = randrange(1,10)
        print(lock_test)
        lock_test = randrange(1,10)
        print(lock_test)
        lock_test = randrange(1,10)
        print(lock_test)
        
        
        #NOTE(BCL):THIS TEST IS NOT WORKING ONLY GOING TO THE ELSE STATEMENT EVEN CODED TO 
        if lock_test == 1:
            print('It explodes in your face hurting you') #NOTE(BCL):NEED TO REMOVE HP
            print('You return to the antichamber empty handed')
        elif 2 <= lock_test and lock_test <= 5:
            print('Despite your best efforts, you cannot quite get the lock to open. It seems like it is broken')
            print('You return to the antichamber empty handed.')
        else:
            print('You find a gleaming steel helmet, useful!')
            print('You put it on and return to the antichamber')


def room_slime(): return 0 

def room_orc(): return 0 

# THIS WORKS stat = randrange(0,10)



main()