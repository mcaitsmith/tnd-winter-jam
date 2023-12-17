# The script of the scene goes in this file.

######### SCENE 9: REUNION (Freddy and Bianca reunite, Steele experiences self-discovery)

# The scene starts here.

label scene9:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show chrome neutral at left

    # These display lines of dialogue.

    chrome "Welcome to Scene 9."

    show bianca neutral at right

    bianca "Now we're going to Scene 10."

    # jump to the next scene - Commented out for Scene Selector

    # jump scene10

    return