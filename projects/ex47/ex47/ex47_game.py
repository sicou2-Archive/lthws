from random import randint
from sys import exit
from textwrap import dedent, fill

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
        Engine.fprint(Text.room['enter'])
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
        #try:
        #    Engine.character.cast['hero']
        #except KeyError:
        #    pass
         #   hero = Engine.character(10, 1, 1, 1,'hero', 10, 0)
         #   Engine.character.cast['hero'] = [10, 1, 1, 1,'hero', 10, 0]
            
        # try:   
            # Engine.cast['lockout']
        # except KeyError:
            # Engine.cast['lockout'] = {
                # 'chest_room': 1,
                # 'slime_room': 1,
                # 'alter_room' : 0,
                # 'alter': 1,
                # }
                # # 1 IS OPEN, 0 IS LOCKED OUT 
                
        Engine.fprint(Text.entrance['intro'])
        #print(fill(dedent(Text.room_entrance['intro']),79))        
        Engine.fprint(Text.entrance['enter'])
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
        # try:
            # Engine.cast['goblin']
        # except KeyError:
            # goblin = Engine.character(1, 1, 1, 1,'goblin', 5, 0)
                # # RETURN GOBLIN HEALTH TO 5
            # Engine.cast['goblin'] = goblin
        
        if Engine.character.cast['goblin'][3] == 1:
            # Check to see if Goblin is still alive when coming from 
            # another room
            
            

            Engine.fprint(Text.antichamber['enter'])
            i = 0
            while True:    
                
                action = input('> ')
               
                if action == '1':
                    next_room = Engine.fight(
                        Engine.character.cast['hero'], 
                        Engine.character.cast['goblin'],
                        'antichamber'
                        )

                    return next_room
                elif action == '2':
                    Engine.fprint(Text.antichamber['run'])
                    return 'end_game'
                        # DOUBLE CHECK THIS IS CORRECT RETURN
                elif i > 3:
                    Engine.fprint(Text.antichamber['stall_death'])
                    return 'end_game'
                else:
                    Engine.fprint(Text.antichamber['stall'])
                    i += 1            
        
        Engine.fprint(Text.antichamber['three_doors'])
        
        while True:

            choice = input('> ')
            
            if choice == '1': 
                if Engine.character.cast['lockout']['chest_room'] == 0:
                    # THIS NEEDS TO BE VERIFIED THAT IT WORKS
                    Engine.fprint(Text.antichamber['no_left_door'])
                    
                            # THESE CHOICES NEED TO BE VERIFIED THEY 
                            # MAKE SENSE
                    continue
                return 'chest'
                    # DOUBLE CHECK THIS RETURN IS CORRECT
            elif choice == '2': 
                if Engine.character.cast['lockout']['slime_room'] == 0:
                    Engine.fprint(Text.antichamber['no_center_door'])
                            # THESE CHOICES NEED TO BE VERIFIED THEY 
                            # MAKE SENSE
                    continue
                return 'slime'
            elif choice == '3': 
                return 'alter'
            elif choice == '4':
                Engine.rest(Engine.character.cast['hero'])
            else: 
                Engine.fprint(Text.antichamber['door_stall'])


class Room_Chest(Room):
    """This is the Chest room class."""
    def enter(self):
        """
        This is the working function for the Chest Room. It has a random 
        chance box to give the player an object to use. It leads only 
        back to the Antichamber.
        """
        while True: 
        
            Engine.fprint(Text.chest['enter'])
                # THIS NEEDS A STYLE REWRITE TO MATCH ANTICHAMBER
        
            action = input('> ')
            
            if action == '1':
                Engine.fprint(Text.chest['pick'])
                
                lock_test = 1 #randint(1,10)
                
                if lock_test == 1:
                    Engine.fprint(Text.chest['explode'])
                    Engine.character.cast['hero'][0] -= randint(1,5) 
                    # RANDOM 1-5 DAMAGE TO HERO
                    Engine.character.cast['hero'][6] = 0 
                    #REMOVES RESTED FLAG
                    
                    if Engine.character.cast['hero'][0] <= 0:
                    # NEED TO ADD A TEXT STATEMENT FOR KILLING PLAYER
                        return 'end_game'
                    
                    Engine.character.cast['lockout']['chest_room'] = 0 
                    Engine.fprint(Text.chest['return_empty'])
                    return 'antichamber'
                elif 2 <= lock_test and lock_test <= 5:
                    Engine.fprint(Text.chest['lock_break'])
                    Engine.fprint(Text.chest['return_empty'])
                    Engine.character.cast['lockout']['chest_room'] = 0
                    return 'antichamber'
                else:
                    Engine.fprint(Text.chest['helmet'])
                    Engine.character.cast['hero'][1] += 1 # +1 TO defence
                    Engine.character.cast['lockout']['chest_room'] = 0
                    return 'antichamber'
            elif action == '2':
                Engine.fprint(Text.chest['look'])
                return 'antichamber'
            elif action == '3': 
                Engine.rest(Engine.character.cast['hero'])
                return 'chest'
            else:
                Engine.fprint(Text.chest['stall'])


