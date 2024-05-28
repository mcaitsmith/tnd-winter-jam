# The script of the scene goes in this file.

### SCENE 12: ROOFTOP

# The scene starts here.

label scene12:

    scene bg rooftop night with fade

    show chrome sad at left:
        xzoom -1.0
    with moveinleft

    chrome sad "{i}I feel like I should have pieced things together sooner.{/i}"

    chrome sad "{i}Nobody expects the suspect to be hiding in plain sight...{/i}"

    chrome sad "{i}...but where else than the roof would you find Santa?{/i}" 

    play sound sfx_impactmetal volume 0.5

    pause 1.0

    chrome neutral "Freddy? Is that you?"

    show freddy shocked at right with moveinright

    $ freddy_on = True
    $ update_layers() # turn on Freddy layer

    show dialogue_box
    nvl show 

    #Freddy has a CIGARETTE- not sure if the asset needs to be called out? Or it’s just part of his character portrait

    freddy_nvl_right shocked "{i}Quién es ese{/i} – what do you want? I’m armed!"

    chrome_nvl_left unassuming "Hey Freddy. Thought I might find you up here."

    freddy_nvl_right neutral "Wait - a robot cop?! Of all things..."

    freddy_nvl_right angry "Whaddya want, metalhead?"

    chrome_nvl_left neutral "The name’s Steele. Chrome Steele. And I’m not a cop, I’m a P.I."

    chrome_nvl_left neutral "I’m just here to talk, Freddy. Can I call you Freddy?"

    # i’d love "freddy nervous" but it doesn’t look like we have that

    freddy_nvl_right sad "I guess. I– that’s fine."

    freddy_nvl_right sad "I didn’t know where else to go."

    freddy_nvl_right angry "God. This town. This job. {i}El mundo entero{/i}."

    freddy_nvl_right angry "One second I was telling Larry I was out - no more scams - the next he was coughing up blood! What the hell else was I supposed to do?"

    hide dialogue_box

    #Narration
    chrome "{i}I size him up. He looks exhausted.{/i}"

    chrome "{i}The ground is littered with cigarette butts. Clove wafts through the air.{/i}"

    show dialogue_box at center

    chrome_nvl_left neutral "You’re OK, Freddy. I just want to talk."

    freddy_nvl_right angry "What about? I didn’t do nothin’!"

    freddy_nvl_right angry "Fuck, what am I doing? I got two rules..."

    freddy_nvl_right angry "Don't talk to cops, and don't talk to bots! And right now, I'm breaking both!"

    hide dialogue_box

    chrome "{i}Uh oh…{/i}"

    menu:

        chrome "{i}He’s riled up. On his last nerve. And clearly I make him uncomfortable. I have to be careful in my approach...{/i}"

        "Logical":
            call logical12 from _call_logical12

        "Unassuming":
            # Programming - ideal +- 1
            call unassuming12 from _call_unassuming12

        "Hardboiled":
            call hardboiled12 from _call_hardboiled12

    # Jump to Scene 12 E 
    jump scene12_e

# 012 ROO B
label hardboiled12:

    show dialogue_box at center
    chrome_nvl_left neutral "Freddy. You’re OK."

    freddy_nvl_right angry "I don’t know you. But I know cops. And {i}fuck cops. Todos ellos{/i}."

    chrome_nvl_left neutral "I’m not a cop. Just an android who gets things done. Let me help you."

    freddy_nvl_right angry "Help me? Fuck you. I ain’t sayin’ nothing."

    freddy_nvl_right angry "Where do you get off anyway? You’re not even a Santa bot, why do you care?"

    freddy_nvl_right angry "I’d say you’ve got a bleeding heart but I know you androids don’t have souls."

    show bg rooftop night with hpunch

    chrome_nvl_left hardboiled "Shut. Up."

    chrome_nvl_left hardboiled "Listen up, you."

    freddy_nvl_right shocked "Wha-what?"

    chrome_nvl_left hardboiled "You’re in a lot of trouble, Freddy."

    chrome_nvl_left hardboiled "A man is dead. And you ran when you shouldn’t have." 

    chrome_nvl_left hardboiled "{i}You’ve got to face what you did, Freddy{/i}."

    freddy_nvl_right shocked "I didn’t mean for any of this to happen! It wasn’t my fault!"

    chrome_nvl_left hardboiled "Cowards run. Don’t be one. You can still fix this."

    freddy_nvl_right sad "What can I do?"

    chrome_nvl_left hardboiled "Testify."

    freddy_nvl_right sad "They won’t believe me, Mariah’s protected -"

    chrome_nvl_left hardboiled "I’ve got all the evidence we need to clear your name."

    chrome_nvl_left hardboiled "Man up. Shake off the shame and protect your daughter. She needs you."

    freddy_nvl_right sad "I… I… You’re right. I just hope Bianca’s OK."

    freddy_nvl_right sad "I didn’t mean for any of this to happen."

    chrome_nvl_left hardboiled "You’ll be OK, Freddy. The Secret Santas are being brought to justice."

    return

