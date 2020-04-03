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
# NOTE(BCL): AM GOING TO USE CLASSES FOR ROOMS AND THE LIKE FOR THE 
# EX43.PY PROJECT 

# NOTE(BCL): NEED TO COMMENT ALL OF THE DIFFERENT PARTS OF THE CODE FOR
# FUTURE BCL. HE IS AN ANGRY AND FORGETFUL FOE

# NOTE(BCL): CHECK TO SEE IF YOU CAN LOCKOUT PLAYER FROM ANTIROOM AFTER 
# KILLING ORC AND ALL GEAR FROM ANTICHAMBER IS FOUND

# TODO(BCL): CREATE SOME KIND OF GAME BALANCE FOR THE COMBAT BITS

# TODO(BCL): CREATE SOME KIND OF RANDOMIZATION TO COMBAT WITH SOME 
# FLAVOR TEXT AND INFO AS TO THE STATUS OF THE PLAYER

# TODO(BCL): LOOK IN TO SOME OF THE LATER GAME TRACEBACK FILES. IT MIGHT
# BE THAT I AM DOING THE ARGUMENT CALLS WRONG GOING FROM ANTI TO ALL 
# OF THE OTHER PLACES IN THE GAME. 
# FOR EXAMPLE:
#Traceback (most recent call last):
  # File "ex36.py", line 577, in <module>
    # main()
  # File "ex36.py", line 63, in main
    # room_antichamber(cast, lockout)
  # File "ex36.py", line 117, in room_antichamber
    # return room_slime(cast, lockout)
  # File "ex36.py", line 206, in room_slime
    # return room_antichamber(cast, lockout)
  # File "ex36.py", line 119, in room_antichamber
    # return room_orc(cast, lockout) #MAYBE NEED TO ADD A KEY
  # File "ex36.py", line 261, in room_orc
    # fight(cast['hero'], cast['orc'])
  # File "ex36.py", line 518, in fight
    # return end_game()
  # NameError: name 'cast' is not defined
  
# I AM NOT SURE BUT IT SEEMS LIKE WE ARE JUST ADDING ROOMS TO THE STACK
# INSTEAD OF LEAVING ONE AND GOING TO THE NEXT
# UPDATE: THIS IS EXACTLY WHAT IS GOING ON. 
# MAYBE CLASSES *WOULD* BE GOOD HERE, WHERE MAIN CAN CALL A ROOM CLASS
# AND EACH ROOM CAN RETURN RoomClass(next_room_to_go_to)
# WILL NEED TO MAKE SURE THAT I KNOW THE GOOD WAY TO PASS CAST AND 
# LOCKOUT (AND ANY OTHERS THAT CROP UP) AROUND TO THE NEW OBJECTS


#######STOPPEDLINE 340

def main(): 
    
    cast = {}
    
    try:
        cast['hero']
    except KeyError:
        hero = character(10, 1, 1, 1,'hero', 10, 0)
        cast['hero'] = hero
    
    try:   #Note(BCL): LOCKOUT MAYBE NEEDS TO BE INSIDE CAST, 
    # FEWER OBJECTS TO PASS AROUND
        lockout
    except NameError:
        lockout = {'chest_room': 1, 'slime_room': 1, 'orc_room' : 1,
                   'alter': 1,
                   } # 1 IS OPEN, 0 IS LOCKED OUT

    room_antichamber(cast, lockout)    
        
def room_antichamber(cast, lockout):

