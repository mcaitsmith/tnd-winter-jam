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
    jump scene12_e

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

    $ glitch_counter +=1 # increment glitch counter

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

label scene12_e:

    #Here comes Mariah and her backup: Santa1, Mariah, Santa2. In this scene also: steele
    #Mariah + The santa goons appear. They threaten Chrome and Freddy.

    hide freddy
    hide chrome

    #Swap to ADV mode

    show mariah at center
    show santa1 at left
    show santa2 at right

    mariah neutral "Wait up."

    play sound sfx_mariahclap

    $ mariah_on = True
    $ larry_santa_on = True
    $ update_layers() # turn on Mariah/Santa layer

    mariah happy "You've handed yourselves over - and on my property!"

    hide santa1 
    hide santa2

    show mariah at left
    show chrome at center
    
    chrome unassuming "How convenient for you, right?"

    chrome thinking "{i}Two Santa robots. EZMK model. Old, modified, likely holding a criminal record. Hell, I'm getting tired of these guys...{/i}"

    #Swap to NVL mode. Steele and Mariah are getting their showdown now.

    show dialogue_box at center

    hide chrome
    show chrome unassuming at right
    show mariah neutral at left

    chrome_nvl_right "Mariah, so good to see you! And you even brought company. We can finally celebrate the return of your employee. Your lost property!"

    chrome_nvl_right "Too bad he wasn't satisfied with the working conditions."

    chrome_nvl_right "Wasn't today his last day?"

    show mariah angry

    mariah_nvl_left "Beat it. What do you know, rustbucket?"

    show chrome happy

    chrome_nvl_right "I know plenty."

    show chrome unassuming

    chrome_nvl_right "Madam, I'm programmed to take my work very seriously."

    chrome_nvl_right "This murder could have been avoided. I dare say you were willing to accept Freddy's resignation."

    chrome_nvl_right "You both play by the book, save a few bucks and carry on with your lives. Oh, but Freddy wanted to pull a final trick and you caught on."

    show mariah neutral

    mariah_nvl_left "This idiot believes he's a detective. Spit it out."

    chrome_nvl_right "You caught him trying to download incriminating information."

    show mariah angry

    mariah_nvl_left "You're wasting your battery."

    chrome_nvl_right "No, Mariah, I get it! He wanted to tarnish your image. I'd be upset too."

    chrome_nvl_right "As an android, I hear derogatory comments all day. I can empathize."

    show mariah neutral

    mariah_nvl_left "Shut up."

    chrome_nvl_right "No, no, please let it out."

    chrome_nvl_right "Mr Fontaine found something about your sales going down. I understand. Online sales are doing a number on physical retail."

    chrome_nvl_right "And what else? You publicly announce a charity campaign, but what's this? Says here, you diverted all the funds directly into your bank account?"

    mariah_nvl_left "What the fuck are you talking about?"

    show chrome thinking

    #narration
    chrome "{i}Sweat is building up under her neck. She's getting nervous. I might be making things worse. No, I mustn't back down, I gotta double up.{/i}"

    #Dialog

    show chrome happy

    chrome_nvl_right "I've got the evidence triple-secured in my hard drive now."

    mariah_nvl_left "Oh, motherf-"

    show chrome unassuming

    chrome_nvl_right "Just doing my job! Let's not get distracted: I believe you really thought you had a reason for murder."

    chrome_nvl_right "And so, you hoped the cookies would be enough of a peace offering for our man Freddy to swallow."

    chrome_nvl_right "But Freddy was too kind. He gave them to our dear Larry, turning this into a tragedy."

    chrome_nvl_right "And that's not all. You're smart. You needed the cops on your side."

    chrome_nvl_right "It wasn't hard to convince the local fuzz. I've met them; not exactly our city's finest."

    chrome_nvl_right "End, the curtains fall: You pushed all the blame on Freddy. Two birds with one stone? Master plan. Too bad, you did it all in a hurry."

    show mariah angry

    mariah_nvl_left "I swear to God, you talk too much."

    show mariah happy

    mariah_nvl_left "Nice guesses, Steele. I couldn't have completed this without you."

    mariah_nvl_left "Following your scent, I've got the right people in the place I want. My property, as you said, on my turf."

    show mariah angry

    mariah_nvl_left "I'll make things quick and clean this time."

    show mariah neutral

    mariah_nvl_left "But you...you're cunning."

    mariah_nvl_left "My people know ways to make you useful. Heck, I'll be generous. I won't even wipe your memory. At least, at first."

    show mariah happy

    mariah_nvl_left "Imagine: one day you wake with your consciousness trapped in a cash-dispensing machine."

    mariah_nvl_left "You try to move your fingers, and the only thing that happens is that cash comes out of your box-shaped mouth."

    mariah_nvl_left "Wait, what if I put you on my phone? You could be my assistant."

    mariah_nvl_left "We could make it so every time I unlock it, you suffer the equivalent of a plasma torch pressed against your receptors. I could browse you all day long."

    show mariah neutral

    mariah_nvl_left "Once I'm done playing games with you, I'll wipe your memory and boot you up into one of these shitty Santas."

    show mariah happy

    mariah_nvl_left "I can't wait for future you to tell me how it feels."

    mariah_nvl_left "Hell, thank you for leading me here, Detective. Now let's find out why new-gen robots go insane after they 'die' for the first time."

    show mariah neutral

    mariah_nvl_left "Santas - Clean this mess up."

    if glitch_counter >= 5:
        call scene12_f # good ending
    elif glitch_counter >= 3:
        call scene12_g # average ending
    else:
        call scene12_h # bad ending

    $ mariah_on = False
    $ larry_santa_on = False
    $ update_layers() # turn off Mariah/Santa layer

    jump scene13 # jump to next scene