# 012 ROO C
label logical12:
    show dialogue_box at center
    chrome_nvl_left neutral "Freddy. No need to get worked up."

    freddy_nvl_right angry "Worked up? What’s that, buckethead?"

    chrome_nvl_left neutral "I do not have a bucket for a head. I am an android."

    chrome_nvl_left neutral "Complex circuitry and advanced logarithmic processing."

    chrome_nvl_left neutral "All encased in a nanomesh exoskeleton with chrome finish."

    chrome_nvl_left neutral "I am about as far from a bucket as Saturn is from the Silver Cat."

    # "freddy confused" may also be a nice art asset to have but i guess we’ve got to draw the line at some point

    freddy_nvl_right neutral "Listen boltbrain. I’m about to skip town. You got a warrant?"

    chrome_nvl_left thinking left "Do you really want to run, Freddy? Let’s look at the facts."

    chrome_nvl_left logical "Larry is dead. Poor bastard."

    freddy_nvl_right sad "Yeah. No shit."

    chrome_nvl_left logical "The police have already presumed your guilt."

    chrome_nvl_left logical "If you run, it makes you look worse."

    chrome_nvl_left logical "More importantly, it makes Mariah Fowler’s claims seem more legitimate."

    chrome_nvl_left logical "I’m a Private Investigator. I follow the facts where they lead."

    chrome_nvl_left logical "I can’t tell you what to do. But I can say that Bianca needs you."

    freddy_nvl_right sad "The poor kid… her daddy’s a fuckup."

    chrome_nvl_left logical "Yes, you did fuck up. You should not have tried to flee."

    chrome_nvl_left logical "Stay here. The truth will come out. Face your judgment."

    chrome_nvl_left logical "Based on your age, health, and other factors, there is a 71 percent likelihood that you will be fine."

    freddy_nvl_right neutral "Loving the vote of confidence."

    chrome_nvl_left logical "No votes have been cast. At least, to my knowledge."

    return

