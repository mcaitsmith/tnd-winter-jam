# The script of the scene goes in this file.

######### SCENE 9: ???

# The scene starts here.

label scene9:

    scene bg freddyoffice

    play sound sfx_door

    show chrome neutral at left:
        xzoom -1.0 
    
    chrome "{i}The Fontaine digs. Three rooms and a toilet chamber. One of hundreds packing this block, nestled between an old-school bodega and a shabby, second-hand pawn shop.{/i}"

    "{i}Exactly 738 square feet if you count the entry vestibule. Which I do.{/i}"

    "{i}Cozy, if not a bit haphazard. I’m one to talk. I suppose Bianca’s doing her best with Freddy on the lam.{/i}"

    show bianca sad at right
    $ bianca_on = True
    $ update_layers() # turn on Bianca layer

    show dialogue_box at center 
    nvl show # show NVL dialogue

    bianca_nvl_right shocked "Mr. Steele! ¡Ay, casi me matas!"
    
    hide dialogue_box
    nvl hide 

    chrome "{i}Almost scared her to death, eh? The irony of human idioms. I don’t need another body tonight.{/i}"

    "{i}She’s on edge. Freddy may be a flake, but Bianca's clearly not averse to the effects of his absence. She could use a friendly voice right. Righ now I'm all she's got.{/i}"

    "{i}She’s hurting. Damn it. It’s hard enough to quit on the case. But it’s harder to quit on the girl.{/i}"

    menu detective_choices9:
        bianca "Did you find my Dad yet?"

        "Hardboiled":
            show dialogue_box at center
            nvl show
            chrome_nvl_left angry "I’m not the only one looking, kiddo. But I just might be the first to jump ship."

            bianca_nvl_right angry "Why? Who else wants to find him?"

            chrome_nvl_left angry "Oh little lady, who doesn’t? He’s more than missing. He’s the prime suspect in the murder of one Larry Moss. And I wasn’t hired for no murders."

            bianca_nvl_right shocked "No! ¡No te creo!"

            bianca_nvl_right angry "He wouldn’t. He couldn’t. Dad’s too soft for that. His soul couldn’t take it. Honest."

            bianca_nvl_right sad "Everyone’s judging him, all the time. Turning him into something he ain’t. You know how much harder he has to try because of it?"

            chrome_nvl_left angry "Well, being an android… I’ve got some idea."

            bianca_nvl_right neutral "Look, my dad’s no murderer. And besides, Larry was his friend. It doesn’t add up."

            bianca_nvl_right neutral "Now, I paid you to find my dad. Are you gonna do that or not?"

            chrome_nvl_left angry "You expect me to uphold my end of this deal, and all the while you’re hiding a cow in a chicken coop?"

            chrome_nvl_left angry "You can’t contain that cow, Miss Fontaine. The coop’s just not big enough. So stop pretending like this is the first time Daddy’s been in trouble."

            bianca_nvl_right angry "Fine! He’s had his issues. The worst of it was a year or so ago. He had to skip town, lay low. Left me alone for over a month."

            bianca_nvl_right shocked "I swear, he never hurt nobody! Just fell into some debt, that’s all."

            chrome_nvl_left angry "Didn’t think to mention this before I wasted my time?"

            bianca_nvl_right sad "I don’t mention it to anyone, most of all, myself."

            bianca_nvl_right sad "Dad’s been so good since. It ain’t fair for people to taint who he is with the shadow of who he was."

            chrome_nvl_left angry "Way I see it, you don’t step into a light without casting a shadow."

            bianca_nvl_right neutral "Well, it’s better to try, ain’t it?"

            chrome_nvl_left angry "Sure, kid. So just to be certain, I’ll give it a try. But first, I oughta learn a bit more about ol’ Freddy Fontaine."

            hide dialogue_box
            nvl clear 

        "Unassuming":

            show dialogue_box at center
            nvl show

            chrome_nvl_left timid "Unfortunately, I haven’t. But I do have a rather distressing lead…"

            chrome_nvl_left timid "The police want him for murder. A man named Larry Moss is dead."

            bianca_nvl_right shocked "No! ¡No te creo!"

            bianca_nvl_right shocked "Larry was Dad’s friend. He may not have a shiny reputation, but my Dad wouldn’t hurt a fly."

            bianca_nvl_right sad "Everyone’s judging him, all the time. Turning him into something he ain’t. You know how much harder he has to try because of it?"

            chrome_nvl_left timid "Too much, I take it?"

            bianca_nvl_right sad "Way too much. Look, my dad’s no killer - he’s just missing, that’s all!"

            chrome_nvl_left neutral "Hmph. If only he had a history of going missing. Strangely, it would make for a stronger alibi."

            chrome_nvl_left timid "Think of a bird migrating for the winter. If this migration were to only happen once in a lifetime, it would be very curious. But as it occurs in pattern, we accept it as a common behavior."

            chrome_nvl_left timid "Disappearing for the first time, just as he’s implicated for murder - I could understand the curiosity surrounding your father…"

            bianca_nvl_right neutral "So you’re saying it would help if..."

            bianca_nvl_right sad "...if this wasn’t the first time he’d gone missing?"

            chrome_nvl_left timid "Certainly. But isn’t it?"

            bianca_nvl_right sad "Mr. Steele, you ever just want to forget something? Leave it in the past?"

            chrome_nvl_left timid "Of course. Luckily, I can simply encrypt my memory files. Though that is proving faulty these days..."

            bianca_nvl_right neutral "Dad’s always been a good man with a bad shake. It ain’t fair to blame him for that. But I can’t go without a father again."
 
            chrome timid "{i}Without a father...{/i}"

            # bianca_nvl_right sad "Turns out, he did it for me. Moved us to keep me safe and left me the rest of his cash for food. If he had paid up, I would’ve starved. But a full belly didn’t stop me from feeling scared and empty."

            # bianca_nvl_right neutral "Dad’s always been a good man with a bad shake. It ain’t fair to blame him for that. But I can’t go without a father again."

            hide dialogue_box
            nvl clear
            ######### SCENE 2A: GLITCH 000 (flashback with glitching animation on Steele & bg grayed out)

            hide bianca # hide Bianca for glitch
            show bg freddyoffice blur # blurs the background
            $ chrome_on = False # turn off Chrome layer for glitch
            $ update_layers(0) # update layers
            call start_glitch # shows Chrome glitching and grays out the background

            # pause for transition
            pause 1.0

            ### GLITCH SCENE #004

            show chrome shocked glitch

            chrome "This one stings. Like I’ve blown a fuse. Bianca and I are more similar than she knows.{/i}"

            show chrome timid glitch

            chrome "{i}As young beings, we adopt the lives of our parents. Our mentors. We learn from them, grow with them, explore the world under their wing.{/i}"

            chrome "{i}Our physical functionality may be independent but our programming is synced.{/i}"

            chrome "{i}We live so naturally together that we forget it is temporary. Expectations are created. Dependencies installed.{/i}"

            chrome "{i}And when the moment comes - when we separate for good - we are forced to reevaluate our entire state of functionality.{/i}"

            show chrome thinking glitch

            chrome "{i}That’s why they thought I did it. That’s why I was the number one suspect in Cane’s disappearance.{/i}"

            chrome "{i}I knew him the best. Lived with him in my infancy. He did not make a move that I couldn’t calculate. Until his final move, that is.{/i}"

            show chrome sad glitch

            chrome "{i}It was only after losing Cane that I understood his gift to me. The culmination of his guidance and care: purpose.{/i}"

            chrome "{i}Cane gave me reason to be. At a certain point, without realizing it, I became the one guiding and caring for him.{/i}"

            chrome "{i}Without him, purpose is lost on me. I have no expectations, nothing to uphold. Nobody to share my existence with.{/i}"

            chrome "{i}I miss Cane. If I ever had a father, it was him.{/i}"

            show chrome thinking glitch

            chrome"{i}Bianca needs Freddy. They are each other’s reason to be.{/i}"

            chrome "{i}And, perhaps…{/i}"

            show chrome happy glitch

            chrome "{i}They are my reason to be.{/i}"

            $ glitch_counter += 1

            show bg freddyoffice # unblur the background
            call end_glitch # return to normal Chrome and normal background
            $ chrome_on = True # turn on Chrome layer
            $ update_layers(0) # update layers
            # show Bianca again
            show bianca neutral at right

            # pause for transition
            pause 1.0

            ######### back to SCENE 9

        "Logical":
            
            show dialogue_box at center 
            nvl show 

            chrome_nvl_left thinking "My dear, you still operate under the assumption that I am indeed searching. Which is what I was hired for, true, but is no longer indicative of the job."
            
            chrome_nvl_left thinking "Thanks to new evidence suggesting your father’s involvement in the murder of Larry Moss, this case is no longer that of a missing person, but that of a murder."

            chrome_nvl_left neutral "Which is to say: this is no longer a search, but a hunt. Your father is not missing. He is hiding!" 

            bianca_nvl_right shocked "That’s bullshit! Yeah, he can throw a punch, but outside the ring that punch becomes a handshake." 

            bianca_nvl_right angry "I don’t know what kind of lies you’ve been feasting on, but if my dad’s hiding, he’s got a good reason to."

            chrome_nvl_left thinking "One would argue that anyone who hides has a good reason to. But what level of good it has hinges on the personal value it has to the reasoner. Hence, if Freddy’s \"good reason\" is that it would spare him from conviction, that’s righteous to him, but unfounded to me."

            bianca_nvl_right angry "Look, my dad’s no murderer. And besides, Larry was his friend. It doesn’t add up."

            bianca_nvl_right angry "Now, I paid you to find my dad. Are you gonna do that or not?"

            chrome_nvl_left thinking "It would be irresponsible of me to continue this investigation without all of the facts. Namely, your father’s history of criminal activity."

            bianca_nvl_right angry "Fine! He’s had his issues. The worst of it was a year or so ago. He had to skip town, lay low. Left me alone for over a month."

            bianca_nvl_right shocked "I swear, he never hurt nobody! Just fell into some debt, that’s all."

            chrome_nvl_left thinking "Never hurt nobody is a double negative. Meaning he always hurts somebody."

            bianca_nvl_right angry "¡Ay dios mío! You know what I’m trying to say."

            chrome_nvl_left thinking "Fascinating. Innocent until proven guilty, even in the wake of guilt."

            bianca_nvl_right neutral "It’s called giving him another chance, Mr. Steele."

            chrome_nvl_left neutral "Right. To prove or disprove one’s hypothesis requires a conclusive experiment."

            chrome_nvl_left neutral "Bianca, I will continue the case. I’ve already noticed several potential clues in this room alone. At this point, our conversation is detracting from my work."
            
            hide dialogue_box
            nvl clear 

    call lookaround
    return

