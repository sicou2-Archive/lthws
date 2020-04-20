from random import randint
from sys import exit

# NEED TO ADD EXIT TO GAME END POINTS

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
# FUTURE BCL. HE IS AN ANGRY AND FORGETFUL FOOL

# NOTE(BCL): CHECK TO SEE IF YOU CAN LOCKOUT PLAYER FROM ANTIROOM AFTER 
# KILLING ORC AND ALL GEAR FROM ANTICHAMBER IS FOUND

# TODO(BCL): CREATE SOME KIND OF GAME BALANCE FOR THE COMBAT BITS

# TODO(BCL): CREATE SOME KIND OF RANDOMIZATION TO COMBAT WITH SOME 
# FLAVOR TEXT AND INFO AS TO THE STATUS OF THE PLAYER

# NEED TO DOCSTRING ALL CLASSES AND FUNCTIONS

# NEED TO FIX ALL STRINGS TO """ """

# Rooms: 
    # enter, exit, go to other rooms you have already gone to/ lockout
        #entrance, antichamber, chest, slime, orc (alter), hallway, crypt, 
        #exit (outside), death/end_game
# Actions: fight, rest, move
# Characters: hero, goblin, orc, bugbear, skeleton, 
# Objects: helmet, sword, gems



###STOPPED AT LINE 37, TRYING TO GET ANITROOM IN INHERIT CAST FROM ROOM
# CLASS


#_____________ROOM________________________

class Room(object):
    
# THIS IS A USELESS CLASS, WHEN YOU RETURN A ROOM THAT IS NOT A ROOM
# YOU DO NOT COME TO THE BASE ROOM  
# MAYBE IF RETURN NONE. TEST THIS LATER
    def enter(self): 
        print("ENTER THE ROOM THAT IS NOT A ROOM, THINGS ARE BROKEN")
        exit(1)        
    
  

#list of [choices, the, player, can, make] since several of them are 
#common in each room, i.e. rest 
    
    
    
class Room_Entrance(Room):


#ADD TO STORY LOOKING FOR JEWELS


    def __init__(self):
#        super().__init__()
    
        try:
            Engine.cast['hero']
        except KeyError:
            hero = Engine.character(10, 1, 1, 1,'hero', 10, 0)
            Engine.cast['hero'] = hero
            
        try:   
            Engine.cast['lockout']
        except KeyError:
            Engine.cast['lockout'] = {
                'chest_room': 1,
                'slime_room': 1,
                'alter_room' : 1,
                'alter': 1,
                } # 1 IS OPEN, 0 IS LOCKED OUT 
        
    def enter(self):

        print("THIS NEEDS THE OPENING STORY")
        return 'antichamber' 

class Room_Antichamber(Room):

    def enter(self):

        try:
            Engine.cast['goblin']
        except KeyError:
            goblin = Engine.character(1, 1, 1, 1,'goblin', 5, 0)
                # RETURN GOBLIN HEALTH TO 5
            Engine.cast['goblin'] = goblin
        
        if Engine.cast['goblin'][3] == 1:
            # Check to see if Goblin is still alive when coming from 
            # another room
            
            

            print("THIS NEEDS BETTER STORY A goblin is here and "
                "attacks.\n1 Engage in combat 2 Run")

            i = 0
            while True:    
                # This is the Goblin fight()
                
                action = input('> ')
               
                if action == '1': #SOMETHING IS BROKEN HERE, NEED TO FIX FIGHT
                    next_room = Engine.fight(
                        Engine.cast['hero'], 
                        Engine.cast['goblin'],
                        'antichamber'
                        )

                    return next_room
                elif action == '2':
                    print("You run from the room and go looking for "
                        "help to continue the fight.")
                    return 'end_game'
                        # DOUBLE CHECK THIS IS CORRECT RETURN
                elif i > 3:
                    print("The Goblin attacks while you stare at him.")
                    return 'end_game'
                else:
                    print("He looks mean, do something! Quick!")
                    i += 1            
        
        while True:
            
            print("You see three doors. \nChoose a door or rest: \n1" 
                "Left, 2 Center, 3 Right, 4 Rest a moment") 
                    # List of decisions after fight
            
            choice = input('> ')
            
            if choice == '1': 
                if Engine.cast['lockout']['chest_room'] == 0:
                    # THIS NEEDS TO BE VERIFIED THAT IT WORKS
                    print("There is no reason to go back in there. "
                        "\nChoose a different room: \n2 Center, 3 "
                        "Right, 4 Rest a moment")
                            # THESE CHOICES NEED TO BE VERIFIED THEY 
                            # MAKE SENSE
                    continue
                return 'chest'
                    # DOUBLE CHECK THIS RETURN IS CORRECT
            elif choice == '2': 
                if Engine.cast['lockout']['slime_room'] == 0:
                    print("There is no reason to go back in there." 
                        "\nChoose a different room: \n1 Left, 3 Right, "
                        "4 Rest a moment"
                        )
                            # THESE CHOICES NEED TO BE VERIFIED THEY 
                            # MAKE SENSE
                    continue
                return 'slime'
            elif choice == '3': 
                return 'alter'
                    # MAYBE NEED TO ADD A KEY TO ENTER THIS ROOM
                    # GIFT KEY FOR FIGHTING AND NOT FIGHTING SLIME
                    # GIFT SWORD FOR FIGHTING SLIME? STILL NOT SURE HOW
                    # I FEEL ABOUT FORCING THAT FIGHT.
            elif choice == '4':
                Engine.rest(Engine.cast['hero'])
            else: 
                print("Moving on is the only hope for you now. Choose a"
                    "room:\n1 Left, 2 Center, 3 Right, 4 Rest a moment")      
 
