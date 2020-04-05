# Rooms: 
    # enter, exit, go to other rooms you have already gone to/ lockout
        #entrance, antichamber, chest, slime, orc (alter), hallway, crypt, 
        #exit (outside), death/end_game
# Actions: fight, rest, move
# Characters: hero, goblin, orc, bugbear, skeleton, 
# Objects: helmet, sword, gems

class Room(object):
    
    def enter(self) # this means room_antichamber.enter()
        pass
    
    def exit(self) 
        pass
#list of [choices, the, player, can, make] since several of them are 
#common in each room, i.e. rest

    
class Room_Entrance(Room):

    def enter(self)
        pass

class Room_Antichamber(Room):

    def enter(self)
        pass
        
class Room_Chest(Room):

    def enter(self)
        pass
        
class Room_Slime(Room):

    def enter(self)
        pass
        
class Room_Alter(Room):

    def enter(self)
        pass
        
class Room_Hallway(Room):

    def enter(self)
        pass
        
class Room_Crypt(Room):

    def enter(self)
        pass
        
class Room_Outside(Room):

    def enter(self)
        pass
        
class Room_End_Game(Room):

    def enter(self)
        pass
        
        
#______________________________________________

class Actions(object):

    def fight():
        pass
        
    def rest():
        pass
        
    def move():
        pass
        
#______________________________________________

class Character(object): #maybe combine with items; things(?)

    def __init__(self, stats):
        pass
    
    def create_character
        pass
        
class Items(object): 

    def create_item
        pass
        
# ____________________________________________


class Map(object):

    def __init__(self, start_scene):
        pass
        
    def next_scene(self, scene_name):
        pass
        
    def opening_scene(self):
        pass
    