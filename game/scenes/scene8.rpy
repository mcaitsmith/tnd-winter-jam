﻿# The script of the scene goes in this file.

######### SCENE 8: FOWLER'S DEPARTMENT STORE (Alley)

label scene8:

    scene bg alley with fade

    $ chrome_on = True # turn on Chrome layer
    $ update_layers(0) # update layers

    show chrome neutral at right with moveinright

    # show chrome neutral at left:
    #     xzoom -1.0 
    # with dissolve

    show chrome neutral at left with moveinleft
    show chrome neutral at left:
        xzoom -1.0

    chrome "{i}I make my way to the alley to inspect the scene.{/i}"

    show larry dead at right with dissolve

    $ larry_santa_on = True
    $ update_layers() # turn on Larry layer


    chrome "Poor Schmuck."

    $ scene8_choice1 = False
    $ scene8_choice2 = False
    $ scene8_choice3 = False

    menu scene8_choices:
        chrome "Strange, I wonder if this really has something to do with Freddy? There's got to be some evidence lurking around here somewhere." 
        "What's that in the snow bank?" if scene8_choice1 == False:
            jump snowbank
        "{s}What's that in the snow bank?{/s}" if scene8_choice1 == True:
            jump snowbank
        "Footprints in the snow?" if scene8_choice2 == False:
            jump footprints
        "{s}Footprints in the snow?{/s}" if scene8_choice2 == True:
            jump footprints
        "What are those red speckles?" if scene8_choice3 == False:
            jump snowblood
        "{s}What are those red speckles?{/s}" if scene8_choice3 == True:
            jump snowblood

label snowbank:
    hide larry dead with moveoutright
    show cookietin at right
    chrome "{i}Hmm. It's a tin filled with Christmas cookies. They seem freshly baked.{/i}"
    hide cookietin
    $ scene8_choice1 = True
    if scene8_choice1 == True and scene8_choice2 == True and scene8_choice3 == True:
        jump cellcell
    else:
        jump scene8_choices

label footprints:
    hide larry dead with moveoutright
    show santaboots at right
    chrome "{i}These look like old Santa boots. Cheap ones too. The footprints are half-melted and inconclusive.{/i}"
    hide santaboots
    $ scene8_choice2 = True
    if scene8_choice1 == True and scene8_choice2 == True and scene8_choice3 == True:
        jump cellcell
    else:
        jump scene8_choices

label snowblood:
    hide larry dead with moveoutright
    show bloodysnow at right
    chrome "{i}Blood droplets in the snow. Something shiny catches my eye.{/i}"
    chrome "{i}Huh. A phone. The cops in all their disinterest haven't even noticed it.{/i}"
    hide bloodysnow
    $ scene8_choice3 = True
    if scene8_choice1 == True and scene8_choice2 == True and scene8_choice3 == True:
        jump cellcell
    else:
        jump scene8_choices

label cellcell:
    show chrome thinking left at left:
        xzoom -1.0
    chrome "{i}Hmm. What's on this phone?{/i}"
    show phone at center
    show chrome shocked
    chrome shocked "{i}There's a message from Freddy. \"Leave me alone, Larry. After tonight, you're dead to me.\"{/i}"
    chrome neutral "{i}This looks bad for Freddy. I know how quickly a missing person case can become suspected murder...{/i}"
    chrome neutral "{i}This is more than I bargained for. I better keep this bit of intel to myself for now, until there's more proof.{/i}"
    
    hide phone

    $ larry_santa_on = False
    $ update_layers() # turn off Larry layer

    $ scene5_choice3 = True

    if scene5_choice1 == True and scene5_choice2 == True and scene5_choice3 == True:
        chrome "{i}I think I've investigated enough here.{/i}"
        chrome "{i}There's some evidence to work with - none of it great for Freddy.{/i}"
        chrome "{i}And some testimony that doesn't quite jibe, but humans are nothing if not... inconsistent.{/i}"
        chrome "{i}It's time I had a heart-to-heart with Bianca. Ask her a few hanging questions.{/i}"
        chrome "{i}Besides, better to tell the kid in person what I found out.{/i}"
        chrome "{i}There's more to this story. I know it.{/i}"
        show chrome at left:
            xzoom 1.0
        hide chrome with moveoutleft
        jump scene9
    else:
        show chrome at left:
            xzoom 1.0
        hide chrome with moveoutleft
        scene bg extstore night with fade

        show chrome neutral at left:
            xzoom -1.0
        with moveinleft
        jump investigate
    
    jump investigate
    