class Room_Slime(Room):
    """This is the Slime room class."""
    def enter(self):
        
        Engine.fprint(Text.slime['enter'])
        
        i = 0
        while True:
            action = input('> ')
            
            if action == '1':
                Engine.fprint(Text.slime['attack'])
                Engine.character.cast['slime'] = Engine.character(
                    1, 1, 1, 1, 'slime', 3, 0)
                        #REBALANCE SLIME AFTER TESTING
                next_room = Engine.fight(
                    Engine.character.cast['hero'], 
                    Engine.character.cast['slime'],
                    'antichamber'
                    )
                Engine.fprint(Text.slime['search'])
                Engine.character.cast['hero'][2] += 1 # ATTACK +1
                Engine.character.cast['lockout']['slime_room'] = 0 
                    #NO NEED TO COME BACK
                Engine.character.cast['lockout']['alter_room'] = 1 
                Engine.fprint(Text.slime['key'])
                return next_room
            elif action == '2':
                Engine.fprint(Text.slime['taunt'])
                Engine.fprint(Text.slime['sword'])
                Engine.character.cast['hero'][2] += 1 # ATTACK +1
                Engine.character.cast['lockout']['slime_room'] = 0 
                    #NO NEED TO COME BACK
                Engine.character.cast['lockout']['alter_room'] = 1 
                Engine.fprint(Text.slime['key'])
                return 'antichamber'
            elif action == '3':
                Engine.fprint(Text.slime['retreat'])
                return 'antichamber'
            elif i > 3:
                Engine.fprint(Text.slime['stall_death'])
                return 'end_game'
            else:
                Engine.fprint(Text.slime['stall'])
                i += 1


