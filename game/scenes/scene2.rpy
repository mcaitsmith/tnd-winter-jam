# The script of the scene goes in this file.

######### SCENE 2: CHROME'S OFFICE (Chrome in his office, Bianca enters, dialogue w Bianca)

# The scene starts here.

# NOTE: GOING UNDER THE ASSUMPTION THAT CHARACTERS ALREADY AT A SCENE ARE ON THE RIGHT 
# AND CHARACTERS ARRIVING AT THE SCENE ARE ON THE LEFT. ALSO, NARRATION IS BOTTOM TEXT BOX 
# IN DIFFERENT FONT AND DIALOGUE IS CENTRAL VERTICAL.

label scene2:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg office
    # fades to black for 1 second then fades in
    with Fade(0.5, 1.0, 0.5)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show chrome neutral at right

    # These display lines of dialogue.

    chrome "{i}Another night, another empty inbox.{/i}"

    chrome "{i}The police wire rattles off petty theft after petty theft.{/i}"

    chrome "{i}Drunken disturbances, faulty old droids...even a cat in a tree.{/i}"

    chrome "{i}Nothing for an android detective. The one and only. In more ways than one...{/i}"

    # placeholder until we get asset
    # play sound knocking volume 0.5 # more like banging, when you use the side of your fist instead of your knuckles

    # add pause to let sound effect play
    # pause 3.0

    show chrome shocked

    chrome "..."

    # placeholder until we get asset
    # play sound knocking volume 1.0 # same banging, maybe even a bit louder

    # add pause to let sound effect play
    # pause 3.0

    # Do we want to say Unknown at first instead of bianca? The character art shouldn’t show yet.
    "Detective Steele! You in there?! C'mon, lemme in!"

    show chrome neutral

    chrome "Enter."

    # placeholder until we get asset
    # play sound buzz

    # add pause to let sound effect play
    # pause 1.0

    # placeholder until we get asset
    # play sound door_open

    # add pause to let sound effect play
    # pause 1.0

    show bianca angry at left
    
    bianca "Finally. What took you so long?"
    
    chrome "And your name is?"

    show bianca neutral

    bianca "BIANCA. Bianca Fontaine. I {i}{b}need{/b}{/i} your help."

    bianca "That's what you do, no? Help people?!"

    # pause to switch to narration
    # pause 1.0

    chrome "{i}There she stood. Bianca Fontaine. Human girl, approximately 16, projecting confidence and determination. Clearly resourceful, yet clearly in need.{/i}"

    chrome "{i}I'll need to talk to her. Figure out what she wants. Weigh the right approach.{/i}"

    # When chrome is having his internal monologue, 
    # his face should also cycle through the representative detective style. 
    # Noted on separate lines, as it is not dialogue.

    show chrome thinking

    chrome "{i}Do I go the LOGICIAN route? Pure analysis and deduction. The Holmesian way?{/i}"

    show chrome timid

    chrome "{i}Or would the CONVERSATIONALIST route work best. Unassuming. Disarming. Underestimated.{/i}"

    show chrome angry

    chrome "{i}Or perhaps the CYNIC. Hardboiled. Direct. No nonsense...{/i}"

    show bianca angry
    show chrome neutral # return to normal when Bianca talks

    bianca "Hey, you listening to me? It's.. it's my dad, Freddy..."

    show bianca sad

    bianca "...he's gone missing."

    chrome "Have you gone to the authorities?"

    bianca "Pff, the cops have no time for me and my dad."

    bianca "They just told me to wait 'til he comes home from whatever bender he's on."

    chrome "Perhaps they're right."

    show bianca angry

    bianca "Look, my dad's been down on his luck since his boxer days, but he's no drunk."

    show bianca neutral

    bianca "He... He's been going out a lot lately. He won't tell me where, but..."

    show chrome thinking

    chrome "I am curious. Why come to me?"

    bianca "..."

    bianca "Word on the street is that you were trained by Forrest Cane."

    ######### SCENE 2A: GLITCH 000 (flashback with glitching animation on Steele & bg grayed out)

    hide bianca # hide Bianca for glitch
    show bg office blur # blurs the background
    call start_glitch # shows Chrome glitching and grays out the background

    # pause for transition
    pause 1.0

    ### GLITCH SCENE #0
    ### This is the first minor glitch. It is a freebie, so no variable tracking.  
    ### It sets up the malfunctions. The floodgates are unleashed at the mention of Forrest Cane.
    ### TEXT OF THE GLITCH WILL BE INSERTED HERE 

    show bg office # unblur the background
    call end_glitch # return to normal Chrome and normal background
    # show Bianca again
    show bianca neutral at left

    # pause for transition
    pause 1.0

    ######### back to SCENE 2

    show chrome angry

    chrome "Then you should know that I'm not the guy for the job."

    show bianca sad

    bianca "Please. I don't know where else to turn..."

    show chrome neutral

    chrome "Scram, kid."

    show bianca angry

    bianca "You saying the rumors are true? That you're just deprecated goods?!"

    bianca "Yeah, well - they say the same stuff about my dad. That he's a loser. A deadbeat. But it {i}{b}ain't{/b}{/i} true."

    bianca "Here's my info. My dad's been known to hang out at the Silver Cat. {i}{b}A lot.{/i}{/b}"

    bianca "If anyone knows anything, that would be a good place to start."

    hide bianca # bianca leaves scene

    # placeholder until we get asset
    # play sound door_slam

    # add pause to let sound effect play
    # pause 1.0

    chrome "{i}I try to ease back into the old routine, but Bianca's words keep percolating to the top of my stack.{/i}"

    chrome "{i}The Silver Cat, huh? I know the joint.{/i}"

    chrome "{i}I could use some jazz to clear my mind...{/i}"

    # jump to the next scene

    jump scene3
