# The script of the scene goes in this file.

######### SCENE 1: "THE TEASE" (crime scene: bg of dept store, Larry dead)

# From Script Guide: LARRY THE ELF lays dead on the snowy sidewalk in front of Fowler’s Department Store.
# One pair of feet shuffle by him, leaving him alone.

# The scene starts here.

label scene1:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg extstore # the sidewalk is snowy, random footprints

    # add pause at beginning of scene
    # pause 3.0

    $ larry_santa_on = True
    $ update_layers() # turn on Larry layer
    $ start_layers() # start playing layers

    # placeholder until we get asset
    # play sound bell # a hand bell typically used by street santa’s rings periodically in the distance

    # add pause to let sound effect play
    # pause 3.0

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # VISUAL: fade-in Larry. He is clearly dead. Some red blood accents.
    show larry dead at center 
    show dialogue_box at center

    # add pause after showing larry
    pause 1.0

    play sound sfx_footsteps # feet shuffling and trailing off

    # add pause to let sfx play
    pause 2.0

    # Optional – should we have a woman scream next, like he is discovered?
    # Either way, we should fade-out and into the next scene, which is Chrome brooding in his dark office.
    hide dialogue_box # return to ADV mode

    $ larry_santa_on = False
    $ update_layers(1) # turn off Larry layer
    # jump to the next scene - Commented out for Scene Selector
    jump scene2 # added fade transition to show scene in scene2 script

    # return
