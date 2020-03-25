# # import list
from random import randrange

# # map creation

# # character

# # enemy

# # items

# def main(): 

    # hero = character()
    
    # room()
    # return print(hero)
    

# def character():

    # hitpoints = 0
    # hitpoints = randrange(0,10)
    
    # attack = 1

    # stats = [randrange(0,10), attack]
    # print(stats)
#NOTE(BCL): check the style guide, I think DEF names are supposed to be capitalized

def main(): 

    hero = character(10,1,1,1)
    
    room_antichamber()
def main_debug(): #NOTE(BCL): THIS IS FOR TESTING INDIVIDUAL MODULES, COMMENT OUT BELOW WHEN NOT IN USE

    hero = character(10, 1, 1, 1,'hero')

    room_antichamber(hero)
# NOTE(BCL): Consider looking up classes and using them for rooms, characters, maybe items
def room_antichamber(hero):
    
    goblin = character(5, 1, 1, 1,'goblin')
    #NOTE(BCL):NEED TO CHECK TO SEE IF GOBLIN IS ALIVE TO SKIP COMBAT
    
    print('A goblin is here and attacks. 1 Fight 2 Run')
    
    i = 0
    
    while True:    
        
        action = input('> ')

    # NOTE(BCL): After fight give chance to rest after fighting module is given
        
       
        if action == '1': 
        
            fight(hero, goblin)
            
            
            print ('Goblin dies, see three rooms. 1 Left, 2 Center, 3 Right')
            
            while True:
                room_choice = input('> ')
                
                if room_choice == '1': return room_chest() 
                elif room_choice == '2': return room_slime() #CENTER ROOM SLIME ROOM
                elif room_choice == '3': return room_orc() #RIGHT ROOM ORC ROOM
                else:
                    print('Moving on is the only hope for you now. Choose a room.')
        elif action == '2': #NEED ELIF THEN LOOP ELSE AT BOTTOM
            print('You run from the room and go looking for help to continue the fight.')
            return end_game()
        elif i > 3:
            print('Goblin attacks while you stare at him.')
            return end_game()
        else:
            print('He looks mean, do something! Quick!')
            i += 1    
def room_chest(): 
    print('You see a chest. 1 Pick lock, 2 Leave alone and return to antichamber, 3 Rest a moment')
    
    while True: #NOTE(BCL): MAYBE A STATEMENT OF SOME KIND HERE TO SKIP THE CHEST AND RETURN TO AC
    
        action = input('> ')
        
        if action == '1':
            print('You attempt to pick the lock...')
            lock_test = randrange(1,10)
            
            if lock_test == 1:
                print('It explodes in your face hurting you') #NOTE(BCL):NEED TO REMOVE HP
                print('You return to the antichamber empty handed')
                return room_antichamber(hero)
            elif 2 <= lock_test and lock_test <= 5:
                print('Despite your best efforts, you cannot quite get the lock to open. It seems like it is broken')
                print('You return to the antichamber empty handed.')
                return room_antichamber(hero)
            else:
                print('You find a gleaming steel helmet, useful!')
                print('You put it on and return to the antichamber')
                return room_antichamber(hero)
                
        elif action == '2':
            print('After looking around and seeing no danger, you return to the antichamber.')
            return room_antichamber(hero)
            
        elif action == '3': 
            print('You take a few moments to gather your strength and mind. You feel better.')
            return room_antichamber(hero) #NOTE(BCL): WITH FIGHT MODULE THIS SHOULD RESTORE HP TO FULL
        else:
            print('You should get a move on. What would you like to do?')
    return 0
def room_slime(): 
    print('Enter and a Slime is quietly digesting a large body. 1 Attack the Slime, 2 Taunt the Slime, 3 Quietly back out of room')
    
    i = 0
    
    while True:
        action = input('> ')
        
        if action == '1':
            print('You ferociously attack and kill the Slime. Under the body it had just started to eat you find a sharp sword. You put your dagger in to your pack and return to the antichamber.')
            return room_antichamber()
        elif action == '2':
            print('You taunt the slime and it starts to follow you around the room. Much faster than it you quickly inspect the fresh body it had started to eat and you find a sharp sword.')
            print('You quickly grab the sword while stowing your dagger and return to the antichamber before the slime can catch up to you.')
            return room_antichamber()
        elif action == '3':
            print('Seemingly content with its current meal the Slime ignores you as you silently back out of the room back in to the antichamber.')
            return room_antichamber()
        elif i > 3:
            print('Suddenly from the ceiling above another Slime plops down crushing you to the floor.')
            print('In its belly, you will find a new definition of pain and suffering, as you are slowly digested over a thousand years.')
            return end_game()
        else:
            print('That slime looks like it might almost be done digesting that body, you should make a decision before it does. What would you like to do?')
            i += 1
    
    return 0 
def room_orc(): return 0 

def character(health, defence, attack, alive, name): #maybe use dicts here? 
    stats = [health, defence, attack, alive, name]
    return stats 

def fight(hero_stats, enemy_stats): 
    
    while True:
        print('1 Fight or 2 Run')
        action = input('> ')
        if action == '1':
            
            print('You attack!')
            hero_stats[0] -= 1
            
            enemy_stats[0] -= 1
            print(hero_stats, enemy_stats)
            if hero_stats[0] == 0:
                'You fall bravely in battle.'
                return end_game()       
            elif enemy_stats[0] == 0:
                print(f'You slay the enemy {enemy_stats[4]}')
                return 0
            else:
                print('The combat continues!')
        
    return 0 

def end_game(): 
    print('Game over man. Game over!')
    return 0 

# main()

main_debug() #NOTE(BCL): LEAVE ME COMMENTED WHEN NOT NEEDED