#        print('Antichamber')
#        return 'end_game'
#        THIS RETURN SHOULD NOT BE NEEDED
class Room_Chest(Room):

    def enter(self):
        
        while True: 
        
            print('You see a chest. 1 Pick lock, 2 Leave alone and '
                'return to Antichamber, 3 Rest a moment')
                # THIS NEEDS A STYLE REWRITE TO MATCH ANTICHAMBER
        
            action = input('> ')
            
            if action == '1':
                print('You attempt to pick the lock...')
                
                lock_test = randint(1,10)
                
                if lock_test == 1:
                    print('It explodes in your face hurting you!') 
                    cast['hero'][0] -= randint(1,5) # RANDOM 1-5 DAMAGE 
                    # TO HERO
                    cast['hero'][6] = 0 # REMOVES RESTED FLAG
                    
                    if cast['hero'][0] == 0:
                        return 'end_game'
                    
                    Engine.cast['lockout']['chest_room'] = 0 
                    print('You return to the Antichamber empty handed')
                    return 'antichamber'
                elif 2 <= lock_test and lock_test <= 5:
                    print('Despite your best efforts, you cannot quite '
                    'get the lock to open. It seems like it is broken')
                    print('You return to the Antichamber empty handed.')
                    Engine.cast['lockout']['chest_room'] = 0
                    return 'antichamber'
                else:
                    print('You find a gleaming steel helmet, useful!') 
                    print('You put it on and return to the Antichamber')
                    Engine.cast['hero'][1] += 1 # +1 to defence
                    Engine.cast['lockout']['chest_room'] = 0
                    return 'antichamber'
            elif action == '2':
                print('After looking around and seeing no danger, you '
                'return to the Antichamber.')
                return 'antichamber'
            elif action == '3': 
                Engine.rest(Engine.cast['hero'])
                
                # print('You take a few moments to gather your strength 
                # and mind. You feel better.')
                # cast['hero'][0] += 5  
                # NOTE(BCL): THIS NEED TO BE REST(HERO)
                # NOTE(BCL): THIS PROBABLY SHOULD NOT 
                # RETURN TO ANTIC AND SHOULD LOOP TO TOP TO GIVE PICKING
                # LOCK ANOTHER CHANCE BEFORE LEAVING
                # NOTE(BCL): DO NOT LOOP THIS UNTIL MAX HP IS INSTALLED 
                # NOTE(BCL): MAYBE NOT REST IN HERE AT ALL SINCE REST IN 
                # ANTICHAMBER
                return 'antichamber'
                #NOTE(BCL): WITH FIGHT MODULE RANDOM THIS SHOULD RESTORE 
                #HP TO FULL
                # THIS SHOULD RETURN TO THE SAME ROOM SO YOU DO NOT 
                # ACCIDENTALLY MISS THE CHEST
                # MAKE SURE WHEN RESTING IN OTHER ROOMS THE ENEMY IS 
                # GONE BEFORE OFFERING REST
            else:
                print('You should get a move on. What would you like to'
                ' do?')        
             
