# this one is like you scripts with argv
def print_two(*args):
    arg1, arg2 = args 
    print(f"arg1: {arg1}, arg2: {arg2}")
    
# ok, that *args is actually pointless, we can just do this
def print_two_again(arg3, arg4):
    print(f"arg3: {arg3}, arg4: {arg4}")
    
# this just takes one argument
def print_one(arg5):
    print(f"arg5: {arg5}")
  
# this one takes no arguments
def print_none():
    print("I got nothin'")
    

print_two("Dog","Gypsy")
print_two_again("Hans","Blaze")
print_one("Lookout")
print_none()


# function checklist
# 1 Did you start your function definition with def?
# 2 Does you function name have only characters and _ (underscore) characters?
# 3 Did you put an open paren right after the function name?
# 4 Did you put your arguments after the paren separated by commas?
# 5 Did you make each argument unique (no duplicate names)?
# 6 Did you put a close paren and colon after the arguments?
# 7 Did you indent all lines of code you want in the function four spaces? No more, no less. 
# 8 Did you "end" your function by going back to writing with no indent (detenting)?

# running using or calling a function (all mean the same thing)
# 1 Did you call/use/run this function by typing its name?
# 2 Did you put the ( character after the name to run it?
# 3 Did you put the values you want into the parentheses separated by commas?
# 4 Did you end the function call with a ) character?