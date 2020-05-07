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
        print(dedent(Text.room_text['enter']))
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
                
        Engine.fprint(Text.entrance_text['intro'])
        #print(fill(dedent(Text.room_entrance_text['intro']),79))        
        print(dedent(Text.entrance_text['enter']))
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
            
            

            print(dedent(Text.antichamber_text['enter']))
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
                    print(dedent(Text.antichamber_text['run']))
                    return 'end_game'
                        # DOUBLE CHECK THIS IS CORRECT RETURN
                elif i > 3:
                    print(dedent(Text.antichamber_text[
                            'stall_death']))
                    return 'end_game'
                else:
                    print(dedent(Text.antichamber_text['stall']))
                    i += 1            
        
        print(dedent(Text.antichamber_text['three_doors']))
        
        while True:

            choice = input('> ')
            
            if choice == '1': 
                if Engine.cast['lockout']['chest_room'] == 0:
                    # THIS NEEDS TO BE VERIFIED THAT IT WORKS
                    print(dedent(Text.antichamber_text[
                        'no_left_door']))    
                    
                            # THESE CHOICES NEED TO BE VERIFIED THEY 
                            # MAKE SENSE
                    continue
                return 'chest'
                    # DOUBLE CHECK THIS RETURN IS CORRECT
            elif choice == '2': 
                if Engine.cast['lockout']['slime_room'] == 0:
                    print(dedent(Text.antichamber_text[
                        'no_center_door']))
                            # THESE CHOICES NEED TO BE VERIFIED THEY 
                            # MAKE SENSE
                    continue
                return 'slime'
            elif choice == '3': 
                return 'alter'
            elif choice == '4':
                Engine.rest(Engine.cast['hero'])
            else: 
                print(dedent(Text.antichamber_text['door_stall']))


class Room_Chest(Room):
    """This is the Chest room class."""
    def enter(self):
        """
        This is the working function for the Chest Room. It has a random 
        chance box to give the player an object to use. It leads only 
        back to the Antichamber.
        """
        while True: 
        
            print(dedent(Text.chest_text['enter']))
                # THIS NEEDS A STYLE REWRITE TO MATCH ANTICHAMBER
        
            action = input('> ')
            
            if action == '1':
                print(dedent(Text.chest_text['pick']))
                
                lock_test = randint(1,10)
                
                if lock_test == 1:
                    print(dedent(Text.chest_text['explode']))
                    cast['hero'][0] -= randint(1,5) 
                    # RANDOM 1-5 DAMAGE TO HERO
                    cast['hero'][6] = 0 
                    #REMOVES RESTED FLAG
                    
                    if cast['hero'][0] == 0:
                        return 'end_game'
                    
                    Engine.cast['lockout']['chest_room'] = 0 
                    print(dedent(Text.chest_text['return_empty']))
                    return 'antichamber'
                elif 2 <= lock_test and lock_test <= 5:
                    print(dedent(Text.chest_text['lock_break']))
                    print(dedent(Text.chest_text['return_empty']))
                    Engine.cast['lockout']['chest_room'] = 0
                    return 'antichamber'
                else:
                    print(dedent(Text.chest_text['helmet']))
                    Engine.cast['hero'][1] += 1 # +1 TO defence
                    Engine.cast['lockout']['chest_room'] = 0
                    return 'antichamber'
            elif action == '2':
                print(dedent(Text.chest_text['look']))
                return 'antichamber'
            elif action == '3': 
                Engine.rest(Engine.cast['hero'])
                return 'chest'
            else:
                print(dedent(Text.chest_text['stall']))


