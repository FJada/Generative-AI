#Initiatize characters
define player = Character("Player")
define stranger = Character("Stranger")

# scene characters
define chad = Character("Chad")
define fratbro = Character("FratBro")

image chad normal = "chad_image.png"
image fratbro normal = "chad_image.png"

#initialize guardian angle variables

# Initialize dictionaries for storing the statistics with default values
$ stats = {
    "good": Var("good", initial=0),
    "evil": Var("evil", initial=0),
    "kind": Var("kind", initial=0),
    "rude": Var("rude", initial=0),
    "sassy": Var("sassy", initial=0),
    "boring": Var("boring", initial=0),  
    "rainbowpower": Var("rainbowpower", initial=0)
}


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

    # Display player thoughts.
    "..."

    # Display player words.
    player "...where am I?"

    # "You awake with a violent gasp"
    #"A disembodied figure comes into focus after you get your bearings"
    # stranger "You... you have died. Welcome to the gray place."
    #stranger "A place neither good nor bad, simply the middle place for neutral souls like yours"

    stranger "You... you have died, and gone to Heaven. Your parents are so proud."

    # Present dialogue options to the player.
    $ learnList = []

    menu learn:
        set learnList :
        player "Really?":
            localize("Innocent +1")
            stats["good"].value += 1
            
        player "You're a real comedian, huh?":
            localize("Sassy +1")
            stats["Sassy"].value += 1
            
        player "Up yours, jerk.":
            localize("Rude +1")
            stats["rude"].value += 1

        player "That can't be.":
            stranger "Well, that was original."
            localize("Boring +1")
            stats["boring"].value += 1
            
        player "But...I'm gay.":
            localize("Rainbow power +1")
            stats["rainbowpower"].value += 1


    player "Woah, what was that? +1 what?"

    stranger "That was a step towards figuring out what kind of guardian angle you will become."

    player "Guardian angle? Wait -- I'm really dead?"

    stranger "Yes. You are in the realm of the departed. The afterlife. But now you have a chance to make a difference for those left."

    player "What was I before?"
        
    stranger "I am the gatekeeper of this realm. You may call me Elysium."

    player "How do you know if I will be a good guardian angle?"

    stranger "We don't. This is your test, and your journey alone."

    player "But--"

    stranger "This is just prototype, grasshopper. Time to start level 1."

    player "Now hold on just a min--"

# Save the statistics to persist the data across sessions
    save("stats", ignore=[], values=list(stats.values()))

    jump firstchoice

    return    

label firstchoice:

    $ persistent.player_pronouns = player_pronouns
    $ persistent.stats = stats

    scene bg scene2
    "You wake up in a confused and dreamlike state. You hear splashes of water echoing in the distance."

    you "Where am I? Arguhh my head!"
    show chad normal at left:
        yalign 0.5
        xalign 0.2
    with dissolve
    chad "YO WHAT'S GOOD! Wait bro... what are you doing on the floor?"
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
            
        "Guzzle an entire bottle of vodka":
            you "You never stop bothering me huh. Fine get that bottle over there!"
            chad "Radical!"
            jump firstchoiceB

    

label firstchoiceA:
    pass
label firstchoiceB:
    pass
        

    


