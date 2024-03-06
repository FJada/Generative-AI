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
define chad = Character("Chad")
define you = Character("You")

image chad normal = "chad_image.png"

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
    
    show intro at transform_intro
    $ renpy.pause(2, hard=True) 
    
    hide intro
    $ renpy.pause(0.5, hard=True) 
    
    hide white 
    $ renpy.pause(1, hard=True) 
    jump press_start

label press_start():
    scene bg scene1-2
    show title3:
        xalign 0.5
        yalign 0.1
    menu:
        "Start Game":
            jump start

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
    scene bg scene1-2

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
            # $ localize("Innocent +1");
            $ stats["good"] += 1
            
        "You're a real comedian, huh?":
            # $ localize("Sassy +1");
            $ stats["sassy"] += 1
            
        "Up yours, jerk.":
            # $ localize("Rude +1");
            $ stats["rude"] += 1

        "That can't be.":
            stranger "Well, that was original."
            # $ localize("Boring +1");
            $ stats["boring"] += 1
            
        # "But...I'm gay.":
        #     $ localize("Rainbow power +1");
            $ stats["rainbowpower"] += 1

    $ persistent.stats = stats

    you "Woah, what was that? +1 what?"

    stranger "That was one stat point towards figuring out what kind of guardian angel you will become."

    you "Guardian angel? Wait -- I'm really dead?"

    stranger "Yes. You are in the realm of the departed. The afterlife. But now you have a chance to make a difference for those left."

    you "What was I before?"
        
    stranger "I am the gatekeeper of this realm. You may call me Elysium."

    you "How do you know if I will be a good guardian angel?"

    stranger "We don't. This is your test, and your journey alone."

    you "But--"

    stranger "This is just prototype, grasshopper. Time to start level 1."

    you "Now hold on just a min--"

    # Save the statistics to persist the data across sessions
    # $ save("stats", ignore=[], values=list(stats.values()))

    jump firstchoice

    return    


label firstchoice:

    $ persistent.player_pronouns = player_pronouns

    scene bg scene2
    "You wake up in a confused and dreamlike state. You hear splashes of water and yelling echoing in the distance."
    you "Where am I? Arguhh my head!"
    show chad normal at left:
        yalign 0.5
        xalign 0.2
    with dissolve
    chad "WHATS GOOD! Wait what are you doing on the floor?"
    you "Oh Chad, whats good bro. Honestly I'm not too sure myself."
    you "Where are we?"
    chad "What are you even going on about? We were talking about this all month?"
    chad "Its the biggest party of the whole semester!"
    you "Oh right."
    chad "Honestly though, its not as fun as I thought it would be..."
    chad "I am known as the daredevil - yet I haven't been able to do anything!"
    stranger "Are you going to live up to your expectations? Be good."
    you "Ow my head!"
    chad "You good?"
    you "Yea its nothing don't worry."
    chad "Well, I am not gonna chicken out. I am gonna do something sick!"
    

    menu dangerouschoice:
        "Let Chad decide to jump off the balcony into the pool and simply watch":
            you "Haha fine, ill watch you jump into the pool."
            chad "Awesome!"
            $ stats["boring"] += 1
            "You gained one stat point in being boring"
            jump firstchoiceA
            
        "Convince Chad to have a drink instead ":
            chad "You never stop bothering me huh. Fine get that bottle over there!"
            $ stats["good"] += 1
            "You gained one stat point in being good"
            jump firstchoiceB
    return
    

label firstchoiceA:
    scene bg roof
    show chad normal:
        xalign 0.5
        yalign 0.5
    chad "Wow this is higher than I thought"
    stranger "No going back for him now huh?"
    you "Shut up."
    chad "Well here goes nothing!"

    menu jumpintopool:
        "Jump":
            chad "AHHHHHH"
            "Hitting his head against the head of the pool, he bleeds out. You can hear all the yelling fade away."
            stranger "Bad job. Freak Accident. He died. Not a good companion."


label firstchoiceB:
    scene bg scene2
    show chad normal at left:
        yalign 0.5
        xalign 0.2
    with dissolve
    chad "Hmm. Not that much fun but atleast this tastes good"
    stranger "Good work. He would have died if he pulled that ridiculous stunt."

    


