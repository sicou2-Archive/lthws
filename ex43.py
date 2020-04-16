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
    
  
    def enter(self): # 
        print("ENTER THE ROOM THAT IS NOT A ROOM, THINGS ARE"
            "BROKEN")
        
        exit(1)        
    
  

#list of [choices, the, player, can, make] since several of them are 
#common in each room, i.e. rest 
    
    
    
class Room_Entrance(Room):

#    def __init__(self):
#        super().__init__()
    
    
    def enter(self):
        Engine.cast['hero'] = [1,2,3]
        print('It works')
        return 'antichamber' # THIS RETURN SHOULD CHANGE TO THE REAL
            # NEXT ROOM

class Room_Antichamber(Room):

    def enter(self):
 
        print('Antichamber')
        return 'end_game'
class Room_Chest(Room):

    def enter(self):
        pass
        
class Room_Slime(Room):

    def enter(self):
        pass
        
class Room_Alter(Room):

    def enter(self):
        pass
        
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
        print('Dead')
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

class Character(object): #maybe combine with items; things(?)

    def __init__(self, stats):
        pass
    
    def create_character():
        pass
        
class Items(object): 

    def create_item():
        pass
        

 #_______________ENGINE___________________
 
class Engine(object):

    def remove_me():
    # NEED self.cast
    # NEED HERO

        # cast = {}
        
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
        pass
        
        
    
    def __init__(self, game_map):
        self.game_map = game_map
        Engine.cast = {} # cast is a list and characters should be a dict
    
    def play(self):
        current_room = self.game_map.opening_room()
        last_room = self.game_map.next_room('end_game')
                
        while current_room != last_room: 
            next_room_name = current_room.enter()
            print(Engine.cast)
            current_room = self.game_map.next_room(next_room_name)
            
        current_room.enter()
     
    def fight(self, hero_stats, enemy_stats): 
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
                print('You block and block the attacks coming from your '
                'for, but eventually you are overwhelmed.')
                return end_game()
            else:
                print('Do not hesitate! Do something, anything!')
                i +=1
        return 0      
        
    def character(health, defence, 
        attack, alive, name, 
        max_hp, rested): 
        
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

    def rest(self, hero): 
    
    #THINK I NEED AN INIT HERE
    
        if self.hero[6] == 1: # 1 IS ALREADY RESTED NO NEED FOR MORE
            print("You already feel as good as you are going to feel. "
            "Better get a move on!")
            return 0 
        else:
            print("You take a moment to catch your breath. You feel like "
            "you can soldier on!")
            self.hero[6] = 1
            self.hero[0] = hero[5]
            return self.hero 
        
        
     #   hero[4] = 1
        return 0      
            
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
 
