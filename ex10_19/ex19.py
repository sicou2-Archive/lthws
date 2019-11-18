def cheese_and_crackers(cheese_count, boxes_of_crackers): # establishes a function called cheese_and_crackers which asks for two variables
    print(f"You have {cheese_count} cheeses!") # prints the functions cheese count
    print(f"You have {boxes_of_crackers} boxes of crackers!") # prints the functions boxes_of_crackers
    print("Man that is enough for a party!") # prints text
    print("Get a blanket.\n") # prints text with a new line
    
    
print("We can just give the function numbers directly:") # prints text
cheese_and_crackers(20, 30) # passes hard numbers as variables
 
 
print("OR, we can use variables form out script:")
amount_of_cheese = 10 # sets variable
amount_of_crackers = 50 # sets variable
 
cheese_and_crackers(amount_of_cheese, amount_of_crackers) # passes above variables
 
 
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6) # does math with hard numbers that are passed
 
 
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) # passes established variables and does math with hard numbers


