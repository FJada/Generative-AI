default stats = {
    "good": 0,
    "evil": 0,
    "kind": 0,
    "rude": 0,
    "sassy": 0,
    "boring": 0,
    "rainbowpower": 0
}


define stranger = Character("Stranger")
define Elysium = Character("Elysium")
define Frank = Character("Frank")
define chad = Character("Chad")
define you = Character("You")

image chad normal = "chad_image.png"
image chef normal = "chef_image.png"

image black = "#000" 
image white = "#ffffff" 
image intro = "wings.png" 


transform transform_intro:
    on show:
        alpha 0 xalign 0.5 yalign 0.5
        linear 2.0 alpha 1
    on hide:
        linear 2.0 alpha 0

transform transform_bg:
    on show:
        alpha 0 
        linear 2.0 alpha 1
    on hide:
        linear 2.0 alpha 0

label splashscreen:
    scene black 
    $ renpy.pause(0.5, hard=True) 
    
    show white at transform_bg
    $ renpy.pause(1, hard=True) 

    play sound "introsound.mp3"
    
    show intro at transform_intro
    $ renpy.pause(2, hard=True) 
    
    hide intro
    $ renpy.pause(0.5, hard=True) 
    
    hide white 
    $ renpy.pause(1, hard=True) 
    jump press_start

label press_start():
    scene bg scene1-2
    play music "startscreen.mp3"
    show title4:
        xalign 0.5
        yalign 0.1
    menu:
        "Start Game":
            jump start
    stop music fadeout 1.0

label start:
    scene black 
    # Display a text prompt asking the player to select their pronouns.
    "Please select your pronouns:"

    # Present the player with three choices for pronouns.
    menu:
        "She/Her":
            $ player_pronouns = "she/her"
        "He/Him":
            $ player_pronouns = "he/him"
        "They/Them":
            $ player_pronouns = "they/them"
        
    # Display a confirmation message with the selected pronouns.
    "You've selected [player_pronouns] as your pronouns."

    # Proceed to the next part of the game.
    jump next_scene

label next_scene:


    $ persistent.player_pronouns = player_pronouns
    python:
        import random
        scenes = [1,2]  # List of scene names
        next_story = random.choice(scenes)  # Choose a random scene from the list

    scene bg scene1-2
    show screen gameUI
    play music "myserioussong.mp3"
    # Display player thoughts.
    "..."

    # Display player words.
    you "...where am I?"

    # "You awake with a violent gasp"
    #"A disembodied figure comes into focus after you get your bearings"
    # stranger "You... you have died. Welcome to the gray place."
    #stranger "A place neither good nor bad, simply the middle place for neutral souls like yours"

    stranger "You... you have died, and gone to Heaven. Your parents are so proud."

    # Present dialogue options to the player.
    # learnList = []

    menu learn:
        # set learnList :
        "Really? Amazing!":
            $ stats["good"] += 1
            "1+ Innocent"
            
        "You're a real comedian, huh?":
            $ stats["sassy"] += 1
            "1+ Sassy +1"
            
        "Up yours, jerk.":
            $ stats["rude"] += 1
            "1+ Rude"
            
        "That can't be.":
            "Boring +1"
            stranger "Well, that was original."
            $ stats["boring"] += 1
            
        "But...I'm gay.":
            $ stats["rainbowpower"] += 1
            "Rainbow power +1"
            

    $ persistent.stats = stats

    you "Woah, what was that? +1 what?"

    stranger "That was one stat point towards figuring out what kind of guardian angel you will become."

    you "Guardian angel? Wait -- I'm really dead?"

    stranger "Yes. You are in the realm of the departed. The afterlife. But now you have a chance to make a difference for those left."

    you "What was I before?"
        
    stranger "I am the gatekeeper of this realm. You may call me Elysium."

    you "How do you know if I will be a good guardian angel?"

    Elysium "We don't. This is your test, and your journey alone."

    you "But--"

    Elysium "This is just prototype, grasshopper. Time to start level 1."

    you "Now hold on just a min--"

    # Save the statistics to persist the data across sessions
    # $ save("stats", ignore=[], values=list(stats.values()))
    stop music fadeout 1.0

    if next_story == 1:
        jump bradstory1
    
    if next_story == 2:
        jump chefstory1

    return    