# 012 ROO D
label unassuming12:
    show dialogue_box at center
    freddy_nvl_right angry "{i}En serio{/i} man. Don’t come any closer."

    chrome_nvl_left unassuming "Well, I actually came up here to ask a favor."

    freddy_nvl_right neutral "A favor? What’s an android need from a piece of shit like me?"

    chrome_nvl_left unassuming "I actually was hoping to bum a cigarette."

    # again "freddy confused" would great here but i’ll work with what we’ve got

    freddy_nvl_right shocked "You... smoke? How?"

    chrome_nvl_left unassuming "Not exactly. But the smell tickled my sensors from a whole floor away."

    chrome_nvl_left unassuming "I’d love a closer look. I like the sensation."

    freddy_nvl_right neutral "Well. Sure. Couldn’t hurt."

    chrome_nvl_left unassuming "You know what they say: smoke ‘em if you got ‘em."

    chrome_nvl_left unassuming "And if you’ve got ‘em, flaunt ‘em!"

    freddy_nvl_right sad "At this point, they’re about all I’ve got. Everything’s fucked."

    chrome_nvl_left unassuming "I’m sure it’s not all bad, friend."

    freddy_nvl_right angry "It’s bad, slick. I don’t even know why I’m talking to you."

    freddy_nvl_right angry "Everybody knows your kind aren’t suited for this sort of thing."

    chrome_nvl_left unassuming "What sort of thing?"

    freddy_nvl_right sad "I swear I didn’t do anything wrong! But try telling that to the cops."

    freddy_nvl_right sad "My daughter can’t stand me. Everyone’s out for my blood."

    freddy_nvl_right sad "I don’t see any way out."

    chrome_nvl_left unassuming "Sounds like you need someone to lend you an ear."

    chrome_nvl_left unassuming "I may not have any, but I can hear you just fine."

    freddy_nvl_right happy "Heh. Fair enough."

    chrome_nvl_left unassuming "You’re safe, Freddy. I’m a P.I. but I ain’t no snitch."

    freddy_nvl_right happy "You’re a funny little bot, aren’t ya?"

    chrome_nvl_left happy "Funny-looking, maybe."

    freddy_nvl_right happy "Haha. That’s not bad. Maybe they were wrong about you."

    chrome_nvl_left unassuming "I think people were wrong about you, too -"

    ######### SCENE 12: GLITCH 6 (flashback with glitching animation on Steele & bg grayed out)

    # hide freddy # hide Freddy for glitch
    # hide dialogue_box # temporarily end convo
    # nvl hide # hide NVL dialogue

    $ chrome_on = False # turn off Chrome layer for glitch
    $ update_layers(0) # update layers

    call start_glitch from _call_start_glitch_1 # shows Chrome glitching and grays out the background
    

    # pause for transition

    ### GLITCH SCENE #6

    show chrome shocked glitch at left:
        xzoom -1.0

    pause 1.0

    chrome "{i}I welcome this glitch. It's a jolt, a shock of radiant energy. Maybe this is what espresso is like.{/i}"

    show chrome happy glitch

    chrome "{i}It's a funny scenario, chatting it up with Freddy in the heat of it all. I couldn't have pictured it yesterday. Yet it's a moment that's flashed through my head hundreds of times, all night.{/i}"

    chrome "{i}A moment from my first ride-along. A killer on the loose. A case to be closed. Cane and I cracking jokes. Enjoying each other's company, despite the turmoil.{/i}"

    chrome "{i}I got my name that day. After our years of consuming fictional detective stories, I wanted my own persona. I asked if that was permitted. Cane told me it was my choice to make.{/i}"

    show chrome angry glitch

    chrome "{i}So I looked in the mirror, and I made my choice. Chrome Steele.{/i}"

    show chrome neutral glitch

    chrome "{i}But a name is nothing if you don't know who you are.{/i}"

    show chrome sad glitch

    chrome "{i}Since the day Cane vanished, misconceptions about me have skyrocketed. From suspicious to malfunctioning. Tin Can. Rent-a-Bot. Metalhead.{/i}"

    chrome "{i}Folks decided that they knew me. And with no idea who I was, I listened to them.{/i}"

    show chrome thinking left glitch

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

    scene bg rooftop night with pixellate # unblur the background
    call end_glitch from _call_end_glitch_1 # return to normal Chrome and normal background
    $ chrome_on = True # turn on Chrome layer
    $ update_layers(0) # update layers

    $ glitch_counter +=1 # increment glitch counter

    # pause for transition

    ######### back to SCENE 2

    # hide chrome
    show chrome unassuming at left:
        xzoom -1.0
    show freddy happy at right
    with dissolve

    show dialogue_box at center # return to convo
    nvl show # show NVL dialogue

    chrome_nvl_left unassuming "Hope isn’t lost Freddy. In fact, Bianca sent me. We’re on to something."

    chrome_nvl_left unassuming "Something that might keep you safe. And maybe even clear your name."

    freddy_nvl_right neutral "I’ll believe it when I see it."

    chrome_nvl_left unassuming "And I believe I’ll try and smoke this cigarette. Got a light?"

    freddy_nvl_right happy "Sure."

    return

