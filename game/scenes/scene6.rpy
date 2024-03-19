# The script of the scene goes in this file.

######### SCENE 6: FOWLER'S DEPARTMENT STORE (MARIAH)

# The scene starts here.

label scene6:

    # scene bg extstore night with fade

    # show chrome neutral at left with moveinleft:
    #     xzoom -1.0

    show mariah neutral at right with moveinright

    $ mariah_on = True
    $ update_layers() # start Mariah layer

    chrome "{i}Mariah Fowler. She must be reaching the tail end of middle aged. Looks visibly annoyed with everyone at the moment.{/i}"

    chrome "{i}There is an air of tension thrumming around her. She has the sharp eyes of a predator, ready to pounce if she sees any weakness.{/i}"

    # show chrome neutral at left with moveinleft:
    #     xzoom -1.0

    pause 1.0

    show dialogue_box at center 
    nvl show # show NVL dialogue

    mariah_nvl_right "Oh great. I thought they shut you Rent-a-Bot cops down."

    mariah_nvl_right "I already answered the real cops' questions."

    chrome_nvl_left "Good news for you, I'm no cop."

    chrome_nvl_left "I’m Chrome Steele, private detective."

    show mariah confused

    pause 0.5

    show mariah angry 

    mariah_nvl_right "It's a Christmas miracle! A Tin Man detective. Even better."
    
    if scene5_choice2 == False and scene5_choice3 == False:

        hide dialogue_box

        show chrome neutral 

        chrome "{i}My initial plan had been to ask about Freddy. However, I couldn’t help my curiosity from getting to me.{/i}"

        chrome "{i}I was designed for solving crimes and one had dropped into my lap. I could always fit some questions about Freddy at the end.{/i}"

        show chrome thinking left at left

        show dialogue_box

    chrome_nvl_left "Would you mind answering a few questions about what happened over here?"

    # show visual chalk outline of the body 

    mariah_nvl_right "Tch. Just what I need. More questions."

    mariah_nvl_right "Fine, ask them."

    mariah_nvl_right "But afterwards I want all of you flatfoots to clear off my parking lot. You hear me?"

    hide dialogue_box

    chrome "{i}The air around Mariah Fowler rises in tension. She’s clearly looking for a fight, ready to defend herself.{/i}"

    chrome "{i}The police questioning was probably long and arduous. If I press too hard, she’ll clam up.{/i}"

    menu: 
        chrome "{i}Now… how should I go about this? {/i}"

        "Logical":
            jump scene6_logical
        "Unassuming":
            jump scene6_unassuming 
        "Hardboiled":
            jump scene6_hardboiled 


    label scene6_hardboiled:

        show dialogue_box

        show chrome hardboiled:
            xzoom -1.0

        chrome_nvl_left "Yeah, because you’re doing a whole lot just standing out here glowering at everyone."
        
        chrome_nvl_left "Look lady, just answer a few of my questions and we both can get on with our day."

        mariah_nvl_right "I don’t need to take that from a tin can."
        
        chrome_nvl_left "Sure, lady. Just tell me about our victim."

        chrome_nvl_left "I don’t got all day, either."

        mariah_nvl_right "Tch, just what I need. A tin can with an attitude snooping around."

        mariah_nvl_right "His name’s Larry. He’s an elf at Santa’s workshop."

        #hide dialogue_box

        #show larry dead at center with dissolve
        
        #pause 0.5
        
        #hide larry dead at center with dissolve

        #show dialogue_box

        chrome_nvl_left "And what did Larry do that got him a permanent red slip?"

        mariah_nvl_right "Well, it’s not like I did it!"

        mariah_nvl_right "I was in my office when I heard people shouting."
        
        mariah_nvl_right "When I ran out here, I found Larry dead on the ground."

        if scene5_choice2 == True:

            chrome_nvl_left "Just like that, huh?"

        mariah_nvl_right "You’d know all of this if you just asked one of the cops over there."

        show mariah angry

        mariah_nvl_right "Now stop wasting my time."

        if scene5_choice2 == False and scene5_choice3 == False:

            hide dialogue_box

            show chrome neutral

            chrome "{i}It looks like Larry is a dead-end. Maybe. I’ll move on to the reason I'm here.{/i}"

            show dialogue_box

            show chrome hardboiled

        chrome_nvl_left "Then let me ask you about someone else. What do you know about a Freddy Fontaine."

        show mariah confused 

        mariah_nvl_right "Freddy?!"

        show mariah angry 

        mariah_nvl_right "Pfft. Today was supposed to be his last day, but he’s gone now. Just left early."

        chrome_nvl_left "And what does Freddy do at Fowler’s?"

        mariah_nvl_right "He’s a Santa. He does Santa stuff. Look it up in that fancy database in your head."

        hide dialogue_box

        show chrome neutral

        chrome "{i}Looks like I found Freddy’s secret destination. He was working as a Mall Santa.{/i}"

        chrome "{i}Probably kept it a secret from Bianca due to the embarrassment.{/i}"

        #chrome "{i}A mall Santa. That’s Freddy’s secret. That’s... disappointing.{/i}"

        #chrome "{i}All of this work, all of Bianca’s worry, all because Freddy was too prideful to tell his daughter he was working a dead-end job.{/i}"

        show mariah neutral 
        
        show dialogue_box

        show chrome hardboiled

        mariah_nvl_right "Actually, now that you bring him up. You should probably look for Freddy."

        mariah_nvl_right "Yeah, he’s probably the one that did this."

        show chrome thinking left at left

        chrome_nvl_left "That’s a rather sudden jump in logic."

        show chrome neutral

        mariah_nvl_right "Maybe for a tin can like you. But Freddy and Larry were thick as thieves."

        mariah_nvl_right "Until this week, that is."

        mariah_nvl_right "The two of them apparently had a falling out. Which probably led to poor Larry’s death."

        show chrome neutral 

        chrome_nvl_left "Is that right? I’ll look into it."

        hide dialogue_box

        chrome "{i}Hmm. This mystery has become a lot more complicated. No, I need more information before I make any conclusions.{/i}"

        jump scene6_postchoice

    label scene6_logical: 

        show dialogue_box

        show chrome logical

        chrome_nvl_left "Hmm. The owner of the store standing in front of a crime scene."

        chrome_nvl_left "If this was just another crime there would be no need for your attention."

        chrome_nvl_left "Which means this crime has to do with the store."

        chrome_nvl_left "An employee, perhaps?"

        show mariah angry 

        mariah_nvl_right "Well, no shit sherlock."

        mariah_nvl_right "I wouldn’t be standing out here in the cold if I wasn’t invested."

        chrome_nvl_left "Just as I said. Now tell me more about our victim."

        show mariah neutral

        mariah_nvl_right "His name is Larry Moss."

        mariah_nvl_right "He’s an elf that works at Santa’s workshop."

        mariah_nvl_right "Well, he was."

        #hide dialogue_box

        #show larry dead at center with dissolve
        
        #pause 0.5
        
        #hide larry dead at center with dissolve

        #show dialogue_box

        chrome_nvl_left "Did he have any enemies?"

        show mariah angry

        mariah_nvl_right "Yeah, Rudolph hated being picked on by an elf!"

        mariah_nvl_right "I don’t keep track of employee relationships."

        mariah_nvl_right "I have better things to do than micromanage every employee."

        show mariah neutral

        mariah_nvl_right "All I know was that I heard shouting."

        mariah_nvl_right "When I came out here, Larry was lying dead on the ground."

        if scene5_choice2 == True:

            chrome_nvl_left "Is there anything else, perhaps? Can you spare more details?"

        show mariah angry    
       
        mariah_nvl_right "If you want to know more, just ask the lazy cops."

        mariah_nvl_right "I’m done with this."

        if scene5_choice2 == False and scene5_choice3 == False:

            show chrome neutral

            hide dialogue_box

            chrome "{i}Fine with me. I’ll move on to the reason I'm here.{/i}"

            show dialogue_box

            show chrome logical

        chrome_nvl_left "Well then, I would like to expand my questioning to a person of interest."

        chrome_nvl_left "What can you tell me about Freddy Fontaine?"

        show mariah confused

        mariah_nvl_right "Freddy?!"

        show mariah angry 

        mariah_nvl_right "Pfft. That idiot? He’s supposed to be the Santa that works with Larry."

        hide dialogue_box

        chrome "{i}Looks like I found Freddy’s secret destination. He was working as a Mall Santa.{/i}"

        chrome "{i}Probably kept it a secret from Bianca due to the embarrassment.{/i}"

        show dialogue_box
       
        show chrome logical:
            xzoom -1.0

        chrome_nvl_left "I see."

        show mariah neutral

        mariah_nvl_right "But he’s been talking about quitting. Said that he couldn’t handle the job anymore."

        mariah_nvl_right "He flaked out - you know the kind."

        mariah_nvl_right "Today was supposed to be his last day, but he’s gone now. Just left early."

        show chrome thinking left at left

        chrome_nvl_left "So he’s Larry’s direct coworker? I assume that the two of them spoke often."

        show mariah angry 

        mariah_nvl_right "Yeah, the two of them were thick as thieves."

        mariah_nvl_right "Except for this final week… Yeah…"

        show mariah neutral 

        mariah_nvl_right "You should look into him. The only person that really talked with Larry was Freddy."
        
        mariah_nvl_right "If anyone would have a reason to kill Larry, it would be Freddy."

        show mariah angry 

        show chrome shocked

        mariah_nvl_right "Now get out of my face. I’ve answered enough questions for one day."

        show chrome neutral:
            xzoom -1.0

        chrome_nvl_left "I’ll leave you alone for now."

        hide dialogue_box

        chrome "{i}Hmm. This mystery has become a lot more complicated. No, I need more information before I make any conclusions.{/i}"

        jump scene6_postchoice


    label scene6_unassuming:

        show dialogue_box

        show chrome unassuming

        chrome_nvl_left "Sorry, sorry."

        chrome_nvl_left "This entire thing has probably been an unpleasant surprise, like getting coal in the stocking, you know."

        chrome_nvl_left "Just… do you think you could run me through what happened, one last time."

        show mariah neutral 

        mariah_nvl_right "It’s been a shitshow."

        mariah_nvl_right "Not only do I have to deal with falling sales..."

        mariah_nvl_right "...but now I have to deal with all these jokers gawking instead of shopping!"

        chrome_nvl_left "It’s like a car crash."

        chrome_nvl_left "People will slow down just to look at it."

        chrome_nvl_left "Not in a helpful way or anything."

        chrome_nvl_left "They’re just slowing down traffic to see what happened."

        mariah_nvl_right "Exactly! It doesn’t matter if they’re inconveniencing me."
        
        mariah_nvl_right "It’s more important that they get a glimpse of a tragedy."

        mariah_nvl_right "Tch, the real tragedy is going to happen in a few months when I need to close."

        chrome_nvl_left "Mm. But about the body…"

        mariah_nvl_right "Right."

        mariah_nvl_right "The guy who died is Larry Moss."

        mariah_nvl_right "He’s a seasonal hire. Little guy, kind of a sad sack."

        mariah_nvl_right "When he first showed up, we immediately threw him in an elf costume."

        mariah_nvl_right "I mean, he was built for the part."

        #hide dialogue_box

        #show larry dead at center with dissolve
        
        #pause 0.5
        
        #hide larry dead at center with dissolve

        #show dialogue_box

        mariah_nvl_right "Earlier today I heard some arguing from my office."

        mariah_nvl_right "I came out and saw the poor bastard sprawled out on the concrete."

        chrome_nvl_right "Man. Can’t imagine what that must’ve been like for you."

        mariah_nvl_right "Yeah. No one cares about management y'know?"

        mariah_nvl_right "I’m expected to just run the store by myself and deal with this crap at the same time."

        if scene5_choice2 == True:

            chrome_nvl_left "So you're saying you heard a commotion and came out to find Larry dead on the ground?"

            chrome_nvl_left "Did I get that right?"

            show mariah angry

            mariah_nvl_right "Did one of your capacitors blow or something? Yeah, that’s what I said."

        chrome_nvl_left "Jeez, I knew that Santa ran a tight ship in his workshop."

        chrome_nvl_left "But I didn’t think he ran it so tight that he’d off one of his elves!"

        show mariah confused

        mariah_nvl_right "You think one of the Santa’s killed him for talking?"

        show chrome shocked:
            xzoom -1.0

        chrome_nvl_left "What? No. Just a joke."

        show mariah neutral 

        mariah_nvl_right "Right. Right. A joke."
        
        show chrome unassuming

        mariah_nvl_right "But I can’t really think of anyone that would kill ol’ Larry."
        
        mariah_nvl_right "He was a bit of a bore, but he kept to himself."

        mariah_nvl_right "Well, I guess he had to talk to Freddy."

        if scene5_choice2 == False and scene5_choice3 == False:

            show chrome neutral

            hide dialogue_box

            chrome "{i}I was suddenly reminded of what brought me here.{/i}"

            show dialogue_box

            show chrome unassuming

        chrome_nvl_left "Freddy? You mean Freddy Fontaine? Doesn't he work here?"

        mariah_nvl_right "What? I mean, yes. Freddy did work here. He was one of my Santas."

        hide dialogue_box

        show chrome neutral

        chrome "{i}Looks like I found Freddy’s secret destination. He was working as a Mall Santa.{/i}"

        chrome "{i}Probably kept it a secret from Bianca due to the embarrassment.{/i}"

        show mariah neutral 
        
        show dialogue_box

        show chrome unassuming

        mariah_nvl_right "In fact, he was Larry's Santa. They were paired together. But not anymore."

        mariah_nvl_right "Today was supposed to be his last day, but he’s gone now. Just left early."

        chrome_nvl_left "Well, that’s not suspicious."

        show mariah confused

        mariah_nvl_right "Come to think of it... it is suspicious."

        show mariah neutral

        mariah_nvl_right "The two of them were close, but I heard that they had a falling out this week."

        mariah_nvl_right "Maybe you should go check that out."

        show chrome neutral

        chrome_nvl_left "Sus... Suspicion... blame -"
        
        # hide dialogue_box
        # nvl clear

        # hide mariah neutral with dissolve
        
        # show bg extstore night blur # blurs the background

        call start_glitch from _call_start_glitch_5

        #pause for transistion 

        show chrome shocked glitch at left:
            xzoom -1.0
   
        pause 1.0

        chrome "{i}Here we go again. Energy surges through me. My systems flood with information, trusting me to interpret the proper pieces. I suspect that I am trying to tell myself something.{/i}"

        show chrome thinking left glitch at left
        
        chrome "{i}Suspicion breeds blame. Blame then circles like a vulture, seeking a host.{/i}"

        chrome "{i}The victim needn’t be responsible. Blame is attracted far more to believability than responsibility.{/i}"

        show chrome sad glitch:
            xzoom -1.0
        
        chrome "{i}I’ve been on both sides of such condemnation. {/i}"

        show chrome neutral glitch 

        chrome "{i}Blame is a defense mechanism. When placed successfully, it brings security to the accuser.{/i}"

        chrome "{i}When taken, blame humbles the accused. It creates a challenge of improvement.{/i}"

        chrome "{i}Before I encrypted these memories, I often wished I were to blame for the vanishing of Forrest Cane.{/i}"

        chrome "{i}It would have been so much easier to shoulder the weight if I could have taken it freely.{/i}" 

        show chrome angry glitch
        
        chrome "{i}Instead, it was forced upon me. A crucifixion of my character.{/i}"
        
        chrome "{i} I denied it voraciously. So much so, that I began to wonder if somehow, indirectly, I was to blame after all. {/i}"

        show chrome sad glitch 
        
        chrome "{i}Eventually, I was acquitted. The plague of blame infected the android unit until it had eaten through all ten of us.{/i}"

        chrome "{i}All remaining threads of trust were severed. The Bureau shuttered the Android Program.{/i}"

        chrome "{i}The only thing that kept us from complete annihilation was Cane. He had installed a biometric kill switch - we couldn’t be shut down without him.{/i}"

        show chrome neutral glitch 
        
        chrome "{i}Naturally, it wasn’t long before the Bureau turned on their once great hero.{/i}"

        chrome "{i}That’s the nature of the beast. First, they blamed us androids for sowing Cane’s demise. Then they blamed Cane for extinguishing our own...{/i}"

        scene bg extstore night with pixellate # unblurs the background
        call end_glitch from _call_end_glitch_4

        $ glitch_counter +=1 # increment glitch counter

        jump scene6_postchoice


    label scene6_postchoice:

        show chrome neutral at left:
            xzoom -1.0

        show mariah angry at right

        show dialogue_box at center
 
        mariah_nvl_right "So, are we done here, metalhead? Yeah??"

        hide dialogue_box

        nvl clear

        show mariah at right:
            xzoom -1.0
        hide mariah neutral with moveoutright

        $ mariah_on = False
        $ update_layers() # stop Mariah layer

        chrome "{i}With that final suggestion, Mariah Fowler turned back to scowling at the cops. I knew a dismissal when I saw one.{/i}"

        chrome "{i}This missing person case has taken an interesting twist.{/i}"

        # show chrome at left:
        #     xzoom 1.0
        # hide chrome with moveoutleft

        $ scene5_choice1 = True

        if scene5_choice1 == True and scene5_choice2 == True and scene5_choice3 == True:
            chrome "{i}I think I've investigated enough here.{/i}"
            chrome "{i}There's some evidence to work with - none of it great for Freddy.{/i}"
            chrome "{i}And some testimony that doesn't quite jibe, but humans are nothing if not... inconsistent.{/i}"
            chrome "{i}It's time I had a heart-to-heart with Bianca. Ask her a few hanging questions.{/i}"
            chrome "{i}Besides, better to tell the kid in person what I found out.{/i}"
            chrome "{i}There's more to this story. I know it.{/i}"
            jump scene9
        else:
            chrome "{i}I should see what else I can learn about Larry and if it has anything to do with Freddy.{/i}"
            jump investigate