label scene12_f: # good ending

    #swap to ADV mode
    hide dialogue_box # end convo
    nvl clear # clear NVL dialogue

    show chrome thinking

    chrome "Not so fast! Haven't you heard?"

    show mariah angry

    mariah "What now? I've had enough with your Sherlock BS."

    chrome "Use your ears, Ms. Fowler."

    play sound sfx_footsteps

    #narration
    chrome "{i}Only treacherous adrenaline can hide the rubbing of rushed strides against the rooftop.{/i}"

    hide chrome
    hide mariah

    show cop at left

    cop shocked "Mariah Fowler! Stand down!"

    show jack at center

    jack shocked "Freddy! He's alive!"

    show freddy at right

    freddy shocked "Hmph."

    jack happy "Can't believe the tin detective got it right."

    cop neutral "Quiet!"

    hide cop
    hide jack
    hide freddy

    show santa1 at left
    show santa2 at right
    show mariah at center

    mariah neutral "Get me the android. NOW!"

    mariah happy "Heh."

    chrome "{i}That smirk. Crap.{/i}"

    chrome "{i}The robots rush at me. I can hear their circuit boards straining. Their expressions are lifeless, their voiceboxes mute.{/i}"

    chrome "{i}Can't stop to think what she's done to them.{/i}"

    hide santa1
    hide mariah
    hide santa2
    show santa1 at center

    chrome "{i}I can't let them surround me.{/i}"

    chrome "{i}There's not a lot of room to maneuver. I sweep sideways.{/i}"

    hide santa1
    show chrome at center

    chrome angry "Try harder, turkey."

    hide chrome
    show santa1 at center

    chrome angry "{i}A claw shoots ahead, minus the festive glove. Sharp, aged, rusty - the ugly secret behind the fatherly figure.{/i}"

    chrome angry "{i}Iron and 4th Grade Aluminum. 24%% Ferric Oxide. Thickness: 232 nm. Estimated body weight: 78 kilograms.{/i}"

    play sound sfx_impactmetal
    with hpunch

    chrome angry "{i}My fist tears through its frame, like a baseball bat against an old beer can.{/i}"

    chrome angry "{i}EZMK models may be big, but their frame is hollow, and the chassis thin.{/i}"

    hide santa1
    show mariah neutral at center

    chrome angry "{i}Mariah's expression is relaxed. Her eyes are shooting in different directions. Her shoulders are tense.{/i}"

    chrome angry "{i}I have to hurry.{/i}"

    hide mariah
    show chrome shocked at left
    show santa2 at right

    santa2 "KILL!"

    hide mariah
    show freddy at center
    
    freddy happy "Over here, ugly tinfoil beardie."

    play sound sfx_punch
    with hpunch

    freddy angry "I'm not going down without a fight."

    hide freddy
    hide santa2
    show mariah happy at right
    show cop shocked at left

    chrome "{i}I have to stop her.{/i}"

    chrome "{i}The cop is holding a gun in his hands. Standard electric discharge pistol. One round can knock any standard-sized person. Unreliable against androids. Its aiming systems are faulty.{/i}"

    chrome "{i}I rush. She's about to fire.{/i}"

    cop "I said stand-!"

    hide cop
    show jack at left

    jack angry "If you won't stop her, I will!"

    chrome "{i}She draws a pocket repeating pistol. Premium. Chevalier brand. 0.2 seconds are enough for 6 shots in a 75º angle barrage.{/i}"

    chrome "{i}Enough to kill a poser kid and a lousy cop.{/i}"

    show chrome at center

    chrome hardboiled "OUT OF THE WAY, BRAT."

    play sound sfx_gunshots
    with hpunch

    $ chrome_on = False
    $ freddy_on = False
    $ larry_santa_on = False
    $ mariah_on = False
    $ update_layers(1) # temporarily stop bg music

    scene black
    with fade

    hide jack
    hide mariah
    hide chrome

    chrome "{i}Damage sustained. Emergency system shutdown.{/i}"

    chrome "{i}Analyzing...{/i}"

    chrome "{i}Unexpected malformation in lower chassis. Cause: Impact.{/i}"

    chrome "{i}Dorsal motion bionics failure.{/i}"

    chrome "{i}Testing...Plate 3234 failure.{/i}"

    chrome "{i}Troubleshooting critical systems.{/i}"

    chrome "{i}Heart clock online.{/i}"

    chrome "{i}Emergency battery online.{/i}"

    chrome "{i}CORE system rerouted.{/i}"

    chrome "{i}declare damaged hardware redundant{/i}"

    chrome "{i}Disengaging damaged hardware.{/i}"

    chrome "{i}Loading identity origin...success.{/i}"

    chrome "{i}Loading identity hardboiled{/i}"

    chrome "{i}Loading identity unassuming{/i}"

    chrome "{i}Loading identity logical <3{/i}"

    chrome "{i}Sensory systems online.{/i}"

    chrome "{i}Rebooting.{/i}"

    # show jack at center

    scene bg rooftop night
    with fade

    show jack at center

    $ chrome_on = True
    $ freddy_on = True
    $ larry_santa_on = True
    $ mariah_on = True
    $ update_layers(1) # resume bg music

    jack shocked "Dude, you're alive?"

    jack happy "Damn, you saved my bacon!"

    hide jack
    show chrome at center

    chrome sad "What happened."

    hide chrome

    show cop angry at center
    show mariah neutral at right

    mariah angry "The trashpile is still up? Just how much are you for parts?"

    cop angry "FOR THE LOVE OF GOD, SHUT. UP!"

    chrome "{i}About damn time the cop did something useful.{/i}"

    cop angry "Ma'am, you have the right to remain silent."

    mariah angry "You have no idea what you're dealing with. No friggin' idea."

    return