label scene12_e:

    show chrome neutral

    freddy_nvl_right neutral "*sigh* {i}Ay no me digas{/i}, just when I thought I could leave all of this behind me."

    freddy_nvl_right neutral "Can you believe I put in my resignation just a few days ago?"

    freddy_nvl_right neutral "Right before this all went down, I went up to Fowler's office and told her I was done."

    freddy_nvl_right neutral "Feels like a lifetime ago."

    #Here comes Mariah and her backup: Santa1, Mariah, Santa2. In this scene also: steele
    #Mariah + The santa goons appear. They threaten Chrome and Freddy.

    hide dialogue_box
    nvl clear

    hide freddy with moveoutleft
    hide chrome
    show chrome neutral at left
    pause 0.2
    hide chrome with moveoutleft

    #Swap to ADV mode

    show mariah neutral at center
    show santa1 at left
    show santa2 at right 
    with moveinright

    mariah neutral "Wait up."

    play sound sfx_mariahclap

    $ mariah_on = True
    $ larry_santa_on = True
    $ update_layers() # turn on Mariah/Santa layer

    mariah happy "You've handed yourselves over - and on my property!"

    hide santa1
    hide santa2 
    with dissolve

    show mariah at right with moveoutright
    show chrome neutral at left:
        xzoom -1.0 
    with moveinleft

    nvl clear
    show dialogue_box at center
    
    chrome_nvl_left unassuming "How convenient for you, right?"

    hide dialogue_box

    show chrome thinking left at left

    chrome "{i}Two Santa robots. The old EZMK model, like the one down on the street. But it seems that these two have gotten Mariah’s ‘upgrade’ - a hostile bodyguard protocol.{/i}"

    #Swap to NVL mode. Steele and Mariah are getting their showdown now.

    show dialogue_box at center

    show chrome unassuming at left:
        xzoom -1.0
    show mariah neutral at right

    chrome_nvl_left "Mariah, so good to see you! And you even brought company. We can finally celebrate the return of your employee. Your lost property!"

    chrome_nvl_left "Too bad he wasn't satisfied with the working conditions."

    chrome_nvl_left "Wasn't today his last day?"

    show mariah angry

    mariah_nvl_right "Beat it. What do you know, rustbucket?"

    show chrome happy

    chrome_nvl_left "I know plenty."

    show chrome logical

    chrome_nvl_left "Madam, I'm programmed to take my work very seriously."

    chrome_nvl_left "This murder could have been avoided."

    chrome_nvl_left "I dare say you were willing to accept Freddy's resignation."

    chrome_nvl_left "You both play by the book, save a few bucks and carry on with your lives."

    chrome_nvl_left "Oh, but Freddy wanted to pull a final trick and you caught on."

    show mariah neutral

    mariah_nvl_right "This idiot believes he's a detective. Spit it out."

    show chrome hardboiled

    chrome_nvl_left "You caught him trying to download incriminating information."

    show mariah angry

    mariah_nvl_right "You're wasting your battery."

    chrome_nvl_left "No, Mariah, I get it!"

    chrome_nvl_left "He wanted to tarnish your image. I'd be upset too."

    chrome_nvl_left "As an android, I hear derogatory comments all day. I can empathize."

    show mariah neutral

    mariah_nvl_right "Shut up."

    chrome_nvl_left "No, no, please let it out."

    show chrome logical

    chrome_nvl_left "Mr. Fontaine found a discrepancy in your sales."

    chrome_nvl_left "I understand; physical retail isn't what it used to be."

    chrome_nvl_left "Freddy dug a little too deep. He found out that the proceeds from your little charity campaign were going right into your pockets."

    mariah_nvl_right "What the fuck are you talking about?"

    show chrome thinking left

    hide dialogue_box

    #narration
    chrome "{i}Sweat is building up under her neck. She's getting nervous. I might be making things worse. No, I mustn't back down, I gotta double up.{/i}"

    show dialogue_box
    #Dialog

    show chrome happy

    chrome_nvl_left "I've got the evidence triple-secured in my hard drive now."

    mariah_nvl_right "Oh, motherf-"

    show chrome unassuming

    chrome_nvl_left "Just doing my job!"

    chrome_nvl_left "But let's not get distracted: I believe you really thought you had a reason for murder."

    chrome_nvl_left "And so, you made some special cookies for Freddy as a little... going away present."

    chrome_nvl_left "But I guess Freddy doesn't have much of a sweet tooth."

    chrome_nvl_left "He gave them to our dear Larry, turning this into a tragedy."

    chrome_nvl_left "And that's not all."

    chrome_nvl_left "You're smart. You needed the cops on your side."

    chrome_nvl_left "It wasn't hard to point the local fuzz towards Freddy. I've met them; not exactly our city's finest."

    chrome_nvl_left "And at this time of year? Any excuse to sweep something like this under the rug."

    chrome_nvl_left "End, the curtains fall: You pushed all the blame on Freddy."

    chrome_nvl_left "Two birds with one stone? Quite the master plan."

    chrome_nvl_left "Too bad you did it all in a hurry."

    show mariah angry

    mariah_nvl_right "I swear to God, you talk too much."

    show mariah happy

    mariah_nvl_right "Nice guesses, Steele. I couldn't have completed this without you."

    show chrome neutral

    mariah_nvl_right "Following your scent, I've got the right people in the place I want. My property, as you said, on my turf."

    show mariah angry

    mariah_nvl_right "As for my secret Santa here, I'll make things quick and clean this time."

    show mariah neutral

    mariah_nvl_right "But you... you're cunning."

    mariah_nvl_right "My people know ways to make you useful."

    mariah_nvl_right "Heck, I'll be generous. I won't even wipe your memory."

    mariah_nvl_right "At least, at first."

    show mariah happy

    mariah_nvl_right "Imagine: one day you wake with your consciousness trapped in a cash-dispensing machine."

    mariah_nvl_right "You try to move your fingers, and the only thing that happens is that cash comes out of your box-shaped mouth."

    mariah_nvl_right "Wait, what if I put you on my phone?"

    mariah_nvl_right "You could be my assistant."

    mariah_nvl_right "We could make it so every time I unlock it, you suffer the equivalent of a plasma torch pressed against your receptors."

    mariah_nvl_right "I could browse you all day long."

    show mariah neutral

    mariah_nvl_right "Once I'm done playing games with you, I'll wipe your memory and boot you up into one of these shitty Santas."

    show mariah happy

    mariah_nvl_right "I can't wait for future you to tell me how it feels."

    mariah_nvl_right "Thank you for leading me here, Detective."

    mariah_nvl_right "You've tied up all my loose ends with a pretty bow."

    show mariah neutral

    mariah_nvl_right "Santas - Clean this mess up."

    show chrome shocked

    if glitch_counter >= 6:
        call scene12_f from _call_scene12_f # good ending
    elif glitch_counter >= 3:
        call scene12_g from _call_scene12_g # average ending
    else:
        call scene12_h from _call_scene12_h # bad ending

    $ mariah_on = False
    $ larry_santa_on = False
    $ bianca_on = False
    $ freddy_on = False
    $ update_layers() # turn off Mariah/Santa layer

    $ stop_layers(1) # pause temporarily

    jump scene13 # jump to next scene