class Room_Slime(Room):

    def enter(self):
        
        print('Enter and a Slime is quietly digesting a large body. 1 '
            'Attack the Slime, 2 Taunt the Slime, 3 Quietly back out of'
            ' room.')
        # THIS NEEDS A STYLE REWRITE TO MATCH ANTICHAMBER
        
        i = 0
        while True:
            action = input('> ')
            
            if action == '1':
                print('You scream in rage and ferociously attack the '
                'Slime.')
                Engine.cast['slime'] = Engine.character(
                    1, 1, 1, 1, 'slime', 3, 0)
                        # REBALANCE SLIME AFTER TESTING
                next_room = Engine.fight(
                    Engine.cast['hero'], 
                    Engine.cast['slime'],
                    'antichamber'
                    )
                print('As the dead Slime oozes out across the floor, '
                'you look at and under the fresh body it had just '
                'started to eat. You find a sharp sword. You put your '
                'dagger in to your pack and return to the Antichamber.') 
                # AND MAYBE ALSO FIND A KEY FOR ORC DOOR
                Engine.cast['hero'][2] += 1 # ATTACK +1
                Engine.cast['lockout']['slime_room'] = 0 
                    #NO NEED TO COME BACK
                return next_room
            elif action == '2':
                print('You taunt the slime and it starts to follow you '
                'around the room. Much faster than it you quickly flip '
                'over the fresh body and find a sharp sword.\n')
                print('You quickly grab the sword while stowing your '
                'dagger and return to the Antichamber before the slime '
                'can catch you.') 
                    # NOTE(BCL): MAYBE NOT GIVE SWORD, RATHER JUST KEY, 
                    # HOWEVER... I LIKE THE WHOLE NOT KILLING JUST TO 
                    # KILL, SO MAYBE NOT.
                Engine.cast['hero'][2] += 1 # ATTACK +1
                Engine.cast['lockout']['slime_room'] = 0 
                    # NO NEED TO COME BACK
                return 'antichamber'
            elif action == '3':
                print('Seemingly content with its current meal, the '
                'Slime ignores you as you silently back out of the room'
                ' back into the Antichamber.')
                return 'antichamber'
            elif i > 3:
                print('Suddenly, from the ceiling above, an unseen '
                'Slime plops down crushing you to the floor.\n')
                print('In its belly, you find a new definition of pain '
                'and suffering, as you are slowly digested over a '
                'thousand years.')
                return 'end_game'
            else:
                print('That slime looks like it might almost be done '
                'digesting that body, you should make a decision before'
                ' it does. What would you like to do?')
                    # THIS NEEDS TO BE REWRITTEN TO INCLUDE CHOICES
                i += 1
                
        ##return 'end_game'
            # PLACE HOLDER RETURN
        
class Room_Alter(Room):

    def enter(self):
        
        ####NEED TO ADD RETURN FROM ROOM_HALLWAY FORCED FIGHT
        try:
            Engine.cast['orc']
        except KeyError:
            orc = Engine.character(1, 1, 1, 1,'orc', 5, 0)
                # REBALANCE BUGBEAR AFTER TESTING
            Engine.cast['orc'] = orc
        
        if Engine.cast['orc'][3] == 1: 
            # CHECK TO SEE IF ORC IS ALIVE WHEN COMING FROM ANOTHER ROOM
            print('As you unlock and enter the door, you see a fierce '
                'orc worshiping at an alter. Further in to the room you'
                ' see a dark hallway. \n1 Attack the Orc, 2 Attempt to '
                'sneak to the hallway, 3 Gently close the door and '
                'return to the Antichamber.')
            
            i = 0
            while True:            
                action = input('> ')
                
                if action == '1': 
                    print('You move in to attack the orc as he stands '
                    'to fight!')
                    next_room = Engine.fight(
                    Engine.cast['hero'], 
                    Engine.cast['orc']
                    None, #I THINK THIS IS FINE AND WILL DO NOTHING BAD
                    ) 
                    break
                elif action == '2': 
                    print('You sneak towards the hallway.')
                    
                    sneak_roll = randint(1,4) 
                    
                    if sneak_roll == 4: 
                        print('You hear the Orc\'s prayers trail off. '
                        'As you look back, you both make eye contact. '
                        'He roars and raises his sword to attack!')
                        next_room = Engine.fight(
                            Engine.cast['hero'], 
                            Engine.cast['orc'],
                            None #I THINK THIS IS FINE AND WILL DO NOTHING BAD
                            )
                        break
                    else:
                        print('You silently enter the hallway and make '
                        'your way into the damp and dark.')
                        return 'hallway'
                elif action == '3': 
                    print('You back in to the Antichamber and slowly '
                    'closing the door and letting the latch fall.')
                    return 'antichamber' 
                elif i == 3:
                    print('The Orc glances at the door. As you make eye'
                    ' contact, the Orc roars and raises his sword to '
                    'attack!')
 
 
 
