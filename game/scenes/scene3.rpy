# The script of the scene goes in this file.

######### SCENE 3: SILVER CAT JAZZ CLUB (jazz bar w jazz music - Chrome enters, meets Jack Scanlon at bar, dialogue w Jack)

# The scene starts here.

label scene3:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bar

    # play music
    play music "audio/AUDIO-2023-12-19-18-56-38.mp3" fadeout 3.0

    # placeholder until we get asset
    # play sound door_open

    # add pause to let sound effect play
    pause 1.0

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # VISUAL: fade-in chrome
    show chrome neutral at left:
        xzoom -1.0 # make him face right
    with dissolve

    # These display lines of dialogue.

    chrome "{i}The moment I enter the Silver Cat the jazz sways and stutters all around me. It's been too long.{/i}"

    chrome "{i}The jazz trio at work follows no rules, no formula, no set pattern. The lack of syncopation is oddly... moving.{/i}"

    chrome "{i}It's enough to make a man cry. I'm sure of it.{/i}"

    chrome "{i}After a quick scan of the joint, I spot a regular at the corner of the bar with a stack of empty glasses in front of him.{/i}"

    chrome "{i}Come to think of it, seems like he's always here.{/i}"

    chrome "{i}If anyone's seen Freddy, it's him.{/i}"

    show jack neutral at right

    # pause to show jack
    pause 1.0

    chrome "Can I buy you another drink?"

    show jack happy

    jack "Ahh, beggars can't be choosers, my mama used to say. Rest her soul."

    jack "Jack Scanlon's the name. To whom do I owe this honor?"

    chrome "Chrome. Chrome Steele. I'm a friend of Freddy's - Freddy Fontaine. You know him?"

    jack "Good ole Freddy. Bianca too - that's his daughter, you see. Lovely girl."

    jack "Fine gin this, ain't it?"

    show jack shocked

    jack "Ahh, I suppose you wouldn't know! Shame..."

    show jack neutral

    jack "Hey, you look like the kind sort. Can I ask for a small loan? Something to get on my feet? I'm good for it..."

    chrome "{i}Jack seemed like the friendly sort. Gregarious. Unfocused. Meandering. His attention wavering like a mercurial jazz riff. I'm sure it had nothing to do with synthahol bombarding my aromatic sensors.{/i}"

    # VARIABLE: Create a glitch counter and set it to 0
    $ glitch_counter = 0

    # CHOICE

    menu:
        chrome "This guy's all over the place. I've got to get through to him..."
        "Logical":
            call scene3_logical
        "Unassuming":
            call scene3_unassuming
        "Hardboiled":
            call scene3_hardboiled

    show chrome neutral

    chrome "Thanks for your time, Jack. It's been..."

    # This variable check is just for this one subtle line of dialogue
    if glitch_counter == 0:
        chrome "...interesting."
    elif glitch_counter == 1:
        chrome "...very helpful."

    show jack happy

    jack "Think nothing of it."

    show jack neutral

    jack "Excuse me now lad, time for a piss and a smoke. I'd ask you to join me, but, y'know..."

    chrome "See you around, Jack."

    #VISUAL: fade-out. Jack leaves scene.
    hide jack
    with dissolve

    # pause after Jack leaves
    pause 1.0

    chrome "{i}Seems like Freddy had some secret business at Fowler's Department Store, of all places.{/i}"

    chrome "{i}It's as good a lead as any, I suppose.{/i}"

    chrome "{i}I take a minute to message Bianca that I'm taking the case.{/i}"

    chrome "{i}For now.{/i}"

    # stop music
    stop music fadeout 3.0

    # jump to the next scene - Commented out for Scene Selector

    # jump scene4
    return

label scene3_logical:

    show chrome thinking

    chrome "I'm curious as to the whereabouts of Freddy."

    jack "Oh really, why's that?"

    chrome "According to Bianca, he vanished without a trace."

    show jack happy

    jack "Did you say Bianca? Good kid, right??"

    chrome "Please my man, just tell me how you know Freddy!"

    show jack neutral

    jack "Oh, me and Freddy?  We go waaay back."

    jack "We used to work together at the docks - after his boxing career fizzled."

    jack "He went through some rough times. In and out of trouble for a while."

    jack "But he straightened himself out."

    chrome "Is there anything else worth note? Think!"

    jack "He used to get his hands on all these fancy cigarettes."

    jack "European shit, right off the boats. Hand-rolled, clove, you name it!"

    show jack happy

    jack "We used to bag off and take smoke breaks all the time..."

    chrome "Sounds... lovely. Can you tell me anything more recent?"

    chrome "And just the facts!"

    show jack neutral

    jack "Eh, sure. Lemme, think..."

    jack "..."

    jack "..."

    show jack happy

    jack "Oh yeah!! He mentioned something about a gig at the Department Store."

    chrome "Fowler's?"

    show jack neutral

    jack "Yeah, that dump!! Didn't really want to talk about it though. Was about a week ago."

    chrome "I see. Is there {i}{b}anything{/b}{/i} else? Anything you forgot to mention?"

    show jack sad

    jack "Well, would you look at this? My glass is empty."

    return