label scene12_f: # good ending

    show chrome thinking left

    chrome_nvl_left "Not so fast! Haven't you heard?"

    show mariah angry

    mariah_nvl_right "What now? I've had enough with your Sherlock BS."

    chrome_nvl_left "Use your ears, Ms. Fowler. Seems the cavalry has arrived."

    play sound sfx_footsteps

    #swap to ADV mode
    hide dialogue_box # end convo
    nvl clear # clear NVL dialogue

    hide chrome
    hide mariah
    with dissolve

    show cop shocked at center with moveinright

    cop shocked "Mariah Fowler! Stand down!"

    show jack shocked at right with moveinright

    jack shocked "Freddy! He's alive!"

    show freddy shocked at left:
        xzoom -1.0
    with moveinleft

    $ bianca_on = True
    $ update_layers() # now all 5 are playing

    freddy shocked "Jack!"

    jack happy "Can't believe the tin detective got it right."

    cop neutral "Quiet!"

    scene bg rooftop night with dissolve

    show santa1 at left
    show santa2 at right
    show mariah neutral at center
    with dissolve

    mariah neutral "Get me the android. NOW!"

    mariah happy "Heh."

    chrome "{i}That smirk. Crap.{/i}"

    chrome "{i}The robots rush at me. I can hear their circuit boards straining. Their expressions are lifeless, their movements rigid.{/i}"

    chrome "{i}Can't stop to think what she's done to them.{/i}"

    hide santa1
    hide mariah
    hide santa2
    with dissolve

    show santa1 at center with dissolve

    chrome "{i}I can't let them surround me.{/i}"

    chrome "{i}There's not a lot of room to maneuver. I sweep sideways.{/i}"

    hide santa1 with dissolve
    show chrome neutral at center with dissolve

    chrome angry "Try harder, turkey."

    hide chrome with dissolve
    show santa1 at center with dissolve

    chrome angry "{i}A claw shoots ahead, minus the festive glove. Sharp-edged, rusty - the ugly secret behind the fatherly figure.{/i}"

    chrome angry "{i}Iron and 4th Grade Aluminum. 24%% Ferric Oxide. Thickness: 232 nm. Estimated body weight: 78 kilograms.{/i}"

    play sound sfx_impactmetal
    with hpunch

    chrome angry "{i}My fist tears through its frame, like a baseball bat against an old beer can.{/i}"

    chrome angry "{i}EZMK models may be big, but their frame is hollow, and the chassis thin.{/i}"

    hide santa1 with dissolve
    show mariah neutral at center with dissolve

    chrome angry "{i}Mariah's expression is relaxed. Her eyes are shooting in different directions. Her shoulders are tense.{/i}"

    chrome angry "{i}I have to hurry.{/i}"

    hide mariah with dissolve
    show chrome shocked at left:
        xzoom -1.0
    show santa2 at right
    with dissolve

    santa2 "KILL!"

    show freddy happy at center:
        xzoom -1.0
    with moveinleft
    
    freddy happy "Over here, ugly tinfoil beardie. Eat some fist!"

    play sound sfx_punch
    with hpunch

    freddy angry "I'm not going down without a fight."
    scene bg rooftop night with dissolve

    show mariah happy at right
    show cop shocked at left
    with dissolve

    hide freddy
    hide santa2
    show mariah happy at right
    show cop shocked at left

    chrome "{i}I have to stop her.{/i}"

    chrome "{i}The cop’s gun is out, but he doesn't look too sure of himself.{/i}"

    chrome "{i}Has this lousy pisspants ever even held one before?{/i}"

    cop "I said stand -!"

    hide cop
    show jack angry at left:
        xzoom -1.0
    with moveinleft

    jack angry "If you won't stop her, I will!"

    chrome "{i}She draws a pocket repeating pistol. Premium. Chevalier brand. 0.2 seconds are enough for 6 shots in a 75º angle barrage.{/i}"

    chrome "{i}More than enough to kill a functioning alcoholic and a lousy cop.{/i}"

    chrome "{i}I can't let that happen.{/i}"

    show chrome angry at center:
        xzoom -1.0 
    with moveinleft

    chrome hardboiled "OUT OF THE WAY, JACK!"

    play sound sfx_gunshots
    with hpunch

    $ chrome_on = False
    $ freddy_on = False
    $ larry_santa_on = False
    $ mariah_on = False
    $ bianca_on = False
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

    chrome "{i}Declare damaged hardware redundant{/i}"

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

    show jack shocked at center

    $ chrome_on = True
    $ freddy_on = True
    $ larry_santa_on = True
    $ mariah_on = True
    $ bianca_on = True
    $ update_layers(1) # resume bg music

    jack shocked "Good God, you're alive?"

    jack happy "Damn, you saved my bacon!"

    hide jack
    show chrome neutral at center

    chrome sad "What happened..."

    hide chrome

    show cop angry at center
    show mariah neutral at right
    with dissolve

    mariah angry "The tin can is still up? What the hell they make you out of?"

    show cop angry at center:
            xzoom -1.0

    cop angry "FOR THE LOVE OF GOD, SHUT. UP!"

    chrome "{i}About damn time the cop did something useful.{/i}"

    cop angry "Ma'am, you have the right to remain silent."

    mariah angry "You have no idea what you're dealing with. Don't you know who I am?!"

    hide cop
    hide mariah
    with dissolve

    show chrome neutral at center with moveinleft

    chrome "{i}By tomorrow everyone will know who Mariah is. A crook. And a murderer.{/i}"

    chrome "{i}My job here is done. Time to get Freddy to safety.{/i}"

    chrome "{i}I know someone who'll be glad to see him.{/i}"

    return

