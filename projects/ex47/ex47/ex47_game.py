from random import randint
from sys import exit
from textwrap import dedent

from game_text import Text




#_____________ROOM________________________


class Room(object):
    """
    This is the generic room that should only run when there is a 
    problem with the map layout or a room is being called that does not
    exist.
    """
    def enter(self): 
        """
        This function states that there is a problem with the room that
        was called.
        """
        print("ENTER THE ROOM THAT IS NOT A ROOM, THINGS ARE BROKEN")
        exit(1)        
    
  
class Room_Entrance(Room):
    """This is the Entrance room class. It should always be the first
    thing that players see.
    """

#ADD TO STORY LOOKING FOR JEWELS
    def enter(self):
        """
        This is the working function for this room. It creates the 
        player character and the room lockouts.
        """
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
                'alter_room' : 0,
                'alter': 1,
                }
                # 1 IS OPEN, 0 IS LOCKED OUT 
                
                
        print("THIS NEEDS THE OPENING STORY\n")
        ## GIVE PLAYER "CHOICE" TO GO IN OR COMEBACK ANOTHER DAY
        return 'antichamber' 


class Room_Antichamber(Room):
    """This is the Antichamber room class."""

    def enter(self):
        """
        This is the working function for the class. It creates a goblin
        to fight and flows to three different rooms (chest, slime, and 
        alter).
        """
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
                "attacks.\n1 Engage in combat 2 Run\n")

            i = 0
            while True:    
                
                action = input('> ')
               
                if action == '1':
                    next_room = Engine.fight(
                        Engine.cast['hero'], 
                        Engine.cast['goblin'],
                        'antichamber'
                        )

                    return next_room
                elif action == '2':
                    print("You run from the room and go looking for "
                        "help to continue the fight.\n")
                    return 'end_game'
                        # DOUBLE CHECK THIS IS CORRECT RETURN
                elif i > 3:
                    print('The Goblin attacks while you stare at '
                    'him.\n')
                    return 'end_game'
                else:
                    print("He looks mean, do something! Quick!\n")
                    i += 1            
        
        print("You see three doors. \nChoose a door or rest: \n1 " 
            "Left, 2 Center, 3 Right, 4 Rest a moment\n") 
        
        while True:

            choice = input('> ')
            
            if choice == '1': 
                if Engine.cast['lockout']['chest_room'] == 0:
                    # THIS NEEDS TO BE VERIFIED THAT IT WORKS
                    print("There is no reason to go back in there. "
                        "\nChoose a different room: \n2 Center, 3 "
                        "Right, 4 Rest a moment\n")
                            # THESE CHOICES NEED TO BE VERIFIED THEY 
                            # MAKE SENSE
                    continue
                return 'chest'
                    # DOUBLE CHECK THIS RETURN IS CORRECT
            elif choice == '2': 
                if Engine.cast['lockout']['slime_room'] == 0:
                    print("There is no reason to go back in there." 
                        "\nChoose a different room: \n1 Left, 3 Right, "
                        "4 Rest a moment\n")
                            # THESE CHOICES NEED TO BE VERIFIED THEY 
                            # MAKE SENSE
                    continue
                return 'slime'
            elif choice == '3': 
                return 'alter'
            elif choice == '4':
                Engine.rest(Engine.cast['hero'])
            else: 
                print("Moving on is the only hope for you now. Choose a"
                    'room:\n1 Left, 2 Center, 3 Right, 4 Rest a '
                    'moment\n')


