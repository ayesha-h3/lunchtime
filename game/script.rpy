
# establishing our cast of characters !
define y = Character("You", color="#d28ef1")
define f = Character("Luca")
define d = Character("Dottie")
define c = Character("Coinflip")
define v = Character("Void Queen")
define b = Character("Bird")
define mystery = Character("???")
define m = Character("Man Who Lost His Name")
define of = Character("Orange Fish")
define bf = Character("Blue Fish")

# The game starts
label start:
# some different variables
    $ confrontation = 0 #determines if you take on the villain yourself
    $ corpses = 0 #unlocks evil route a la undertale
    $ insanity = 0 #how willing you are to stay
    $ benevolence = 0 #your leadership capability
    $ confusion = 0

    "It's a warm spring day. You and your friend are walking in the city to _____."

    f "So, where do we want to head for lunch? I was thinking of this sushi place that I've been wanting to try out."

    y "Ooh! Sounds yummy. How long is the walk?"
    f "It looks like if we take the route to the left it'll be faster, but more traffic. If we go to the right it'll be longer but calmer."
    y "Well which way do you want to go?"
    f "I don't know, that's why I'm asking you!"

    menu:
        "Let's go left, I'm starving!":
            jump left
        "Taking the longer route seems better.":
            jump right

    label left:
        f "Okay! It says this intersection is busy often but we should be fine."
        y "Awesome! I don't see any cars coming, let's go--"
        "In your excitement, you didn't see that the walk sign hadn't turned on yet."
        f "WAIT--"
        "THUD!"
        $ insanity+=1
        jump forest

    label right:
        f "Fair choice. This way passes through a less busy intersection."
        y "Ok, cool! Let's get going then."
        f "Oh ew, it's one of those crazy e-bike kids. Slow down! No, actually, SLOW DOWN--"
        "Some middle schooler looking for an adrenaline rush decided to go 20 miles per hour on a sidewalk. Unfortunately, he wasn't paying attention to where he was going--right into you."
        jump forest
    

    label forest:
        "You open your eyes."
        y "...huh?"
        "Do you hear that sound?"

        menu:
            "The birds?":
                jump birds
            "The...weird voice?":
                jump narrator

        label birds:
            "A bright yellow bird lands on your face, chirping happily."
            b "Hey Dottie, did you see this weirdo?"
            y "Was that..."
            "You try poking at the bird."
            b "Ew! Get your fat finger away from me!"
            y "Ow! What was that for?"
            $ confusion +=3
            jump dottie

        label narrator:
            "You try to find the source of the voice--"
            "Wait, you mean this voice?"
            y "Yeah, who are you? What is this, The Stanley Parable?"
            "Uhhh...sure?"
            $ insanity +=5
            jump dottie

    label dottie:
        show dottie happy
        d "She awakens!"
        y "Who...awakens?"
        c "I thought she was going to be taller, if I'm being honest."
        d "Well, beggars can't be choosers. I guess we'll have to make do with what we got."
        menu:
            "Are you looking for someone?":
                jump whosthis
            "Is this some sort of Chosen One moment or something?":
                jump selfaware

    label whosthis:
        $ confusion += 3
        c "Wait, are you not the General?"
        d "Coinflip! Stop being so rude! I apologize on my friend's behalf."
        y "This has got to be some sort of dream."
        c "I know, right! Sometimes I think this place is too good to be true. Except for the Void Queen, of course. But it's totally real."
        d "Stop overwhelming her! Sorry about...her. Anyways, I'm Dottie, and this is Coinflip. What she's TRYING to ask is, are you the General?"
        y "I have no idea who that is. But good luck finding them, I guess?"
        c "See, that's where you're mistaken. You ARE the General, obviously."
        y "...how?"
        d "What I think she's trying to say is that you fit the profile we were given."
        c "So...do you know anything about stopping world-destroying entities?"
        jump meetvoid
        


    label selfaware:
        $ confrontation += 5
        d "Woah, she knows!"
        c "Of course she does. She probably already knows all about the whole situation."
        y "Is that coin talking?"
        c "Whoa, whoa, whoa. Slow down, buttercup. I'm not just ANY coin. I'm the one and only Coinflip! But you already knew that, I bet."
        y "I'm dead. I'm either dead or hallucinating."
        d "I can assure you you're neither."
        y "That's what a hallucination would say."
        y "If you're so real, what's your name, who's the president of the United States right now, and can you pinch me?"
        d "Dottie, Calvin Coolidge, and why would I do that?"
        y "Tangible evidence."
        d "Fine."
        y "That was a paper cut. What?"
        d "How is a piece of paper supposed to pinch you? It's the best I could do."
        y "Wait, did you say CALVIN COOLIDGE?"
        d "You asked who the president is right now!"
        y "I think if I think about this any more my brain is going to explode."
        y "Wait, what was that...situation you mentioned earlier? The one I supposedly already know about?"
        c "There's only one situation I COULD be talking about."

        jump meetvoid


    label meetvoid:

    label savecoin:

    label sacrificecoin:

    label manwholostname:
        y "Who are you?"
        mystery "That's a good question. She's a smart one, isn't she?"
        mystery "My name is..."
        mystery "Oh yeah! I lost it."
        y "You lost...your name?"
        d "It's complicated."
        mystery "That's why they call me, The Man Who Lost His Name!"
        y "That's a bit of a mouthful, though, don't you think?"
        m "Well, do you have a better idea? And besides, it has a nice ring to it."

    label fish:
        d "We've arrived at the lake, home to the fish!"
        y "Aww, they're kind of cute!"
        m "It's customary for a potential leader to be tested by the fish."
        y "Wait, huh?"
        bf "One of us tells the truth..."
        of "And one of us lies."
        "Which fish do you trust?"
        menu:
            "The orange fish.":
                jump orange
            "The blue fish.":
                jump blue

    label orange:
        $ benevolence +=5
        bf "I'm the one that tells LIES!"
        of "Congratulations, your judgment rings true!"
        of "Also, you weren't supposed to tell her that."
        m "You were right! She IS some sort of miracle!"

    label blue:
        bf "You are CORRECT!"
        of "He's lying."
        y "What...?"
        $ confusion +=5
        d "It's okay, you don't have to worry about them. The blue fish tells lies."
        m "Don't feel bad about getting it wwrong. They get in your head like that."
        d "That's why any future leader would have advisors! Like us!"



    label meetdancer:

    label savedancer:

    label sacrificedancer:

    label crossroads:

    label savedottie:

    label sacrificedottie:

    label chooserank:
        m "Well, clearly we don't have much time left."
        m "Our army needs its leader. Someoe who isn't afraid to take charge and fight."
        if corpses>2:
            m "And considering that all my friends are dead, I guess you're the only one left."
        else:
            m "And clearly you've proven yourself to be capable."
        m "So, what do you say? Are you up to the task you came here to fulfill?"
        y "You guys need to stop saying that. And..."
        menu:
            "I would be honored.":
                jump general
            "I'm not sure if I'm ready yet.":
                jump footman
            "Who said I would join you?" if corpses>2:
                jump evil

    label general:

    label footman:

    label evil:
        m "...what do you mean?"
    label confrontation:

    label battle:

    menu: #this is for testing endings, this will NOT be in the final version!!!
        "good things happen to good people":
            jump goodthingsgoodpeople
        "death is a mercy":
            jump deathisamercy
        "void dominion":
            jump voidDominion






    label goodthingsgoodpeople:
        mystery "Seems to me that it's your lucky day!"
        y "What?"
        mystery "Rejoice! It appears you have found your one ticket home."
        mystery "You really did help us out."
        "The VOID QUEEN exists when despair is high. Did you know that for every life you saved, despair was released from their hearts?"
        mystery "Everyone had given up hope. They've been waiting to die for so long, no one expected their spirits to be renewed. I think..."
        mystery "I think you may have helped push back the Void Queen for good!"
        mystery "Head down that path. You'll find the Nexus there, which will grant you your path home!"
        "You make your way to the path revealed by the Man Who Lost his Name."
        "The trees around you thin until you reach a stone temple that has fallen into disrepair."
        y "What is this place...?"
        "You make your way around the rocks and vines to reveal a glittering gemstone amidst offerings placed on a stone altar."
        "You pick up the gemstone you now know is the Nexus. Cool to the touch, the gemstone hums with echoes of power."
        y "I wish...to return home."
        "The scenery changes around you. You wonder if this world is real, or just a figment of your definitely injured brain."
        y "Hey!"
        "What? You know it's true."
        "Seeing as you can still hear that disembodied voice--Hey!"
        jump theend

    label deathisamercy:
        mystery "Oh, so it's you..."
        mystery "Sigh, I should have seen this coming. Are you going to kill me too?"
        "The VOID QUEEN exists when despair is ihgh. Did you know that with every death you caused, that despair became stronger?"
        mystery "A couple days ago this clearing was free of any trace of the VOID but recently there’s been an uptick in despair which has led to the scene you see now."
        mystery "If you had arrived earlier you could’ve taken the path through the clearing and reached the Nexus which would’ve taken you home."
        mystery "Such a shame the Nexus was overtaken by the VOID. Seems you have no path home!"
        mystery "I’ve wondered why you are so cruel."
        mystery "Perhaps to you we are nothing worth mourning for." 
        mystery "An object being lost or a memory being forgotten is nothing of importance to you is that right? Something no one remembers exist isn’t worth crying about."
        mystery "I’ll tell you a secret."
        mystery "I lied about not knowing what happens to humans who fall into the VOID."
        mystery "Humans are erased from existence."
        mystery "The parents that raised you, the friends up adored, the lovers you tangle with, not a single one will know you are missing. Not a single one knows you existed at all."
        mystery "You will die here with no one to mourn you. Not in this world or your own." 
        "As the VOID encroaches the air seems to still. When the inky blackness reaches “The Man who Lost His Name” He turns and looks at you one last time."
        "The Man Who Lost His Name disperses in a puff of black smoke."
        "The Man Who Lost His Name blocks his forgotten memory from ———(character name)."
        "Two souls are left in this world. Your name becomes a blot in the history books that shall never be written."
        "As the Void comes closer you think, How beautiful. How terrible. These actions are your own and so too are the consequences. Your skin unfurls from the gore that is your flesh. Fat melts off of muscle and meat falls off bone."
        "You are not of course the only victim. Even the text box that Narrated your journey falls victim to the encroaching VOID. Perhaps you find solace in this."
        "All I can say is this seems to be a moment to rejoice! Our murderer seems to be dying the same way they killed us."
        "Your END is Oblivion."
        jump theend

    label voidDominion:
        mystery "You have made a wise decision."
        y "I know."
        "The VOID QUEEN reveals herself from the shadows, a glistening scepter in hand."
        v "You have proven yourself to me, you know. You're capable. Powerful. Ruthless."
        v "Just what I look for in a right hand."
        v "Join me, and we shall conquer universes...together."




    
    # This ends the game.
    label theend:
        return