label scene12_g: # average ending

    show chrome thinking left

    chrome_nvl_left "Not so fast! Haven't you heard?"

    show mariah angry

    mariah_nvl_right "What now? I've had enough with your Sherlock BS."

    chrome_nvl_left "Use your ears, Ms. Fowler. Seems the cavalry has arrived."

    play sound sfx_footsteps

    #swap to ADV mode
    hide dialogue_box # end convo
    nvl clear # clear NVL dialogue

    hide chrome
    hide mariah
    with dissolve

    show cop shocked at center with moveinright

    cop shocked "Mariah Fowler! Stand down!"

    show jack shocked at right with moveinright

    jack shocked "Freddy! He's alive!"

    show freddy shocked at left:
        xzoom -1.0
    with moveinleft

    freddy shocked "Jack!"

    jack happy "Can't believe the tin detective got it right."

    cop neutral "Quiet!"

    scene bg rooftop night with dissolve

    show santa1 at left
    show santa2 at right
    show mariah neutral at center
    with dissolve

    mariah neutral "Get me the android. NOW!"

    mariah happy "Heh."

    #narration
    chrome "{i}...{/i}"

    chrome "{i}The robots rush at me. I can hear their circuit boards straining. Their expressions are lifeless, their movements rigid.{/i}"

    chrome "{i}Can’t stop to think what she’d done to them.{/i}"

    hide santa1
    hide mariah
    hide santa2
    show santa1 at center

    chrome "{i}I can't let them surround me.{/i}"

    chrome "{i}There's not a lot of room to maneuver. I sweep sideways.{/i}"

    hide santa1
    show chrome neutral at center

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
    show chrome shocked at left:
        xzoom -1.0
    show santa2 at right

    santa2 "KILL!"

    hide mariah
    show freddy happy at center:
        xzoom -1.0
    with moveinleft

    
    freddy happy "Over here, ugly tinfoil beardie. Eat some fist!"

    play sound sfx_punch
    with hpunch

    freddy angry "I'm not going down without a fight."

    scene bg rooftop night with dissolve

    show mariah happy at right
    show cop shocked at left
    with dissolve

    chrome "{i}I have to stop her.{/i}"

    chrome "{i}The cop’s gun is out, but he doesn't look too sure of himself.{/i}"

    chrome "{i}Has this lousy pisspants ever even held one before?{/i}"

    cop "I said stand -!"

    hide cop
    show jack angry at left:
        xzoom -1.0
    with moveinleft

    jack angry "If you won't stop her, I will!"

    chrome "{i}She draws a pocket repeating pistol. Premium. Chevalier brand. 0.2 seconds are enough for 6 shots in a 75º angle barrage.{/i}"

    chrome "{i}More than enough to kill a functioning alcoholic and a lousy cop.{/i}"

    chrome "{i}I can't let that happen.{/i}"

    show chrome shocked at center with moveinleft

    chrome shocked "Duck! Duck!"

    hide jack
    hide chrome

    play sound sfx_gunshots
    with hpunch
    pause 1.0

    hide mariah with moveoutright

    play sound sfx_footsteps
    pause 1.0
    play sound sfx_gunshots

    show chrome neutral at left
    chrome angry "Get to cover, damn it!"

    play sound sfx_gunshots
    show chrome angry:
            xzoom -1.0

    #Narration
    chrome "{i}...{/i}"

    play sound sfx_footsteps

    chrome "{i}In all the commotion, Mariah escaped.{/i}"

    chrome "{i}The cops can deal with her. There's more than enough evidence to put her away when they do.{/i}"

    chrome "{i}My job here is done. Time to get Freddy to safety.{/i}"

    chrome "{i}I know someone who'll be glad to see him.{/i}"

    return