class Room_Chest(Room):
    """This is the Chest room class."""
    def enter(self):
        """
        This is the working function for the Chest Room. It has a random 
        chance box to give the player an object to use. It leads only 
        back to the Antichamber.
        """
        while True: 
        
            print('You see a locked chest. 1 Pick lock, 2 Leave alone '
            'and return to Antichamber, 3 Rest a moment\n')
                # THIS NEEDS A STYLE REWRITE TO MATCH ANTICHAMBER
        
            action = input('> ')
            
            if action == '1':
                print('You attempt to pick the lock...\n')
                
                lock_test = randint(1,10)
                
                if lock_test == 1:
                    print('It explodes in your face hurting you!\n') 
                    cast['hero'][0] -= randint(1,5) 
                    # RANDOM 1-5 DAMAGE TO HERO
                    cast['hero'][6] = 0 
                    #REMOVES RESTED FLAG
                    
                    if cast['hero'][0] == 0:
                        return 'end_game'
                    
                    Engine.cast['lockout']['chest_room'] = 0 
                    print('You return to the Antichamber empty '
                    'handed\n')
                    return 'antichamber'
                elif 2 <= lock_test and lock_test <= 5:
                    print('Despite your best efforts, you cannot quite '
                    'get the lock to open. It seems like it is '
                    'broken.\n')
                    print('You return to the Antichamber empty '
                    'handed.\n')
                    Engine.cast['lockout']['chest_room'] = 0
                    return 'antichamber'
                else:
                    print('You find a gleaming steel helmet, useful!\n') 
                    print('You put it on and return to the '
                    'Antichamber\n')
                    Engine.cast['hero'][1] += 1 # +1 TO defence
                    Engine.cast['lockout']['chest_room'] = 0
                    return 'antichamber'
            elif action == '2':
                print('After looking around and seeing no danger, you '
                'return to the Antichamber.\n')
                return 'antichamber'
            elif action == '3': 
                Engine.rest(Engine.cast['hero'])
                return 'chest'
            else:
                print('You should get a move on. What would you like to'
                ' do?\n')        


class Room_Slime(Room):
    """This is the Slime room class."""
    def enter(self):
        
        print('Enter and a Slime is quietly digesting a large body. 1 '
            'Attack the Slime, 2 Taunt the Slime, 3 Quietly back out of'
            ' room.\n')
        # THIS NEEDS A STYLE REWRITE TO MATCH ANTICHAMBER
        
        i = 0
        while True:
            action = input('> ')
            
            if action == '1':
                print('You roar and ferociously attack the Slime.\n')
                Engine.cast['slime'] = Engine.character(
                    1, 1, 1, 1, 'slime', 3, 0)
                        #REBALANCE SLIME AFTER TESTING
                next_room = Engine.fight(
                    Engine.cast['hero'], 
                    Engine.cast['slime'],
                    'antichamber'
                    )
                print('As the dead Slime oozes out across the floor, '
                'you look at and under the fresh body it had just '
                'started to eat. You find a sharp sword. You put your '
                'dagger in to your pack and return to the '
                'Antichamber.\n') 
                Engine.cast['hero'][2] += 1 # ATTACK +1
                Engine.cast['lockout']['slime_room'] = 0 
                    #NO NEED TO COME BACK
                Engine.cast['lockout']['alter_room'] = 1 
                print('As you step out in to the Antichamber you notice'
                ' a key tied to the hilt of the sword.\n')
                return next_room
            elif action == '2':
                print('You taunt the slime and it starts to follow you '
                'around the room. Much faster than it, you quickly flip'
                ' over the fresh body and find a sharp sword.\n')
                print('You quickly grab the sword while stowing your '
                'dagger and return to the Antichamber before the slime '
                'can catch you.\n') 
                Engine.cast['hero'][2] += 1 # ATTACK +1
                Engine.cast['lockout']['slime_room'] = 0 
                    #NO NEED TO COME BACK
                Engine.cast['lockout']['alter_room'] = 1 
                print('As you step out in to the Antichamber you notice'
                ' a key tied to the hilt of the sword.\n')
                return 'antichamber'
            elif action == '3':
                print('Seemingly content with its current meal, the '
                'Slime ignores you as you silently back out of the room'
                ' back into the Antichamber.\n')
                return 'antichamber'
            elif i > 3:
                print('Suddenly, from the ceiling above, an unseen '
                'Slime plops down crushing you to the floor.\n')
                print('In its belly, you find a new definition of pain '
                'and suffering, as you are slowly digested over a '
                'thousand years.\n')
                return 'end_game'
            else:
                print('That slime looks like it might almost be done '
                'digesting that body, you should make a decision before'
                ' it does. What would you like to do?\n1 Attack the '
                'Slime, 2 Taunt the Slime, 3 Quietly back out of the '
                'room.\n')
                i += 1


