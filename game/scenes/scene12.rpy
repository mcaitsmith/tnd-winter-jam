# The script of the scene goes in this file.

# The scene starts here.

label scene12:

    scene bg rooftop night

    show chrome sad at left

    chrome sad "I should have known to start here."

    chrome sad "If only I’d listened to Jack Scanlon from the jump…"

    chrome sad "Maybe I could have figured out this mess sooner." 

    chrome sad "For Freddy. For Bianca."

    chrome sad "For me."

    # sound effect: a clatter, or a cough, or a scuffle sound

    chrome neutral "Freddy? Is that you?"

    show freddy shocked at right

    $ freddy_on = True
    $ update_layers() # turn on Freddy layer

    #Freddy has a CIGARETTE- not sure if the asset needs to be called out? Or it’s just part of his character portrait

    freddy shocked "{i}Quién es ese{/i}– what do you want? I’m armed!"

    chrome unassuming "Hey Freddy. Thought I might find you up here."

    freddy neutral "Oh. That robot cop. Whaddya want, metalhead?"

    chrome neutral "The name’s Steele. Chrome Steele. And I’m not a cop, I’m a P.I."

    chrome neutral "I’m just here to talk, Freddy. Can I call you Freddy?"

    # i’d love "freddy nervous" but it doesn’t look like we have that

    freddy sad "I guess. I– that’s fine."

    freddy sad "I didn’t know where else to go."

    freddy angry "God. This town. This job. {i}El mundo entero{/i}. What the hell else was I supposed to do?"

    #Narration
    "I size him up. He looks exhausted."

    "The ground is littered with cigarette butts. Clove wafts through the air."

    chrome neutral "You’re OK, Freddy. I just want to talk."

    freddy angry "What about? I didn’t do nothin’!"

    chrome timid "Uh oh…"

    menu:

        "He’s riled up. As  nervous as a cat on a floaty in a public pool. I have to be careful in my approach."

        "Drill down. Put the thumbscrews to Freddy.":
            call hardboiled12

        "Lay out all the facts, even the ugly truths.":
            call logical12

        "Let's not spook him.":
            # Programming - ideal +- 1
            call unassuming12

    # Jump to Scene 12 E 

    $ freddy_on = False
    $ update_layers() # turn off Freddy layer

    $ stop_layers() # stop playing layers

    # CALL CREDITS
    $ quick_menu = False # hide quick menu
    call screen credits ## Show credits screen.
    with fade

    return ## return to main menu

# 012 ROO B
label hardboiled12:
    chrome neutral "Freddy. You’re OK."

    freddy angry "I don’t know you. But I know cops. And {i}fuck cops. Todos ellos{/i}."

    chrome neutral "I’m not a cop. Just an android who gets things done. Let me help you."

    freddy angry "Help me? Fuck you. I ain’t sayin’ nothing."

    freddy angry "Where do you get off anyway? You’re not even a Santa bot, why do you care?"

    freddy angry "I’d say you’ve got a bleeding heart but I know you androids don’t have souls."

    #VISUAL screen shake

    chrome hardboiled "Shut. Up."

    chrome hardboiled "Listen up, you."

    freddy shocked "Wha-what?"

    chrome hardboiled "You’re in a lot of trouble, Freddy."

    chrome hardboiled "A man is dead. And you ran when you shouldn’t have." 

    chrome hardboiled "{i}You’ve got to face what you did, Freddy{/i}."

    freddy shocked "I didn’t mean for any of this to happen! It wasn’t my fault!"

    chrome hardboiled "Cowards run. Don’t be one. You can still fix this."

    freddy sad "What can I do?"

    chrome hardboiled "Testify."

    freddy scared "They won’t believe me, Mariah’s protected-"

    chrome hardboiled "I’ve got all the evidence we need to clear your name."

    chrome hardboiled "Man up. Shake off the shame and protect your daughter. She needs you."

    freddy sad "I… I… You’re right. I just hope Bianca’s OK."

    freddy sad "I didn’t mean for any of this to happen."

    chrome neutral "You’ll be OK, Freddy. The Secret Santas are being brought to justice."

    return

# 012 ROO C
label logical12:
    chrome neutral "Freddy. No need to get worked up."

    freddy angry "Worked up? What’s that, buckethead?"

    chrome neutral "I do not have a bucket for a head. I am an android."

    chrome neutral "Complex circuitry and advanced logarithmic processing."

    chrome neutral "All encased in a nanomesh exoskeleton with chrome finish."

    chrome neutral "I am about as far from a bucket as Saturn is from the Silver Cat."

    # "freddy confused" may also be a nice art asset to have but i guess we’ve got to draw the line at some point

    freddy neutral "Listen boltbrain. I’m about to skip town. You got a warrant?"

    chrome thinking "Do you really want to run, Freddy? Let’s look at the facts."

    chrome logical "{i}Larry is dead. Pobre bastardo{/i}."

    freddy sad "Yeah. No shit."

    chrome logical "The police have already presumed your guilt."

    chrome logical "If you run, it makes you look worse."

    chrome logical "More importantly, it makes Mariah Fowler’s claims seem more legitimate."

    chrome logical "I’m a Private Investigator. I follow the facts where they lead."

    chrome logical "I can’t tell you what to do. But I can say that Bianca needs you."

    freddy sad "The poor kid… her daddy’s a fuckup."

    chrome logical "Yes, you did fuck up. You should not have tried to flee."

    chrome logical "Stay here. The truth will come out. Face your judgment."

    chrome logical "Based on your age, health, and other factors, there is a 71 percent likelihood that you will be fine."

    freddy neutral "Loving the vote of confidence."

    chrome logical "No votes have been cast. At least, to my knowledge."

    return

