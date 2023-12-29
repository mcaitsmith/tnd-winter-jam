# The script of the scene goes in this file.

######### SCENE 6: 

# The scene starts here.

label scene6:

    scene bg extstore night

    show mariah neutral at right

    $ mariah_on = True
    $ update_layers() # start Mariah layer

    chrome "{i}Mariah Fowler. Human female, she’s reaching the tail end of middle aged, looks visibly annoyed with everyone at the moment.{/i}"

    chrome "{i}There is an air of tension thrumming around her. She has the eyes of a predator, sharp and clear and ready to deliver violence if she sees any weakness.{/i}"

    show chrome neutral at left with moveinleft:
        xzoom -1.0

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
    
    hide dialogue_box

    show chrome neutral 

    chrome "{i}My initial plan had been to ask about Freddy. However, I couldn’t help my curiosity from getting to me.{/i}"

    chrome "{i}I was designed for solving crimes and one had dropped into my lap. I could always fit some questions about Freddy at the end.{/i}"

    hide chrome
    show chrome thinking left at left

    show dialogue_box

    chrome_nvl_left "Would you mind answering a few of my questions about what happened over here?"

    # show visual chalk outline of the body 

    mariah_nvl_right "Tch. Just what I need. More questions."

    mariah_nvl_right "Fine, ask them."

    mariah_nvl_right "But afterwards I want all of you flatfoots to clear off my parking lot. You hear me?"

    hide dialogue_box

    chrome "{i}The air around Mariah Fowler rises in tension. She’s clearly looking for a fight, ready to defend herself.{/i}"

    chrome "{i}The police’s questioning was probably long and arduous. If I press too hard, she’ll clam up.{/i}"

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

        chrome_nvl_left "Yeah, because you’re doing a whole lot just standing out here glowering at everyone."
        
        chrome_nvl_left "Look lady, just answer a few of my questions and we both can get on with our day."

        mariah_nvl_right "I don’t need to take that from a tin can."
        
        show chrome angry:
            xzoom -1.0

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

        mariah_nvl_right "You’d know all of this if you just asked one of the cops over there."

        mariah_nvl_right "Now stop wasting my time."

        hide dialogue_box

        chrome "{i} Well, it looks like Larry is a deadend. Fine, I shouldn’t be messing around with a crime scene, anyways. I’ll move on to my actual job.{/i}"

        hide chrome
        show chrome thinking left at left

        show dialogue_box

        chrome_nvl_left "Well, that’s fine. No need to aggravate a lady with such a delicate physique."

        chrome_nvl_left "Then let’s ask about someone else. What do you know about a Freddy Fontaine."

        show mariah confused 

        mariah_nvl_right "Freddy?"

        show mariah angry 

        mariah_nvl_right "I can tell you that he’s a no show."
        
        mariah_nvl_right "Today was supposed to be his last day, but he hasn’t shown up for his shift."

        show chrome neutral 

        chrome_nvl_left "And what does Freddy do at Fowler’s?"

        mariah_nvl_right "He’s a Santa. He does Santa stuff. Look it up in that fancy database in your head."

        hide dialogue_box

        chrome "{i}A mall Santa. That’s Freddy’s secret. Well, that’s disappointing.{/i}"

        chrome "{i}All of this work, all of Bianca’s worry, all because Freddy was too prideful to tell his daughter he was working a dead-end job.{/i}"

        show mariah neutral 
        
        show dialogue_box

        mariah_nvl_right "Actually, now that you bring him up. You should probably look for Freddy. Yeah, he’s probably the one that did this."

        hide chrome
        show chrome thinking left at left

        chrome_nvl_left "That’s a rather sudden jump in logic."

        mariah_nvl_right "Maybe for a tin can like you. But Freddy and Larry were thick as thieves."

        mariah_nvl_right "Until this week, that is."

        mariah_nvl_right "The two of them apparently had a falling out. Which probably led to poor Larry’s death."

        show chrome neutral 

        chrome_nvl_left "Well, I’ll look into it."

        hide dialogue_box
        nvl clear

        chrome "{i}What a twist. This was supposed to be a simple missing person’s case, but now I have a murder intertwined to it.{/i}"

        chrome "{i}No, I shouldn’t make any judgments yet. I can judge Freddy once I have evidence that he’s a part of this. {/i}"

        chrome "{i}I should take another look around and see if I can’t find more information.{/i}"


        jump scene6_postchoice

    label scene6_logical: 

        show dialogue_box

        chrome_nvl_left "The owner of the store standing in front of a crime scene."

        chrome_nvl_left "If this was just another crime there would be no need for your attention."

        chrome_nvl_left "Which means this crime has to do with the store."

        chrome_nvl_left "An employee, perhaps?"

        show mariah angry 

        mariah_nvl_right "Well, no shit sherlock."

        mariah_nvl_right "I wouldn’t be standing out here in the cold if I wasn’t invested."

        show chrome neutral:
            xzoom -1.0

        chrome_nvl_left "Yeah, yeah. Just tell me about our victim."

        mariah_nvl_right "His name is Larry Moss."

        mariah_nvl_right "He’s an elf that works at Santa’s workshop."

        mariah_nvl_right "Well, he was."

        #hide dialogue_box

        #show larry dead at center with dissolve
        
        #pause 0.5
        
        #hide larry dead at center with dissolve

        #show dialogue_box

        chrome_nvl_left "Did he have any enemies?"

        mariah_nvl_right "Yeah, Rudolph hated being picked on by an elf!"

        mariah_nvl_right "I don’t keep track of employee relationships."

        mariah_nvl_right "I have better things to do than micromanage every employee."

        mariah_nvl_right "All I know was that I heard shouting and when I came out here, Larry was lying dead on the ground."

        mariah_nvl_right "If you want to know more, just ask the other Rent-a-Bot cops."

        mariah_nvl_right "I’m done with this."


        hide dialogue_box

        chrome "{i}Well, looks like if I want to know more I’ll need to ask one of the cops. But that’s fine, I can move on to my actual job.{/i}"

        show dialogue_box

        hide chrome
        show chrome thinking left at left

        chrome_nvl_left "Well, then I would like to expand my questioning to a person of interest."

        chrome_nvl_left "What can you tell me about Freddy?"

        show mariah confused

        mariah_nvl_right "Freddy?"

        show mariah angry 

        mariah_nvl_right "That idiot was a no show. He’s supposed to be the Santa that works with Larry."

        hide dialogue_box

        chrome "{i}Well, looks like I found Freddy’s secret destination. He was working as a Mall Santa. Demeaning job. Probably kept a secret from Bianca due to embarrassment. {/i}"

        show dialogue_box
       
        show chrome neutral:
            xzoom -1.0

        chrome_nvl_left "I see."

        show mariah neutral

        mariah_nvl_right "However, he’s been talking about quitting."

        mariah_nvl_right "Said that he couldn’t handle the job anymore. I thought he just flaked out."

        hide chrome
        show chrome thinking left at left

        chrome_nvl_left "So he’s Larry’s direct coworker? I assume that the two of them spoke often."

        show mariah angry 

        mariah_nvl_right "Yeah, the two of them were thick as thieves."

        mariah_nvl_right "Except for this final week… Yeah…"

        show mariah neutral 

        mariah_nvl_right "You should look into him. The only person that really talked with Larry was Freddy."
        
        mariah_nvl_right "If anyone would have a reason to kill Larry, it would be Freddy."

        show mariah angry 

        mariah_nvl_right "Now get out of my face. I’ve had enough of you Rent-a-Bots."

        show chrome neutral:
            xzoom -1.0

        chrome_nvl_left "I’ll leave you alone for now."

        hide dialogue_box

        chrome "{i}Well, this mystery has become a lot more complicated. No, I need more information before I make any conclusions.{/i}"

        jump scene6_postchoice


    label scene6_unassuming:

        show dialogue_box

        chrome_nvl_left "Sorry, sorry."

        chrome_nvl_left "This entire thing has probably been an unpleasant surprise, like actually getting coal in the stocking, you know."

        chrome_nvl_left "Just… do you think you could run me through what happened, one last time."

        show mariah neutral 

        mariah_nvl_right "It’s been a shitshow."

        mariah_nvl_right "Not only do I have to deal with the falling sales, but now I have to deal with all of these jokers gawking instead of shopping."

        chrome_nvl_left "It’s like a car crash."

        chrome_nvl_left "People will slow down just to look at it."

        chrome_nvl_left "Not in a helpful way or anything."

        chrome_nvl_left "They’re just slowing down traffic to see what happened."

        mariah_nvl_right "Exactly!"
        
        mariah_nvl_right "It doesn’t matter if they’re inconveniencing a bunch of people, it’s more important that they get a glimpse of a tragedy."

        mariah_nvl_right "Tch, the real tragedy is going to happen in a few months when I need to close."

        chrome_nvl_left "Mmm. But about the body…"

        mariah_nvl_right "Right."

        mariah_nvl_right "The guy who died is Larry Moss."

        mariah_nvl_right "He’s a seasonal hire. Little guy, kind of a sad sack."

        mariah_nvl_right "We threw him in one of the elf costumes and put him in one of the Santa’s workshops."

        #hide dialogue_box

        #show larry dead at center with dissolve
        
        #pause 0.5
        
        #hide larry dead at center with dissolve

        #show dialogue_box

        chrome_nvl_left "Geez, I knew that Santa ran a tight ship, but I didn’t think he ran it so tight that he’d off one of his elves."

        show mariah confused

        mariah_nvl_right "You think one of the Santa’s killed him for talking?"

        show chrome shocked:
            xzoom -1.0

        chrome_nvl_left "What? No. Just a joke."

        show mariah neutral 

        mariah_nvl_right "Right. Right. A joke."
        
        mariah_nvl_right "But I can’t really think of anyone that would kill ol’ Larry."
        
        mariah_nvl_right "He was a bit of a bore, but he kept to himself."

        mariah_nvl_right "Well, I guess he had to talk to Freddy."

        hide dialogue_box

        chrome "{i}And suddenly I was reminded about my original job. As interesting as this mystery murder is, I was supposed to find Bianca’s father.{/i}"

        show dialogue_box

        chrome_nvl_left "Freddy? Is that someone that worked here?"

        mariah_nvl_right "What? I mean, yes. Freddy did work here. He was one of my Santas."

        mariah_nvl_right "In fact, he was Larry's Santa. They were paired together. But not anymore. Today was supposed to be his last day, but he’s gone now. Just left early."

        show chrome neutral

        chrome_nvl_left "Well, that’s not suspicious."

        show mariah neutral 

        mariah_nvl_right "Come to think of it... it is suspicious."

        mariah_nvl_right "The two of them were close, but I heard that they had a falling out this week."

        mariah_nvl_right "Maybe you should go check that out."

        chrome_nvl_left "Suspicion... blame -"
        
        hide dialogue_box
        nvl clear

        hide mariah neutral with dissolve
        
        show bg extstore night blur # blurs the background

        call start_glitch

        #pause for transistion 

        pause 1.0

        show chrome shocked glitch 

        chrome "{i}Here we go again. Energy surges through me. My systems flood with information, trusting me to interpret the proper pieces. I suspect that I am trying to tell myself something.{/i}"

        hide chrome
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

        chrome "{i}That’s the nature of the beast. First, they blamed us androids for sowing Cane’s demise. Then they blamed Cane for extinguishing our own.{/i}"

        show bg extstore night # unblurs the background
        call end_glitch

        $ glitch_counter +=1 # increment glitch counter

        jump scene6_postchoice


    label scene6_postchoice:

        show chrome neutral

        show mariah angry 
 
        mariah "So, we done hear, metalhead? Now go find my Santa!"

        hide mariah neutral with moveoutright

        $ mariah_on = False
        $ update_layers() # stop Mariah layer

        chrome "{i}With that final suggestion, Mariah Fowler turned back to scowling at the cops. I knew a dismissal when I saw one.{/i}"

        chrome "{i}Well, this missing person’s case has suddenly taken an interesting twist. I should see what else I can learn about Larry and if it has anything to do with our missing father.{/i}"

        jump scene7
