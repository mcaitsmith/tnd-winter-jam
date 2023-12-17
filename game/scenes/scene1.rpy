# The script of the scene goes in this file.

######### SCENE 1: "THE TEASE" (crime scene: bg of dept store, Larry dead)

# The scene starts here.

label scene1:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show larry

    # These display lines of dialogue.

    larry "Welcome to Scene 1."

    larry "Now we're going to Scene 2."

    # jump to the next scene - Commented out for Scene Selector
    #jump scene2

    return
