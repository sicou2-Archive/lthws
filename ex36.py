from random import randint
from sys import exit

# map creation
#https://stackoverflow.com/questions/53017026/how-can-i-access-list-values-in-a-dictionary

# items

#NEED TO DO STORY CLEAN UP 

# DUNGEON PLAN FOR LATER
# ANTICHAMBER ROOM
# |
# |
# CHEST ROOM  or   SLIME ROOM   or  (LOCKED) ORC ROOM
# +1 armor     1 Sword and KEY          /  
                                      #/  
                            # BUGBEAR HALLWAY    or    ALTER IN ORC ROOM 
                               #/                           +5 HP                 
                             #/     
           # CRYPT IN BUGBEAR ROOM ----> IGNORE CRYPT ----> EXIT DUNGEON
                      # |
                      # |
           # FIND JEWLES IN CRYPT ---> SKELETON ATTACK ---> EXIT DUNGEON
                                                            
# NOTE(BCL): Consider looking up classes and using them for rooms, 
# characters, maybe items

######STOPPED LINE 367

def main(): 
    
    cast = {}
    
    try:
        cast['hero']
    except KeyError:
        hero = character(10, 1, 1, 1,'hero')
        cast['hero'] = hero
    try:
        lockout
    except NameError:
        lockout = {'chest_room': 1, 'slime_room': 1, 'orc_room' : 1}

    room_hallway(cast)
#    room_antichamber(cast, lockout)    
        
def room_antichamber(cast, lockout):
# NOTE(BCL): NEED A REST TO MAXHP
#ADD TO STORY LOOKING FOR JEWLES
    try:
        cast['goblin']
    except KeyError:
        goblin = character(5, 1, 1, 1,'goblin')
        cast['goblin'] = goblin
        


    if cast['goblin'][3] == 1:
        print('A goblin is here and attacks. 1 Engage in combat 2 Run')
        i = 0
        
        while True:    
            action = input('> ')
        # NOTE(BCL): After fight give chance to rest after fighting module is given
           
            if action == '1': 
                fight(cast['hero'], cast['goblin'])
                print('Above the body of your foe, you look around.')
                break
            elif action == '2':
                print('You run from the room and go looking for help '
                'to continue the fight.')
                return end_game()
            elif i > 3:
                print('Goblin attacks while you stare at him.')
                return end_game()
            else:
                print('He looks mean, do something! Quick!')
                i += 1    
    
    print ('You see three doors. Choose a door (1 Left, 2 Center, 3 '
        'Right) or rest (4). ')
            
    while True:
        room_choice = input('> ') #this variable should be changed to 
        #choice since room + rest is now an option
        print
        if room_choice == '1': 
            if lockout['chest_room'] == 0:
                print('There is no reason to go back in there. Choose '
                'a different room.')
                continue
            return room_chest(cast, lockout) 
        elif room_choice == '2': 
            if lockout['slime_room'] == 0:
                print('There is no reason to go back in there. Choose '
                'a different room.')
                continue
            return room_slime(cast, lockout) 
        elif room_choice == '3': 
            if lockout['orc_room'] == 0:
                print('There is no reason to go back in there. Choose '
                'a different room.')
                continue
            return room_orc(cast) #RIGHT ROOM ORC ROOM
        elif room_choice == '4':
            if cast['hero'][0] >= 10: #MAX HP HERE ONCE INSTALLED
                print('You feel as rested as you can be. Time to move '
                'on.')
                continue
            else:
                print('You take a moment to catch your breath. You feel'
                ' as strong as you are going to get for now.')
                cast['hero'][0] += 5 #This needs max hp once installed
            continue
        else: 
            print('Moving on is the only hope for you now. Choose a '
            'room.') 
        
def room_chest(cast, lockout): 
   
    print('You see a chest. 1 Pick lock, 2 Leave alone and return to '
    'antichamber, 3 Rest a moment')
    
    while True: #NOTE(BCL): MAYBE A STATEMENT OF SOME KIND HERE TO SKIP 
    #THE CHEST AND RETURN TO AC
        action = input('> ')
        
        if action == '1':
            print('You attempt to pick the lock...')
            lock_test = randint(1,10)
            
            if lock_test == 1:
                print('It explodes in your face hurting you') 
                #NOTE(BCL):NEED TO REMOVE HP
                cast['hero'][0] -= randint(1,5) #NOTE(BCL): NEED TO 
                #COME BACK AND MAKE THIS FAIR SO NOT RANDO KILL PLAYER, 
                #NEED A CHANCE TO REST IN ANTICHAMBER
                if cast['hero'][0] == 0:
                    return end_game()
                lockout['chest_room'] = 0
                print('You return to the antichamber empty handed')
                return room_antichamber(cast, lockout)
            elif 2 <= lock_test and lock_test <= 5:
                print('Despite your best efforts, you cannot quite get '
                'the lock to open. It seems like it is broken')
                print('You return to the antichamber empty handed.')
                lockout['chest_room'] = 0
                return room_antichamber(cast, lockout)
            else:
                print('You find a gleaming steel helmet, useful!') 
                #NOTE(BCL): NEED TO +1 DEFENCE EVENTUALLY ONCE RAND 
                #IS INSTALLED
                print('You put it on and return to the antichamber')
                cast['hero'][1] += 1
                lockout['chest_room'] = 0
                return room_antichamber(cast, lockout)
                
        elif action == '2':
            print('After looking around and seeing no danger, you '
            'return to the antichamber.')
            return room_antichamber(cast, lockout)
        elif action == '3': 
            print('You take a few moments to gather your strength and '
            'mind. You feel better.')
            cast['hero'][0] += 5  #NOTE(BCL): THIS PROBABLY SHOULD NOT 
            #RETURN TO ANTIC AND SHOULD LOOP TO TOP TO GIVE PICKING LOCK
            #ANOTHER CHANCE BEFORE LEAVING
            #NOTE(BCL): DO NOT LOOP THIS UNTIL MAX HP IS INSTALLED 
            #NOTE(BCL): MAYBE NOT REST IN HERE AT ALL SINCE REST IN 
            #ANTICHAMBER
            return room_antichamber(cast, lockout) 
            #NOTE(BCL): WITH FIGHT MODULE RANDOM THIS SHOULD RESTORE 
            #HP TO FULL
        else:
            print('You should get a move on. What would you like to '
            'do?')           
        