#ADD TO STORY LOOKING FOR JEWELS

    try:
        cast['goblin']
    except KeyError:
        goblin = character(5, 1, 1, 1,'goblin', 5, 0)
        cast['goblin'] = goblin

    if cast['goblin'][3] == 1: #Check to see if Goblin is still alive
                               #When coming from another room
        print('A goblin is here and attacks. 1 Engage in combat 2 Run')
        
        i = 0
        while True:    # This is the Goblin fight()
            
            action = input('> ')
           
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
    
    
            
    while True:
        
        print ('You see three doors. Choose a door (1 Left, 2 Center, 3 '
        'Right) or rest a moment (4). ') #List of decisions after fight
        
        choice = input('> ')
        
        if choice == '1': 
            if lockout['chest_room'] == 0:
                print('There is no reason to go back in there. Choose '
                'a different room.')
                continue
            return room_chest(cast, lockout) 
        elif choice == '2': 
            if lockout['slime_room'] == 0:
                print('There is no reason to go back in there. Choose '
                'a different room.')
                continue
            return room_slime(cast, lockout) 
        elif choice == '3': 
            return room_orc(cast, lockout) #MAYBE NEED TO ADD A KEY
                                           #TO ENTER THIS ROOM
        elif choice == '4':
            rest(cast['hero'])
        else: 
            print('Moving on is the only hope for you now. Choose a '
            'room.') 
        
def room_chest(cast, lockout): 
   
    
    
    while True: 
    
        print('You see a chest. 1 Pick lock, 2 Leave alone and return to '
    'Antichamber, 3 Rest a moment')
    
        action = input('> ')
        
        if action == '1':
            print('You attempt to pick the lock...')
            lock_test = randint(1,10)
            
            if lock_test == 1:
                print('It explodes in your face hurting you') 
                cast['hero'][0] -= randint(1,5) # RANDOM 1-5 DAMAGE TO 
                # HERO
                cast['hero'][6] = 0 # REMOVES RESTED FLAG
                if cast['hero'][0] == 0:
                    return end_game()
                lockout['chest_room'] = 0 
                print('You return to the Antichamber empty handed')
                return room_antichamber(cast, lockout)
            elif 2 <= lock_test and lock_test <= 5:
                print('Despite your best efforts, you cannot quite get '
                'the lock to open. It seems like it is broken')
                print('You return to the Antichamber empty handed.')
                lockout['chest_room'] = 0
                return room_antichamber(cast, lockout)
            else:
                print('You find a gleaming steel helmet, useful!') 

                print('You put it on and return to the Antichamber')
                cast['hero'][1] += 1 # +1 to defence
                lockout['chest_room'] = 0
                return room_antichamber(cast, lockout)
                
        elif action == '2':
            print('After looking around and seeing no danger, you '
            'return to the Antichamber.')
            return room_antichamber(cast, lockout)
        elif action == '3': 
            rest(cast['hero'])
            
            #print('You take a few moments to gather your strength and '
            #'mind. You feel better.')
            #cast['hero'][0] += 5  
            #NOTE(BCL): THIS NEED TO BE REST(HERO)
            #NOTE(BCL): THIS PROBABLY SHOULD NOT 
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
            print('You scream in rage and ferociously attack the '
            'Slime.')
            cast['slime'] = character(3, 1, 1, 1, 'slime', 3, 0)
            fight(cast['hero'], cast['slime'])
            print('As the dead Slime oozes out across the floor, you '
            'look at and under the fresh body it had just started to '
            'eat. You find a sharp sword. You put your dagger in to '
            'your pack and return to the Antichamber.') 
            # AND MAYBE ALSO FIND A KEY FOR ORC DOOR
            cast['hero'][2] += 1 # ATTACK +1
            lockout['slime_room'] = 0 #NO NEED TO COME BACK
            return room_antichamber(cast, lockout) 
        elif action == '2':
            print('You taunt the slime and it starts to follow you '
            'around the room. Much faster than it you quickly flip over'
            ' the fresh body and find a sharp sword.\n')
            print('You quickly grab the sword while stowing your dagger'
            ' and return to the Antichamber before the slime can catch '
            'you.') # NOTE(BCL): MAYBE NOT GIVE SWORD, RATHER JUST KEY, 
            # HOWEVER... I LIKE THE WHOLE NOT KILLING JUST TO KILL, SO 
            # MAYBE NOT.
            cast['hero'][2] += 1 # ATTACK +1
            lockout['slime_room'] = 0 #NO NEED TO COME BACK
            return room_antichamber(cast, lockout)
        elif action == '3':
            print('Seemingly content with its current meal, the Slime '
            'ignores you as you silently back out of the room back into'
            ' the Antichamber.')
            return room_antichamber(cast, lockout)
        elif i > 3:
            print('Suddenly, from the ceiling above, an unseen Slime '
            'plops down crushing you to the floor.\n')
            print('In its belly, you find a new definition of pain and '
            'suffering, as you are slowly digested over a thousand '
            'years.')
            return end_game()
        else:
            print('That slime looks like it might almost be done '
            'digesting that body, you should make a decision before it '
            'does. What would you like to do?')
            i += 1
    