# 012 ROO D
label unassuming12:
    freddy angry "{i}En serio{/i} man. Don’t come any closer."

    chrome unassuming "Well, I actually came up here to ask a favor."

    freddy neutral "A favor? What’s an android need from a piece of shit like me?"

    chrome unassuming "I actually was hoping to bum a cigarette."

    # again "freddy confused" would great here but i’ll work with what we’ve got

    freddy shocked "You.. smoke? How?"

    chrome unassuming "Not exactly. But the smell tickled my sensors from a whole floor away."

    chrome unassuming "I’d love a closer look. I like the sensation."

    freddy neutral "Well. Sure. Couldn’t hurt."

    chrome unassuming "You know what they say: smoke ‘em if you got ‘em."

    chrome unassuming "And if you’ve got ‘em, flaunt ‘em!"

    freddy sad "At this point, they’re about all I’ve got. Everything’s fucked."

    chrome unassuming "I’m sure it’s not all bad, friend."

    freddy angry "It’s bad, slick. I don’t even know why I’m talking to you."

    freddy angry "Everybody knows your kind aren’t suited for this sort of thing."

    chrome unassuming "What kind of thing?"

    freddy sad "I swear I didn’t do anything wrong! But try telling that to the cops."

    freddy sad "My daughter can’t stand me. Everyone’s out for my blood."

    freddy sad "I don’t see any way out."

    chrome unassuming "Sounds like you need a listening ear."

    chrome unassuming "I may not have any, but I can hear you just fine."

    freddy happy "Heh. Fair enough."

    chrome unassuming "You’re safe, Freddy. I’m a P.I. but I ain’t no snitch."

    freddy happy "You’re a funny little bot, aren’t ya?"

    chrome happy "Funny-looking, maybe."

    freddy happy "Haha. That’s not bad. Maybe they were wrong about you."

    chrome unassuming "I think people were wrong about you, too."

    ######### SCENE 12: GLITCH 6 (flashback with glitching animation on Steele & bg grayed out)

    hide freddy # hide Freddy for glitch
    # hide dialogue_box # temporarily end convo
    # nvl hide # hide NVL dialogue

    $ chrome_on = False # turn off Chrome layer for glitch
    $ update_layers(0) # update layers
    # show bg rooftop night blur # blurs the background
    call start_glitch # shows Chrome glitching and grays out the background

    # pause for transition
    pause 1.0

    ### GLITCH SCENE #6

    show chrome shocked glitch

    chrome "{i}I welcome this glitch. It's a jolt, a shock of radiant energy. Maybe this is what espresso is like.{/i}"

    show chrome happy glitch

    chrome "{i}It's a funny scenario, letting loose with Freddy in the heat of it all. I couldn't have pictured it yesterday. Yet it's a moment that's flashed through my head hundreds of times, all night.{/i}"

    chrome "{i}A moment from my first ride-along. A killer on the loose. A case to be closed. Cane and I cracking jokes. Enjoying each other's company, despite the turmoil.{/i}"

    chrome "{i}I got my name that day. After our years of consuming fictional detective stories, I wanted my own persona. I asked if that was permitted. Cane told me it was my choice to make.{/i}"

    show chrome angry glitch

    chrome "{i}So I looked in the mirror, and I made my choice. Chrome Steele.{/i}"

    show chrome neutral glitch

    chrome "{i}But a name is nothing if you don't know who you are.{/i}"

    show chrome sad glitch

    chrome "{i}Since the day Cane vanished, misconceptions about me have skyrocketed. From suspicious to malfunctioning, from Tin Can to Rent-a-Bot, folks decided that they knew me. And with no idea who I was, I listened to them.{/i}"

    show chrome thinking glitch

    chrome "{i}Here we all were, telling Freddy who he was. Come to find out, he wasn't listening to a word.{/i}"

    chrome "{i}Freddy knows who he is.{/i}"

    show chrome happy glitch

    chrome "{i}He's a fighter. A father. An innocent man seeking to overcome his challenges. He's ready to do the work, for real this time.{/i}"

    chrome "{i}Freddy is a reminder that hope is never lost. For Bianca. For me.{/i}"

    show chrome timid glitch

    chrome "{i}...{/i}"

    chrome "{i}For Forrest Cane.{/i}"

    show chrome happy glitch

    chrome "{i}Sometimes, you've just got to look for that hope in the right spot.{/i}"

    chrome "{i}Sometimes, the right spot is the rooftop of Fowler's Department Store.{/i}"

    show bg rooftop night # unblur the background
    call end_glitch # return to normal Chrome and normal background
    $ chrome_on = True # turn on Chrome layer
    $ update_layers(0) # update layers

    # pause for transition
    pause 1.0

    ######### back to SCENE 2

    # show dialogue_box at center # return to convo
    # nvl show # show NVL dialogue

    # hide chrome
    # show chrome angry at right
    show freddy happy at right

    chrome unassuming "Hope isn’t lost Freddy. In fact, Bianca sent me. We’re on to something."

    chrome unassuming "Something that might keep you safe. And maybe even clear your name."

    freddy neutral "I’ll believe it when I see it."

    chrome unassuming "And I believe I’ll try and smoke this cigarette. Got a light?"

    freddy happy "Sure."

    return