class Room_Alter(Room):
    """This is the Alter room class."""

    def enter(self):
        
        if Engine.cast['lockout']['alter_room'] == 0:
            print('You attempt to open the door, but the handle only '
            'rattles in your hand. This door is locked.\n')
            return 'antichamber'

        try:
            Engine.cast['orc']
        except KeyError:
            orc = Engine.character(1, 1, 1, 1,'orc', 5, 0)
                #REBALANCE ORC AFTER TESTING
            Engine.cast['orc'] = orc

        if Engine.cast['orc'][3] == 1 and Engine.cast.get(
            'bugbear',False): 
            #CHECK TO SEE IF ORC IS ALIVE WHEN COMING FROM ANOTHER ROOM
            #AND IF BUGBEAR EXISTS
            print('You see the fierce orc still worshiping at the '
            'alter. Further in to the room you see the door back to the'
            ' Antichamber. \n1 Attack the Orc, 2 Attempt to sneak to '
            'the Antichamber.\n')

            i = 0
            while True:            
                action = input('> ')
                
                if action == '1': 
                    print('You move in to attack the orc as he stands '
                    'to fight!\n')
                    next_room = Engine.fight(
                    Engine.cast['hero'], 
                    Engine.cast['orc'],
                    'alter',
                    ) 
                    return next_room
                elif action == '2': 
                    print('You sneak towards the Antichamber.\n')
                    
                    sneak_roll = randint(1,4) 
                    
                    if sneak_roll == 4: 
                        print('You hear the Orc\'s prayers trail off. '
                        'As you look back, you both make eye contact. '
                        'He roars and raises his sword to attack!\n')
                        next_room = Engine.fight(
                            Engine.cast['hero'], 
                            Engine.cast['orc'],
                            'alter',
                            )
                        return next_room
                    else:
                        print('You silently pad across the room and '
                        'slip through the still cracked door in to the '
                        'Antichamber.\n')
                        return 'antichamber'
                    return 'antichamber' 
                elif i == 3:
                    print('The Orc glances in your direction. As you '
                    'make eye contact, the Orc roars and raises his '
                    'sword to attack!\n')
                    next_room = Engine.fight(
                        Engine.cast['hero'],
                        Engine.cast['orc'],
                        'alter',
                        )
                    return next_room
                else: 
                    print('Hurry! Do something! He might notice you!\n')
                    i += 1

        if Engine.cast['orc'][3] == 1: 
            # CHECK TO SEE IF ORC IS ALIVE WHEN COMING FROM ANOTHER ROOM
            print('You unlock and open the door and see a fierce orc '
            'worshiping at an alter. Further in to the room you see a '
            'dark hallway. \n1 Attack the Orc, 2 Attempt to sneak to '
            'the hallway, 3 Gently close the door and return to the '
            'Antichamber.\n')
            i = 0
            while True:            
                action = input('> ')
                
                if action == '1': 
                    print('You move in to attack the orc as he stands '
                    'to fight!\n')
                    next_room = Engine.fight(
                    Engine.cast['hero'], 
                    Engine.cast['orc'],
                    'alter',
                    ) 
                    return next_room
                elif action == '2': 
                    print('You sneak towards the hallway.\n')
                    
                    sneak_roll = randint(1,4) 
                    
                    if sneak_roll == 4: 
                        print('You hear the Orc\'s prayers trail off. '
                        'As you look back, you both make eye contact. '
                        'He roars and raises his sword to attack!\n')
                        next_room = Engine.fight(
                            Engine.cast['hero'], 
                            Engine.cast['orc'],
                            'alter',
                            )
                        return next_room
                    else:
                        print('You silently enter the hallway and make '
                        'your way into the damp and dark.\n')
                        return 'hallway'
                elif action == '3': 
                    print('You back in to the Antichamber and slowly '
                    'closing the door and letting the latch fall.\n')
                    return 'antichamber' 
                elif i == 3:
                    print('The Orc glances at the door. As you make eye'
                    ' contact, the Orc roars and raises his sword to '
                    'attack!\n')
                    next_room = Engine.fight(
                        Engine.cast['hero'],
                        Engine.cast['orc'],
                        'alter',
                        )
                    return next_room
                else: 
                    print('Hurry! Do something! He might notice you!\n') 
                    i += 1

        while True: 
            
            print('You look around the room above the stench of the '
            'dead orc. You see an alter and a dark hallway. 1 Inspect '
            'the Alter 2 Enter the hallway 3 Rest a moment 4 Return to '
            'the Antichamber.\n')
                # REWRITE TO MATCH ANTIROOM STYLE
            
            action = input('> ')
                    
            if action == '1': 
                if Engine.cast['lockout']['alter'] == 0:
                    print('You have already received the gift of Dak, '
                    'better move on.\n')
                    continue
                print('You approach the alter. Amazing! It is an alter '
                    'of strength. 1 Pray a prayer of strength and offer'
                    ' a ceremonial Red Mushroom 2 Leave the alter in '
                    'peace.\n')
                
                i = 0
                while True:
                
                    choice = input('> ')
                
                    if choice == '1': 
                        event = randint(1,4)
                        if event == 1:
                            print('You feel a wave of dread as you look'
                                ' down and dread your ghastly mistake. '
                                'It is an Alter of Deceit! You feel '
                                'your blood run cold as the darkness '
                                'overtakes you.\n')
                            return 'end_game'
                        else:
                            print('You suddenly feel stronger than you '
                            'have ever been before! Like you could take'
                            'on the whole empire!\n')
                            Engine.cast['hero'][5] += 5 
                                #maxhp +5
                            Engine.cast['hero'][0] = Engine.cast[
                                'hero'][5] 
                                #HEALTH TO MAX
                            Engine.cast['lockout']['alter'] = 0 
                            break
                    elif choice == '2': 
                        print('You slowly back away from the beautiful '
                        'artifact.\n')
                        break
                    elif i == 3:
                        print('You *feel* the Alter become annoyed with'
                        'your indecisiveness. You see a flash of '
                        'cranapple as your mind is blistered by the '
                        'infinity of time. You like turtles. You think '
                        'you can smell purple.\n')
                        return 'end_game'
                    else:
                        print('You cannot let yourself become too '
                        'excited. Make a choice!\n')
                        i += 1
            elif action == '2': 
                return 'hallway'
            elif action == '3': 
                Engine.rest(Engine.cast['hero']) 
            elif action == '4': 
                if (Engine.cast['lockout']['chest_room'] == 0 and 
                    Engine.cast['lockout']['slime_room'] == 0):
                    print('There is no reason to go back there. Time '
                    'to look forward!\n')
                else:
                    print('You decide to go back to the Antichamber\n')
                    return 'antichamber'
            else:
                print('No time like the present. Better get a move on '
                'and make a choice.\n')        