class Room_Alter(Room):
    """This is the Alter room class."""

    def enter(self):
        
        if Engine.character.cast['lockout']['alter_room'] == 0:
            Engine.fprint(Text.alter['locked'])
            return 'antichamber'

        # try:
            # Engine.cast['orc']
        # except KeyError:
            # orc = Engine.character(1, 1, 1, 1,'orc', 5, 0)
                # # REBALANCE ORC AFTER TESTING
            # Engine.cast['orc'] = orc

        if Engine.cast['orc'][3] == 1 and Engine.cast.get(
            'bugbear',False): 
            
            ###THIS IS BROKEN WITH CHARACTER UPDATE NEED SOLUTION TO FIX
            
            #CHECK TO SEE IF ORC IS ALIVE WHEN COMING FROM ANOTHER ROOM
            #AND IF BUGBEAR EXISTS
            Engine.fprint(Text.alter['back_enter'])
            
            i = 0
            while True:            
                action = input('> ')
                
                if action == '1': 
                    Engine.fprint(Text.alter['attack'])
                    next_room = Engine.fight(
                    Engine.cast['hero'], 
                    Engine.cast['orc'],
                    'alter',
                    ) 
                    return next_room
                elif action == '2': 
                    Engine.fprint(Text.alter['back_sneak'])
                    sneak_roll = randint(1,4) 
                    
                    if sneak_roll == 4: 
                        Engine.fprint(Text.alter['caught'])
                        next_room = Engine.fight(
                            Engine.cast['hero'], 
                            Engine.cast['orc'],
                            'alter',
                            )
                        return next_room
                    else:
                        Engine.fprint(Text.alter['sneak_anti'])
                        return 'antichamber'
                    return 'antichamber' 
                elif i == 3:
                    Engine.fprint(Text.alter['caught'])
                    next_room = Engine.fight(
                        Engine.cast['hero'],
                        Engine.cast['orc'],
                        'alter',
                        )
                    return next_room
                else: 
                    Engine.fprint(Text.alter['stall'])
                    i += 1

        if Engine.cast['orc'][3] == 1: 
            # CHECK TO SEE IF ORC IS ALIVE WHEN COMING FROM ANOTHER ROOM
            Engine.fprint(Text.alter['enter'])
            i = 0
            while True:            
                action = input('> ')
                
                if action == '1': 
                    Engine.fprint(Text.alter['attack'])
                    next_room = Engine.fight(
                    Engine.cast['hero'], 
                    Engine.cast['orc'],
                    'alter',
                    ) 
                    return next_room
                elif action == '2': 
                    Engine.fprint(Text.alter['sneak'])
                    
                    sneak_roll = randint(1,4) 
                    
                    if sneak_roll == 4: 
                        Engine.fprint(Text.alter['caught'])
                        next_room = Engine.fight(
                            Engine.cast['hero'], 
                            Engine.cast['orc'],
                            'alter',
                            )
                        return next_room
                    else:
                        Engine.fprint(Text.alter['hall'])
                        return 'hallway'
                elif action == '3': 
                    Engine.fprint(Text.alter['retreat'])
                    return 'antichamber' 
                elif i == 3:
                    Engine.fprint(Text.alter['caught'])
                    next_room = Engine.fight(
                        Engine.cast['hero'],
                        Engine.cast['orc'],
                        'alter',
                        )
                    return next_room
                else: 
                    Engine.fprint(Text.alter['stall'])
                    i += 1

        while True: 
            
            Engine.fprint(Text.alter['victory'])
            
            action = input('> ')
                    
            if action == '1': 
                if Engine.cast['lockout']['alter'] == 0:
                    Engine.fprint(Text.alter['already_strong'])
                    continue
                Engine.fprint(Text.alter['alter'])
                
                i = 0
                while True:
                
                    choice = input('> ')
                
                    if choice == '1': 
                        event = randint(1,4)
                        if event == 1:
                            Engine.fprint(Text.alter['deceit'])
                            return 'end_game'
                        else:
                            Engine.fprint(Text.alter['strong'])
                            Engine.cast['hero'][5] += 5 
                                #maxhp +5
                            Engine.cast['hero'][0] = Engine.cast[
                                'hero'][5] 
                                #HEALTH TO MAX
                            Engine.cast['lockout']['alter'] = 0 
                            break
                    elif choice == '2': 
                        Engine.fprint(Text.alter['leave_alone'])
                        break
                    elif i == 3:
                        Engine.fprint(Text.alter['stall_alter_death'])
                        return 'end_game'
                    else:
                        Engine.fprint(Text.alter['stall_alter'])
                        i += 1
            elif action == '2': 
                return 'hallway'
            elif action == '3': 
                Engine.rest(Engine.cast['hero']) 
            elif action == '4': 
                if (Engine.cast['lockout']['chest_room'] == 0 and 
                    Engine.cast['lockout']['slime_room'] == 0):
                    Engine.fprint(Text.alter['urge_advance'])
                else:
                    Engine.fprint(Text.alter['return'])
                    return 'antichamber'
            else:
                Engine.fprint(Text.alter['urge_choice'])


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
                Engine.fprint(Text.hallway['enter'])
                action = input("> ")
                      
                if action == '1':
                    Engine.fprint(Text.hallway['attack'])
                    next_room = Engine.fight(
                        Engine.cast['hero'], 
                        Engine.cast['bugbear'],
                        'crypt',
                        )
                    Engine.fprint(Text.hallway['victory'])
                    return next_room
                elif action == '2':        
                  
                    sneak_roll = randint(1,4)

                    if sneak_roll == 1:
                        Engine.fprint(Text.hallway['sneak_fail'])
                        next_room = Engine.fight(
                            Engine.cast['hero'], 
                            Engine.cast['bugbear'],
                            'crypt'
                            )
                        return next_room
                    else:
                        Engine.fprint(Text.hallway['sneak_success'])
                        #THIS IS NOT CORRECT SHOULD RETURN SOMETHING 
                        #HERE 
                        # IN THE HALLWAY I THINK
                    
                        if Engine.cast['orc'][3] == 1:
                            Engine.fprint(Text.hallway['retreat_choice'])
                            
                            choice = input('> ')
                            i = 0
                            while True:
                                if choice == '1': 
                                    return 'alter' 
                                elif choice == '2': 
                                    sneak_roll = randint(1,4)
                                    
                                    if sneak_roll == 1:
                                        Engine.fprint(Text.hallway[
                                        'rest_fail'])
                                        next_room = Engine.fight(
                                            Engine.cast['hero'], 
                                            Engine.cast['bugbear'],
                                            'crypt',
                                            )
                                        Engine.fprint(Text.hallway['advance'])
                                        #MAYBE ADD A CHANCE TO GO BACK 
                                        #TO THE BUGBEAR?
                                        #SHOULD MAYBE DO THIS IN 
                                        #ROOM_CRYPT
                                    else: 
                                        Engine.rest(Engine.cast['hero'])
                                        return 'hallway'
                                elif i == 3:
                                    Engine.fprint(Text.hallway[
                                    'stall_sneak_death'])
                                    return 'end_game'
                                else:
                                    Engine.fprint(Text.hallway['stall'])
                                    i += 1
                        else:
                            return 'alter'
                else:
                    Engine.fprint(Text.hallway['stall_death'])
                    return 'end_game'
        elif Engine.cast['bugbear'][3] == 0:
            Engine.fprint(Text.hallway['victory'])
            return 'crypt'
        else:
            Engine.fprint(Text.hallway['room_error'])
            return None


