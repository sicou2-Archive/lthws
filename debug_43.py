class Scene(object):
    i = 1
    def enter(self):
        print('')
        pass

class Death(Scene):

    def enter(self):
        print('')
        pass

class CentralCorridor(Scene):

    def enter(self):
        print('')
        pass

class LaserWeaponArmory(Scene):
    print('4')

    def enter(self):
        print('')
        pass

class TheBridge(Scene):
    print('5')

    def enter(self):
        print('')
        pass

class EscapePod(Scene):
    print('6')

    def enter(self):
        print('')
        pass

# ---------------------------------------------------

class Engine(object):
    print('7')

    def __init__(self, scene_map):
        print('10')
        pass

    def play(self):
        print('11')
        pass

# --------------------------------------------------

class Map(object):
    print('8')

    def __init__(self, start_scene):
        print('9')
        pass

    def next_scene(self, scene_name):
        print('')
        pass

    def opening_scene(self):
        print('')
        pass

# ----------------------------------------------------

print('First')
a_map = Map('central_corridor')
print('Second')
a_game = Engine(a_map)
print('Third')
a_game.play()
print('Fourth')
