from sys import argv

script, filename = argv

open_filename = open(filename)

print(open_filename.read())
