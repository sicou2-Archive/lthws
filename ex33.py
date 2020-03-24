

    
def while_loop():
    
    print("Where would you like to stop?")
    stop = int(input("> "))
   
    print("What would you like to step by?")
    step = int(input("> "))
    
    i = 0
    numbers = []

    while i < stop:
        print(f"At the top i is {i}.")
        numbers.append(i)
        
        i += step
        print("Numbers now: ", numbers)
        print(f"At the botton i is {i}.")
        
    return numbers   
        
def for_loop(): 
    print("Where would you like to stop?")
    stop = int(input("> "))
   
    print("What would you like to step by?")
    step = int(input("> "))
    
    numbers = []
    
    for i in range(0, stop, step):
        print(f"At the top i is {i}.")
        numbers.append(i)
        
        print("Numbers now: ", numbers)
        print(f"At the botton i is {i}.")
    
    return numbers
    
# he seems to be asking for a range loop or with the last ex32 something about ranges without looping? I am not sure
    
def range_loop(): return 0 # not sure I need this


    
digits = while_loop()    
        
print("The numbers: ")

for num in digits:
    print(num)
    
digits = for_loop()  
  
print("The numbers: ")

for num in digits:
    print(num)