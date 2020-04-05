class Scene(object):

    def enter(self):
        pass
  

  
class Death(Scene):
    print('death')
    def enter(self):
        pass

class CentralCorridor(Scene):
    print('You are in the central_corridor')
#    def enter(self):
#        pass
        
class LaserWeaponArmory(Scene):
    print('fun')
    def enter(self):
        pass
        
class TheBridge(Scene):

    def enter(self):
        pass
        
class EscapePod(Scene):

    def enter(self):
        pass
   
# ---------------------------------------------------   
        
class Engine(object):
    
    def __init__(self, scene_map):
        pass
        
    def play(self):
        pass
        #this needs 
        #print('This is in play')
        #a_map.opening_scene

# --------------------------------------------------

class Map(object):
    
    def __init__(self, start_scene):
        pass
        
    def next_scene(self, scene_name):
        pass
        
    def opening_scene(self):
        print('This is the opening scene.')
        pass
        
# ----------------------------------------------------

        
a_map = Map('ded')
a_game = Engine(a_map)
a_game.play()