def room_orc(cast, lockout): 
    ####NEED TO ADD RETURN FROM ROOM_HALLWAY FORCED FIGHT
    try:
        cast['orc']
    except KeyError:
        orc = character(5, 1, 1, 1,'orc', 5, 0)
        cast['orc'] = orc
    
    if cast['orc'][3] == 1: # CHECK TO SEE IF ORC IS ALIVE WHEN COMING
                            # FROM ANOTHER ROOM
        print('As you unlock and enter the door, you see a fierce orc '
            'worshiping at an alter. Further in to the room you see a '
            'dark hallway. \n1 Attack the Orc, 2 Attempt to sneak to '
            'the hallway, 3 Gently close the door and return to the '
            'Antichamber.')
        
        i = 0
        while True:
        
            action = input('> ')
            
            if action == '1': 
                print('You move in to attack the orc as he stands to '
                'fight!')
                fight(cast['hero'], cast['orc'])
                break
            elif action == '2': 
                print('You sneak towards the hallway.')
                
                sneak_roll = randint(1,4) 
                
                if sneak_roll == 4: 
                    print('You hear the Orc\'s prayers trail off. As '
                    'you look back, you both make eye contact. He '
                    'roars and raises his sword to attack!')
                    fight(cast['hero'], cast['orc'])
                    break
                else:
                    print('You silently enter the hallway and make your'
                    ' way into the damp and dark.')
                    return room_hallway(cast, lockout)
            elif action == '3': 
                print('You back in to the Antichamber and slowly '
                'closing the door and letting the latch fall.')
                return room_antichamber(cast, lockout) 
            elif i == 3:
                print('The Orc glances at the door. As you make eye '
                'contact, the Orc roars and raises his sword to '
                'attack!')
                fight(cast['hero'], cast['orc'])
                break

            else: 
                print('Hurry! Do something! He might notice you!') 
                i += 1

    while True: 
        
        print('You look around the room above the stench of the dead '
        'orc. You see an alter and a dark hallway. 1 Inspect the Alter '
        '2 Enter the hallway 3 Rest a moment 4 Return to the '
        'Antichamber.')
        
        action = input('> ')
                
        if action == '1': 
            if lockout['alter'] == 0:
                print('You have already received the gift of Dak, '
                'better move on.')
                continue
            print('You approach the alter. Amazing! It is an alter of '
                'strength. 1 Pray a prayer of strength and offer a '
                'ceremonial Red Mushroom 2 Leave the alter in peace.')
            
            i = 0
            while True:
            
                choice = input('> ')
            
                if choice == '1': 
                    event = randint(1,4)
                    if event == 1:
                        print('You feel a wave of dread as you look '
                        'down and realize your ghastly mistake. It is '
                        'an Alter of Deceit! You feel your blood run '
                        'cold as the darkness overtakes you.')
                        end_game()
                    else:
                        print('You suddenly feel stronger than you have'
                        ' ever been before! Like you could take on the '
                        'whole empire!')
                        cast['hero'][5] += 5 #maxhp +5
                        cast['hero'][0] = cast['hero'][5] #HEALTH TO MAX
                        lockout['alter'] = 0 
                        break
                elif choice == '2': 
                    print('You slowly back away from the beautiful '
                    'artifact.')
                    break
                elif i == 3:
                    print('You *feel* the Alter become annoyed with '
                    'your indecisiveness. You see a flash of cranapple '
                    'as your mind is blistered by the infinity of time.'
                    ' You like turtles.')
                    return end_game()
                else:
                    print('You cannot let yourself become too excited. '
                    'Make a choice!')
                    i += 1
        elif action == '2': 
            room_hallway(cast, lockout)
        elif action == '3': 
            rest(cast['hero']) 
        elif action == '4': 
            if (lockout['chest_room'] == 0 and 
                lockout['slime_room'] == 0):
                print('There is no reason to go back there. Time '
                'to look forward!')
            else:
                print('You decide to go back to the Antichamber')
                return room_antichamber(cast, lockout)
        else:
            print('No time like the present. Better get a move on '
            'and make a choice.')
    
