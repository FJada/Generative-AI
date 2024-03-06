define stranger = Character("Stranger")
define chad = Character("Chad")
define you = Character("You")

image chad normal = "chad_image.png"

label start:

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
    "You wake up in a confused and dreamlike state. You hear splashes of water echoing in the distance"
    you "Where am I? Arguhh my head"
    show chad normal at left:
        yalign 0.5
        xalign 0.2
    with dissolve
    chad "WHATS GOOD! Wait what are you doing on the floor?"
    you "Oh Chad, whats good bro. Honestly I'm not too sure myself"
    you "Where are we?"
    chad "What are you even going on about? We were talking about this all month?"
    chad "Its the biggest party of the whole semester!"
    you "Oh right."
    chad "Honestly though, its not as fun as I thought it would be..."
    chad "You're known as the daredevil yet I haven't seen you do anything"
    stranger "Are you going to live up to your expectations?"
    you "Ow my head!"
    chad "You good?"
    you "Yea its nothing don't worry"
    chad "Well, are you gonna chicken out or what. Do something sick!"

    menu dangerouschoice:
        "Decide to jump off the roof into the pool":
            you "Haha fine, watch me jump into the pool from that roof"
            chad "Awesome!"
            jump firstchoiceA
            
        "Guzzle an entire bottle of vodka":
            you "You never stop bothering me huh. Fine get that bottle over there"
            chad "Radical!"
            jump firstchoiceB

    

label firstchoiceA:
    pass
label firstchoiceB:
    pass
        

    


