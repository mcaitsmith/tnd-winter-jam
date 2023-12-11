# The script of the scene goes in this file.

######### SCENE 8: ROOFTOP (find Freddy, dialogue with Freddy, then Mariah appears for climax, then cop & Jack Scanlon)

# The scene starts here.

label scene8:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show freddy neutral at left

    # These display lines of dialogue.

    freddy "Welcome to Scene 8."

    ######### SCENE 8A: ENDING 1 (best ending, if get 5-6/6 choices right)

    show chrome neutral at center

    chrome "This is Scene 8A."

    ######### SCENE 8B: ENDING 2 (average ending, if get 3-4/6 choices right)

    show mariah neutral at right

    mariah "This is Scene 8B."

    ######### SCENE 8C: ENDING 3 (worst ending, if get 0-2/6 choices right)

    freddy "This is Scene 8C."

    chrome "Now we're going to Scene 9."

    # jump to next scene

    jump scene9