def room_slime(cast, lockout): 
    print('Enter and a Slime is quietly digesting a large body. 1 '
    'Attack the Slime, 2 Taunt the Slime, 3 Quietly back out of room')
    i = 0
    
    while True:
        action = input('> ')
        
        if action == '1':
            #print('You ferociously attack and kill the Slime. Under 
            #the body it had just started to eat you find a sharp sword.
            #You put your dagger in to your pack and return to the 
            #antichamber.')
            #NEED TO UPDATE THE COMBAT TEXT HERE
            print('Fight slime')
            cast['slime'] = character(3, 1, 1, 1, 'slime')
            fight(cast['hero'], cast['slime'])
            print('Dead foe, sword get.')
            cast['hero'][2] += 1
            lockout['slime_room'] = 0
            return room_antichamber(cast, lockout) #NOTE(BCL): NEED TO 
            #+1 ATTACK ONCE RAND COMBAT IS INSTALLED, ALSO MAYBE GIVE 
            #KEY TO OPEN ORC DOOR? 
        elif action == '2':
            print('You taunt the slime and it starts to follow you '
            'around the room. Much faster than it you quickly inspect '
            'the fresh body it had started to eat and you find a sharp '
            'sword.')
            print('You quickly grab the sword while stowing your dagger'
            ' and return to the antichamber before the slime can catch '
            'up to you.') #NOTE(BCL): MAYBE NOT GIVE SWORD, RATHER 
            #JUST KEY, HOWEVER...
            # I LIKE THE WHOLE NOT KILLING JUST TO KILL, SO MAYBE NOT.
            cast['hero'][2] += 1            
            lockout['slime_room'] = 0
            return room_antichamber(cast, lockout)
        elif action == '3':
            print('Seemingly content with its current meal the Slime '
            'ignores you as you silently back out of the room back in '
            'to the antichamber.')
            return room_antichamber(cast, lockout)
        elif i > 3:
            print('Suddenly from the ceiling above another Slime plops '
            'down crushing you to the floor.')
            print('In its belly, you will find a new definition of '
            'pain and suffering, as you are slowly digested over a '
            'thousand years.')
            return end_game()
        else:
            print('That slime looks like it might almost be done '
            'digesting that body, you should make a decision before it '
            'does. What would you like to do?')
            i += 1

    return 0 
    
def room_orc(cast): 
    print('As you unlock and enter the door, you see a fierce orc '
    'worshiping at an alter. Further in to the room you see a dark '
    'hallway. \n1 Attack the Orc, 2 Attempt to sneak to the hallway, 3 '
    'Gently close the door and return to the Antichamber.')
    
    try:
        cast['orc']
    except KeyError:
        orc = character(5, 1, 1, 1,'orc')
        cast['orc'] = orc
        
    i = 0
    while True:
        action = input('> ')
        if action == '1': 
            print('You move in to attack the orc as he stands to '
            'fight!')
            fight(cast['hero'], cast['orc'])
            return 0 #need to resolve the fight and offer hallway
            # or alter OR REST A MOMENT
        elif action == '2': 
            print('You sneak towards the hallway.')
            
            sneak_roll = randint(1,4)
            
            if sneak_roll == 4:
                print('You hear the Orc\'s prayers trail off. As you '
                'look back you both make eye contact. He raises his '
                'sword to attack!')
                fight(cast['hero'], cast['orc'])
                #need to resolve the fight and offer the alter
            else:
                print('You silently enter the hallway and make your way'
                ' into the damp and dark.')
                return room_hallway()
            return 0
        elif action == '3': 
            print('You back in to the Antichamber and slowly let the '
            'latch down.')
            return room_antichamber(cast) 
        elif i == 3:
            print('The Orc glances at the door. As you make eye contact'
            ' he raises his sword to attack!')
            fight(cast['hero'], cast['orc'])
            return 0 #resolve fight and offer alter
        else: 
            print('Hurry! Make a decision. He might notice you!') 
        
    return 0 
    