class Room_Hallway(Room):
    """This is the Hallway room class."""
    def enter(self):

        try:
            Engine.cast['bugbear']
        except KeyError:
            bugbear = Engine.character(1, 1, 1, 1,'bugbear', 5, 0)
                # REBALANCE BUGBEAR AFTER TESTING
            Engine.cast['bugbear'] = bugbear
        
        if Engine.cast['bugbear'][3] == 1:
            #IF BUGBEAR IS STILL ALIVE
            i = 0
            while True:
                print('As you walk down the hallway, suddenly out of '
                'the darkness a giant lumbering Bugbear appears out of '
                'the darkness. 1 Attack 2 Retreat in to the shadows.\n')
                action = input("> ")
                      
                if action == '1':
                    print("You lunge forward to attack!\n")
                    next_room = Engine.fight(
                        Engine.cast['hero'], 
                        Engine.cast['bugbear'],
                        'crypt',
                        )
                    print("after combat move forward in to the crypt\n")
                    #THIS NEEDS A REWRITE
                    return next_room
                elif action == '2':        
                  
                    sneak_roll = randint(1,4)

                    if sneak_roll == 1:
                        print('It seems he cannot see very well in the '
                        'dark as you disappear back in to the shadows. '
                        'However, as you hold your breath hoping it '
                        'turns around and walks away, he begins to '
                        'sniff the air. He creeps ever closer. You '
                        'can\'t move!\n He bumps in to you and jumps '
                        'back with a shout. Drawing your weapon, you '
                        'realize it is a fight!\n')
                        next_room = Engine.fight(
                            Engine.cast['hero'], 
                            Engine.cast['bugbear'],
                            'crypt'
                            )
                        return next_room
                    else:
                        print('It seems he cannot see very well in the '
                            'dark as you disappear back in to the '
                            'shadows.\n')
                        #THIS IS NOT CORRECT SHOULD RETURN SOMETHING 
                        #HERE 
                        # IN THE HALLWAY I THINK
                    
                        if Engine.cast['orc'][3] == 1:
                            print('Frozen in the darkness you realize '
                            'you cannot go back without going back to '
                            'fight the Orc. You could also rest here a '
                            'moment and hope the Bugbear does not see '
                            'you before you are ready. 1 Return to '
                            'fight the Orc 2 Rest\n') 
                            
                            choice = input('> ')
                            i = 0
                            while True:
                                if choice == '1': 
                                    return 'alter' 
                                elif choice == '2': 
                                    sneak_roll = randint(1,4)
                                    
                                    if sneak_roll == 1:
                                        print('While trying to gather '
                                        'your strength, you hear a low '
                                        'chuckle as the gruesome '
                                        'smiling Bugbear emerges from '
                                        'the darkness.\n')
                                        next_room = Engine.fight(
                                            Engine.cast['hero'], 
                                            Engine.cast['bugbear'],
                                            'crypt',
                                            )
                                        print('With nothing in your '
                                        'way, you cautiously advance '
                                        'though the hallway.\n')
                                        #MAYBE ADD A CHANCE TO GO BACK 
                                        #TO THE BUGBEAR?
                                        #SHOULD MAYBE DO THIS IN 
                                        #ROOM_CRYPT
                                    else: 
                                        Engine.rest(Engine.cast['hero'])
                                        return 'hallway'
                                elif i == 3:
                                    print('You feel a sudden jolt in '
                                    'your neck before you realize out '
                                    'of the corner of your eye, you see'
                                    ' everything you hope to not see as'
                                    ' you lose conciousness.\n')
                                    return 'end_game'
                                else:
                                    print('Indecision will get you '
                                    'killed here, choose!\n')
                                    i += 1
                        else:
                            return 'alter'
                else:
                    print('Frozen in indecision, the Bugbear sees your '
                    'wide, terrified eyes and he ruthlessly detatches '
                    'your head from the rest of your body.\n')
                    return 'end_game'
        elif Engine.cast['bugbear'][3] == 0:
            print("You walk down the dark hallway, squeezing past the "
            "dark lump of your fallen foe.\n")
            return 'crypt'
        else:
            print("You should not be here, something is broken.\n")
            return None