def room_hallway(cast, lockout): 
    
    try:
        cast['bugbear']
    except KeyError:
        bugbear = character(5, 1, 1, 1,'bugbear', 5, 0)
        cast['bugbear'] = bugbear
    
    i = 0
    while True:
        print("As you walk down the hallway, suddenly out of the darkness "
              "a giant lumbering Bugbear appears out of the darkness. 1 "
              "Attack 2 Retreat in to the shadows.")
        action = input("> ")
              
        if action == '1':
            print("You lunge forward to attack!")
            fight(cast['hero'], cast['bugbear'])
            print("after combat move forward in to the crypt")
            return room_crypt(cast)
        elif action == '2':        
          
            sneak_roll = randint(1,4)
            
            if sneak_roll == 1:
                print('It seems he cannot see very well in the dark as you '
                'disappear back in to the shadows. However, as you hold '
                'your breath hoping it turns around and walks away, he '
                'begins to sniff the air. He creeps ever closer. You can\'t'
                ' move!\n He bumps in to you and jumps back with a shout. '
                'Drawing your weapon, you realize it is a fight!')
                fight(cast['hero'], cast['bugbear'])
                return 0 # NEED TO RESOLVE THIS FIGHT
            else:
                print('It seems he cannot see very well in the dark as '
                      'you disappear back in to the shadows.')
            
                if cast['orc'][3] == 1:
                    print('Terrified in the darkness you realize you cannot'
                    ' go back without going back to fight the Orc. You '
                    'could also rest here a moment and hope the Bugbear '
                    'does not see you before you are ready. 1 Return to '
                    'fight the Orc 2 Rest') 
                    
                    choice = input('> ')
                    i = 0
                    while True:
                        if choice == '1': 
                            return room_orc(cast, lockout) 
                        elif choice == '2': 
                            sneak_roll = randint(1,4)
                            
                            if sneak_roll == 1:
                                print('While trying to gather your strength'
                                ', you hear a low chuckle as the gruesome '
                                'smiling Bugbear emerges from the '
                                'darkness.')
                                fight(cast['hero'], cast['bugbear'])
                                print('With nothing in your way, you '
                                'cautiously advance though the hallway.')
                                #MAYBE ADD A CHANCE TO GO BACK TO THE
                                #BUGBEAR?
                                #SHOULD MAYBE DO THIS IN ROOM_CRYPT
                            else: 
                                rest(cast['hero'])
                                return room_hallway(cast, lockout)
                        elif i == 3:
                            print('You feel a sudden jolt in your neck '
                            'before you realize out of the corner of your '
                            'eye, you see everything you did not hope to '
                            'see as you lose conciousness.')
                            return end_game()
                        else:
                            print('Indecision will get you killed here, '
                            'choose!')
                            i += 1
                else:
                    return room_orc(cast, lockout)
        else:
            print('Frozen in indecision, the Bugbear sees your wide, '
                  'terrified eyes and he ruthlessly detatches your '
                  'head from the rest of your body.')
            return end_game()
                  
