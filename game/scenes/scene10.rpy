﻿# The script of the scene goes in this file.

######### SCENE 10: SECRET ENDING (if get 6/6 choices right - closure of Steele's backstory)

# The scene starts here.

label scene10:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show chrome neutral

    # These display lines of dialogue.

    chrome "Welcome to Scene 10."

    chrome "Now going to next scene"

    # jump to next scene

    jump scene11

    # This ends the game.

    # return