import json

from_file = 'game_text.py'

with open(from_file) as f:
    text = f.read()
    #print(text)
#    for i in range(200):
#        print(f.readlines())

to_file = 'game_text.json'

with open(to_file, 'w') as f:
    json.dump(text, f, indent=2)