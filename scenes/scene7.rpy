# The script of the scene goes in this file.

######### SCENE 7: MARIAH'S OFFICE (more clickable areas as investigate office)

# The scene starts here.

label scene7:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    chrome "Welcome to Scene 7."

    chrome "Now we're going to Scene 8."

    # jump to next scene

    jump scene8