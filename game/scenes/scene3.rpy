# The script of the scene goes in this file.

######### SCENE 3: SILVER CAT JAZZ CLUB (jazz bar w jazz music - Chrome enters, meets Jack Scanlon at bar, dialogue w Jack)

# The scene starts here.

label scene3:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show jack neutral

    # These display lines of dialogue.

    jack "Welcome to Scene 3."

    hide jack

    ######### SCENE 3A: GLITCH 2

    show chrome neutral

    chrome "GLITCH GLITCH GLITCH"

    ######### back to SCENE 3

    chrome "Woah that was weird"

    ######### SCENE 3B (?): I'll TAKE THE JOB (outside jazz bar or back in office - Chrome calls Bianca and says he'll take the job)

    chrome "Now we're going to Scene 4."

    # jump to next scene

    jump scene4