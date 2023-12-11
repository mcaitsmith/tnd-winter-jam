# The script of the scene goes in this file.

######### SCENE 5: FREDDY'S APARTMENT

# The scene starts here.

label scene5:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    chrome "Welcome to Scene 5."

    # next 2 subscenes can be played in any order

    ######### SCENE 5A: BIANCA

    bianca "This is Scene 5A."

    ######### SCENE 5A-1: GLITCH 5

    chrome "GLITCH GLITCH GLITCH"

    ######### back to SCENE 5A

    chrome "Woah that was weird"

    ######### SCENE 5B: INVESTIGATE APARTMENT (more clickable areas?)

    chrome "This is Scene 5B."

    chrome "Now we're going to Scene 6."

    # jump to next scene

    jump scene6