label scene3_unassuming:

    show chrome timid

    chrome "So, about Freddy. Nice guy, huh?"

    jack "Oh, me and Freddy? We go waaay back."

    jack "We used to work together at the docks - after his boxing career fizzled."

    jack "He went through some rough times. In and out of trouble for a while."

    jack "But he straightened himself out, Freddy did."

    chrome "Good for him. Still, he's a real character, huh?"

    jack "I'll say. He used to get his hands on all these fancy cigarettes."

    jack "European shit, right off the boats. Hand-rolled, clove, you name it!"

    show jack happy

    jack "We used to bag off and take smoke breaks all the time..."

    chrome "Ahh, good times. So, listen..."

    chrome "I hear Bianca's been looking for her old man."

    chrome "Any idea what he's been up to? So's I can pass it along?"

    show jack neutral

    jack "Eh, sure. Lemme, think..."

    jack "..."

    jack "..."

    show jack happy
    
    jack "Oh, yeah! He mentioned something about a gig at the Department Store."

    chrome "Fowler's?"

    show jack neutral

    jack "Yeah, that dump!! Didn't really want to talk about it though. Was about a week ago."

    chrome "That's great! Boy, that's wonderful. I see. Anything else?"

    show jack sad

    jack "Well, would you look at this? My glass is empty."

    return

label scene3_hardboiled:

    show chrome angry

    chrome "Let's cut to the chase. Freddy's missing."

    chrome "And Bianca's real worried. Thinks he might be in danger."

    show jack shocked

    jack "Danger, you say?"

    chrome "Tell me, how do you know Freddy?"

    chrome "And don't leave anything out."

    show jack neutral

    jack "Oh! Me and Freddy? We go waaay back."

    jack "We used to work together at the docks - after his boxing career fizzled."

    jack "He went through some rough times. In and out of trouble for a while."

    jack "But he straightened himself out, Freddy did."

    chrome "Are you sure about that?"

    show jack angry

    jack "I swear on a stack of bibles. I mean... as far as I know."

    show jack neutral

    jack "What I mean to say is... Freddy went dark once before, long time ago."

    show jack sad

    jack "It was real rough for Bianca, and Freddy felt terrible about it."

    show jack angry

    jack "He would never do that to her again, not if he could help it. That's a fact!"

    ######### SCENE 3A: GLITCH 001

    hide jack # hide Jack for glitch
    # show bg bar blur # blurs the background - placeholder until we get asset
    call start_glitch # shows Chrome glitching and grays out the background

    # pause for transition
    pause 1.0

    ### TEXT OF THE GLITCH WILL BE INSERTED HERE 

    show bg bar # unblur the background
    call end_glitch # return to normal Chrome and normal background
    # show Jack again
    show jack neutral at right

    # pause for transition
    pause 1.0

    ######### back to SCENE 3

    # resume music
    play music "audio/AUDIO-2023-12-19-18-56-38.mp3" fadeout 1.0

    $ glitch_counter +=1 # increment glitch counter

    show chrome angry

    chrome "Anything else you leaving out? Spill the beans. All of 'em."

    jack "He used to get his hands on all these fancy cigarettes."

    jack "European shit, right off the boats. Hand-rolled, clove, you name it!"

    show jack happy

    jack "We used to bag off and take smoke breaks all the time..."

    chrome "Okay, that's enough. Focus, man! This is serious."

    chrome "Tell me about the last time you spoke."

    show jack neutral

    jack "Eh, sure. Lemme, think..."

    jack "..."

    jack "..."

    show jack happy

    jack "Oh yeah!! He mentioned something about a gig at the Department Store."

    chrome "Fowler's?"

    show jack neutral

    jack "Yeah, that dump!! Didn't really want to talk about it though. Was about a week ago."

    chrome "I see. Is there {i}{b}anything{/b}{/i} else? Anything at all?"

    show jack sad

    jack "Well, would you look at this? My glass is empty."

    return