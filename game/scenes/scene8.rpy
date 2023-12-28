# The script of the scene goes in this file.

######### SCENE 8

label scene8:

    scene bg extstore

    show chrome neutral at left:
        xzoom -1.0 

    show larry dead at right

    $ larry_santa_on = True
    $ update_layers() # turn on Larry layer

    chrome "Poor Schmuck."

    menu scene8_choices:
        chrome "Strange, I wonder if this has something to do with Freddy? There's got to be some evidence lurking around here somewhere." 
        "What's that in the snow bank?":
            hide larry dead with moveoutright
            show cookietin at right
            chrome "Hm. A cookie tin filled with freshly baked Christmas cookies. Is this involved somehow?"
            jump scene8_choices
        "Footprints in the snow?":
            hide larry dead with moveoutright
            show santaboots
            chrome "These look like santa boots."
            jump scene8_choices
        "What are those red speckles?":
            hide larry dead with moveoutright
            # show #blood?
            chrome "On closer inspection, that seems to be blood droplets in the snow."
            call cellcell
            return

label cellcell:
    chrome thinking "Hm. What's on this phone?"
    show phone at center
    chrome shocked "Leave me alone, Larry. After tonight, you're dead to me."
    chrome neutral "This looks bad for Freddy. How quickly a missing persons case can become murder. Better tell the kid in person."
    
    $ larry_santa_on = False
    $ update_layers() # turn off Larry layer
    
    jump scene9
    