label scene12_h: # bad ending

    show chrome thinking left

    chrome_nvl_left "Not so fast! Haven't you heard?"

    show mariah angry

    mariah_nvl_right "What now? I've had enough with your Sherlock BS."

    chrome_nvl_left "Use your ears, Ms. Fowler. Seems the cavalry has arrived."

    play sound sfx_footsteps

    #swap to ADV mode
    hide dialogue_box # end convo
    nvl clear # clear NVL dialogue

    hide chrome
    hide mariah
    with dissolve

    show cop shocked at center with moveinright

    cop shocked "Mariah Fowler! Stand down!"

    show jack shocked at right with moveinright

    jack shocked "Freddy! He's alive!"

    show freddy shocked at left:
        xzoom -1.0
    with moveinleft

    freddy shocked "Jack!"

    jack happy "Can't believe the tin detective got it right."

    cop neutral "Quiet!"

    scene bg rooftop night with dissolve

    show santa1 at left
    show santa2 at right
    show mariah neutral at center
    with dissolve

    mariah neutral "Really? Is that all?"

    mariah happy "Get me the android. NOW!"

    chrome "{i}...{/i}"

    show bg rooftop night with hpunch

    chrome "{i}The robots rush at me. I can hear their circuit boards straining. Their expressions are lifeless, their movements rigid.{/i}"

    chrome "{i}What did she do to them?{/i}"

    chrome "{i}It's horrifying.{/i}"

    hide santa1
    hide mariah
    hide santa2
    with dissolve
    show santa1 at center

    chrome "{i}I can't let them surround me.{/i}"

    chrome "{i}There's not a lot of room to maneuver. I sweep sideways.{/i}"

    hide santa1 with dissolve
    show chrome confused at center with dissolve

    chrome confused "Foul play!"

    hide chrome
    show santa1 at center

    chrome confused "{i}A claw shoots ahead, minus the festive glove. Sharp, aged, rusty - the ugly secret behind the fatherly figure.{/i}"

    chrome confused "{i}Analyzing… Dah, no time.{/i}"

    play sound sfx_impactmetal
    with hpunch

    chrome "{i}I took a hit!{/i}"

    chrome "{i}Minor damage.{/i}"

    hide santa1
    show chrome neutral at center
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
    show chrome shocked at left:
        xzoom -1.0
    show santa2 at right

    santa2 "KILL!"

    hide mariah
    show freddy happy at center:
        xzoom -1.0
    with moveinleft
    
    freddy happy "Over here, ugly tinfoil beardie. Eat some fist!"

    play sound sfx_punch
    with hpunch

    santa2 "..."
    santa2 "KILL."

    freddy angry "Fuck, this is bad."
    scene bg rooftop night with dissolve

    show mariah happy at right
    show cop shocked at left
    with dissolve

    chrome "{i}The cop’s gun is out, but he doesn't look too sure of himself.{/i}"

    chrome "{i}Has this lousy pisspants ever even held one before?{/i}"

    cop "I said stand -!"

    hide cop
    show jack angry at left:
        xzoom -1.0
    with moveinleft

    jack angry "If you won't stop her, I will!"

    chrome "{i}She draws a pocket repeating pistol. Premium. Chevalier brand. 0.2 seconds are enough for 6 shots in a 75º angle barrage.{/i}"

    chrome "{i}No, no, no.{/i}"

    hide mariah
    hide jack
    show chrome neutral at center

    chrome shocked "WAIT!"

    hide chrome
    show mariah happy at right
    show jack at left

    jack shocked "Wh-"

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
    freddy shocked "Come on, get up, buddy!"

    chrome "{i}Blood on the ground. He’s grown cold already. His spark… extinguished.{/i}"
    chrome "{i}I don’t have the courage to assess the damage. There’s no heartbeat.{/i}"
    show chrome neutral at left
    chrome neutral "He’s dead."
    freddy sad "Why? Why you...?"

    #Narration
    chrome "{i}...{/i}"

    play sound sfx_footsteps

    chrome "{i}In all the commotion, Mariah escaped.{/i}"

    chrome "{i}The cops can deal with her. There's more than enough evidence to put her away when they do.{/i}"

    chrome "{i}Not to mention Jack's sacrifice...{/i}"

    chrome "{i}My job here is done. Time to get Freddy to safety.{/i}"

    chrome "{i}I know someone who'll be glad to see him.{/i}"

    return