class Room_Crypt(Room):
    """This is the Crypt room class."""


    def enter(self):
        try:
            Engine.cast['skeleton']
        except KeyError:
            skeleton = Engine.character(5, 1, 1, 1,'skeleton', 5, 0)
            Engine.cast['skeleton'] = skeleton

        print('You walk in to a mostly empty chamber. You see a well '
        'preserved crypt. Across the room you see a set of stairs '
        'leading up to a large stone door.\n1 Inspect the Crypt 2 Go up'
        ' stairs and through the door 3 Rest a moment 4 Return through '
        'the hallway to the Alter room\n')
        ### THE RETURN FROM LEAVING THE GEMS ALONE DOES NOT MAKE 
        ### SENSE HERE #FIX TEXT FOR LEAVE GEMS ALONE

        while True:
        
            action = input("> ")
            
            try:
                Engine.cast['gem']
            except KeyError:
                gem = 0
                Engine.cast['gem'] = gem

            if action == '1': 
                print('You move closer and inspect the crypt. It is '
                'masterfully crafted in granite and onyx. Laid in the '
                'stone are dozens of dazzlingly cut gems.\n1 Take gems'
                ' 2 Leave them alone and back away from the crypt\n')

                i = 0
 
                while True:
                    choice = input("> ")
                    
                    if choice == '1':
                        Engine.cast['gem'] = 1
                        print("You take the flawless gems and put them "
                        "in to your pack. As you close the bag you "
                        "look up and see a skeleton rising out of the "
                        "crypt. 1 Attack 2 Run toward the stairs 3 Run "
                        "toward the hallway\n")
                        false_choice = input("> ")
                        
                        if false_choice == '1':
                            print("You bravely defend your life and "
                            "treasure!\n")
                            next_room = Engine.fight(
                                Engine.cast['hero'], 
                                Engine.cast['skeleton'],
                                'outside',
                                )
                            print('Your only option now is to climb the'
                            ' stairs. As you get to the door, you begin'
                            ' to push open the heavy door. You look up ' 
                            'and see another set of stairs and begin to'
                            ' climb.\nYou see a bright light above you '
                            'as you climb toward it.\n')
                            return next_room
                        elif false_choice == '2' or false_choice == '3':
                            print("You start to run, but you feel a "
                            "spell freeze your feet in place. You turn "
                            "to fight for your life and treasure!\n")
                            next_room = Engine.fight(
                                Engine.cast['hero'], 
                                Engine.cast['skeleton'],
                                'outside',
                                )
                            print('Your only option now is to climb the'
                            ' stairs. As you get to the door, you begin'
                            ' to push open the heavy door. You look up ' 
                            'and see another set of stairs and begin to'
                            ' climb.\nYou see a bright light above you '
                            'as you climb toward it.\n')
                            return next_room
                        else:
                            print("Your indecision costs you your life "
                            "and treasure!\n")
                    elif choice == '2':
                        print("You leave the treasure in its place and "
                        "go return to the middle of the room.\n1 "
                        "Inspect Crypt 2 Go up the stairs and through "
                        "the door 3 Rest a moment\n")
                        break
                    elif i == 3:
                        print('You hear a loud crack and turn to see '
                        'the evil Lich Paul looming behind you. As you '
                        'freeze in terror his hateful stare glows as a '
                        'a pair of skeletal arms reach around you from '
                        'the crypt behind you. You understand now what '
                        'this dungeon is now and how terrible a mistake'
                        ' it was to come here. Your last though is that'
                        ' maybe your unlife as an undead minion will '
                        'not be as bad as your life working in the '
                        'stables of the old inn.\n')
                        return 'end_game'
                    else:
                        print('You feel that standing here thinking '
                        'about what to do is probably not the most '
                        'intelligent thing that you could be doing with'
                        ' your time right now. Do something.\n1 Take '
                        'gems 2 Leave them alone and back away from the'
                        ' crypt\n')
                        i += 1
            elif action == '2': 
                print("You ignore the crypt and move up the stairs. "
                "After a moment pushing, you manage to open the heavy "
                "stone door and see out in to the wilderness.\n")
                return 'outside'
            elif action == '3': 
                Engine.rest(Engine.cast['hero'])
                continue
            elif action == '4':
                if Engine.cast['lockout']['alter'] == 0:
                    print('There is no reason to go back.\n')
                else:
                    print('You go back through the hallway.\n')
                    return 'alter'
            else: 
                print("It is time to move on, make a choice.\n")