###### STOPPED HERE FIXING ALL OF THE FIGHT METHODS ##########
 
 
 
 
                   Engine.fight(
                        Engine.cast['hero'],
                        Engine.cast['orc']
                        )
                    break
                else: 
                    print('Hurry! Do something! He might notice you!') 
                    i += 1

        while True: 
            
            print('You look around the room above the stench of the '
            'dead orc. You see an alter and a dark hallway. 1 Inspect '
            'the Alter 2 Enter the hallway 3 Rest a moment 4 Return to '
            'the Antichamber.')
                # REWRITE TO MATCH ANTIROOM STYLE
            
            action = input('> ')
                    
            if action == '1': 
                if Engine.cast['lockout']['alter'] == 0:
                    print('You have already received the gift of Dak, '
                    'better move on.')
                    continue
                print('You approach the alter. Amazing! It is an alter '
                    'of strength. 1 Pray a prayer of strength and offer'
                    ' a ceremonial Red Mushroom 2 Leave the alter in '
                    'peace.')
                
                i = 0
                while True:
                
                    choice = input('> ')
                
                    if choice == '1': 
                        event = randint(1,4)
                        if event == 1:
                            print('You feel a wave of dread as you look'
                                ' down and realize your ghastly '
                                'mistake. It is an Alter of Deceit! You'
                                ' feel your blood run cold as the '
                                'darkness overtakes you.')
                            return 'end_game'
                        else:
                            print('You suddenly feel stronger than you '
                            'have ever been before! Like you could take'
                            'on the whole empire!')
                            Engine.cast['hero'][5] += 5 
                                # maxhp +5
                            Engine.cast['hero'][0] = Engine.cast[
                                'hero'][5] 
                                    #HEALTH TO MAX
                            Engine.cast['lockout']['alter'] = 0 
                            break
                    elif choice == '2': 
                        print('You slowly back away from the beautiful '
                        'artifact.')
                        break
                    elif i == 3:
                        print('You *feel* the Alter become annoyed with'
                        'your indecisiveness. You see a flash of '
                        'cranapple as your mind is blistered by the '
                        'infinity of time. You like turtles.')
                        return 'end_game'
                    else:
                        print('You cannot let yourself become too '
                        'excited. '
                        'Make a choice!')
                        i += 1
            elif action == '2': 
                return 'hallway'
            elif action == '3': 
                Engine.rest(Engine.cast['hero']) 
            elif action == '4': 
                if (Engine.cast['lockout']['chest_room'] == 0 and 
                    Engine.cast['lockout']['slime_room'] == 0):
                    print('There is no reason to go back there. Time '
                    'to look forward!')
                else:
                    print('You decide to go back to the Antichamber')
                    return 'antichamber'
            else:
                print('No time like the present. Better get a move on '
                'and make a choice.')        
            
            
        
#        return 'end_game'
        
