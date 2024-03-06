﻿define stranger = Character("Stranger")
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

    play sound "woof.mp3"
    
    show intro at transform_intro
    $ renpy.pause(2, hard=True) 
    
    hide intro
    $ renpy.pause(0.5, hard=True) 
    
    hide white 
    $ renpy.pause(1, hard=True) 
    jump press_start

label press_start():
    scene bg scene1-2
    show title4:
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

# label next_scene:

#     "Hello, [player_pronouns]. Welcome to the game!"
#     # You can also store the selected pronouns in a persistent variable
#     # to be used throughout the game.
#     $ persistent.player_pronouns = player_pronouns


label next_scene:

    $ persistent.player_pronouns = player_pronouns
    scene bg scene1-2

    "You wake with a violent gasp of air"

    # Display dialogue from another character.
    "A disembodied figure comes into focus after you get your bearings"

    stranger "You... you have died. Welcome to the gray place."

    stranger "A place neither good nor bad, simply the middle place for neutral souls like yours"


    # Present dialogue options to the player.
    $ learnList = []

    menu learn:
        set learnList
        "Who are you?":
            stranger "I am the gatekeeper of this realm. You may call me Elysium."
            
        "Where am I?":
            stranger "You are in the realm of the departed, the afterlife."
            
        "Why am I here?":
            stranger "That's for you to discover. Your journey has just begun."
            
        "I don't believe you.":
            stranger "Believe what you will, but the truth remains."

        "Ok, I am ready...":
            jump firstchoice

    jump learn     
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
    chad "You're known as the daredevil - yet I haven't seen you do anything!"
    stranger "Are you going to live up to your expectations?"
    you "Ow my head!"
    chad "You good?"
    you "Yea its nothing don't worry."
    chad "Well, are you gonna chicken out or what. Do something sick!"

    menu dangerouschoice:
        "Decide to jump off the roof into the pool":
            you "Haha fine, watch me jump into the pool from that roof."
            chad "Awesome!"
            jump firstchoiceA
            
        "Drink 3 shots of vodka":
            you "You never stop bothering me huh. Fine get that bottle over there!"
            chad "Radical!"
            jump firstchoiceB
    return
    

label firstchoiceA:
    scene bg scene7
    you "Wow this is higher than I thought"
    stranger "No going back now huh?"
    you "Shut up."
    you "Well here goes nothing!"

    menu jumpintopool:
        "Jump":
            you "AHHHHHH"
            "Hitting your head against the head of the pool, you slowly bleed out. You can hear Chad's yelling fade away."
            stranger "Good job. Freak Accident. You died."


label firstchoiceB:
    scene bg scene2
    show chad normal at left:
        yalign 0.5
        xalign 0.2
        

    


