from sys import exit
from random import randint
from textwrap import dedent #Remove any common leading whitespace from 
                            #every line in text. Allows for allign left
                            #when dealing with ''' '''

# ---------------------------------------------------   
        

# -------------------------------------------------------------

class Scene(object):

    def enter(self):
        ''' 
        This seems to tell the user that the called scene is not built
        and that it needs to be added to the code. I wonder why every 
        sub-class needs enter. Maybe we will eventually find out. 
        ''' 
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1) # I wonder what he has exit(1) set up to do. 
    
class Death(Scene):
    
    def enter(self):
        pass

class CentralCorridor(Scene):

    def enter(self):
        print("SOME THINGS FOR CENTRAL CORRIDOR")
        
        action = input("> ")
        
        if action == "thing":
            print("BAD THING")
            
            return 'death'
            
        else:
            print("DOES NOT COMPUTE")
            return 'central_corridor'
    
        
class LaserWeaponArmory(Scene):

    
    def enter(self):

        pass
        
class TheBridge(Scene):

    
    def enter(self):

        pass
        
class EscapePod(Scene):

    
    def enter(self):

        pass
   
class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
        
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            
        # Be sure to print out the last scene
        current_scene.enter() # This line is causing a problem at the 
                              # point in which I stopped. 
    #########STOPPED HERE###################

# --------------------------------------------------

class Map(object): 
    # I kind of want to believe that class Map and Engine should be one
    # class together. 


    scenes = { 
        # This is a dict of all of the scenes 
        # I wonder if it would be better placed in the scene class? 
        # Maybe not, I will probably want to have a think about it. 
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        #'finished': Finished(), # This needs to be created above
    }
        
    def __init__(self, start_scene):
        self.start_scene = start_scene
        
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
        
    def opening_scene(self):
        return self.next_scene(self.start_scene)
        
# ----------------------------------------------------

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()