def room_crypt(cast): 
    
    try:
        cast['skeleton']
    except KeyError:
        skeleton = character(5, 1, 1, 1,'skeleton', 5, 0)
        cast['skeleton'] = skeleton
        

    
    while True:
    
        print('Walk in to an empty chamber with a well kept crypt and set '
            'of stairs leading up to a large door. 1 Inspect Crypt 2 Go up'
            'stairs 3 Rest a moment 4 Return through the hallway to the '
            'Alter room')
   
        
        action = input("> ")
        gem = 0
        
        if action == '1': 
            print("Move to inspect crypt, see gems. 1 Take gems 2 Leave"
            " alone")
            
            i = 0
            
            while i != 1:
                choice = input("> ")
                
                if choice == '1':
                    gem = 1
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
                        return room_exit(gem)
                    elif false_choice == '2' or false_choice == '3':
                        print("You start to run, but you feel a spell "
                        "freeze your feet in place. You turn to fight for "
                        "your life and treasure!")
                        fight(cast['hero'], cast['skeleton'])
                        print("Dead skelly, go up stairs")
                        return room_exit(gem)
                    else:
                        print("Your indecision costs you your life and "
                        "treasure!")
                elif choice == '2':
                    print("You leave the treasure in its place and back"
                    " up to the middle of the room.\n1 Inspect Crypt 2 "
                    "Go up the stairs 3 Rest a moment")
                    i = 1
                    
               
                
#            return 0 
        elif action == '2': 
            print("You ignore the crypt and move up the stairs. After "
            "a moment pushing, you manage to open the heavy stone door "
            "and see out in to the wilderness.")
            room_exit(gem)

            return 0 
        elif action == '3': 
            rest(cast['hero'])
            continue
        elif action == '4':
            if lockout['alter'] == 0:
                print('There is no reason to go back.')
            else:
                print('You go back through the hallway.')
                return room_orc(cast, lockout)
        else: 
            print("It is time to move on, please make a choice.")
        

    return 0 

def room_exit(gem): 
    if gem == 1:
    
        print('As you step out in to the light and to safety with your '
              'hard fought treasure, you begin to seriously consider '
              'if adventuring is worth the effort. Maybe you should '
              'quit while you are rich and open an inn or something.')
        return end_game()
    else:
        print('As you step out in to the light and to safety, you might'
        ' not have the treasure you entered looking for, but you still '
        'have your life! You begin to seriously consider if adventuring' 
        ' is worth the effort. Maybe you should try to get you old job '
        ' at the stable back. The horses were not that bad.')
        return end_game()

def character(health, defence, attack, alive, name, max_hp, rested): 
#Add rested flag here? 
# IS THIS THE BEST FUNCTION TO DO THIS? WHY NOT JUST PASS INFO 
#TO THE CAST DICT?
# THERE ARE A LOT OF ARGUMENTS HERE
    stats = [health, defence, attack, alive, name, max_hp, rested]
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
    hero_stats[6] = 0
    while True:
        print('You engage in combat! 1 Fight or 2 Run')
        action = input('> ')
        if action == '1':
            
            print('You attack!')
            hero_stats[0] -= enemy_stats[2]
            enemy_stats[0] -= hero_stats[2]
            print(hero_stats, enemy_stats)
            
            if hero_stats[0] <= 0:
                print('You fall bravely in battle.')
                return end_game()       
            elif enemy_stats[0] <= 0:
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

def rest(hero): 
    if hero[6] == 1: # 1 IS ALREADY RESTED NO NEED FOR MORE
        print("You already feel as good as you are going to feel. "
        "Better get a move on!")
        return 0 
    else:
        print("You take a moment to catch your breath. You feel like "
        "you can soldier on!")
        hero[6] = 1
        hero[0] = hero[5]
        return hero 
    
    
 #   hero[4] = 1
    return 0  

def end_game(): 


# THERE IS A BUG HERE WHEN COMING FROM FIGHT(), IT ONLY HAS TWO ELEMENTS
# OF CAST AND NOT THE WHOLE ARGUMENT OF "CAST". NEED TO LOOK IN TO HOW 
# TO 1 MAKE THIS WORK, 2 MAKE IT WORK WELL

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