label bradstory1:

    $ persistent.player_pronouns = player_pronouns
    $ persistent.stats = stats

    scene bg scene2
    show screen gameUI
    "You wake up in a confused and dreamlike state. There are splashes of water and yelling echoing in the distance."
    you "Where am I? Arguhh my head!"
    play music "<loop 0.1>partysong.mp3"
    show chad normal at left:
        yalign 0.5
        xalign 0.2
    with dissolve
    chad "WHAT'S GOOD BRO! Wait, what are you doing on the floor?"
    you "Oh Chad, what's good man. Honestly, I'm not too sure myself."
    you "Where are we?"
    chad "What are you even going on about? We were talking about this all month!!"
    chad "It's the biggest party of the whole semester!"
    you "Oh, right."
    chad "Honestly though, its not as fun as I thought it would be..."
    chad "You know I'm the daredevil, but this place has been so lame I haven't been able to do anything crazy!"
    Elysium "...Are you going to live up to your expectations? Time to be good, guardian angel."
    you "Ugh, my head."
    chad "Dude, you good? You look half-dead, bro."
    you "Yeah, it's nothin'. Don't worry."
    chad "Well, I am NOT gonna chicken out. I am gonna do something sick!"
    hide chad

    Elysium "You have 10 seconds to make a choice:"

    menu dangerouschoice:
        "Let Chad decide to jump off the balcony into the pool and simply watch":
            you "Ugh. Okay, I guess I'll watch you jump into the pool."
            chad "Awesome!"
            $ stats["rude"] += 1
            $ stats["evil"] += 1
            "You gained: 1+ Rude and 1+ Evil"
            jump firstchoiceA
            
        "Convince Chad to have a drink instead ":
            chad "You never stop bothering me, huh. Fine, get that bottle over there!"
            $ stats["good"] += 1
            "You gained: +1 Good"
            jump firstchoiceB
    

    Elysium "...Interesting choice."
    Elysium "But no time to dwell, others await."




label firstchoiceA:
    scene bg roof
    show screen gameUI
    show chad normal:
        xalign 0.5
        yalign 0.5
    chad "Wow, this is higher than I thought."
    Elysium "You are really bad at this whole guardian angle thing."
    you "Shut up."
    chad "Well, here goes nothing! YOLO!!"
    
    menu jumpintopool:
        "Jump":
            hide chad
            chad "AHHHHHH"
            "Hitting his head against the head of the pool, Chad takes an L on life. You can hear all the yelling fade away."
            Elysium "Another 'Fratboy Freak Accident by the Pool' for the books."
            jump end_scene


label firstchoiceB:
    scene bg scene2
    show screen gameUI
    show chad normal at left:
        yalign 0.5
        xalign 0.2
    with dissolve
    chad "Hmm. Not that much fun, but at least this tastes good!"
    Elysium "Good work. He would have died if he pulled that ridiculous stunt."
    $ stats["boring"] += 1
    jump end_scene



label end_scene:
    scene bg scene1-2
    show screen gameUI
    play music "startscreen.mp3"
    show title4:
        xalign 0.5
        yalign 0.1  

    $ persistent.player_pronouns = player_pronouns
    $ persistent.stats = stats

    Elysium "Entertaining, as always."
    you "So...how did I do?"
    Elysium "Let us see..."

    "click on stats to view"
        
    # Present the player with option to play again.
    menu:
        "Play Again?":
            jump start
    return

label chefstory1:
    scene bg scene6

    Elysium "I sense a troubled situation in a kitchen..."
    show chef normal at left:
        yalign 0.5
        xalign 0.2
    with dissolve

    "You enter the chaotic cooking show set, where you observe Frank, a nervous chef."

    Frank "Panicking) This can't be happening! I'm going to ruin everything."

    "Frank's thoughts: 'I can't believe I signed up for this amateur show! Pressure's getting to me.'"

    Elysium "Dont stand there do something!"

    menu chefhelp:
        "Culinary Inspiration":
            Elysium "Why don't I send him an imaginary Gordon Ramsay-like voice for motivation, but with a comedic twist?'"
            "Frank: (Laughing nervously) Wait, is that Chef Ramsey... err, his hilarious twin encouraging me? It's working!"
            $ stats["good"] += 1
            "you gained a good point"
            jump culinaryinspiration
            
        "Kitchen Mishap Redirection":
            "Guardian Angel: 'Let's cause Frank to accidentally drop an oven mitt, diverting his attention from the stove.'"
            "Frank: (Distracted) Oops, my mitt fell! I feel like i cant breathe"
            "The mitt bounces and causes a pan to flip over causeing a fire"
            $ stats["evil"] += 1
            "you gained a evil point"
           
        
label culinaryinspiration:
    scene bg scene6
    Elysium "I sense positivity here."
    show chef normal at left:
        yalign 0.5
        xalign 0.2
    with dissolve
    Frank "By remembering my inspiration for getting into cooking i was able to channel my skills better"
    Frank "Thank you!"
    jump end_scene

label mishap:
    scene bg scene6
    Elysium "I sense a troubled situation in a kitchen..."
    show chef normal at left:
        yalign 0.5
        xalign 0.2
    with dissolve
    Frank "Everything burned to a crisp. What will i do? This was my great grandpa's restaurant?"
    Elysium "Wow that was really bad. I dont think ive seen fire that hot and ive been to hell before"
    jump end_scene