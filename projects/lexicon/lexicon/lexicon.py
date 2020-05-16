lexicon = {
    'direction': ['north', 'south', 'east', 'west', 'down', 'up', 'left',
                  'right', 'back', ],
    'verb': ['go', 'stop', 'kill', 'eat', ],
    'stop': ['the', 'in', 'of', 'from', 'at', 'it', ],
    'noun': ['door', 'bear', 'princess', 'cabinet', ],
    'number': [],
    'error': [],
}


def split_input():
    stuff = input('> ')
    print(stuff)
    words = stuff.split()


def _convert_number(convert):
    for index, i in enumerate(convert):
        try:
            number = convert[index] = int(i)
            present = 1
            lexicon['number'].append(number)
            # print(lexicon)
        except ValueError:
            return None


def scan(command):
    """Scan should take a single argument and decide that it is verb of
    direction and return a list of tuples of the (verb, argument)"""
    words = command.split(' ')
    # print(words)
    words_lower = command.lower().split(' ')
    # print(words_lower)
    commands = []
    _convert_number(words)
    for word, lower in zip(words, words_lower):
        present = 0
        for k, v in lexicon.items():
            if lower in v or word in v:
                present = 1
                tup = (k, word)
                commands.append(tup)
                # print(lexicon)
        if not present:
            tup = ('error', word)
            commands.append(tup)
    return commands


# command = '15 54 98'
# r = scan(command)
# print(r)