class Room_Outside(Room):
    """This is the Outside room class."""
    def enter(self):
    
        if Engine.cast['gem'] == 1:
        
            print('As you step out in to the light and to safety with '
            'your hard fought treasure, you begin to seriously '
            'consider if adventuring is worth the effort. Maybe you '
            'should quit while you are still alive and open an inn or '
            'something.\n')
            return 'end_game'
        else:
            print('As you step out in to the light and to safety, you '
            'might not have the treasure you were looking for, but you '
            'still have your life! You begin to seriously consider if '
            'adventuring is worth the effort. Maybe you should try to '
            'get you old job back. The stable smelled but the horses '
            'were not that bad.\n')
            return 'end_game'


class Room_End_Game(Room):
    """
    This is the End Game room class. This should always be the last room
    that a player sees.
    """

    def enter(self):
    
### THIS FEELS LIKE IT SHOULD HAVE A TRY EXCEPT TO CLEAN IT UP A BIT
        print('Game over man. Game over! Play again? "y/n"\n')
        choice = input('> ')
        if choice == 'y':
            Engine.cast = {}
            return 'entrance'
        elif choice == 'n':
           exit(0)
        else:
            while True:
                print('Would you like to play again? "y/n"\n')
                choice = input('> ')
                if choice == 'y':
                    Engine.cast = {}
                    return 'entrance'
                elif choice == 'n':
                    exit(0)
                else:
                    pass


#_________________ACTIONS_____________________________


class Actions(object):
    """
    This is the EMPTY Action class for a potential split out of Engine
    to clean up many of the if-statements in the game.
    """
    def fight():
        """This a place holder for moving the fight function here."""
        pass
        
    def rest():
        """This a place holder for moving the rest function here."""
        pass
        
    def move():
        """
        This a place holder creating a move function here. This will be
        to create a better and more modular movement system to clean up
        the nest of if-statements.
        """
        pass


#__________________CHARACTER____________________________


class Character(object): 
    """
    This is the EMPTY Character class for a potential game clean up from
    the try statements.
    """
#maybe combine with items; things(?) maybe
# make this a sub-class like battery in ElectricCar? 

    def __init__(self, stats):
        """This is a place holder __init__ if needed."""
        pass
    
    def create_character():
        """This a place holder for moving the rest function here."""
        pass