label scene12_g: # average ending

    #swap to ADV mode
    hide dialogue_box # end convo
    nvl clear # clear NVL dialogue

    play sound sfx_footsteps

    hide chrome
    hide mariah

    show cop at left 
    
    cop shocked "Mariah Fowler! Stand down!!"

    show jack at center

    jack shocked "Freddy! He’s alive!"

    show freddy at right

    freddy shocked "Hmph."

    jack happy "Can’t believe the tin detective got it right."

    cop neutral "Quiet!"

    hide cop

    hide jack

    hide freddy

    show santa1 at left

    show santa2 at right

    show mariah at center

    mariah neutral "Get me the android. NOW!"

    mariah happy "Heh."

    #narration
    chrome "{i}...{/i}"

    chrome "{i}The robots rush at me. I can hear their circuit boards straining. Their expressions are lifeless, their voiceboxes mute.{/i}"

    chrome "{i}Can’t stop to think what she’d done to them.{/i}"

    hide santa1
    hide mariah
    hide santa2
    show santa1 at center

    chrome "{i}I can't let them surround me.{/i}"

    chrome "{i}There's not a lot of room to maneuver. I sweep sideways.{/i}"

    hide santa1
    show chrome at center

    chrome angry "What are you waiting for? Hit me!"

    hide chrome
    show santa1 at center

    chrome angry "{i}A claw shoots ahead, minus the festive glove. Sharp, aged, rusty - the ugly secret behind the fatherly figure.{/i}"

    chrome angry "{i}Iron frame. Clear signs of Fe2O3. Also aluminum.{/i}"

    play sound sfx_impactmetal
    with hpunch

    chrome angry "{i}My fist tears through its frame, like a baseball bat against an old beer can.{/i}"

    chrome angry "{i}EZMK models may be big, but their frame is hollow, and the chassis thin.{/i}"

    hide santa1
    show mariah neutral at center

    chrome angry "{i}Mariah's expression is relaxed. Her eyes are shooting in different directions. Her shoulders are tense.{/i}"

    chrome angry "{i}Crap. What is she doing? And what’s the cop waiting for?{/i}"

    hide mariah
    show chrome shocked at left
    show santa2 at right

    santa2 "KILL!"

    hide mariah
    show freddy at center
    
    freddy happy "Over here, ugly tinfoil beardie."

    play sound sfx_punch
    with hpunch

    freddy angry "I'm not going down without a fight."

    hide freddy
    hide santa2
    show mariah happy at right
    show cop shocked at left

    chrome "{i}I have to stop her.{/i}"

    chrome "{i}The cop is holding a gun in his hands. Standard electric discharge pistol. One round can knock any person of standard complexion. Unreliable against androids. Its aiming systems are mishandled.{/i}"

    chrome "{i}I rush. She's about to...{/i}"

    cop "I said stand-!"

    hide cop
    show jack at left

    jack angry "If you won't stop her, I will!"

    chrome "{i}She draws a pocket repeating pistol. Premium. Chevalier brand. 0.2 seconds are enough for 6 shots in a 75º angle barrage.{/i}"

    chrome "{i}Enough to kill a poser kid and a lousy cop.{/i}"

    show chrome at center

    chrome shocked "Duck! Duck!"

    hide jack
    hide chrome

    play sound sfx_gunshots
    with hpunch
    pause 1.0

    hide mariah

    play sound sfx_footsteps
    pause 1.0
    play sound sfx_gunshots

    show chrome at left
    chrome angry "Get to cover, dammit!"

    play sound sfx_gunshots

    #Narration
    chrome "{i}...{/i}"
    play sound sfx_footsteps
    chrome "{i}She escaped.{/i}"

    return

