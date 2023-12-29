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

    play sound sfx_door

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

    show dialogue_box at center

    hide chrome
    show chrome neutral at left:
        xzoom -1.0 # make him face right
    show jack neutral at right

    # pause to show jack
    # pause 1.0

    chrome_nvl_left "Can I buy you another drink?"

    show jack happy

    jack_nvl_right "Ahh, beggars can't be choosers, my mama used to say. Rest her soul."

    jack_nvl_right "Jack Scanlon's the name. To whom do I owe this honor?"

    chrome_nvl_left "Chrome. Chrome Steele. I'm a friend of Freddy's - Freddy Fontaine. You know him?"

    jack_nvl_right "Good ol' Freddy. Salt of the earth. His daughter too, um... Bianca! Lovely girl..."

    jack_nvl_right "Fine gin this, ain't it?"

    show jack shocked

    jack_nvl_right "Ahh, I suppose you wouldn't know! Shame..."

    show jack neutral

    jack_nvl_right "Hey, you look like the kind sort. Can I ask for a small loan? Something to get on my feet? I'm good for it..."

    chrome "{i}Jack seemed like the friendly sort. Gregarious. Unfocused. Meandering. His attention wavering like a mercurial jazz riff.{/i}"

    chrome "{i}I'm sure it had nothing to do with synthahol bombarding my aromatic sensors.{/i}"

    # CHOICE

    menu:
        chrome "{i}This guy's all over the place. I have to get him to focus somehow. I have to be careful which tact I choose, so I can get the most info...{/i}"
        "Logical":
            call scene3_logical
        "Unassuming":
            call scene3_unassuming
        "Hardboiled":
            call scene3_hardboiled

    show chrome neutral

    chrome_nvl_left "Thanks for your time, Jack. It's been..."

    # This variable check is just for this one subtle line of dialogue
    if glitch_counter == 1:
        chrome_nvl_left "...interesting."
    elif glitch_counter == 2:
        chrome_nvl_left "...very helpful."

    show jack happy

    jack_nvl_right "Think nothing of it."

    show jack neutral

    jack_nvl_right "Excuse me now Steeley boy, time for a piss and a smoke. I'd ask you to join me, but, y'know..."

    chrome_nvl_left "See you around, Jack."

    hide dialogue_box # end convo
    nvl clear # clear NVL dialogue

    #VISUAL: fade-out. Jack leaves scene.
    hide jack
    with dissolve

    # pause after Jack leaves
    # pause 1.0

    chrome "{i}Seems like Freddy had some secret business at Fowler's Department Store, of all places.{/i}"

    chrome "{i}It's as good a lead as any, I suppose.{/i}"

    chrome "{i}I take a minute to message Bianca that I'm taking the case.{/i}"

    chrome "{i}For now.{/i}"

    # stop music
    stop music fadeout 3.0

    $ start_layers(3) # start playing layers

    # jump to the next scene (skip scene 4)

    jump scene5

label scene3_logical:

    show chrome thinking

    chrome_nvl_left "I'm curious as to the whereabouts of Freddy."

    jack_nvl_right "Oh really, why's that?"

    chrome_nvl_left "According to Bianca, he vanished without a trace."

    show jack happy

    jack_nvl_right "Did you say Bianca? Good kid, right??"

    chrome_nvl_left "Focus, sir! Just tell me how you know Freddy."

    show jack neutral

    jack_nvl_right "Oh, me and Freddy?  We go waaay back."

    jack_nvl_right "We used to work together at the docks - after his boxing career fizzled."

    jack_nvl_right "He went through some rough times. In and out of trouble for a while."

    jack_nvl_right "But he straightened himself out."

    chrome_nvl_left "Is there anything else worth note? Think!"

    jack_nvl_right "He used to get his hands on all these fancy cigarettes."

    jack_nvl_right "European shit, right off the boats. Hand-rolled, clove, you name it!"

    show jack happy

    jack_nvl_right "We used to bag off and take smoke breaks all the time..."

    chrome_nvl_left "Sounds... lovely. Can you tell me anything more recent?"

    chrome_nvl_left "And just the facts!"

    show jack neutral

    jack_nvl_right "Eh, sure. Lemme, think..."

    jack_nvl_right "..."

    jack_nvl_right "..."

    show jack happy

    jack_nvl_right "Oh yeah!! He mentioned something about a gig at the Department Store."

    chrome_nvl_left "Fowler's?"

    show jack neutral

    jack_nvl_right "Yeah, that dump!! Didn't really want to talk about it though. Was about a week ago."

    chrome_nvl_left "I see. Is there {i}{b}anything{/b}{/i} else? Anything you forgot to mention?"

    show jack sad

    jack_nvl_right "Well, would you look at this? My glass is empty."

    return

label scene3_unassuming:

    show chrome timid

    chrome_nvl_left "So, about Freddy. Nice guy, huh?"

    jack_nvl_right "Oh, me and Freddy? We go waaay back."

    jack_nvl_right "We used to work together at the docks - after his boxing career fizzled."

    jack_nvl_right "He went through some rough times. In and out of trouble for a while."

    jack_nvl_right "But he straightened himself out, Freddy did."

    chrome_nvl_left "Good for him. Still, he's a real character, huh?"

    jack_nvl_right "I'll say. He used to get his hands on all these fancy cigarettes."

    jack_nvl_right "European shit, right off the boats. Hand-rolled, clove, you name it!"

    show jack happy

    jack_nvl_right "We used to bag off and take smoke breaks all the time..."

    chrome_nvl_left "Ahh, good times. So, listen..."

    chrome_nvl_left "I hear Bianca's been looking for her old man."

    chrome_nvl_left "Any idea what he's been up to? So's I can pass it along?"

    show jack neutral

    jack_nvl_right "Eh, sure. Lemme, think..."

    jack_nvl_right "..."

    jack_nvl_right "..."

    show jack happy
    
    jack_nvl_right "Oh, yeah! He mentioned something about a gig at the Department Store."

    chrome_nvl_left "Fowler's?"

    show jack neutral

    jack_nvl_right "Yeah, that dump!! Didn't really want to talk about it though. Was about a week ago."

    chrome_nvl_left "That's great! Boy, that's wonderful. I see. Anything else?"

    show jack sad

    jack_nvl_right "Well, would you look at this? My glass is empty."

    return

