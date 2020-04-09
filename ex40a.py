# import mystuff


# # mystuff.apple()

# # mything = {'apple': "I AM APPLES!"}
# # print(mything['apple'])

# # print(mystuff.tangerine)

# # mything['apple'] # Get apple from dict
# # mystuff.apple() # Get apple from the module
# # mystuff.tangerine # Same thing, it's just a variable

# #CLASSES
# thing = MyStuff()
# thing.apple()
# print(thing.tangerine)

# #Not totally sure what is going on here. Something is not right. 

from mystuff import *

dict_apple = {'apple': "I AM APPLES"}
print(dict_apple)

func_apple()
print(tangerine)

# class Horse_Apple(object):
    
    # def __init__(self):
        # self.pear = "And now a thousand years between"
        
    # def classy_apple(self):
        # print("I AM CLASSY APPLES")
        
thing = Horse_Apple()
thing.classy_apple()
print(thing.pear)




