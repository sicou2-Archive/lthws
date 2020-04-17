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
    def enter(self): # 
        print("ENTER THE ROOM THAT IS NOT A ROOM, THINGS ARE"
            "BROKEN")
        
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
        #Note(BCL): LOCKOUT MAYBE NEEDS TO BE INSIDE CAST, 
        # FEWER OBJECTS TO PASS AROUND
            Engine.cast['lockout']
        except KeyError:
            Engine.cast['lockout'] = {
                'chest_room': 1,
                'slime_room': 1,
                'alter_room' : 1,
                'alter': 1,
                } # 1 IS OPEN, 0 IS LOCKED OUT 
        
    def enter(self):

        print('It works')
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
            
            print('A goblin is here and attacks.'
                '\n1 Engage in combat 2 Run')

            i = 0
            while True:    
                # This is the Goblin fight()
                
                action = input('> ')
               
                if action == '1': 
                    Engine.fight(Engine.cast['hero'], Engine.cast['goblin'])
                    print('Above the body of your foe, you look '
                    'around.')
                    break
                elif action == '2':
                    print('You run from the room and go looking for '
                    'help to continue the fight.')
                    return 'end_game'
                        # DOUBLE CHECK THIS IS CORRECT RETURN
                elif i > 3:
                    print('Goblin attacks while you stare at him.')
                    return 'end_game'
                else:
                    print('He looks mean, do something! Quick!')
                    i += 1            
        
        while True:
            
            print ('You see three doors. \nChoose a door or rest: '
                '\n1 Left, 2 Center, 3 Right, 4 Rest a moment') 
                    # List of decisions after fight
            
            choice = input('> ')
            
            if choice == '1': 
                if Engine.cast['lockout']['chest_room'] == 0:
                    # THIS NEEDS TO BE VERIFIED THAT IT WORKS
                    print('There is no reason to go back in there. '
                        '\nChoose a different room: \n'
                        '2 Center, 3 Right, 4 Rest a moment')
                            # THESE CHOICES NEED TO BE VERIFIED THEY 
                            # MAKE SENSE
                    continue
                return 'chest'
                    # DOUBLE CHECK THIS RETURN IS CORRECT
            elif choice == '2': 
                if Engine.cast['lockout']['slime_room'] == 0:
                    print('There is no reason to go back in there. '
                        '\nChoose a different room: \n'
                        '1 Left, 3 Right, 4 Rest a moment')
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
                print('Moving on is the only hope for you now. Choose a'
                ' room:\n1 Left, 2 Center, 3 Right, 4 Rest a moment')      
 
#        print('Antichamber')
#        return 'end_game'
#        THIS RETURN SHOULD NOT BE NEEDED
class Room_Chest(Room):

    def enter(self):
        return 'end_game'
            # PLACE HOLDER RETURN
        
class Room_Slime(Room):

    def enter(self):
        return 'end_game'
            # PLACE HOLDER RETURN
        
class Room_Alter(Room):

    def enter(self):
        return 'end_game'
        
class Room_Hallway(Room):

    def enter(self):
        pass
        
class Room_Crypt(Room):

    def enter(self):
        pass
        
class Room_Outside(Room):

    def enter(self):
        pass
        
class Room_End_Game(Room):

    def enter(self):
    
# THERE IS A BUG HERE WHEN COMING FROM FIGHT(), IT ONLY HAS TWO ELEMENTS
# OF CAST AND NOT THE WHOLE ARGUMENT OF "CAST". NEED TO LOOK IN TO HOW 
# TO 1 MAKE THIS WORK, 2 MAKE IT WORK WELL

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
                    dungeon_map = Map('entrance') 
                    # dungeon_map.start_room = 'entrance'
                    new_game = Engine(dungeon_map) 
                    # new_game.game_map = dungeon_map.start_room = 
                    # 'entrance'
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
                    return 'end_game'       
                elif enemy_stats[0] <= 0:
                    print(f'You slay the enemy {enemy_stats[4]}')
                    enemy_stats[3] = 0
                    return (hero_stats, enemy_stats)
                else:
                    print('The combat continues!')
            elif action == '2':
                print('You retreat from the battle!') 
                    # NOTE(BCL): THIS NEEDS TO RETURN TO A PREVIOUS ROOM 
                    # OR LEAVE IF IN ANTI-C
                return end_game() 
            elif i == 4:
                print('You block and block the attacks coming from your'
                ' foe, eventually, you are overwhelmed.')
                return end_game()
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
 
