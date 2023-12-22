# The script of the scene goes in this file.

######### SCENE 4: FOWLER'S DEPARTMENT STORE (outside store - woman by door, officer near alley, crime scene)

# The scene starts here.

label scene4:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show chrome neutral at left

    # These display lines of dialogue.

    chrome "Welcome to Scene 4. (This scene is deprecated?)"

    chrome "Now we're going to Scene 5."

    # jump to the next scene

    jump scene5