class Room_Hallway(Room):

    def enter(self):

        try:
            Engine.cast['bugbear']
        except KeyError:
            bugbear = Engine.character(1, 1, 1, 1,'bugbear', 5, 0)
                # REBALANCE BUGBEAR AFTER TESTING
            Engine.cast['bugbear'] = bugbear
        
        i = 0
        while True:
            print("As you walk down the hallway, suddenly out of the "
                "darkness a giant lumbering Bugbear appears out of the "
                "darkness. 1 Attack 2 Retreat in to the shadows.")
            action = input("> ")
                  
            if action == '1':
                print("You lunge forward to attack!")
                Engine.fight(
                    Engine.cast['hero'], 
                    Engine.cast['bugbear'])
                print("after combat move forward in to the crypt")
                return 'crypt'
            elif action == '2':        
              
                sneak_roll = randint(1,4)
                
                if sneak_roll == 1:
                    print('It seems he cannot see very well in the '
                    'dark as you disappear back in to the shadows. '
                    'However, as you hold your breath hoping it turns '
                    'around and walks away, he begins to sniff the '
                    'air. He creeps ever closer. You can\'t move!\n He '
                    'Bumps in to you and jumps back with a shout. '
                    'Drawing your weapon, you realize it is a fight!')
                    Engine.fight(
                        Engine.cast['hero'], 
                        Engine.cast['bugbear'])
                    return 'crypt'
                else:
                    print('It seems he cannot see very well in the '
                        'dark as you disappear back in to the shadows.')
                    # THIS IS NOT CORRECT SHOULD RETURN SOMETHING HERE 
                        # IN THE HALLWAY I THINK
                
                    if Engine.cast['orc'][3] == 1:
                        print('Frozen in the darkness you realize you '
                        'cannot go back without going back to fight '
                        'the Orc. You could also rest here a moment '
                        'and hope the Bugbear does not see you before '
                        'you are ready. 1 Return to fight the Orc 2 '
                        'Rest') 
                        
                        choice = input('> ')
                        i = 0
                        while True:
                            if choice == '1': 
                                return 'alter' 
                            elif choice == '2': 
                                sneak_roll = randint(1,4)
                                
                                if sneak_roll == 1:
                                    print('While trying to gather your '
                                    'strength, you hear a low chuckle '
                                    'as the gruesome smiling Bugbear '
                                    'emerges from the darkness.')
                                    Engine.fight(
                                        Engine.cast['hero'], 
                                        Engine.cast['bugbear'])
                                    print('With nothing in your way, '
                                        'you cautiously advance though '
                                        'the hallway.')
                                    #MAYBE ADD A CHANCE TO GO BACK TO THE
                                    #BUGBEAR?
                                    #SHOULD MAYBE DO THIS IN ROOM_CRYPT
                                else: 
                                    Engine.rest(Engine.cast['hero'])
                                    return 'hallway'
                            elif i == 3:
                                print('You feel a sudden jolt in your '
                                'neck before you realize out of the '
                                'corner of your eye, you see '
                                'everything you hope to not see as you '
                                'lose conciousness.')
                                return 'end_game'
                            else:
                                print('Indecision will get you killed '
                                'here, choose!')
                                i += 1
                    else:
                        return 'alter'
            else:
                print('Frozen in indecision, the Bugbear sees your '
                'wide, terrified eyes and he ruthlessly detatches your '
                'head from the rest of your body.')
                return 'end_game'

#        return 'end_game'
        
