# The script of the scene goes in this file.

######### SCENE 2: CHROME'S OFFICE (Chrome in his office, Bianca enters, dialogue w Bianca)

# The scene starts here.

label scene2:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg office

    # start Chrome music

    $ chrome_on = True
    $ update_layers() # turn on Chrome layer
    $ start_layers(3) # start playing layers

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show chrome neutral at left:
        xzoom -1 # this flips the image so he is facing toward the right

    # These display lines of dialogue.

    chrome "Welcome to Scene 2."

    ######### SCENE 2A: GLITCH 1 (flashback with glitching animation on Steele & bg grayed out)

    show bg office blur # blurs the background
    call start_glitch # shows Chrome glitching and grays out the background

    chrome "GLITCH GLITCH GLITCH"

    ######### back to SCENE 2

    show bg office # unblur the background
    call end_glitch # return to normal Chrome and normal background

    $ bianca_on = True # turn on Bianca layer
    $ update_layers(0) # update layers

    show bianca neutral at right

    bianca "Now we're going to Scene 3."

    $ mariah_on = True # turn on Bianca layer
    $ update_layers(0) # update layers

    show mariah neutral at center

    mariah "TEST"

    $ stop_layers(3) # stop playing layers

    bianca "test"

    # jump to next scene

    jump scene3