def room_hallway(cast): 
    
    try:
        cast['bugbear']
    except KeyError:
        bugbear = character(5, 1, 1, 1,'bugbear')
        cast['bugbear'] = bugbear
        
    print("As you walk down the hallway, suddenly out of the darkness "
          "a giant lumbering Bugbear appears out of the darkness. 1 "
          "Attack 2 Retreat in to the shadows")
    action = input("> ")
          
    if action == '1':
        print("You lunge forward to attack!")
        fight(cast['hero'], cast['bugbear'])
        print("after combat move forward in to the crypt")
        return room_crypt(cast)
    elif action == '2':
        print("It seems he cannot see very well in the dark as "
        "you disappear back in to the shadows")
        #NEED TO RESOLVE EITHER GOING BACK IN TO THE ORC ROOM
        #OR HIDING TO REST A MOMENT
        return 0
    
    return 0 

def room_crypt(cast): 
    
    try:
        cast['skeleton']
    except KeyError:
        skeleton = character(5, 1, 1, 1,'skeleton')
        cast['skeleton'] = skeleton
        
    print("Walk in to an empty chamber with a well kept crypt and set "
        "of stairs leading up to a large door. 1 Inspect Crypt 2 Go up"
        "stairs 3 Rest a moment") #Return to other rooms?
    action = input("> ")
    
    while True:
        if action == '1': 
            print("Move to inspect crypt, see gems. 1 Take gems 2 Leave"
            " alone"
            if choice == '1':
                print("You take the flawless gems and put them in to "
                "your pack. As you close the bag you look up and see a "
                "skeleton coming up out of the crypt. 1 Attack 2 Run "
                "toward the stairs 3 Run toward the hallway")
                #GEM GET FOR DIFFERENT ENDING?
                false_choice = input("> ")
                
                if false_choice == '1':
                    print("You bravely defend your life and treasure!")
                    fight(cast['hero'], cast['skeleton'])
                    print("Dead skelly, go up stairs")
                    return room_exit(cast)
                elif false_choice == '2' or false_choice == '3':
                    print("You start to run, but you feel a spell "
                    "freeze your feet in place. You turn to fight for "
                    "your life and treasure!")
                    fight(cast['hero'], cast['skeleton'])
                    print("Dead skelly, go up stairs")
                else:
                    print("Your indecision costs you your life and "
                    "treasure!")
                
                
            return 0 
        elif action == '2': 
            print("You ignore the crypt and move up the stairs. After "
            "a moment pushing, you manage to open the heavy stone door "
            "and see out in to the wilderness.")
            end_game(cast)

            return 0 
        elif action == '3': 
            rest(cast['hero']
            continue
        else: 
#######STOPPED HERE NEED TO LOOP TO TOP###########            
            return 0 
        

    return 0 

def room_exit(): return 0 

def character(health, defence, attack, alive, name): #maybe use dicts 
#here? # IS THIS THE BEST FUNCTION TO DO THIS? WHY NOT JUST PASS INFO 
#TO THE CAST DICT?
    stats = [health, defence, attack, alive, name]
    #maybe max hp and current hp for resting? 
    # hitpoints = 0
    # hitpoints = randrange(0,10)
    
    # attack = 1

    # stats = [randrange(0,10), attack]
    # print(stats)
    
    return stats 

def fight(hero_stats, enemy_stats): 
   # EXPAND COMBAT FOR MORE INFO AND !FUN!
    i = 0   
    while True:
        print('You engage in combat! 1 Fight or 2 Run')
        action = input('> ')
        if action == '1':
            
            print('You attack!')
            hero_stats[0] -= enemy_stats[2]
            enemy_stats[0] -= hero_stats[2]
            print(hero_stats, enemy_stats)
            if hero_stats[0] == 0:
                'You fall bravely in battle.'
                return end_game()       
            elif enemy_stats[0] == 0:
                print(f'You slay the enemy {enemy_stats[4]}')
                enemy_stats[3] = 0
                return (hero_stats, enemy_stats)
            else:
                print('The combat continues!')
        elif action == '2':
            print('You retreat from the battle!') #NOTE(BCL): THIS NEEDS
#            TO RETURN TO A PREVIOUS ROOM OR LEAVE IF IN ANTI-C
            return end_game() 
        elif i == 4:
            print('You block and block the attacks coming from your '
            'for, but eventually you are overwhelmed.')
            return end_game()
        else:
            print('Do not hesitate! Do something, anything!')
            i +=1
    return 0 

def rest(hero):return 0 

def end_game(cast): 
    print('Game over man. Game over! Play again? "y/n"')
    choice = input('> ')
    if choice == 'y':
       main()
    elif choice == 'n':
       exit()
    else:
        while True:
            print('Would you like to play again? "y/n"')
            choice = input('> ')
            if choice == 'y':
                main()
            elif choice == 'n':
                exit()
            else:
                pass
    return 0 

main()

#main_debug() #NOTE(BCL): LEAVE ME COMMENTED WHEN NOT NEEDED