class Room_Crypt(Room):
    """This is the Crypt room class."""


    def enter(self):
        try:
            Engine.cast['skeleton']
        except KeyError:
            skeleton = Engine.character(5, 1, 1, 1,'skeleton', 5, 0)
            Engine.cast['skeleton'] = skeleton

        Engine.fprint(Text.crypt['enter'])
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
                Engine.fprint(Text.crypt['crypt'])

                i = 0
 
                while True:
                    choice = input("> ")
                    
                    if choice == '1':
                        Engine.cast['gem'] = 1
                        Engine.fprint(Text.crypt['gem_get'])
                        false_choice = input("> ")
                        
                        if false_choice == '1':
                            Engine.fprint(Text.crypt['defend'])
                            next_room = Engine.fight(
                                Engine.cast['hero'], 
                                Engine.cast['skeleton'],
                                'outside',
                                )
                            Engine.fprint(Text.crypt['climb'])
                            return next_room
                        elif false_choice == '2' or false_choice == '3':
                            Engine.fprint(Text.crypt['run'])
                            next_room = Engine.fight(
                                Engine.cast['hero'], 
                                Engine.cast['skeleton'],
                                'outside',
                                )
                            Engine.fprint(Text.crypt['climb'])
                            return next_room
                        else:
                            Engine.fprint(Text.crypt['gem_stall_death'])
                    elif choice == '2':
                        Engine.fprint(Text.crypt['gem_leave'])
                        break
                    elif i == 3:
                        Engine.fprint(Text.crypt['gem_stall_death'])
                        return 'end_game'
                    else:
                        Engine.fprint(Text.crypt['stall_gem'])
                        i += 1
            elif action == '2': 
                Engine.fprint(Text.crypt['no_gem_leave'])
                return 'outside'
                
            elif action == '3': 
                Engine.rest(Engine.cast['hero'])
                continue
            elif action == '4':
                if Engine.cast['lockout']['alter'] == 0:
                    Engine.fprint(Text.crypt['no_return'])
                else:
                    Engine.fprint(Text.crypt['return'])
                    return 'alter'
            else: 
                Engine.fprint(Text.crypt['stall'])


class Room_Outside(Room):
    """This is the Outside room class."""
    def enter(self):
    
        if Engine.cast['gem'] == 1:
        
            Engine.fprint(Text.outside['enter'])
            return 'end_game'
        else:
            Engine.fprint(Text.outside['no_gem_enter'])
            return 'end_game'


