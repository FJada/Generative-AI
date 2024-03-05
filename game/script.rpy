
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

label next_scene:

    "Hello, [player_pronouns]. Welcome to the game!"
    # You can also store the selected pronouns in a persistent variable
    # to be used throughout the game.
    $ persistent.player_pronouns = player_pronouns

    # Continue with the rest of your game.
    # Add more labels and scenes as needed.