class Room_Slime(Room):
    """This is the Slime room class."""
    def enter(self):
        
        print(dedent(Text.slime_text['enter']))
        
        i = 0
        while True:
            action = input('> ')
            
            if action == '1':
                print(dedent(Text.slime_text['attack']))
                Engine.cast['slime'] = Engine.character(
                    1, 1, 1, 1, 'slime', 3, 0)
                        #REBALANCE SLIME AFTER TESTING
                next_room = Engine.fight(
                    Engine.cast['hero'], 
                    Engine.cast['slime'],
                    'antichamber'
                    )
                print(dedent(Text.slime_text['search']))
                Engine.cast['hero'][2] += 1 # ATTACK +1
                Engine.cast['lockout']['slime_room'] = 0 
                    #NO NEED TO COME BACK
                Engine.cast['lockout']['alter_room'] = 1 
                print(dedent(Text.slime_text['key']))
                return next_room
            elif action == '2':
                print(dedent(Text.slime_text['taunt']))
                print(dedent(Text.slime_text['sword']))
                Engine.cast['hero'][2] += 1 # ATTACK +1
                Engine.cast['lockout']['slime_room'] = 0 
                    #NO NEED TO COME BACK
                Engine.cast['lockout']['alter_room'] = 1 
                print(dedent(Text.slime_text['key']))
                return 'antichamber'
            elif action == '3':
                print(dedent(Text.slime_text['retreat']))
                return 'antichamber'
            elif i > 3:
                print(dedent(Text.slime_text['stall_death']))
                return 'end_game'
            else:
                print(dedent(Text.slime_text['stall']))
                i += 1


