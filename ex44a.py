class Parent(object):

    def implicit(self):
        print("PARENT implicit()")
        
    def override(self):
        print("PARENT override()")
        
    def altered(self):
        print("PARENT altered()")
        
class Child(Parent):

    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init__()
    
    def override(self):
        print("CHILD override()")
    
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        #This does things within Child.altered and completes all things.
#        super(Child, self).altered()
        super().altered()
        #This goes up to Parent and does everthing Parent.altered() 
        #does.
        #Looking at PYDOCS it does not look like they use (Child, self)
        #super().altered() seems like it would work just fine. 
        #Testing seems to show it works. 
        print("CHILD, AFTER PARENT altered()")
        #This return to Child.altered() and completes any remaining 
        #things to do. 
    
dad = Parent()
son = Child('fun')

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()