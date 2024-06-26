﻿# The script of the scene goes in this file.

######### SCENE 2: CHROME'S OFFICE (Chrome in his office, Bianca enters, dialogue w Bianca)

# The scene starts here.

# NOTE: GOING UNDER THE ASSUMPTION THAT CHARACTERS ALREADY AT A SCENE ARE ON THE RIGHT 
# AND CHARACTERS ARRIVING AT THE SCENE ARE ON THE LEFT. ALSO, NARRATION IS BOTTOM TEXT BOX 
# IN DIFFERENT FONT AND DIALOGUE IS CENTRAL VERTICAL.

label scene2:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg office night
    # fades to black for 1 second then fades in
    with Fade(0.5, 1.0, 0.5)

    # start Chrome music

    $ chrome_on = True
    $ update_layers() # turn on Chrome layer
    $ start_layers(3) # start playing layers

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show chrome neutral at right

    # These display lines of dialogue.

    chrome "{i}Another night, another empty inbox.{/i}"

    chrome "{i}The police wire rattles off petty theft after petty theft.{/i}"

    chrome "{i}Drunken disturbances, faulty old droids... even a cat in a tree.{/i}"

    chrome "{i}Nothing for an android detective. The one and only. In more ways than one...{/i}"

    # placeholder until we get asset
    play sound sfx_knocking volume 0.5 # more like banging, when you use the side of your fist instead of your knuckles

    # add pause to let sound effect play
    pause 2.0

    show chrome shocked

    chrome "..."

    # placeholder until we get asset
    play sound sfx_knocking volume 1.0 # same banging, maybe even a bit louder

    # add pause to let sound effect play
    pause 2.0

    # Do we want to say Unknown at first instead of bianca? The character art shouldn’t show yet.
    "???" "Detective Steele! You in there?! C'mon, lemme in!"

    show chrome neutral

    chrome "Enter."

    # placeholder until we get asset
    # play sound buzz

    # add pause to let sound effect play
    # pause 1.0

    play sound sfx_door

    # add pause to let sound effect play
    pause 2.0
    
    $ bianca_on = True # turn on Bianca layer
    $ update_layers(0) # update layers

    show chrome neutral at right
    show bianca angry at left with moveinleft

    show dialogue_box at center
    
    bianca_nvl_left "Finally. What took you so long?"
    
    show chrome thinking

    chrome_nvl_right "And your name is?"

    show bianca neutral

    bianca_nvl_left "BIANCA. Bianca Fontaine. I {i}{b}need{/b}{/i} your help."

    bianca_nvl_left "That's what you do, no? Help people?!"

    show chrome neutral

    # pause to switch to narration
    # pause 1.0

    hide dialogue_box

    chrome "{i}There she stood. Bianca Fontaine. Human girl, approximately 16, projecting confidence and determination. Clearly resourceful, yet clearly in need.{/i}"

    chrome "{i}I'll need to talk to her. Figure out what she wants. Weigh the right approach.{/i}"

    # When chrome is having his internal monologue, 
    # his face should also cycle through the representative detective style. 
    # Noted on separate lines, as it is not dialogue.

    chrome "{i}Loading interrogation identities...{/i}"

    show chrome logical

    chrome "{i}Do I go the logician route? {b}LOGICAL.{/b} Pure analysis and deduction. The Holmesian way?{/i}"

    show chrome unassuming

    chrome "{i}Or would the conversationalist route work best. {b}UNASSUMING.{/b} Disarming. Underestimated.{/i}"

    show chrome hardboiled

    chrome "{i}Or perhaps the cynic. {b}HARDBOILED.{/b} Direct. No nonsense...{/i}"

    show bianca angry
    show chrome neutral # return to normal when Bianca talks

    show dialogue_box at center

    bianca_nvl_left "Hey, you listening to me? It's... it's my dad, Freddy..."

    show bianca sad

    bianca_nvl_left "...he's gone missing."

    show chrome thinking

    chrome_nvl_right "Have you gone to the authorities?"

    bianca_nvl_left "Pff, the cops have no time for me and my dad."

    bianca_nvl_left "They just told me to wait 'til he comes home from whatever bender he's on."

    show chrome neutral

    chrome_nvl_right "Perhaps they're right."

    show bianca angry

    bianca_nvl_left "Look, my dad's been down on his luck since his boxing days, but he's no drunk."

    show bianca neutral

    bianca_nvl_left "He... He's been going out a lot lately. He won't tell me where, but..."

    show chrome thinking

    chrome_nvl_right "I'm curious. Why come to me?"

    chrome_nvl_right "Organics aren't so keen on me taking their cases."

    bianca_nvl_left "Organics, synthetics... I don't care. My dad is {b}missing.{/b}"

    bianca_nvl_left "And besides..."

    bianca_nvl_left "...word on the street is that you were trained by Forrest Cane."

    show chrome shocked

    chrome_nvl_right "Forrest Cane. That name - "
 
    ######### SCENE 2A: GLITCH 000 (flashback with glitching animation on Steele & bg grayed out)

    # hide bianca # hide Bianca for glitch
    # hide dialogue_box # temporarily end convo
    # nvl hide # hide NVL dialogue

    $ chrome_on = False # turn off Chrome layer for glitch
    $ update_layers(0) # update layers
    # show bg office night blur # blurs the background
    call start_glitch from _call_start_glitch_3 # shows Chrome glitching and grays out the background

    show chrome shocked glitch at right

    # pause for transition
    pause 1.0

    ### GLITCH SCENE #0
    ### This is the first minor glitch. It is a freebie, so no variable tracking.  
    ### It sets up the malfunctions. The floodgates are unleashed at the mention of Forrest Cane.

    chrome "{i}My circuitry burns like fire. I imagine. So hot that the intricate systems feeding information through my body go numb.{/i}"

    show chrome confused glitch

    chrome "{i}What is this? Fleetingly, I lose sense of the world around me. Flashes of images, lines of code, all rush through me at once.{/i}" 

    chrome "{i}I'm nowhere and everywhere. Everything I know, have known, have forgotten, fills my synthetic frame.{/i}"

    chrome "{i}I must be glitching... somehow..."

    show chrome shocked glitch

    chrome "{i}Then I see his face. Angular, laugh lines at the corners of his mouth. Tangled silver hair and horn-rimmed glasses that magnify deep, kind eyes. Eyes that listened as much as they saw.{/i}"

    show chrome sad glitch

    chrome "{i}Forrest Cane.{/i}"

    chrome "{i}But he's not here. He can't be...{/i}"

    chrome "{i}Cane disappeared from this world long ago.{/i}"

    chrome "{i}Powerful as my processor may be, I could never reconcile that dissonance. Cane, gone from the world but present in my mind. After some time, I did the only thing that made sense.{/i}"

    chrome "{i}I cleared my cache and locked him away. Every memory I had of him, encrypted and buried.{/i}"

    show chrome angry glitch

    chrome "{i}And yet, here he is, back to haunt me. Breaking free of his prison just as I'm tasked with finding another missing person.{/i}"

    chrome "{i}I'm not sure I can handle that.{/i}"

    chrome "{i}Not yet.{/i}"

    chrome "{i}I've got to get a grip...{/i}"
    
    scene bg office night with pixellate # unblur the background
    call end_glitch from _call_end_glitch_2 # return to normal Chrome and normal background
    $ chrome_on = True # turn on Chrome layer
    $ update_layers(0) # update layers

    # pause for transition
    # pause 1.0

    ######### back to SCENE 2

    $ glitch_counter +=1 # increment glitch counter

    show chrome angry at right
    show bianca neutral at left
    with dissolve

    show dialogue_box at center # return to convo
    nvl show # show NVL dialogue

    chrome_nvl_right "Then... Then you should know that I'm not the guy for the job."

    show bianca sad

    bianca_nvl_left "{i}Imbécil.{/i} Please. I don't know where else to turn..."

    show chrome neutral

    chrome_nvl_right "Scram, kid."

    show bianca angry

    bianca_nvl_left "You saying the rumors are true? That you're just deprecated goods?! {i}Metal inútil?!{/i}"

    bianca_nvl_left "Yeah, well - they say the same stuff about my dad."

    bianca_nvl_left "That he's a loser. A deadbeat."

    bianca_nvl_left "But it {i}{b}ain't{/b}{/i} true."

    bianca_nvl_left "Here's my info. My dad's been known to hang out at the Silver Cat. {i}{b}A lot.{/b}{/i}"

    bianca_nvl_left "If anyone knows anything, that would be a good place to start..."

    bianca_nvl_left "... when you're done feeling sorry for yourself."

    chrome_nvl_right "..."

    hide dialogue_box # end convo
    nvl clear # clear NVL dialogue

    hide bianca with moveoutleft # bianca leaves scene
    
    $ bianca_on = False # turn off Bianca layer
    $ update_layers(0) # update layers

    # placeholder until we get asset
    play sound sfx_doorslam

    # add pause to let sound effect play
    pause 1.0

    chrome "{i}I try to ease back into the old routine, but Bianca's words keep percolating to the top of my stack.{/i}"

    chrome "{i}The Silver Cat, huh? I know the joint.{/i}"

    chrome "{i}What the hell. I could use some jazz to clear my mind...{/i}"

    show chrome at right:
        xzoom -1.0
    hide chrome with moveoutright

    $ stop_layers(3) # stop playing layers

    # jump to next scene

    jump scene3