class Room_Crypt(Room):

    def enter(self):
        try:
            Engine.cast['skeleton']
        except KeyError:
            skeleton = Engine.character(5, 1, 1, 1,'skeleton', 5, 0)
            Engine.cast['skeleton'] = skeleton
            

        
        while True:
        
            print('Walk in to an empty chamber with a well kept crypt '
            'and set of stairs leading up to a large door. 1 Inspect '
            'Crypt 2 Go up stairs 3 Rest a moment 4 Return through the '
            'hallway to the Alter room')       
            
            action = input("> ")
            
            try:
                Engine.cast['gem']
            except KeyError:
                gem = 0
                Engine.cast['gem'] = gem            

            
            if action == '1': 
                print("Move to inspect crypt, see gems. 1 Take gems "
                "2 Leave them alone")
                
                i = 0 # I AM NOT SURE ABOUT THIS LOOP
                # MAYBE HAVE A STALLING PUNISHMENT TO FORCE SKELLY FIGHT?
                
                while i != 1:
                    choice = input("> ")
                    
                    if choice == '1':
                        Engine.gem = 1
                        print("You take the flawless gems and put them "
                        "in to your pack. As you close the bag you "
                        "look up and see a skeleton rising out of the "
                        "crypt. 1 Attack 2 Run toward the stairs 3 Run "
                        "toward the hallway")
                        #GEM GET FOR DIFFERENT ENDING?
                        false_choice = input("> ")
                        
                        if false_choice == '1':
                            print("You bravely defend your life and "
                            "treasure!")
                            Engine.fight(
                                Engine.cast['hero'], 
                                Engine.cast['skeleton'])
                            print("Dead skelly, go up stairs")
                            return 'outside'
                        elif false_choice == '2' or false_choice == '3':
                            print("You start to run, but you feel a "
                            "spell freeze your feet in place. You turn "
                            "to fight for your life and treasure!")
                            Engine.fight(
                                Engine.cast['hero'], 
                                Engine.cast['skeleton'])
                            print("Dead skelly, go up stairs")
                            return 'outside'
                        else:
                            print("Your indecision costs you your life "
                            "and treasure!")
                    elif choice == '2':
                        print("You leave the treasure in its place and "
                        "go back up to the middle of the room.\n1 "
                        "Inspect Crypt 2 Go up the stairs 3 Rest a "
                        "moment")
                        i = 1
                    elif choice == '3':
                        Engine.rest(Engine.cast['hero'])
                    
                   
                    
    #            return 0 
            elif action == '2': 
                print("You ignore the crypt and move up the stairs. "
                "After a moment pushing, you manage to open the heavy "
                "stone door and see out in to the wilderness.")
                return 'outside'
                 
            elif action == '3': 
                Engine.rest(Engine.cast['hero'])
                continue
            elif action == '4':
                if Engine.cast['lockout']['alter'] == 0:
                    print('There is no reason to go back.')
                else:
                    print('You go back through the hallway.')
                    return 'alter'
            else: 
                print("It is time to move on, please make a choice.")
            
        
#        return 'end_game'
        
class Room_Outside(Room):

    def enter(self):
    
        if Engine.cast['gem'] == 1:
        
            print('As you step out in to the light and to safety with '
            'your hard fought treasure, you begin to seriously '
            'consider if adventuring is worth the effort. Maybe you '
            'should quit while you are rich and open an inn or '
            'something.')
            return 'end_game'
        else:
            print('As you step out in to the light and to safety, you '
            'might not have the treasure you entered looking for, but '
            'you still have your life! You begin to seriously consider '
            'if adventuring is worth the effort. Maybe you should try '
            'to get you old job at the stable back. The horses were '
            'not that bad.')
            return 'end_game'
        
class Room_End_Game(Room):

    def enter(self):
    
# THERE IS A BUG HERE WHEN COMING FROM FIGHT(), IT ONLY HAS TWO ELEMENTS
# OF CAST AND NOT THE WHOLE ARGUMENT OF "CAST". NEED TO LOOK IN TO HOW 
# TO 1 MAKE THIS WORK, 2 MAKE IT WORK WELL

# THERE IS A BUG THAT THE GAME DOES NOT RESET WHEN PLAYING AGAIN

### THIS FEELS LIKE IT SHOULD HAVE A TRY EXCEPT TO CLEAN IT UP A BIT

        print('Game over man. Game over! Play again? "y/n"')
        choice = input('> ')
        if choice == 'y':
            dungeon_map = Map('entrance') 
            # dungeon_map.start_room = 'entrance'
            new_game = Engine(dungeon_map) 
            # new_game.game_map = dungeon_map.start_room = 'entrance'
            new_game.play()
        elif choice == 'n':
           exit(1)
        else:
            while True:
                print('Would you like to play again? "y/n"')
                choice = input('> ')
                if choice == 'y':
                    Engine.cast = {}
                    new_game.play()
                elif choice == 'n':
                    exit(1)
                else:
                    pass

#        print('Dead')
        #return 'end_game'
        
        
#_________________ACTIONS_____________________________

class Actions(object):

    def fight():
        pass
        
    def rest():
        pass
        
    def move():
        pass
        
#__________________CHARACTER____________________________

class Character(object): #maybe combine with items; things(?) maybe
# make this a sub-class like battery in ElectricCar? 

    def __init__(self, stats):
        pass
    
    def create_character():
        pass
        
class Items(object): 

    def create_item():
        pass
        

 #_______________ENGINE___________________
 
class Engine(object):

