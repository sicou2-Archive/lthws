class Text():

    room = {
        'enter':
        """
        ENTER THE ROOM THAT IS NOT A ROOM, THINGS ARE BROKEN.
        """,
        }

    entrance = {
        'intro':
        """
        ADD TO STORY LOOKING FOR JEWELS AND THEN YOU WILL NEED TO GO TO THE
        STORE FOR SOME FOOD BEFORE UNDERSTANDING THAT SOMETIMES YOU DO LIKE
        LONG WALKS ALONG THE BEACH TO TEACH THE LESSON THAT KIDS CAN BE THE
        FUTURE IF THEY SO CHOOSE TO BE. WHICH THEY IN FACT SHOULD REGARDLESS
        OF WHAT THEY ARE TOLD ON SUNDAY AND THAT NO THEY ARE NOT DOOMED FOREVER
        AND SHOULD NOT EVEN TRY TO BE A BETTER HUMAN
        """,
        'enter':
        """
        THIS NEEDS THE OPENING STORYTHIS NEEDS THE OPENING STORY THIS NEEDS THE
        OPENING STORY THIS NEEDS THE OPENING STORY THIS NEEDS THE OPENING STORY
        THIS NEEDS THE OPENING STORY THIS NEEDS THE OPENING STORY THIS NEEDS
        THE OPENING STORY THIS NEEDS THE OPENING STORY
        """,
        }

    antichamber = {
        'enter':
        """
        THIS NEEDS BETTER STORY A goblin is here and attacks.\n
        1 Engage in combat 2 Run
        """,
        'run':
        """
        You run from the room and go looking for help to continue the fight.
        """,
        'stall_death':
        """
        The Goblin attacks while you stare at him.
        """,
        'stall': """He looks mean, do something! Quick!""",
        'three_doors':
        """
        You see three doors.\n
        Choose a door or rest:\n
        1 Left, 2 Center, 3 Right, 4 Rest a moment
        """,
        'no_left_door':
        """
        There is no reason to go back in there.\n
        Choose a different room:\n
        2 Center, 3 Right, 4 Rest a moment
        """,
        'no_center_door':
        """
        There is no reason to go back in there.\n
        Choose a different room:\n
        1 Left, 3 Right, 4 Rest a moment
        """,
        'door_stall':
        """
        Moving on is the only hope for you now. Choose a room:\n
        1 Left, 2 Center, 3 Right, 4 Rest a moment
        """,
        }

    chest = {
        'enter':
        """
        You see a locked chest.\n
        1 Pick lock, 2 Leave alone and return to Antichamber, 3 Rest a
        moment
        """,
        'pick': """You attempt to pick the lock...""",
        'explode': """It explodes in your face hurting you!""",
        'return_empty':
        """
        You return to the Antichamber empty handed
        """,
        'lock_break':
        """
        Despite your best efforts, you cannot quite get the lock to open. It
        seems like it is broken.
        """,
        'helmet':
        """
        You find a gleaming steel helmet, useful!\n
        You put it on and return to the Antichamber
        """,
        'look':
        """
        After looking around and seeing no danger, you return to the
        Antichamber.
        """,
        'stall':
        """
        You should get a move on. What would you like to do?
        """,
        }

    slime = {
        'enter':
        """
        Enter and a Slime is quietly digesting a large body.\n
        1 Attack the Slime, 2 Taunt the Slime, 3 Quietly back out of room.
        """,
        'attack':
        """
        You roar and ferociously attack the Slime.
        """,
        'search':
        """
        As the dead Slime oozes out across the floor, you look at and under the
        fresh body it had just started to eat. You find a sharp sword. You put
        your dagger in to your pack and return to the Antichamber.
        """,
        'key':
        """
        As you step out in to the Antichamber you notice a key tied to the hilt
        of the sword.
        """,
        'taunt':
        """
        You taunt the slime and it starts to follow you around the room. Much
        faster than it, you quickly flip over the fresh body and find a sharp
        sword.
        """,
        'sword':
        """
        You quickly grab the sword while stowing your dagger and return to the
        Antichamber before the slime can catch you.
        """,
        'retreat':
        """
        Seemingly content with its current meal, the Slime ignores you as you
        silently back out of the room back into the Antichamber.
        """,
        'stall_death':
        """
        Suddenly, from the ceiling above, an unseen Slime plops down crushing
        you to the floor.\n
        In its belly, you find a new definition of pain and suffering, as you
        are slowly digested over a thousand years.
        """,
        'stall':
        """
        That slime looks like it might almost be done digesting that body, you
        should make a decision before it does.\n
        What would you like to do?\n
        1 Attack the Slime, 2 Taunt the Slime, 3 Quietly back out of the
        room.
        """,
        }

    alter = {
        'locked':
        """
        You attempt to open the door, but the handle only rattles in your hand.
        This door is locked.
        """,
        'back_enter':
        """
        You see the fierce orc still worshiping at the alter. Further in to the
        room you see the door back to the Antichamber.\n
        1 Attack the Orc, 2 Attempt to sneak to the Antichamber.
        """,
        'attack':
        """
        You move in to attack the orc as he stands to fight!
        """,
        'back_sneak':
        """
        You sneak towards the Antichamber.
        """,
        'caught':
        """
        You hear the Orc's prayers trail off. As you look back, you both make
        eye contact. He roars and raises his sword to attack!
        """,
        'sneak_anti':
        """
        You silently pad across the room and slip through the still cracked
        door in to the Antichamber.
        """,
        'stall': """Hurry! Do something! He might notice you!""",
        'enter':
        """
        You unlock and open the door and see a fierce orc worshiping at an
        alter. Further in to the room you see a dark hallway.\n
        1 Attack the Orc, 2 Attempt to sneak to the hallway, 3 Gently close the
        door and return to the Antichamber.
        """,
        'sneak': """You sneak towards the hallway.""",
        'hall':
        """
        You silently enter the hallway and make your way into the damp and
        dark.
        """,
        'retreat':
        """
        You back in to the Antichamber and slowly closing the door and letting
        the latch fall.
        """,
        'victory':
        """
        You look around the room above the stench of the dead orc. You see an
        alter and a dark hallway.\n
        1 Inspect the Alter 2 Enter the hallway 3 Rest a moment 4 Return to the
        Antichamber.
        """,
        'already_strong':
        """
        You have already received the gift of Dak, better move on.
        """,
        'alter':
        """
        You approach the alter. Amazing! It is an alter of strength.\n
        1 Pray a prayer of strength and offer a ceremonial Red Mushroom 2 Leave
        the alter in peace.
        """,
        'deceit':
        """
        You feel a wave of dread as you look down and dread your ghastly
        mistake. It is an Alter of Deceit! You feel your blood run cold as the
        darkness overtakes you.
        """,
        'strong':
        """
        You suddenly feel stronger than you have ever been before! Like you
        could take on the whole empire!
        """,
        'leave_alone': """You slowly back away from the beautiful artifact.""",
        'stall_death_alter':
        """
        You *feel* the Alter become annoyed with your indecisiveness. You see a
        flash of cranapple as your mind is blistered by the infinity of time.
        You like turtles. You think you can smell purple.
        """,
        'stall_alter':
        """
        You cannot let yourself become too excited. Make a choice!
        """,
        'urge_advance':
        """
        There is no reason to go back there. Time to look forward!
        """,
        'return': """You decide to go back to the Antichamber""",
        'urge_choice':
        """
        No time like the present. Better get a move on and make a choice.
        """,
        }

    hallway = {
        'enter':
        """
        As you walk down the hallway, suddenly out of the darkness a giant
        lumbering Bugbear appears out of the darkness.\n
        1 Attack 2 Retreat in to the shadows.
        """,
        'attack': """You lunge forward to attack!""",
        'victory':
        """
        You walk down the dark hallway, squeezing past the dark lump of your
        fallen foe.
        """,
        'sneak_fail':
        """
        It seems he cannot see very well in the dark as you disappear back in
        to the shadows. However, as you hold your breath hoping it turns around
        and walks away, he begins to sniff the air. He creeps ever closer. You
        can't move!\n
        He bumps in to you and jumps back with a shout. Drawing your weapon,
        you realize it is a fight!
        """,
        'sneak_success':
        """
        It seems he cannot see very well in the dark as you disappear back in
        to the shadows.
        """,
        'retreat_choice':
        """
        Frozen in the darkness you realize you cannot go back without returning
        to face the Orc. You could also rest here a moment and hope the Bugbear
        does not see you before you are ready.\n
        1 Return to fight the Orc 2 Rest
        """,
        'rest_fail':
        """
        While trying to gather your strength, you hear a low chuckle as the
        gruesome smiling Bugbear emerges from the darkness.
        """,
        'advance':
        """
        With nothing in your way, you cautiously advance though the hallway.
        """,
        'stall_sneak_death':
        """
        You feel a sudden jolt in your neck before you realize out of the
        corner of your eye, you see everything you hope to not see as you lose
        conciousness.
        """,
        'stall':
        """
        Indecision will get you killed here, choose!
        """,
        'stall_death':
        """
        Frozen in indecision, the Bugbear sees your wide, terrified eyes and he
        ruthlessly detatches your head from the rest of your body.
        """,
        'room_error':
        """
        You should not be here, something is broken.\n
        Please contact the developer and tell them that you somehow managed to
        get here.
        Good job!
        """,
        }

    crypt = {
        'enter':
        """
        You walk in to a mostly empty chamber. You see a well preserved crypt.
        Across the room you see a set of stairs leading up to a large stone
        door.\n
        1 Inspect the Crypt 2 Go up stairs and through the door 3 Rest a moment
        4 Return through the hallway to the Alter room
        """,
        'crypt':
        """
        You move closer and inspect the crypt. It is masterfully crafted in
        granite and onyx. Laid in the stone are dozens of dazzlingly cut gems.
        \n1 Take gems 2 Leave them alone and back away from the crypt
        """,
        'gem_get':
        """
        You take the flawless gems and put them in to your pack. As you close
        the bag you look up and see a skeleton rising out of the crypt.\n
        1 Attack 2 Run toward the stairs 3 Run toward the hallway
        """,
        'defend':
        """
        You bravely defend your life and treasure!
        """,
        'climb':
        """
        Your only option now is to climb the stairs. As you get to the door,
        you begin to push open the heavy door. You look up and see another set
        of stairs and begin to climb.\n
        You see a bright light above you as you climb toward it.
        """,
        'run':
        """
        You start to run, but you feel a spell freeze your feet in place. You
        turn to fight for your life and treasure!
        """,
        'gem_leave':
        """
        You leave the treasure in its place and go return to the middle of the
        room.\n
        1 Inspect Crypt 2 Go up the stairs and through the door 3 Rest a moment
        """,
        'gem_stall_death':
        """
        You hear a loud crack and turn to see the evil Lich Paul looming behind
        you. As you freeze in terror his hateful stare glows as a pair of
        skeletal arms reach around you from the crypt behind you. You
        understand now what this dungeon is now and how terrible a mistake it
        was to come here. Your last though is that maybe your unlife as an
        undead minion will not be as bad as your life working in the stables of
        the old inn.
        """,
        'stall_gem':
        """
        You feel that standing here thinking about what to do is probably not
        the most intelligent thing that you could be doing with your time right
        now. Do something.\n
        1 Take gems 2 Leave them alone and back away from the crypt
        """,
        'no_gem_leave':
        """
        You ignore the crypt and move up the stairs. After a moment of pushing,
        you manage to open the heavy stone door climb another set of stairs,
        and see out in to the wilderness.
        """,
        'no_return': """There is no reason to go back.""",
        'return': """You go back through the hallway.""",
        'stall': """It is time to move on, make a choice.""",
        }

    outside = {
        'enter':
        """
        As you step out in to the light and to safety with your hard fought
        treasure, you begin to seriously consider if adventuring is worth the
        effort. Maybe you should quit while you are still alive and open an inn
        or something.
        """,
        'no_gem_enter':
        """
        As you step out in to the light and to safety, you might not have the
        treasure you were looking for, but you still have your life! You begin
        to seriously consider if adventuring is worth the effort. Maybe you
        should try to get you old job back. The stable smelled but the horses
        were nice.
        """,
        }

    end_game = {
        'end': """Game over man. Game over! Play again? "y/n\"""",
        'except_end': """Would you like to play again? "y/n\"""",
        }

    fight = {
        'fight':
        """
        You engage in combat!\n
        1 Fight or 2 Run
        """,
        'attack': """You attack!""",
        'die': """You fall bravely in battle.""",
        'victory_1': """You slay the enemy """,
        'look': """Above the body of your foe, you look around.""",
        'continue': """The combat continues!""",
        'retreat': """You retreat from the battle!""",
        'stall_death':
        """
        You block and block the attacks coming from your foe, eventually, you
        are overwhelmed.
        """,
        'stall': """Do not hesitate! Do something, anything!""",
        }

    rest = {
        'rested': """You already feel rested. Better get a move on!""",
        'rest':
        """
        You take a moment to catch your breath. You feel ready to soldier on!
        """,
        }

if __name__ == '__main__':
    pass
