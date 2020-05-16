lexicon = {
    'direction': ['north', 'south', 'east', 'west', 'down', 'up', 'left',
                  'right', 'back', ],
    'verb': ['go', 'stop', 'kill', 'eat', ],
    'stop': ['the', 'in', 'of', 'from', 'at', 'it', ],
    'noun': ['door', 'bear', 'princess', 'cabinet', ],
    'number': [],
    'error': [],
}

# When word not in lexicon return then the (TOKEN, WORD) token should be set
# to an error token and tell the user that they did not enter a good word.


def split_input():
    stuff = input('> ')
    print(stuff)
    words = stuff.split()


def convert_number(convert):
    for index, i in enumerate(convert):
        try:
            number = convert[index] = int(i)
            lexicon['number'].append(number)
        except ValueError:
            return None


def scan(command):
    """Scan should take a single argument and decide that it is verb of
    direction and return a list of tuples of the (verb, argument)"""
    words = command.lower().split(' ')
    commands = []
    convert_number(words)
    for word in words:
        for k, v in lexicon.items():
            if word in v:
                tup = (k, word)
                commands.append(tup)
            # else: # This else is catching all of the keys that
            # # the word is not in, need to figure a better way for this.
            #     tup = ('error', word)
            #     lexicon['error'].append(word)
    return commands


# test = ('1234 6543')
# accept = scan(test)
# print(accept)
# print(lexicon)