class Items(object): 
    """
    This is the EMPTY Items class for a potential game clean up or 
    expansion for the few items in the game.
    """   
    def create_item():
        """
        This is a place holder for creating_items to give to the 
        different characters/objects in the game.
        """
        pass


 #_______________ENGINE___________________

 
class Engine(object):
    """
    This is the game Engine class. It is responsible for the game loop.
    """

    cast = {} 
        #THIS IS A CLASS VARIABLE FOR CAST, LOCKOUT, AND GEM STATUS
    
    def __init__(self, game_map):
        """
        This is the __init__ function that uses attribure of start room
        from the Map class
        """
        self.game_map = game_map
    
    def play(self):
        """This is the function for the game loop itself."""
        current_room = self.game_map.opening_room()
#        last_room = self.game_map.next_room('end_game')
# THIS IS COMMENTED OUT DUE TO END GAME EXITING OR RETURNING TO START
# NO NOT REMOVE THIS LINE UNTIL DECISION TO ALWAYS LET PLAYER CHOOSE TO 
# EXIT THE GAME
                
        while current_room:# != last_room: 
            next_room_name = current_room.enter()
            current_room = self.game_map.next_room(next_room_name)
            
        current_room.enter()
     
    def fight(hero_stats, enemy_stats, win_next_room): 
        """
        This is the fight function that resolves game combat. It also
        resets the players rest flag when combat is entered that if 
        they survive they can rest again.
        """
       # EXPAND COMBAT FOR MORE INFO AND !FUN!
        i = 0   
        hero_stats[6] = 0
        while True:
            print('You engage in combat! 1 Fight or 2 Run\n')
            action = input('> ')
            if action == '1':
                
                print('You attack!\n')
                hero_stats[0] -= enemy_stats[2]
                enemy_stats[0] -= hero_stats[2]
#                print(hero_stats, enemy_stats)
                
                if hero_stats[0] <= 0:
                    print('You fall bravely in battle.\n')
                    return 'end_game'       
                elif enemy_stats[0] <= 0:
                    print(f'You slay the enemy {enemy_stats[4]}')
                    print("Above the body of your foe, you look "
                    "around.\n") 
                    # NOT SUPER SURE THIS FITS HERE NEED TO TEST
                    enemy_stats[3] = 0
                    return win_next_room
                else:
                    print('The combat continues!\n')
            elif action == '2':
                print('You retreat from the battle!\n') 
                    # NOTE(BCL): THIS NEEDS TO RETURN TO A PREVIOUS ROOM 
                    # OR LEAVE IF IN ANTI-C
                return 'end_game'
            elif i == 4:
                print('You block and block the attacks coming from your'
                ' foe, eventually, you are overwhelmed.\n')
                return 'end_game'
            else:
                print('Do not hesitate! Do something, anything!\n')
                i +=1
        return 0      
        
    def character(
        health, defence, attack, alive,
        name, max_hp, rested): 
        """
        This is the character creation function. It creates a key-value
        pair for the Engine.cast dict. 
        """
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
        """
        This is the rest function. It resets the 'hero' hit point count 
        to the set max_hp.
        """
        if Engine.cast['hero'][6] == 1: 
            #1 FLAG = IS ALREADY RESTED NO MORE NEEDED
            print("You already feel rested. Better get a move on!\n")
        else:
            print("You take a moment to catch your breath. You feel "
            "ready to soldier on!\n")
            Engine.cast['hero'][6] = 1
                #SET RESTED FLAG TO RESTED
            Engine.cast['hero'][0] = hero[5]
                #SET HERO HEALTH TO MAX HEALTH


# _______________MAP_____________________________


class Map(object):
    """
    This is the Map class that establishes the dict for the different
    rooms in the game and functions that lead around the map.
    """

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
        """
        The Map.__init__ establishes the first room that the player will
        enter at the start of the game. It should always be 'entrance' 
        otherwise the game will not initialize the cast properly.
        """
        self.start_room = start_room
        
    def next_room(self, room_name):
        """This function returns the 'key' to the next room."""
        dict_room_value = Map.dict_rooms.get(room_name)
        return dict_room_value        
        
    def opening_room(self):
        """
        This function sets the opening room for .next_room to pass to 
        the Engine for the first room established from the map object 
        creation.
        """
        return self.next_room(self.start_room)


dungeon_map = Map('entrance')
new_game = Engine(dungeon_map)
new_game.play()
 