#    def remove_me():
    # NEED self.cast
    # NEED HERO

    cast = {} 
        # This is a class variable for the cast of the game and the room 
        # lockout status
        
    # This is a class variable, apparently this is all that 
        # is needed for this to work. 
        
        
        # try:
            # cast['hero']
        # except KeyError:
            # hero = character(10, 1, 1, 1,'hero', 10, 0)
            # cast['hero'] = hero
        
        # try:   #Note(BCL): LOCKOUT MAYBE NEEDS TO BE INSIDE CAST, 
        # FEWER OBJECTS TO PASS AROUND
            # lockout
        # except NameError:
            # lockout = {'chest_room': 1, 'slime_room': 1, 'orc_room' : 1,
                       # 'alter': 1,
                       # } # 1 IS OPEN, 0 IS LOCKED OUT

        # room_antichamber(cast, lockout)    
        #pass
        
        
    
    def __init__(self, game_map):
        self.game_map = game_map
    #    Engine.cast = {} # cast is a list and characters should be a 
                        # dict
    
    def play(self):
        current_room = self.game_map.opening_room()
        last_room = self.game_map.next_room('end_game')
                
        while current_room != last_room: 
            next_room_name = current_room.enter()
            current_room = self.game_map.next_room(next_room_name)
            
        current_room.enter()
     
    def fight(hero_stats, enemy_stats, win_next_room): 
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
                    return 'end_game'       
                elif enemy_stats[0] <= 0:
                    print(f'You slay the enemy {enemy_stats[4]}')
                    print("Above the body of your foe, you look "
                    "around.") # NOT SUPER SURE THIS FITS HERE NEED TO TEST
                    enemy_stats[3] = 0
                    return win_next_room
                    #I do not think I need to return stats any more. 
                    #return (hero_stats, enemy_stats)
                else:
                    print('The combat continues!')
            elif action == '2':
                print('You retreat from the battle!') 
                    # NOTE(BCL): THIS NEEDS TO RETURN TO A PREVIOUS ROOM 
                    # OR LEAVE IF IN ANTI-C
                    # THERE IS A BUG HERE THAT YOU DO NOT RETURN END GAME
                return 'end_game'
            elif i == 4:
                print('You block and block the attacks coming from your'
                ' foe, eventually, you are overwhelmed.')
                    # THINK THE SAME BUG IS HERE WHERE YOU DO NOT RETURN TO 
                    # END GAME
                return 'end_game'
            else:
                print('Do not hesitate! Do something, anything!')
                i +=1
        return 0      
        
    def character(
        health,
        defence, 
        attack,
        alive,
        name, 
        max_hp,
        rested): 
        
# IS THIS THE BEST FUNCTION TO DO THIS? WHY NOT JUST PASS INFO 
#TO THE CAST DICT?
# THERE ARE A LOT OF ARGUMENTS HERE
        stats = [health, defence, attack, alive, name, max_hp, rested]

        # hitpoints = 0
        # hitpoints = randrange(0,10)
        
        # attack = 1

        # stats = [randrange(0,10), attack]
        # print(stats)
        
        return stats   

    def rest(hero): 
       
        if Engine.cast['hero'][6] == 1: 
            # 1 FLAG IS ALREADY RESTED NO NEED FOR MORE
            print("You already feel as good as you are going to feel. "
            "Better get a move on!")
        else:
            print("You take a moment to catch your breath. You feel like "
            "you can soldier on!")
            Engine.cast['hero'][6] = 1
                # SET RESTED FLAG TO RESTED
            Engine.cast['hero'][0] = hero[5]
                # SET HERO HEALTH TO MAX HEALTH
                 
# _______________MAP_____________________________


class Map(object):

    dict_rooms = {
        'entrance': Room_Entrance(),
        'antichamber': Room_Antichamber(),
        'chest': Room_Chest(),
        'slime': Room_Slime(),
        'alter': Room_Alter(),
        'hallway': Room_Hallway(),
        'crypt': Room_Crypt(),
        'outside': Room_Outside(),
        'end_game': Room_End_Game(),
        None: Room(),
        }
    

    def __init__(self, start_room):
       self.start_room = start_room
        
    def next_room(self, room_name):
        dict_room_value = Map.dict_rooms.get(room_name)
        return dict_room_value        
        
    def opening_room(self):
        return self.next_room(self.start_room)
                    
            
            
            
            
    

dungeon_map = Map('entrance') # dungeon_map.start_room = 'entrance'
new_game = Engine(dungeon_map) # new_game.game_map = dungeon_map.start_room = 'entrance'
new_game.play()
 