class Room_End_Game(Room):
    """
    This is the End Game room class. This should always be the last room
    that a player sees.
    """

    def enter(self):
    
### THIS FEELS LIKE IT SHOULD HAVE A TRY EXCEPT TO CLEAN IT UP A BIT
        Engine.fprint(Text.end_game['end'])
        choice = input('> ')
        if choice == 'y':
            Engine.cast = {}
            return 'entrance'
        elif choice == 'n':
           exit(0)
        else:
            while True:
                Engine.fprint(Text.end_game['except_end'])
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
        
    def sneak():
        """This is a place holder for creating a sneak function here."""
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

    def __init__(self): #taking out stats not sure if it is needed
        """This is a place holder __init__ if needed."""
        self.cast = {
        'hero' : [10, 1, 1, 1,'hero', 10, 0],
        'goblin': [1, 1, 1, 1,'goblin', 5, 0],
        'slime': [1, 1, 1, 1, 'slime', 3, 0],
        'orc': [1, 1, 1, 1,'orc', 5, 0],
        'bugbear': [1, 1, 1, 1,'bugbear', 5, 0],
        'skeleton': [5, 1, 1, 1,'skeleton', 5, 0], 
        'lockout': { # 1 is unlocked, 0 is locked.
            'chest_room': 1,
            'slime_room': 1,
            'alter_room': 0,
            'alter': 1,
            }
        }
    
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

#    cast = {} 
        #THIS IS A CLASS VARIABLE FOR CAST, LOCKOUT, AND GEM STATUS
    
    def __init__(self, game_map):
        """
        This is the __init__ function that uses attribure of start room
        from the Map class
        """
        self.game_map = game_map
        Engine.character = Character()
    
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
            Engine.fprint(Text.fight['fight'])
            action = input('> ')
            if action == '1':
                
                Engine.fprint(Text.fight['attack'])
                hero_stats[0] -= enemy_stats[2]
                enemy_stats[0] -= hero_stats[2]
#                print(hero_stats, enemy_stats)
                
                if hero_stats[0] <= 0:
                    Engine.fprint(Text.fight['die'])
                    return 'end_game'       
                elif enemy_stats[0] <= 0:
                    Engine.fprint(Text.fight['victory_1'] + enemy_stats[4])
                    Engine.fprint(Text.fight['look'])
                    # NOT SUPER SURE THIS FITS HERE NEED TO TEST
                    enemy_stats[3] = 0
                    return win_next_room
                else:
                    print('The combat continues!\n')
            elif action == '2':
                Engine.fprint(Text.fight['retreat'])
                    # NOTE(BCL): THIS NEEDS TO RETURN TO A PREVIOUS ROOM 
                    # OR LEAVE IF IN ANTI-C
                return 'end_game'
            elif i == 4:
                Engine.fprint(Text.fight['stall_death'])
                return 'end_game'
            else:
                Engine.fprint(Text.fight['stall'])
                i +=1
        return 0      
        
    # def character(
        # health, defence, attack, alive,
        # name, max_hp, rested): 
        # """
        # This is the character creation function. It creates a key-value
        # pair for the Engine.cast dict. 
        # """
# # IS THIS THE BEST FUNCTION TO DO THIS? WHY NOT JUST PASS INFO 
# # TO THE CAST DICT?
# # THERE ARE A LOT OF ARGUMENTS HERE
        # stats = [health, defence, attack, alive, name, max_hp, rested]

        # # hitpoints = 0
        # # hitpoints = randrange(0,10)
        
        # # attack = 1

        # # stats = [randrange(0,10), attack]
        # # print(stats)
        
        # return stats   

    def rest(hero): 
        """
        This is the rest function. It resets the 'hero' hit point count 
        to the set max_hp.
        """
        if Engine.cast['hero'][6] == 1: 
            #1 FLAG = IS ALREADY RESTED NO MORE NEEDED
            Engine.fprint(Text.rest['rested'])
        else:
            Engine.fprint(Text.rest['rest'])
            Engine.cast['hero'][6] = 1
                #SET RESTED FLAG TO RESTED
            Engine.cast['hero'][0] = hero[5]
                #SET HERO HEALTH TO MAX HEALTH
                
    def fprint(to_print):
        print(fill(dedent(to_print),79))


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
 
