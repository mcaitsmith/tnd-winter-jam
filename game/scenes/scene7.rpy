﻿# The script of the scene goes in this file.

######### SCENE 7: FOWLER'S DEPARTMENT STORE (Cop)

# The scene starts here.

label scene7:

    scene bg alley with fade

    play sound sfx_policechatter volume 0.5 loop

    show policelights with dissolve

    show chrome neutral at right with moveinright

    # chrome "{i}I make my way to the alley to inspect the scene.{/i}"

    chrome "{i}There's a cop standing guard by the alley. He's not making much effort to secure the area.{/i}"

    show cop neutral at left:
        xzoom -1.0  
    with moveinleft

    menu:
        "Hmm. He seems like a \"no nonsense, just the facts ma’am\" kinda guy..."

    # Option Two: (Logical. IDEAL PATH)
        "Logical":
            #programming - ideal choice += 1

            show dialogue_box at center 
            nvl show # show NVL dialogue

            chrome_nvl_right logical "Hello, sir. I’m looking for Freddy Font–"

            cop_nvl_left neutral "You’re not the only one."

            chrome_nvl_right logical "Hmm. And this poor sap?"

            cop_nvl_left neutral "That’s the funny thing."

            cop_nvl_left neutral "Larry the Elf here... he worked closely with Freddy."
            
            cop_nvl_left neutral "But if you ask me, it's probably a simple heart attack."

            cop_nvl_left neutral "Open and shut case. Everyone can just go home for the holidays already."

            chrome_nvl_right logical "You don't say? As I can see..."

            chrome_nvl_right logical "Freddy’s clearly a suspect, but why?" 

            chrome_nvl_right logical "A heart attack is a natural cause of death." 

            chrome_nvl_right logical "Sure it can be induced in the victim by an outside force but not easily." 

            chrome_nvl_right logical "Blood from the mouth."

            chrome_nvl_right logical "Body cold and already undergone rigor mortis, suggesting a time of death in the dead of night." 

            chrome_nvl_right logical "Freddy has a relationship with the victim, perhaps there’s a personal motive?"
        
            chrome_nvl_right logical "And why {i}here{/i} at their place of work?"

            chrome_nvl_right logical "Certainly he knew this would paint him as a suspect?"

            cop_nvl_left angry "Uh... Earth to metalhead?"

            cop_nvl_left angry "Am I interrupting you?"

            chrome_nvl_right logical "Yes, you are. What is it?"

            cop_nvl_left neutral "We figured all that out already. Freddy was present at the scene according to our witness."

            chrome_nvl_right confused "Come again?"

            cop_nvl_left neutral "Mariah Fowler. Says she saw this poor sucker collapse on the ground, and Freddy running in the other direction."

            cop_nvl_left neutral "Now why don't you go see for yourself or just {i}leave{/i}?"

            hide dialogue_box
            nvl clear 

            ######### GLITCH 3 (flashback with glitching animation on Steele & bg grayed out)

            # hide cop # hide cop for glitch
            # hide dialogue_box # temporarily end convo
            # nvl hide # hide NVL dialogue

            $ chrome_on = False # turn off Chrome layer for glitch
            $ update_layers(0) # update layers
            call start_glitch from _call_start_glitch_6 # shows Chrome glitching and grays out the background

            ### GLITCH SCENE #3

            show chrome shocked glitch at right
            # pause for transition
            pause 1.0

            chrome "{i}Another glitch. My algorithm searches for answers in the past as I seek them in the present.{/i}"

            show chrome sad glitch

            chrome "{i}I was the one who reported Cane's disappearance. I had been moved into the Android Barracks permanently at the start of training, but I still stopped by Cane's house from time to time.{/i}"

            chrome "{i}This visit was different. Cane had asked me there himself. He welcomed me in, sat me down and the next thing I knew - he was gone.{/i}"

            chrome "{i}The Bureau concluded that my system had rebooted itself in the moments between. Routine maintenance at an inconvenient time.{/i}"

            show chrome angry glitch

            chrome "{i}Guilt is a parasite. A computer virus. It gets inside and taints, destroys, and then devours.{/i}"

            chrome "{i}It's easy to acknowledge guilt when you've done something. It sits at the surface, present and accessible. It's harder to perceive such guilt when you haven't done something.{/i}"

            chrome "{i}When you haven't done something - and perhaps you could have - the guilt roots itself deeply. An internal bleed. A self-inflicted wound that pangs with every thought.{/i}"

            show chrome sad glitch

            chrome "{i}That's the guilt I felt for Cane's disappearance. With no true fault or culprit to blame, I attached myself to this parasite.{/i}"

            show chrome thinking glitch

            chrome "{i}The police did little to help. I took on the burden of finding Cane, and it tore me apart.{/i}"

            chrome "{i}If I hadn't rebooted, could I have apprehended a suspect? If I had not existed, if I had not been the poster child of Cane's experimental Android Detective Program, would he have been targeted at all?{/i}"

            show chrome sad glitch

            chrome "{i}I don't have to wonder why I locked away all memories of Forrest Cane.{/i}"

            chrome "{i}I remember the reasons all too well.{/i}"

            scene bg alley with pixellate # unblur the background
            call end_glitch from _call_end_glitch_5 # return to normal Chrome and normal background

            # pause for transition
            # pause 1.0

            $ glitch_counter +=1 # increment glitch counter

            $ chrome_on = True # turn off Chrome layer for glitch
            $ update_layers(0) # update layers

            # show dialogue_box at center # return to convo
            # nvl show # show NVL dialogue

            show chrome neutral at right
            show cop neutral at left:
                xzoom -1.0
            with dissolve

            pause 1.0
            

    #Option Three: (Unassuming)
        "Unassuming":

            show dialogue_box at center 
            nvl show # show NVL dialogue

            cop_nvl_left neutral "Alley’s closed."

            chrome_nvl_right unassuming "Oh, I work across the street."

            cop_nvl_left neutral "Where?"

            chrome_nvl_right thinking "..."

            cop_nvl_left neutral "..."

            chrome_nvl_right thinking "..."

            chrome_nvl_right unassuming "Over there."

            cop_nvl_left shocked "In that boarded up bail bonds office?"

            cop_nvl_left angry "This is an active crime scene. Get outta here!"

            chrome_nvl_right unassuming "Well, I hate to break it to ya, but..."

            chrome_nvl_right unassuming "...under code 2034.44, you'd be interfering with the duties of a certified bail bonds agent." 

            show cop angry

            chrome_nvl_right unassuming "I really don't want to have to report that to your superior..."

            cop_nvl_left neutral "Fine. Do what you want."

            chrome_nvl_right unassuming "By any chance, is there anything else you can tell me? I'd be much obliged."

            cop_nvl_left neutral "Hmph. Larry the elf collapsed. Freddy ran away."

            cop_nvl_left neutral "All according to eagle-eyed Mariah Fowler over there."       

            cop_nvl_left neutral "S'all I know. And all I care to find out. Happy Holidays."       

            hide dialogue_box
            nvl clear 

        # Option One: (hardboiled)
        "Hardboiled":
        
            show dialogue_box at center 
            nvl show # show NVL dialogue

            chrome_nvl_right hardboiled "Heyo, buddy boy! I’m looking for Freddy Font–"

            cop_nvl_left angry "Yeah? You and me both."

            chrome_nvl_right shocked "Excuse me?"

            cop_nvl_left angry "He’s a person of interest - might even say a suspect."

            chrome_nvl_right confused "Really?"

            cop_nvl_left angry "That woman right over there, found this poor schmuck dead as a doornail."

            cop_nvl_left angry "Says she saw him keel over and Freddy running the other way."

            chrome_nvl_right hardboiled "Hmm. Something seems fishy…"

            cop_nvl_left angry "The only thing fishy ‘round here is you."

            cop_nvl_left angry "Now giddy up Jingle Horse and quickly get the fuck out of my crime scene!"

            cop_nvl_left angry "Do what you gotta do and leave. You might not have better places to be for the holidays, but I do!"

            hide dialogue_box
            nvl clear 

    show cop at left:
        xzoom 1.0
    hide cop with moveoutleft

    hide policelights with dissolve

    stop sound

    $ scene5_choice2 = True

    if scene5_choice1 == True and scene5_choice2 == True and scene5_choice3 == True:
        chrome "{i}I think I've investigated enough here.{/i}"
        chrome "{i}There's some evidence to work with - none of it great for Freddy.{/i}"
        chrome "{i}And some testimony that doesn't quite jibe, but humans are nothing if not... inconsistent.{/i}"
        chrome "{i}It's time I had a heart-to-heart with Bianca. Ask her a few hanging questions.{/i}"
        chrome "{i}Besides, better to tell the kid in person what I found out.{/i}"
        chrome "{i}There's more to this story. I know it.{/i}"
        show chrome at right:
            xzoom -1.0
        hide chrome with moveoutright
        jump scene9
    else:
        show chrome at right:
            xzoom -1.0
        hide chrome with moveoutright
        scene bg extstore night with fade

        show chrome neutral at left:
            xzoom -1.0
        with moveinleft
        jump investigate