class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
        
#happy_bday = Song(["Happy birthday to you",
#                   "I don't want to get sued",
#                   "So I'll stop right there"])
 

happy_bday = Song('')

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])
                        
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

boat_drinks = [
    "Boat drinks.",
    "Boys in the band ordered boat drinks.", 
    "Visitors just scored on the home rink.",
    "Everything seems to be wrong."
    ]

lyric = boat_drinks

 
play_song = Song(lyric)



play_song.sing_me_a_song()