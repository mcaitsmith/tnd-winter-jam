# The script of the scene goes in this file.

######### SCENE 6: FOWLER'S DEPARTMENT STORE 2 (same scene but Mariah not there anymore - talk to robot Santa)

# The scene starts here.

label scene6:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show santa

    # These display lines of dialogue.

    santa "Welcome to Scene 6."

    hide santa

    ######### SCENE 6A: GLITCH 6

    show chrome neutral

    chrome "GLITCH GLITCH GLITCH"

    ######### back to SCENE 6

    chrome "Woah that was weird"

    chrome "Now we're going to Scene 7."

    # jump to next scene

    jump scene7