label scene3_hardboiled:

    show chrome angry

    chrome_nvl_left "Let's cut to the chase. Freddy's missing."

    chrome_nvl_left "And Bianca's real worried. Thinks he might be in danger."

    show jack shocked

    jack_nvl_right "Danger, you say?"

    chrome_nvl_left "Tell me, how do you know Freddy?"

    chrome_nvl_left "And don't leave anything out."

    show jack neutral

    jack_nvl_right "Oh! Me and Freddy? We go waaay back."

    jack_nvl_right "We used to work together at the docks - after his boxing career fizzled."

    jack_nvl_right "He went through some rough times. In and out of trouble for a while."

    jack_nvl_right "But he straightened himself out, Freddy did."

    chrome_nvl_left "Are you sure about that?"

    show jack angry

    jack_nvl_right "I swear on a stack of bibles. I mean... as far as I know."

    show jack neutral

    jack_nvl_right "What I mean to say is... Freddy went dark once before, long time ago."

    show jack sad

    jack_nvl_right "It was real rough for Bianca, and Freddy felt terrible about it."

    show jack angry

    jack_nvl_right "He would never do that to her again, not if he could help it. That's a fact!"

    chrome "{i}Bianca... abandoned - {/i}"

    $ music_pos = renpy.music.get_pos('music') # get current time position of music
    $ music_pos_str = str(music_pos) # convert to string
    # If the user has all options muted, we'll set the current position to 0
    if music_pos == None:
        $ music_pos_str = "0"

    ######### SCENE 3A: GLITCH 001

    hide jack # hide Jack for glitch
    hide dialogue_box # temporarily end convo
    nvl hide # hide NVL dialogue

    # show bg bar blur # blurs the background - placeholder until we get asset
    call start_glitch # shows Chrome glitching and grays out the background

    # pause for transition
    pause 1.0

    show chrome shocked glitch

    chrome "{i}It hits me again. A burning wave of memory, of images and sounds tattooed with situational states of being. Emotions, so to speak. All of them at once, culminating in a big bang and then an oasis of darkness.{/i}"

    chrome "{i}I'd been in the dark for a long while. Cut off from everyone. Sulking in my office or in the Silver Cat. I had become a perpetual friend to morose isolation.{/i}"

    show chrome sad glitch

    chrome "{i}No. I was morose isolation. And I was so deep into it that I had forgotten why I had faced such loneliness in the first place.{/i}"

    chrome "{i}With memories of Forrest Cane returned to me, I could trace my aching emptiness back to his absence. My CPU had been no match for the abridged grief of sudden loss.{/i}"

    chrome "{i}I knew how Bianca felt. Right now, she was telling herself that Freddy may yet come home. I had told myself the same thing, way back when.{/i}"

    show chrome angry glitch

    chrome "{i}Why was this happening!? A malfunction in my hard drive? An error with encryption? The source of these glitches remains a mystery to my self-repair protocol.{/i}"

    show chrome sad glitch

    chrome "{i}Whatever I was facing now, I wouldn't wish it on anyone, much less a sixteen year old girl with rotten luck and a troubled father.{/i}"

    chrome "{i}I can't say that looking for Freddy would make any difference. I've walked that road before and it held no solace.{/i}"

    chrome "{i}But for Bianca, a young girl still bargaining with her loss, I can't say it wouldn't make all the difference in the world.{/i}"

    show bg bar # unblur the background
    call end_glitch # return to normal Chrome and normal background
    $ stop_layers() # stop playing layers (since layers start in end_glitch)

    # pause for transition
    pause 1.0

    ######### back to SCENE 3

    # resume music
    play music "<from " + music_pos_str + ">audio/AUDIO-2023-12-19-18-56-38.mp3" fadeout 1.0

    $ glitch_counter +=1 # increment glitch counter

    show dialogue_box at center # return to convo
    nvl show # show NVL dialogue

    hide chrome
    show chrome angry at left:
        xzoom -1.0 # make him face right
    show jack neutral at right

    chrome_nvl_left "..."

    chrome_nvl_left "Anything else you leaving out? Spill the beans. All of 'em."

    jack_nvl_right "He used to get his hands on all these fancy cigarettes."

    jack_nvl_right "European shit, right off the boats. Hand-rolled, clove, you name it!"

    show jack happy

    jack_nvl_right "We used to bag off and take smoke breaks all the time..."

    chrome_nvl_left "Okay, that's enough. Focus, man! This is serious."

    chrome_nvl_left "Tell me about the last time you spoke."

    show jack neutral

    jack_nvl_right "Eh, sure. Lemme, think..."

    jack_nvl_right "..."

    jack_nvl_right "..."

    show jack happy

    jack_nvl_right "Oh yeah!! He mentioned something about a gig at the Department Store."

    chrome_nvl_left "Fowler's?"

    show jack neutral

    jack_nvl_right "Yeah, that dump!! Didn't really want to talk about it though. Was about a week ago."

    chrome_nvl_left "I see. Is there {i}{b}anything{/b}{/i} else? Anything at all?"

    show jack sad

    jack_nvl_right "Well, would you look at this? My glass is empty."

    return