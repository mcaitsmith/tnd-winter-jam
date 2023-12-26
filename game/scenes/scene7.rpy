# The script of the scene goes in this file.

######### SCENE 7: Alley

# The scene starts here.

label scene7:

    scene bg alley

    show chrome at right    

    show cop at left   

    menu:
        "Hm. He seems like a \"no nonsense, just the facts ma’am\" kinda guy. I wonder what approach I should take?"

    # Option One: (hardboiled)
        "Hardboiled":

            chrome hardboiled "Heyo, buddy boy! I’m looking for Freddy Font–"

            cop angry "Yeah? You and me both."

            chrome shocked "Excuse me?"

            cop angry "He’s a person of interest- might even say a suspect."

            chrome angry "Really?"

            cop angry "That woman right over there, found this poor schmuck dead as a doornail."

            cop angry "Combine that with the fact Freddy didn’t show up today, his last day…"

            chrome confused "Hm. Something seems fishy…"

            cop angry "The only thing fishy ‘round here is you! Now giddy up Jingle Horse and get the fuck out of my active crime scene!"

    # Option Two: (Logical. IDEAL PATH)
        "Logical":
            #programming - ideal choice += 1

            chrome logical "Hello, sir. I’m looking for Freddy Fontaine–"

            cop neutral "You’re not the only one."

            chrome logical "Hm. Interesting. Locate any evidence?"

            cop neutral "That’s the funny thing. He died from a heart attack."

            chrome confused "Heart attack? Something doesn’t add up here."

            cop neutral "Whelp, we’ve got a witness...."

            chrome confused "Who?"

            cop neutral "Mariah Fowler. Saw this poor sucker collapse on the ground, and Freddy running the other direction"

            chrome logical "Very interesting. Thanks."

            ######### GLITCH 3 (flashback with glitching animation on Steele & bg grayed out)

            hide cop # hide cop for glitch
            # hide dialogue_box # temporarily end convo
            # nvl hide # hide NVL dialogue

            $ chrome_on = False # turn off Chrome layer for glitch
            $ update_layers(0) # update layers
            # show bg alley blur # blurs the background
            call start_glitch # shows Chrome glitching and grays out the background

            # pause for transition
            pause 1.0

            ### GLITCH SCENE #3

            show chrome shocked glitch

            chrome "{i}Another glitch. My algorithm searches for answers in the past as I seek them in the present.{/i}"

            show chrome sad glitch

            chrome "{i}I was the one who reported Cane's disappearance. I had been moved into the Android Barracks permanently at the start of training, but I still stopped by Cane's house from time to time.{/i}"

            chrome "{i}This visit was different. Cane had asked me there himself. He welcomed me in, sat me down and the next thing I knew-he was gone.{/i}"

            chrome "{i}The Bureau concluded that my system had rebooted itself in the moments between. Routine maintenance at an inconvenient time.{/i}"

            show chrome angry glitch

            chrome "{i}Guilt is a parasite. A computer virus. It gets inside and taints, destroys, and then devours.{/i}"

            chrome "{i}It's easy to acknowledge guilt when you've done something. It sits at the surface, present and accessible. It's harder to perceive such guilt when you haven't done something.{/i}"

            chrome "{i}When you haven't done something-and perhaps you could have-the guilt roots itself deeply. An internal bleed. A self-inflicted wound that pangs with every thought.{/i}"

            show chrome sad glitch

            chrome "{i}That's the guilt I felt for Cane's disappearance. With no true fault or culprit to blame, I attached myself to this parasite.{/i}"

            show chrome thinking glitch

            chrome "{i}The police did little to help. I took on the burden of finding Cane, and it tore me apart.{/i}"

            chrome "{i}If I hadn't rebooted, could I have apprehended a suspect? If I had not existed, if I had not been the poster child of Cane's experimental Android Detective Program, would he have been targeted at all?{/i}"

            show chrome sad glitch

            chrome "{i}I don't have to wonder why I locked away all memories of Forrest Cane.{/i}"

            chrome "{i}I remember the reasons all too well.{/i}"

            show bg alley # unblur the background
            call end_glitch # return to normal Chrome and normal background
            $ chrome_on = True # turn on Chrome layer
            $ update_layers(0) # update layers

            # pause for transition
            pause 1.0

            $ glitch_counter +=1 # increment glitch counter

            ######### back to SCENE 2

            # show dialogue_box at center # return to convo
            # nvl show # show NVL dialogue

            # hide chrome
            # show chrome angry at right
            show cop neutral at left

    #Option Three: (Unassuming)
        "Unassuming":

            cop neutral "Alley’s closed."

            chrome unassuming "Oh, I work across the street."

            cop neutral "Where?"

            chrome thinking "..."

            cop neutral "..."

            chrome thinking "..."

            chrome hardboiled "Over there."

            cop shocked "In that boarded up bail bonds office?"

            cop angry "This is an active crime scene. Get outta here!"

            chrome angry "..."

            chrome logical "Under code 2034.44 You, sir, are interfering with the duties of a certified bail bonds agent…" 

            show cop angry

            chrome unassuming "Would you like me to report THAT to your superior?"

            cop angry  "Fine. Go through"


    jump scene8