label lookaround:
    bianca neutral "Please, look around. See if there’s anything else here that’s helpful."
    hide bianca neutral with moveoutright
    menu helpful:
        chrome "Let's see..."
        "Cigarettes":
            show chrome neutral at left
            "{i}My aromatic sensors are picking something up.{/i}"
            show cigarettes at right
            "{i}Ah, clove cigarettes. Just like Jack mentioned. Supply looks low. Maybe Freddy took one for the road.{/i}"
            hide cigarettes

            jump helpful
        "Boxing Gloves":
            show chrome neutral at left
            show gloves at right
            chrome "{i}My database highlighted Freddy’s days as an amateur boxer. Seems like he’s hung up the gloves for now.{/i}"

            hide gloves

            show bianca neutral at right with moveinright

            show dialogue_box at center
            nvl show

            bianca_nvl_right neutral "Ever been in a fight?"

            chrome_nvl_left neutral "Not if I can help it."

            bianca_nvl_right happy "Don’t blame ya. Es muy estúpido, ¿no? Better ways to make money than losing teeth and collecting concussions."

            chrome_nvl_left neutral "Worse ways too."

            bianca_nvl_right sad "Yeah. That’s why I tried it once, when Dad was spiraling. It didn’t last as long as I’d hoped."

            chrome_nvl_left confused "But you just said boxing is stupid."

            bianca_nvl_right happy "Sí, it is {i}incredibly{/i} stupid. But it was me and my dad. It was the two of us, away from the world, inside the ropes."

            bianca_nvl_right happy "Every minute he wasn’t off on some shady job was a minute he spent with me. That’s worth being stupid for."

            hide bianca happy with moveoutright

            chrome_nvl_left neutral "I see. At least you’ve still got all your teeth."

            hide dialogue_box
            nvl hide 

            jump helpful
        "Santa Toy": 
            show chrome thinking at left

            show santa toy at right

            chrome "Some kind of toy model. Like one of those Santa androids at the department store. Typical. Milking androidkind for commercial value while giving us the societal cold shoulder."

            play sound sfx_rattle

            chrome "Wait a second - is this Santa droid hiding something?"

            hide santa toy

            show bianca neutral at right with moveinright

            show dialogue_box at center
            nvl show

            chrome_nvl_left thinking "Where did this come from? Is it new?"

            bianca_nvl_right neutral "Oh, Dad brought it home a few days ago. It’s probably a gift. Funny enough, he’s not great at hiding when it comes to gifts."

            chrome_nvl_left happy "Oh it’s a gift, alright. A gift for me. And with any luck, I’ve been a real good boy this year."

            hide dialogue_box
            nvl hide

            play sound sfx_breakmetaltoy

            hide bianca neutral right with moveoutright

            show memorystick at right

            show chrome shocked at left

            chrome "Aha! It was hiding a memory stick! Now let me just plug into it…"

            play sound sfx_santabeepscan

            chrome "Damn. It’s corrupted. I can only see one file…"

            hide memorystick

            show creditcard at right

            show chrome thinking at left

            chrome "Hmm. ‘Card Reader Schematics.’ ‘Install on all registers’. These credit card readers are programmed to redirect sales to a private bank account!"

            show chrome neutral at left

            chrome "I wanted to believe Bianca. But it looks like I’ve discovered Santa’s secret - Freddy’s been embezzling cash over at the department store." 

            show chrome confused at left

            chrome "Was Larry in on it? Is that why he’s dead? I must be missing something over at Fowler’s. One stone left unturned…"

            show chrome neutral at left

            hide creditcard 

            show bianca neutral at right with moveinright

            show dialogue_box at center
            nvl show

            bianca_nvl_right neutral "Share with the class, Mr. Steele! Did that Santa droid give you everything you asked for this year?"

            chrome_nvl_left thinking "Not everything. Not yet. But there’s another Santa out there who may just do exactly that…"

            hide dialogue_box
            nvl clear

            $ bianca_on = False
            $ update_layers() # turn off Larry layer
            jump scene10
