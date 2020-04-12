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
        print("ENTER THE ROOM THAT IS NOT A ROOM, THINGS ARE"
            "BROKEN")
        exit(1)        
    
    # def enter(enter_text, player_options): # I HAVE THIS IN HERE TWICE
        
        # print(enter_text)
        
        # choice = int(input('>>> '))
        
        # while True: # Maybe make this a for-loop?
            # break # Replace with player_options
            
    def exit(self): # I dont think I need this
        pass
#list of [choices, the, player, can, make] since several of them are 
#common in each room, i.e. rest 
    
    
    
class Room_Entrance(Room):
    
    def enter(self):
        print('It works')

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
        
    def next_room(self, room_name):
        dict_room_value = self.dict_rooms.get(room_name)
        return dict_room_value

        pass
        
    def opening_room(self):
        return self.next_room(self.start_room)
        
 
 #_______________ENGINE___________________
 
class Engine(object):
    
    def __init__(self, game_map):
        self.game_map = game_map
    
    def play(self):
        current_room = self.game_map.opening_room()
        
        while current_room != Room_End_Game:
            next_room = current_room.enter()
    ###STOPPED HERE, THIS DOES NOT WORK 
            current_room = self.game_map.next_room(next_room)
            
    

dungeon_map = Map('entrance') # dungeon_map.start_room = 'entrance'
new_game = Engine(dungeon_map) # new_game.game_map = dungeon_map.start_room = 'entrance'
new_game.play()
 
