define stranger = Character("Stranger")

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

    "You wake with a violent gasp of air"

    # Display dialogue from another character.
    "A disembodied figure comes into focus after you get your bearings"

    stranger "You... you have died. Welcome to the gray place."

    stranger "A place neither good nor bad, simply the middle place for neutral souls like yours"


    # Present dialogue options to the player.
    menu:
        "Who are you?":
            stranger "I am the gatekeeper of this realm. You may call me Elysium."
        "Where am I?":
            stranger "You are in the realm of the departed, the afterlife."
        "Why am I here?":
            stranger "That's for you to discover. Your journey has just begun."
        "I don't believe you.":
            stranger "Believe what you will, but the truth remains."

    # After the player selects a dialogue option, continue with the game.
    jump next_scene_continued

label next_scene_continued:
    # Continue with the rest of your game.
    # Add more labels and scenes as needed.