label scene12_h: # bad ending

    #swap to ADV mode
    hide dialogue_box # end convo
    nvl clear # clear NVL dialogue

    play sound sfx_footsteps

    mariah neutral "Wait. What now?"

    chrome "{i}She turns her gaze behind us.{/i}"
    chrome "{i}Dammit. Someone’s coming.{/i}"

    hide chrome
    hide mariah

    show cop at left

    cop shocked "Mariah Fowler! Stand down!"

    show jack at center

    jack shocked "Freddy! He's alive!"

    show freddy at right

    freddy shocked "Hmph."

    jack happy "Can't believe the tin detective got it right."

    cop neutral "Quiet!"

    hide cop
    hide jack
    hide freddy

    show santa1 at left
    show santa2 at right
    show mariah at center

    mariah neutral "Really? Is that all?"

    mariah happy "Get me the android. NOW!"

    chrome "{i}...{/i}"

    chrome "{i}The robots rush at me. I can hear their circuit boards straining. Their expressions are lifeless, their voiceboxes mute.{/i}"

    chrome "{i}What did she do to them?{/i}"

    chrome "{i}It's horrifying.{/i}"

    hide santa1
    hide mariah
    hide santa2
    show santa1 at center

    chrome "{i}I can't let them surround me.{/i}"

    chrome "{i}There's not a lot of room to maneuver. I sweep sideways.{/i}"

    hide santa1
    show chrome at center

    chrome confused "Foul play!"

    hide chrome
    show santa1 at center

    chrome confused "{i}A claw shoots ahead, minus the festive glove. Sharp, aged, rusty - the ugly secret behind the fatherly figure.{/i}"

    chrome confused "{i}Analysing… Dah, no time.{/i}"

    play sound sfx_impactmetal
    with hpunch

    chrome "{i}I took a hit!{/i}"

    chrome "{i}Minor damage.{/i}"

    hide santa1
    show chrome at center
    chrome angry "Sorry, man!"

    hide chrome
    show santa1 at center

    play sound sfx_impactmetal
    with hpunch

    chrome "{i}Huh?{/i}"
    chrome "{i}My fist tears through its frame, like a baseball bat against an old beer can.{/i}"
    chrome "{i}EZMK models may be big… How come they’re so light?{/i}"

    hide santa1
    show mariah neutral at center

    mariah "*Laughter*"

    chrome "{i}Crap. What is she doing? And what’s the cop waiting for?{/i}"

    hide mariah
    show chrome shocked at left
    show santa2 at right

    santa2 "KILL!"

    hide mariah
    show freddy at center
    
    freddy happy "Over here, ugly tinfoil beardie."

    play sound sfx_punch
    with hpunch

    santa2 "..."
    santa2 "KILL."

    freddy angry "Fuck, this is bad."

    hide freddy
    hide santa2
    show mariah happy at right
    show cop shocked at left

    chrome "{i}The cop’s gun is out.{/i}"

    chrome "{i}Has this lousy pisspants ever even held one before?{/i}"

    cop "I said stand-!"

    hide cop
    show jack at left

    jack angry "If you won't stop her, I will!"

    chrome "{i}She draws a pocket repeating pistol. Premium. Chevalier brand. 0.2 seconds are enough for 6 shots in a 75º angle barrage.{/i}"

    chrome "{i}No, no, no.{/i}"

    hide mariah
    hide jack
    show chrome at center

    chrome shocked "WAIT!"

    hide chrome
    show mariah happy at right
    show jack at left

    jack scared "Wh-"

    play sound sfx_gunshots
    with hpunch

    hide jack
    hide mariah
    pause 1.0
    play sound sfx_footsteps

    show cop at center
    cop angry "Freeze, Fowler!"
    cop angry "God."

    show freddy at right
    freddy shocked "Jack!"
    freddy shocked "Come on, get up, buddy"

    chrome "{i}Blood on the ground. He’s grown cold already. His spark… extinguished.{/i}"
    chrome "{i}I don’t have the courage to assess the damage. There’s no heartbeat.{/i}"
    show chrome at left
    chrome neutral "He’s dead."
    freddy sad "Why? Why you...?"

    return