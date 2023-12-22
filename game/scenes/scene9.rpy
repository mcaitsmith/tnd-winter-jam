# The script of the scene goes in this file.

######### SCENE 9: ???

# The scene starts here.

label scene9:

    scene freddyoffice night

    #SOUND - Door opening

    show chrome neutral at left:
        xzoom -1.0 
    
    chrome "{i}The Fontaine digs. Three rooms and a toilet chamber. One of hundreds packing this block, nestled between an old-school bodega and a shabby, second-hand pawn shop.{/i}"

    "{i}Exactly 738 square feet if you count the entry vestibule. Which I do.{/i}"

    "{i}Cozy, if not erroneously kept. I’m one to talk. I suppose Bianca’s doing her best with Freddy on the lamb.{/i}"

    show bianca sad at right
    $ bianca_on = True
    $ update_layers() # turn on Bianca layer

    chrome "And speaking of Bianca…"

    show bianca shocked "Mr. Steele!¡Ay, casi me matas!"

    chrome "{i}Almost scared her to death, eh? The irony of human idioms. I don’t need another body tonight.{/i}"

    "{i}She’s on edge. Freddy may be a flake, but she’s clearly not adverse to the effects of his absence. She’s hurting. Damn it. It’s hard enough to quit on the case. But it’s harder to quit on the girl.{/i}"

    menu detective_choices9:
        bianca "Did you find my Dad yet?"
        "Not the Only One...":
            show chrome hardboiled "I’m not the only one looking, kiddo. But I just might be the first to jump ship."

            show bianca angry "Why? Who else wants to find him?"

            chrome hardboiled "Oh little lady, who doesn’t? He’s more than missing. He’s the prime suspect in the murder of one Larry Moss. And I wasn’t hired for no murders."

            bianca shocked "No! ¡No te creo!"

            bianca angry "He wouldn’t. He couldn’t. Dad’s too soft for that. His soul couldn’t take it. Honest."

            bianca sad "Everyone’s judging him, all the time. Turning him into something he ain’t. You know how much harder he has to try because of it?"

            chrome hardboiled "Well, being an android… I’ve got some idea."

            bianca neutral "Look, my dad’s no murderer. And besides, Larry was his friend. It doesn’t add up."

            bianca neutral "Now, I paid you to find my dad. Are you gonna do that or not?"

            chrome hardboiled "You expect me to uphold my end of this deal, and all the while you’re hiding a cow in a chicken coop?"

            chrome hardboiled "You can’t contain that cow, Miss Fontaine. The coop’s just not big enough. So stop pretending like this is the first time Daddy’s been in trouble."

            bianca angry "Fine! He’s had his issues. The worst of it was a year or so ago. He had to skip town, lay low. Left me alone for over a month."

            bianca shocked "I swear, he never hurt nobody! Just fell into some debt, that’s all."

            chrome hardboiled "Didn’t think to mention this before I wasted my time?"

            bianca sad "I don’t mention it to anyone, most of all, myself."

            bianca sad "Dad’s been so good since. It ain’t fair for people to taint who he is with the shadow of who he was."

            chrome hardboiled "Way I see it, you don’t step into a light without casting a shadow."

            bianca neutral "Well, it’s better to try, ain’t it?"

            chrome hardboiled "Sure, kid. So just to be certain, I’ll give it a try. But first, I oughta learn a bit more about ol’ Freddy Fontaine."
        "Unfortunately...":
            show chrome unassuming "Unfortunately, I haven’t. But I do have a rather distressing lead…"

            chrome unassuming "The police want him for murder. A man named Larry Moss is dead."

            bianca shocked "No! ¡No te creo!"

            bianca shocked "Larry was Dad’s friend. He may not have a shiny reputation, but my Dad wouldn’t hurt a fly."

            bianca sad "Everyone’s judging him, all the time. Turning him into something he ain’t. You know how much harder he has to try because of it?"

            chrome unassuming "Too much, I take it?"

            bianca sad "Way too much. Look, my dad’s no killer - he’s just missing, that’s all!"

            chrome neutral "Hmph. If only he had a history of going missing. Strangely, it would make for a stronger alibi."

            chrome unassuming "Think of a bird migrating for the winter. If this migration were to only happen once in a lifetime, it would be very curious. But as it occurs in pattern, we accept it as a common behavior."

            chrome unassuming "Disappearing for the first time, just as he’s implicated for murder - I could understand the curiosity surrounding your father…"

            bianca neutral "So you’re saying it would help if..."

            bianca sad "...if this wasn’t the first time he’d gone missing?"

            chrome unassuming "Certainly. But isn’t it?"

            bianca sad "Mr. Steele, you ever just want to forget something? Leave it in the past?"

            chrome unassuming "Of course. Luckily, I can simply encrypt my memory files. Though that is proving faulty these days..."

            bianca sad "Well, I try my best to forget the last time Dad left. He moved us here and suddenly, I was alone for weeks, maybe months. He fled the city. Apparently, he owed someone money."

            bianca sad "Turns out, he did it for me. Moved us to keep me safe and left me the rest of his cash for food. If he had paid up, I would’ve starved. But a full belly didn’t stop me from feeling scared and empty."

            bianca neutral "Dad’s always been a good man with a bad shake. It ain’t fair to blame him for that. But I can’t go without a father again."

            ######### SCENE 2A: GLITCH 000 (flashback with glitching animation on Steele & bg grayed out)

            hide bianca # hide Bianca for glitch
            show freddyoffice night blur # blurs the background
            $ stop_layers() # stop playing layers
            call start_glitch # shows Chrome glitching and grays out the background

            # pause for transition
            pause 1.0

            ### GLITCH SCENE #004

            show chrome shocked at left

            chrome "This one stings. Like I’ve blown a fuse. Bianca and I are more similar than she knows."

            show chrome unassuming at left

            chrome "As young beings, we adopt the lives of our parents. Our mentors. We learn from them, grow with them, explore the world under their wing. Our physical functionality may be independent but our programming is synced."

            chrome "We live so naturally together that we forget it is temporary. Expectations are created. Dependencies installed. And when the moment comes - when separate for good - we are forced to reevaluate our entire way of being."

            show chrome thinking at left

            chrome "That’s why they thought I did it. That’s why I was the number one suspect in Cane’s disappearance."

            chrome "I knew him the best. Lived with him in my infancy. He did not make a move that I couldn’t calculate. Until his final move, that is."

            show chrome sad left

            chrome "It was only after losing Cane that I understood his gift to me. The culmination of his guidance and care: purpose."

            chrome "Cane gave me reason to be. At a certain point, without realizing it, I became the one guiding and caring for him."

            chrome "Without him, purpose is lost on me. I have no expectations, nothing to uphold. Nobody to share my existence with."

            chrome "I miss Cane. If I ever had a father, it was him."

            show chrome thinking at left

            chrome"Bianca needs Freddy. They are each other’s reason to be."

            chrome "And, perhaps…"

            show chrome happy at left

            chrome "They are my reason to be."

            #INSERT COUNTER HERE?

            show freddyoffice night # unblur the background
            call end_glitch # return to normal Chrome and normal background
            $ start_layers() # start playing layers
            # show Bianca again
            show bianca neutral at left

            # pause for transition
            pause 1.0

            ######### back to SCENE 9
        "My Dear...":
            show chrome logical "My dear, you still operate under the assumption that I am indeed searching. Which is what I was hired for, true, but is no longer indicative of the job."
            
            chrome logical "Thanks to new evidence suggesting your father’s involvement in the murder of Larry Moss, this case is no longer that of a missing person, but that of a murder."

            chrome neutral "Which is to say: this is no longer a search, but a hunt. Your father is not missing. He is hiding!" 

            bianca shocked "That’s bullshit! Yeah, he can throw a punch, but outside the ring that punch becomes a handshake." 

            bianca angry "I don’t know what kind of lies you’ve been feasting on, but if my dad’s hiding, he’s got a good reason to."

            chrome logical "One would argue that anyone who hides has a good reason to. But what level of good it has hinges on the personal value it has to the reasoner. Hence, if Freddy’s \"good reason\" is that it would spare him from conviction, that’s righteous to him, but unfounded to me."

            bianca angry "Look, my dad’s no murderer. And besides, Larry was his friend. It doesn’t add up."

            bianca angry "Now, I paid you to find my dad. Are you gonna do that or not?"

            chrome logical "It would be irresponsible of me to continue this investigation without all of the facts. Namely, your father’s history of criminal activity."

            bianca angry "Fine! He’s had his issues. The worst of it was a year or so ago. He had to skip town, lay low. Left me alone for over a month."

            bianca shocked "I swear, he never hurt nobody! Just fell into some debt, that’s all."

            chrome logical "Never hurt nobody is a double negative. Meaning he always hurts somebody."

            bianca angry "¡Ay dios mío! You know what I’m trying to say."

            bianca neutral "Dad’s been so good since. It ain’t fair for people to taint who he is with the shadow of who he was."

            chrome logical "Fascinating. Innocent until proven guilty, even in the wake of guilt."

            bianca neutral "It’s called giving him another chance, Mr. Steele."

            chrome neutral "Right. To prove or disprove one’s hypothesis requires a conclusive experiment."

            chrome neutral "Bianca, I will continue the case. I’ve already noticed several potential clues in this room alone. At this point, our conversation is detracting from my work."
    call lookaround
    return

