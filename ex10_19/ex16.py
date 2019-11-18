from sys import argv

script, filename = argv

print(f"We are going to erase {filename}.")
# print("If you do not want that, hit CTRL-C *now*.")
# print("If you do want that, hit ENTER.")

# input("?")

print("Opening the file...")
target = open(filename, 'w+')

# print("Truncating the file. Goodbye!")
# target.truncate()

print("Now I am going to ask you for three lines.")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

print("I am going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

target.seek(0) # This is needed, I figured it out all by me self
print(target.read()) # testing 'w' modifier 

print("And finally, we close it.")
target.close()