class Room_Alter(Room):
    """This is the Alter room class."""

    def enter(self):
        
        if Engine.cast['lockout']['alter_room'] == 0:
            print(dedent(Text.alter_text['locked']))
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
            print(dedent(Text.alter_text['back_enter']))
            
            i = 0
            while True:            
                action = input('> ')
                
                if action == '1': 
                    print(dedent(Text.alter_text['attack']))
                    next_room = Engine.fight(
                    Engine.cast['hero'], 
                    Engine.cast['orc'],
                    'alter',
                    ) 
                    return next_room
                elif action == '2': 
                    print(dedent(Text.alter_text['back_sneak']))
                    sneak_roll = randint(1,4) 
                    
                    if sneak_roll == 4: 
                        print(dedent(Text.alter_text['caught']))
                        next_room = Engine.fight(
                            Engine.cast['hero'], 
                            Engine.cast['orc'],
                            'alter',
                            )
                        return next_room
                    else:
                        print(dedent(Text.alter_text[
                            'sneak_anti']))
                        return 'antichamber'
                    return 'antichamber' 
                elif i == 3:
                    print(dedent(Text.alter_text['caught']))
                    next_room = Engine.fight(
                        Engine.cast['hero'],
                        Engine.cast['orc'],
                        'alter',
                        )
                    return next_room
                else: 
                    print(dedent(Text.alter_text['stall']))
                    i += 1

        if Engine.cast['orc'][3] == 1: 
            # CHECK TO SEE IF ORC IS ALIVE WHEN COMING FROM ANOTHER ROOM
            print(dedent(Text.alter_text['enter']))
            i = 0
            while True:            
                action = input('> ')
                
                if action == '1': 
                    print(dedent(Text.alter_text['attack']))
                    next_room = Engine.fight(
                    Engine.cast['hero'], 
                    Engine.cast['orc'],
                    'alter',
                    ) 
                    return next_room
                elif action == '2': 
                    print(dedent(Text.alter_text['sneak']))
                    
                    sneak_roll = randint(1,4) 
                    
                    if sneak_roll == 4: 
                        print(dedent(Text.alter_text['caught']))
                        next_room = Engine.fight(
                            Engine.cast['hero'], 
                            Engine.cast['orc'],
                            'alter',
                            )
                        return next_room
                    else:
                        print(dedent(Text.alter_text['hall']))
                        return 'hallway'
                elif action == '3': 
                    print(dedent(Text.alter_text['retreat']))
                    return 'antichamber' 
                elif i == 3:
                    print(dedent(Text.alter_text['caught']))
                    next_room = Engine.fight(
                        Engine.cast['hero'],
                        Engine.cast['orc'],
                        'alter',
                        )
                    return next_room
                else: 
                    print(dedent(Text.alter_text['stall']))
                    i += 1

        while True: 
            
            print(dedent(Text.alter_text['victory']))
            
            action = input('> ')
                    
            if action == '1': 
                if Engine.cast['lockout']['alter'] == 0:
                    print(dedent(Text.alter_text[
                        'already_strong']))
                    continue
                print(dedent(Text.alter_text['alter']))
                
                i = 0
                while True:
                
                    choice = input('> ')
                
                    if choice == '1': 
                        event = randint(1,4)
                        if event == 1:
                            print(dedent(Text.alter_text[
                                'deceit']))    
                            return 'end_game'
                        else:
                            print(dedent(Text.alter_text[
                                'strong']))
                            Engine.cast['hero'][5] += 5 
                                #maxhp +5
                            Engine.cast['hero'][0] = Engine.cast[
                                'hero'][5] 
                                #HEALTH TO MAX
                            Engine.cast['lockout']['alter'] = 0 
                            break
                    elif choice == '2': 
                        print(dedent(Text.alter_text[
                            'leave_alone']))
                        break
                    elif i == 3:
                        print(dedent(Text.alter_text[
                        'stall_alter_death']))
                        return 'end_game'
                    else:
                        print(dedent(Text.alter_text[
                            'stall_alter']))
                        i += 1
            elif action == '2': 
                return 'hallway'
            elif action == '3': 
                Engine.rest(Engine.cast['hero']) 
            elif action == '4': 
                if (Engine.cast['lockout']['chest_room'] == 0 and 
                    Engine.cast['lockout']['slime_room'] == 0):
                    print(dedent(Text.alter_text['urge_advance']))
                else:
                    print(dedent(Text.alter_text['return']))
                    return 'antichamber'
            else:
                print(dedent(Text.alter_text['urge_choice']))


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
                print(dedent(Text.hallway_text['enter']))
                action = input("> ")
                      
                if action == '1':
                    print(dedent(Text.hallway_text['attack']))
                    next_room = Engine.fight(
                        Engine.cast['hero'], 
                        Engine.cast['bugbear'],
                        'crypt',
                        )
                    print(dedent(Text.hallway_text['victory']))
                    return next_room
                elif action == '2':        
                  
                    sneak_roll = randint(1,4)

                    if sneak_roll == 1:
                        print(dedent(Text.hallway_text[
                            'sneak_fail']))
                        next_room = Engine.fight(
                            Engine.cast['hero'], 
                            Engine.cast['bugbear'],
                            'crypt'
                            )
                        return next_room
                    else:
                        print(dedent(Text.hallway_text[
                            'sneak_success']))    
                        #THIS IS NOT CORRECT SHOULD RETURN SOMETHING 
                        #HERE 
                        # IN THE HALLWAY I THINK
                    
                        if Engine.cast['orc'][3] == 1:
                            print(dedent(Text.hallway_text[
                                'retreat_choice']))
                            
                            choice = input('> ')
                            i = 0
                            while True:
                                if choice == '1': 
                                    return 'alter' 
                                elif choice == '2': 
                                    sneak_roll = randint(1,4)
                                    
                                    if sneak_roll == 1:
                                        print(dedent(
                                            Text.hallway_text[
                                            'rest_fail']))
                                        next_room = Engine.fight(
                                            Engine.cast['hero'], 
                                            Engine.cast['bugbear'],
                                            'crypt',
                                            )
                                        print(dedent(
                                            Text.hallway_text[
                                            'advance']))
                                        #MAYBE ADD A CHANCE TO GO BACK 
                                        #TO THE BUGBEAR?
                                        #SHOULD MAYBE DO THIS IN 
                                        #ROOM_CRYPT
                                    else: 
                                        Engine.rest(Engine.cast['hero'])
                                        return 'hallway'
                                elif i == 3:
                                    print(dedent(
                                        Text.hallway_text[
                                        'stall_sneak_death']))
                                    return 'end_game'
                                else:
                                    print(dedent(
                                        Text.hallway_text[
                                        'stall']))
                                    i += 1
                        else:
                            return 'alter'
                else:
                    print(dedent(Text.hallway_text['stall_death']))
                    return 'end_game'
        elif Engine.cast['bugbear'][3] == 0:
            print(dedent(Text.hallway_text['victory']))
            return 'crypt'
        else:
            print(dedent(Text.hallway_text['room_error']))
            return None