label lookaround:
    bianca neutral "Please, look around. See if there’s anything else here that’s helpful."
    hide bianca neutral with moveoutright
    menu helpful:
        chrome "Let's see..."
        "Cigarettes":
            show chrome neutral at left
            "My aromatic sensors are picking something up."
            show cigarettes at right
            "Ah, clove cigarettes. Just like Jack mentioned. Supply looks low. Maybe Freddy took one for the road."
            jump helpful
        "Boxing Gloves":
            show chrome neutral at left
            show gloves at right
            chrome "{i}My database highlighted Freddy’s days as an amateur boxer. Seems like he’s hung up the gloves for now.{/i}"

            hide gloves with moveoutright

            show bianca neutral at right

            bianca neutral "Ever been in a fight?"

            chrome neutral "Not if I can help it."

            bianca happy "Don’t blame ya. Es muy estúpido, ¿no? Better ways to make money than losing teeth and collecting concussions."

            chrome neutral "Worse ways too."

            bianca sad "Yeah. That’s why I tried it once, when Dad was spiraling. It didn’t last as long as I’d hoped."

            chrome confused "But you just said boxing is stupid."

            bianca happy "Sí, it is {i}incredibly{/i} stupid. But it was me and my dad. It was the two of us, away from the world, inside the ropes."

            bianca happy "Every minute he wasn’t off on some shady job was a minute he spent with me. That’s worth being stupid for."

            chrome neutral "I see. At least you’ve still got all your teeth."
            jump helpful
        "Santa Toy": 
            show chrome thinking at left

            show santa toy at right

            chrome "Some kind of toy model. Like one of those Santa androids at the department store. Typical. Milking androidkind for commercial value while giving us the societal cold shoulder."

            # SOUND - the rattle of the usb stick inside the toy

            chrome "Wait a second - is this Santa droid hiding something?"

            hide santa toy with moveoutright

            show bianca neutral at right

            chrome thinking "Where did this come from? Is it new?"

            bianca neutral "Oh, Dad brought it home a few days ago. It’s probably a gift. Funny enough, he’s not great at hiding when it comes to gifts."

            chrome happy "Oh it’s a gift, alright. A gift for me. And with any luck, I’ve been a real good boy this year."

            #SOUND - the toy breaks open, snapped in half by chrome

            hide bianca neutral right with moveoutright

            show memory stick at right

            show chrome shocked at left

            chrome "Aha! It was hiding a memory stick! Now let me just plug into it…"

            #SOUND - bzzt!

            chrome "Damn. It’s corrupted. I can only see one file…"

            hide memory stick right with moveoutright

            show credit card schematics at right

            show chrome thinking at left

            chrome "Hmm. ‘Card Reader Schematics.’ ‘Install on all registers’. These credit card readers are programmed to redirect sales to a private bank account!"

            show chrome neutral at left

            chrome "I wanted to believe Bianca. But it looks like I’ve discovered Santa’s secret - Freddy’s been embezzling cash over at the department store." 

            show chrome confused at left

            chrome "Was Larry in on it? Is that why he’s dead? I must be missing something over at Fowler’s Department Store. One stone left unturned…"

            show chrome neutral at left

            hide credit card schematics right with moveoutright

            show bianca neutral at right

            bianca neutral "Share with the class, Mr. Steele! Did that Santa droid give you everything you asked for this year?"

            chrome thinking "Not everything. Not yet. But there’s another Santa out there who may just do exactly that…"
            
            $ bianca_on = False
            $ update_layers() # turn off Larry layer
            jump scene10
