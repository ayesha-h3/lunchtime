
# establishing our cast of characters !
define y = Character("You", color="#d28ef1")
define f = Character("Luca", color="#347b9e")
define d = Character("Dottie", color="#2b2b2b")
define c = Character("Coinflip")
define v = Character("Void Queen")
define b = Character("Bird", color="#2dbab8")
define mystery = Character("???")
define m = Character("Man Who Lost His Name")
define of = Character("Orange Fish", color="a15005")
define bf = Character("Blue Fish", color="#0508a1")
define da = Character("Dancer", color="#f296e3")

# The game starts
label start:
# some different variables
    $ confrontation = 0 #determines if you take on the villain yourself
    $ corpses = 0 #unlocks evil route a la undertale
    $ insanity = 0 #how willing you are to stay
    $ benevolence = 0 #your leadership capability
    $ confusion = 0 

    "It's a warm spring day. You and your friend Luca are walking in the city, heading to get lunch."
    show luca stand

    f "So, where do we want to head for lunch? I was thinking of this sushi place that I've been wanting to try out."

    y "Ooh! Sounds delicious. How long is the walk?"
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
        hide luca
        "THUD!"
        "Everything goes black."
        $ insanity+=1
        jump forest

    label right:
        f "Fair choice. This way passes through a less busy intersection."
        y "Ok, cool! Let's get going then."
        f "Come on! The crossing is open now."
        "You've only taken a few steps before the ground begins to rumble."
        f "What is THAT?"
        "A crack in the road appears beneath your feet."
        f "Why aren't you moving? GET AWAY FROM THAT THING!"
        y "I'm TRYING!"
        "You try to jump away but it's too late. The crack widens to a gaping hole...pulling you into the newly opened abyss."
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
            show bird inface
            "A stark black bird lands on your face, chirping happily."
            b "Hey Dottie, did you see this weirdo?"
            y "Was that..."
            "You try poking at the bird."
            b "Ew! Get your fat finger away from me!"
            show bird finger
            y "OW! MY FINGER!"
            "You look down at your hand in shock, only to find that all your fingers are still fully intact."
            y "What? How did that..."
            mystery "It's just a trick of the light! Is that what you call it? Anyways, don't worry about it."
            y "I just watched my finger get eaten off by a bird, of course I'm worried!"
            y "Wait, who was that? Where are you? Come out!"
            hide bird
            $ confusion +=3
            jump dottie

        label narrator:
            "You try to find the source of the voice--"
            "Wait, you mean this voice?"
            y "Yeah, who are you? What is this, The Stanley Parable?"
            "Uhhh...sure?"
            y "Is this some sort of internal monologue? Am I going insane?"
            "No and no. It's best if you don't think about it too hard."
            $ insanity +=5
            jump dottie

    label dottie:
        show dottie happy at right
        d "She awakens!"
        y "Who...awakens?"
        show coinflip side at top, left
        c "I thought she was going to be taller, if I'm being honest."
        d "Well, beggars can't be choosers. I guess we'll have to make do with what we got."
        menu:
            "Are you looking for someone?":
                jump whosthis
            "Is this some sort of Chosen One moment or something?":
                jump selfaware

    label whosthis:
        $ confusion += 5
        c "Wait, are you not the General?"
        d "Coinflip! Stop being so rude! I apologize on my friend's behalf."
        y "This has got to be some sort of dream."
        c "I know, right! Sometimes I think this place is too good to be true. Except for the Void Queen, of course. But it's totally real."
        d "Stop overwhelming her! Sorry about...her. Anyways, I'm Dottie, and this is Coinflip. What he's TRYING to ask is, are you the General?"
        y "I have no idea who that is. But good luck finding them, I guess?"
        c "See, that's where you're mistaken. You ARE the General, obviously."
        y "...how?"
        d "What I think he's trying to say is that you fit the profile we were given."
        show coinflip concern 
        c "So...do you know anything about stopping world-destroying entities?"
        show coinflip side 
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
        show dottie sad
        d "You asked who the president is right now!"
        y "I think if I think about this any more my brain is going to explode."
        y "Wait, what was that...situation you mentioned earlier? The one I supposedly already know about?"
        c "There's only one situation I COULD be talking about."

        jump meetvoid


    label meetvoid:
        hide dottie
        hide coinflip
        mystery "Would you look at that."
        d "Was that...?"
        c "No. She doesn't come out like some sort of foot soldier."
        mystery "Oh, but it's such a special occasion! I simply HAD to come see this for myself."
        d "When I say run, RUN."
        y "What's happening? Who is that?"
        c "The situation."
        show voidqueen with dissolve
        "A strange figure steps out of the shadows."
        v "Well, well, well. So it looks like you've found your little leader. A bit scrawny, isn't she." 
        "The area surrounding the figure looks strange, almost like a faded-out photo."
        hide voidqueen with dissolve
        "And as soon as she appeared, she vanishes."
        show dottie sad
        show coinflip angry
        y "You didn't answer my question. Who is that?"
        d "The...Void Queen."
        c "She sucks the color out of everything she touches. Literally."
        y "How did she just disappear like that? Are we safe now?"
        show coinflip side
        c "Think so!"
        "You see a flash of something black skitter across the clearing where the Void Queen just was."
        y "You saw that, right?"
        d "I think that was one of the Void Queen's beetles. They're deadly if you provoke them. Thankfully--"
        c ""

        

    label savecoin:
        $ benevolence += 5

    label sacrificecoin:
        hide dottie
        show coinflip side
        c "It's okay, kid. Sometimes, you gotta make the hard decisions. It's war, what did you expect?"
        show coinflip death1
        c "At least I know it's not going to be for nothing. I was honored to be of service."
        "You feel a tinge of remorse having to send Coinflip to this fate, but like he said, war calls for difficult choices."
        show coinflip death2
        c "I know you'll do the right thing when the time calls for it."
        show coinflip rust
        "There's nothing left to do now but keep moving."
        hide coinflip
        $ corpses +=1

    label manwholostname:
        show noname at right
        y "Who are you?"
        mystery "That's a good question. She's a smart one, isn't she?"
        mystery "My name is..."
        mystery "Oh yeah! I lost it."
        y "You lost...your name?"
        show dottie happy at right
        d "It's a complicated situation. He's just a tad off his rockers is all.."
        mystery "BUt since you're human, your little flappy thing doesn't make the same sounds as us. So I think you can call me The Man Who Lost His Name!"
        y "That's a bit of a mouthful, though, don't you think?"
        m "Well, do you have a better idea? And besides, it has a nice ring to it."
        m "Anyways, where are you guys headed?"
        d "We were on our way to the lake before heading to _____"
        m "No way, that's my favorite part! I'm tagging along now."
        d "If you say so?"

    label fish:
        d "We've arrived at the lake, home to the fish!"
        y "Aww, they're kind of cute!"
        m "It's customary for a potential leader to be tested by the fish."
        y "Wait, huh?"
        "You look down in the lake."
        hide dottie
        hide noname
        show bluefish
        show orangefish
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
        hide bluefish
        hide orangefish
        show noname
        m "You were right! She IS some sort of miracle!"
        jump voidlake

    label blue:
        bf "You are CORRECT!"
        of "He's lying."
        y "What...?"
        $ confusion +=5
        hide orangefish
        hide bluefish
        show dottie happy at right
        show noname at left
        d "It's okay, you don't have to worry about them. The blue fish tells lies."
        m "Don't feel bad about getting it wwrong. They get in your head like that."
        d "That's why any future leader would have advisors! Like us!"
        jump voidlake

    label voidlake:
        hide dottie
        hide noname
        show orangefish
        show bluefish
        of "Hey Blue, do you...see that?"
        bf "I don't see anything at all. Nothing whatsoever!"
        of "Oh, great."
        of "Hey, Dottie? I think you're going to want to have a look at this."  
        hide bluefish
        hide orangefish
        "You and the group look to the lake's opposite shore, where the sand has started turning grey."
        d "How is it already here? I didn't think it would catch up to us this fast."
        m "Now's probably a good time to skedaddle before we all become void toast."
        d "But what about the fish?"
        m "What about them?"
        d "We can't just LEAVE them here!"
        m "Uhh, yeah we can. None of this will mean ANYTHING if we don't survive."
        menu:
            "We have to at least try to help them.":
                jump savefish
            "I don't think there's anything we can do.":
                jump sacrificefish

    label savefish:
        $benevolence +=7
        "You scoop the orange fish up in your arms."
        m "Well, I guess we're doing this now."
        "The Man Who Lost His Name follows, grabbing the blue fish."
        d "We can't keep them out of the water for too long. Over there should be a small pond where they can take shelter."
        hide dottie
        hide noname
        show orangefish
        show bluefish
        of "Thank you! Thank you thank you thank you!" 
        bf "No one's ever showed us this much compassion before. Most people just think we're an annoying gimmick."
        menu:
            "Why does this keep happening, though?":
                jump what
            "She can't keep doing this, taking away your homes.":
                jump outforblood


    label what:
        $confusion += 3
        hide orangefish
        hide bluefish
        show noname at left
        show dottie happy at right
        m "Maybe she's insane. Maybe she's jealous. Who knows!"
        of "Well, we're grateful nonetheless."
        d "That's our future General!"
        jump meetdancer
    
    label outforblood:
        hide orangefish
        hide bluefish
        show dottie happy at right 
        show noname at left
        m "Don't worry, you'll get your opportuntiy for revenge soon enough."
        d "Be patient. And don't encourage her to do something irrational!"
        y "This is only one of what, tens of places she's destroyed? Hundreds? Thousands?"
        y "If we don't stop her, who will?"
        $confrontation +=3
        jump meetdancer

    label sacrificefish:
        m "Let's keep going. Sorry guys, it's nothing personal."
        of "I've always hoped that I'd be able to go out with a bang. ENSURE OUR DEATHS WERE NOT IN VAIN, YOUNG WARRIOR!"
        bf "You were always the melodramatic one."
        of "Sure, sure."
        hide orangefish
        hide bluefish
        "The darkness spreads across the surface of the lake. As it approaches the fish, you wonder if this really was the only thing you could do."
        show dottie sad at right
        show noname at left
        d "He's right, you know. You won't always be able to save everyone."
        "You're not sure if what Dottie said is true. What if you had tried, at least?"
        "What if, what if, what if. There are so many things that could have been changed."
        m "I can see you dwelling on it. Now's not the time for sulking, it's time for JUSTICE!"
        $corpses+=1
        jump meetdancer


    label meetdancer:
        hide noname
        d "Okay, you need to be REALLY careful here. We don't want to scare her."
        y "Who's here?"
        "CRACK! The sound of a broken twig rings eerily."
        hide dottie
        show dancer shocked at left
        da "Where did you come from? Who are you? Why are you here?"
        d "It's me!"
        m "And me! And a friend."
        show dancer side
        da "Oh. Okay..."
        da "No one followed you here, right?"
        m "Of course not!"
        m "So that was awful timing."

    label savedancer:

    label sacrificedancer:
        show dancer shocked
        show dancer death1
        show dancer death2
        show dancer dust
        hide dancer
        show jhumka
        $ corpses +=1
        hide jhumka

    label crossroads:

    label savedottie:

    label sacrificedottie:
        show dottie sad
        d "What's...happening?"
        show dottie death1
        d "It was nice knowing you..."
        show dottie death2
        y "I'm sorry, Dottie."
        show dottie death3
        d "Goodbye."
        show dottie inkstained
        "All that remains where Dottie once stood is an inkstained leaflet."
        "You pick it up, a reminder of what you lost."
        hide dottie
        $ corpses +=1

    label chooserank:
        m "Well, clearly we don't have much time left."
        m "Our army needs its leader. Someoe who isn't afraid to take charge and fight."
        if corpses>2:
            m "And considering that my friends are dying left and right, I guess you're the only one left."
        else:
            m "And clearly you've proven yourself to be capable."
        m "So, what do you say? Are you up to the task you came here to fulfill?"
        y "You guys need to stop saying that. And..."
        menu:
            "I would be honored.":
                jump general
            "I'm not sure if I'm ready yet.":
                jump footman
            "Who said I would join you?" if corpses>3:
                jump evil

    label general:
        m ""
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
