# Rooms: 
    # enter, exit, go to other rooms you have already gone to/ lockout
        #entrance, antichamber, chest, slime, orc (alter), hallway, crypt, 
        #exit (outside), death/end_game
# Actions: fight, rest, move
# Characters: hero, goblin, orc, bugbear, skeleton, 
# Objects: helmet, sword, gems


#_____________ROOM________________________

class Room(object):
   
    def enter(self): # this means room_antichamber.enter()
        go_in_to = Room.dict_rooms[self.room]
        print("ENTER THE ROOM")
        pass        
    
    # def enter(enter_text, player_options): # I HAVE THIS IN HERE TWICE
        
        # print(enter_text)
        
        # choice = int(input('>>> '))
        
        # while True: # Maybe make this a for-loop?
            # break # Replace with player_options
            
    def exit(self):
        pass
#list of [choices, the, player, can, make] since several of them are 
#common in each room, i.e. rest 
    
    
    
class Room_Entrance(Room):
    
    
    def enter(self):
        print("Enter the entrance of the cave")

class Room_Antichamber(Room):

    def enter(self):
        pass
        
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
        pass
        
        
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
        
    def next_scene(self, room_name):
        pass
        
    def opening_scene(self, start_room):
        print("here be opening_scene")
        self.Room.enter(start_room)
        
        
        pass
 
 #_______________ENGINE___________________
 
class Engine(object):
    
    def __init__(self, game_map):
        self.game_map = game_map
    
    def play(self):
        print('The game starts and everything is fine')
        print('Go to the first room (entrance)')
        thing = Room()
        thing.enter()  
    


thing = Room('entrance')
thing.enter()



# dungeon_map = Map('entrance')
# new_game = Engine(dungeon_map)
# new_game.play()
 