class Room_Crypt(Room):
    """This is the Crypt room class."""


    def enter(self):
        try:
            Engine.cast['skeleton']
        except KeyError:
            skeleton = Engine.character(5, 1, 1, 1,'skeleton', 5, 0)
            Engine.cast['skeleton'] = skeleton

        print(dedent(Text.crypt_text['enter']))
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
                print(dedent(Text.crypt_text['crypt']))

                i = 0
 
                while True:
                    choice = input("> ")
                    
                    if choice == '1':
                        Engine.cast['gem'] = 1
                        print(dedent(Text.crypt_text['gem_get']))
                        false_choice = input("> ")
                        
                        if false_choice == '1':
                            print(dedent(Text.crypt_text[
                                'defend']))
                            next_room = Engine.fight(
                                Engine.cast['hero'], 
                                Engine.cast['skeleton'],
                                'outside',
                                )
                            print(dedent(Text.crypt_text['climb']))
                            return next_room
                        elif false_choice == '2' or false_choice == '3':
                            print(dedent(Text.crypt_text['run']))
                            next_room = Engine.fight(
                                Engine.cast['hero'], 
                                Engine.cast['skeleton'],
                                'outside',
                                )
                            print(dedent(Text.crypt_text['climb']))
                            return next_room
                        else:
                            print(dedent(Text.crypt_text[
                                'gem_stall_death']))
                    elif choice == '2':
                        print(dedent(Text.crypt_text['gem_leave']))
                        break
                    elif i == 3:
                        print(dedent(Text.crypt_text[
                            'gem_stall_death']))
                        return 'end_game'
                    else:
                        print(dedent(Text.crypt_text['stall_gem']))
                        i += 1
            elif action == '2': 
                print(dedent(Text.crypt_text['no_gem_leave']))
                return 'outside'
                
            elif action == '3': 
                Engine.rest(Engine.cast['hero'])
                continue
            elif action == '4':
                if Engine.cast['lockout']['alter'] == 0:
                    print(dedent(Text.crypt_text['no_return']))
                else:
                    print(dedent(Text.crypt_text['return']))
                    return 'alter'
            else: 
                print(dedent(Text.crypt_text['stall']))


class Room_Outside(Room):
    """This is the Outside room class."""
    def enter(self):
    
        if Engine.cast['gem'] == 1:
        
            print(dedent(Text.outside_text['enter']))
            return 'end_game'
        else:
            print(dedent(Text.outside_text['no_gem_enter']))
            return 'end_game'


class Room_End_Game(Room):
    """
    This is the End Game room class. This should always be the last room
    that a player sees.
    """

    def enter(self):
    
### THIS FEELS LIKE IT SHOULD HAVE A TRY EXCEPT TO CLEAN IT UP A BIT
        print(dedent(Text.end_game_text['end']))
        choice = input('> ')
        if choice == 'y':
            Engine.cast = {}
            return 'entrance'
        elif choice == 'n':
           exit(0)
        else:
            while True:
                print(dedent(Text.end_game_text['except_end']))
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
            print(dedent(Text.engine_fight_text['fight']))
            action = input('> ')
            if action == '1':
                
                print(dedent(Text.engine_fight_text['attack']))
                hero_stats[0] -= enemy_stats[2]
                enemy_stats[0] -= hero_stats[2]
#                print(hero_stats, enemy_stats)
                
                if hero_stats[0] <= 0:
                    print(dedent(Text.engine_fight_text['die']))
                    return 'end_game'       
                elif enemy_stats[0] <= 0:
                    print(dedent(Text.engine_fight_text['victory_1'] 
                        + enemy_stats[4]))
                    print(dedent(Text.engine_fight_text['look']))
                    # NOT SUPER SURE THIS FITS HERE NEED TO TEST
                    enemy_stats[3] = 0
                    return win_next_room
                else:
                    print('The combat continues!\n')
            elif action == '2':
                print(dedent(Text.engine_fight_text['retreat']))
                    # NOTE(BCL): THIS NEEDS TO RETURN TO A PREVIOUS ROOM 
                    # OR LEAVE IF IN ANTI-C
                return 'end_game'
            elif i == 4:
                print(dedent(Text.engine_fight_text['stall_death']))
                return 'end_game'
            else:
                print(dedent(Text.engine_fight_text['stall']))
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
            print(dedent(Text.engine_rest_text['rested']))
        else:
            print(dedent(Text.engine_rest_text['rest']))
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
 
