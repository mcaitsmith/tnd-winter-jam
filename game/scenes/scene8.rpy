﻿# The script of the scene goes in this file.

######### SCENE 8: FOWLER'S DEPARTMENT STORE (Alley)

label scene8:

    scene bg alley

    $ chrome_on = True # turn on Chrome layer
    $ update_layers(0) # update layers

    show chrome neutral at right

    # show chrome neutral at left:
    #     xzoom -1.0 
    # with dissolve

    chrome "{i}I make my way to the alley to inspect the scene.{/i}"

    show chrome neutral at left with moveinleft
    show chrome neutral at left:
        xzoom -1.0

    show larry dead at right with dissolve

    $ larry_santa_on = True
    $ update_layers() # turn on Larry layer


    chrome "Poor Schmuck."

    menu scene8_choices:
        chrome "Strange, I wonder if this has something to do with Freddy? There's got to be some evidence lurking around here somewhere." 
        "What's that in the snow bank?":
            hide larry dead with moveoutright
            show cookietin at right
            chrome "{i}Hm. A cookie tin filled with freshly baked Christmas cookies. Is this involved somehow?{/i}"
            hide cookietin
            jump scene8_choices
        "Footprints in the snow?":
            hide larry dead with moveoutright
            show santaboots at right
            chrome "{i}These look like Santa boots.{/i}"
            hide santaboots
            jump scene8_choices
        "What are those red speckles?":
            hide larry dead with moveoutright
            show bloodysnow at right
            chrome "{i}Blood droplets in the snow. Something shiny catches my eye.{/i}"
            chrome "{i}Huh. A phone. The cops in all their disinterest haven't even noticed it.{/i}"
            hide bloodysnow

            call cellcell from _call_cellcell
            return

label cellcell:
    show chrome thinking left at left:
        xzoom -1.0
    chrome "{i}Hmm. What's on this phone?{/i}"
    show phone at center
    show chrome shocked
    chrome shocked "{i}There's a message from Freddy. \"Leave me alone, Larry. After tonight, you're dead to me.\"{/i}"
    chrome neutral "{i}This looks bad for Freddy. How quickly a missing persons case can become murder. This is more than I bargained for. Better tell the kid in person.{/i}"
    
    $ larry_santa_on = False
    $ update_layers() # turn off Larry layer
    
    jump scene9
    