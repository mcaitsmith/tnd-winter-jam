# The script of the scene goes in this file.

######### SCENE 6: 

# The scene starts here.

label scene6:

    scene bg folwer department 

    show mariah neutral at right

    $ mariah_on = True
    $ update_layers() # start Mariah layer

    chrome "{i}Mariah Fowler, the owner of Fowler’s Department Store. Human female, she’s reaching the tail end of middle aged, looks visibly annoyed with everyone at the moment.{/i}"

    chrome "{i}There is an air of tension thrumming around her. She has the eyes of a predator, sharp and clear and ready to deliver violence if she sees any weakness.{/i}"

    show chrome neutral at left with moveinleft:
        xzoom -1.0

    chrome "Hello, ma’am."

    mariah "Oh great. Another Rent-a-Bot cop. I’ll tell you what I told the other one. I already answered the cops' questions. So scram."

    chrome "I think you’ve mistaken me for a lesser bot, ma’am. I’m Chrome Steele, private detective."

    show mariah surprised

    pause 0.5

    show mariah angry 

    mariah "Wait a second, I’m pretty sure there aren’t any Rent-a-Bot detectives. Pretty sure that entire line got scrapped."

    show chrome angry 

    chrome "Not all of us ma’am."

    mariah "Fine. Whatever. The more of you (insult to robots) working on this case the faster it’s done and out of my life."

    show chrome neutral 

    chrome "{i}My initial plan had been to ask about Freddy. However, I couldn’t help my curiosity from getting to me.{/i}"

    chrome "{i} was designed for solving crimes and one had dropped into my lap. I could always fit some questions about Freddy at the end.{/i}"

    show chrome thinking 

    chrome "Would you mind answering a few of my questions about what happened over here?"

    # show visual chalk outline of the body 

    mariah "Tch. Just what I need. More questions. Fine, ask them. But afterwards I want all of you (insert robot insult here) to clear off my parking lot. You hear me?"

    chrome "{i}The air around Mariah Fowler rises in tension. She’s clearly looking for a fight, ready to defend herself.{/i}"

    chrome "{i}The police’s questioning was probably long and arduous. If I press too hard, she’ll clam up.{/i}"

    menu: 
        chrome "{i}Now… how should I go about this? {/i}"

        "Harboiled":
            jump scene6_hardboiled 
        "Logical":
            jump scene6_logical
        "Unassuming":
            jump scene6_unassuming 


    label scene6_hardboiled:

        chrome "Yeah, because you’re doing a whole lot just standing out here glowering at everyone. Look lady, just answer a few of my questions and we both can get on with our day."

        mariah "I don’t need to take that from a tin can."
        
        show chrome angry

        chrome "Sure, lady. Blah, blah, blah, Rent-a-cops. Just tell me about our victim. I don’t got all day, either."

        mariah "Tch, just what I need. A Tin Can with an attitude snooping around."

        mariah "His name’s Larry. He’s an elf at Santa’s workshop."

        #Visual show Larry as an elf (not too sure how to go about this)

        chrome "And what did Larry do that got him a permanent red slip."

        mariah "Well, it’s not like I did it! I was in my office when I heard people shouting. When I ran out here, I found Larry dead on the ground."

        mariah "You’d know all of this if you just asked one of the cops over there. Now stop wasting my time."

        chrome "{i} Well, it looks like Larry is a deadend. Fine, I shouldn’t be messing around with a crime scene, anyways. I’ll move on to my actual job.{/i}"

        show chrome thinking 

        chrome "Well, that’s fine. No need to aggravate a lady with such a delicate physique."

        chrome "Then let’s ask about someone else. What do you know about a Freddy Fontaine."

        show mariah shocked 

        mariah "Freddy?"

        show mariah angry 

        mariah "I can tell you that he’s a no show. Today was supposed to be his last day, but he hasn’t shown up for his shift."

        show chrome neutral 

        chrome "And what does Freddy do at Fowler’s?"

        mariah "He’s a Santa. He does Santa stuff. Look it up in that fancy database in your head."

        chrome "{i}A mall Santa. That’s Freddy’s secret. Well, that’s disappointing.{/i}"

        chrome "{i}All of this work, all of Bianca’s worry, all because Freddy was too prideful to tell his daughter he was working a dead-end job.{/i}"

        show mariah neutral 

        mariah "Actually, now that you bring him up. You should probably look for Freddy. Yeah, he’s probably the one that did this."

        show chrome thinking 

        chrome "That’s a rather sudden jump in logic."

        mariah "Maybe for a tin can like you. But Freddy and Larry were thick as thieves. Until this week, that is."

        mariah "The two of them apparently had a falling out. Which probably led to poor Larry’s death."

        show chrome neutral 

        chrome "Well, I’ll look into it."

        chrome "{i}What a twist. This was supposed to be a simple missing person’s case, but now I have a murder intertwined to it.{/i}"

        chrome "{i}No, I shouldn’t make any judgments yet. I can judge Freddy once I have evidence that he’s a part of this. {/i}"

        chrome "{i}I should take another look around and see if I can’t find more information.{/i}"

        jump scene6_postchoice

    label scene6_logical: 

        chrome "The owner of the store standing in front of a crime scene. If this was just another crime there would be no need for your attention."

        chrome "Which means this crime has to do with the store. An employee, perhaps?"

        show mariah angry 

        mariah "Well, no shit sherlock. I wouldn’t be standing out here in the cold if I wasn’t invested."

        show chrome neutral 

        chrome "Yeah, yeah. Just tell me about our victim."

        mariah "His name is Larry Moss. He’s an elf that works at one of Santa’s workshop. Well, he was."

        #Visual show Larry as an elf (not too sure how to go about this)

        chrome "Did he have any enemies that could have done this?"

        mariah "Yeah, Rudolph hated being picked on by an elf!"

        mariah "I don’t keep track of my employees relationships. I have better things to do than micromanage every employee."

        mariah "All I know was that I heard shouting and when I came out here, Larry was lying dead on the ground."

        mariah "If you want to know more, just ask the other Rent-a-Bot cops. I’m done with this."

        chrome "{i}Well, looks like if I want to know more I’ll need to ask one of the cops. But that’s fine, I can move on to my actual job.{/i}"

        show chrome thinking 

        chrome "Well, then I would like to expand my questioning to a person of interest. What can you tell me about Freddy?"

        show mariah suprised 

        mariah "Freddy?"

        show mariah angry 

        mariah "That idiot was a no show. He’s supposed to be the Santa that works with Larry."

        chrome "{i}Well, looks like I found Freddy’s secret destination. He was working as a Mall Santa. Demeaning job. Probably kept a secret from Bianca due to embarrassment. {/i}"

        show chrome neutral 

        chrome "I see."

        show mariah neutral

        mariah "However, he’s been talking about quitting. Said that he couldn’t handle the job anymore. I thought he just flaked out."

        show chrome thinking

        chrome "So he’s Larry’s direct coworker? I assume that the two of them spoke often."

        show mariah angry 

        mariah "Yeah, the two of them were thick as thieves. Except for this final week… Yeah…"

        show mariah neutral 

        mariah "You should look into him. The only person that really talked with Larry was Freddy. If anyone would have a reason to kill Larry, it would be Freddy."

        show mariah angry 

        mariah "Now get out of my face. I’ve had enough of you Rent-a-Bots."

        show chrome neutral 

        chrome "I’ll leave you alone for now."

        chrome "{i}Well, this mystery has become a lot more complicated. No, I need more information before I make any conclusions.{/i}"

        jump scene6_postchoice


    label scene6_unassuming:

        chrome "Sorry, sorry. This entire thing has probably been an unpleasant surprise, like actually getting coal in the stocking, you know."

        chrome "Just… do you think you could just run me through what happened, one last time."

        show mariah neutral 

        mariah "It’s been a shitshow. Not only do I have to deal with the falling sales, but now I have to deal with all of these jokers gawking instead of shopping."

        chrome "It’s like a car crash. People will slow down just to look at it. Not in a helpful way or anything. They’re just slowing down traffic to see what happened."

        mariah "Exactly! It doesn’t matter if they’re inconveniencing a bunch of people, it’s more important that they get a glimpse of a tragedy."

        mariah "Tch, the real tragedy is going to happen in a few months when I need to close."

        chrome "Mmm. But about the body…"

        mariah "Right. The guy who died is Larry Moss. He’s a seasonal hire. Little guy, kind of a sad sack."

        mariah "We threw him in one of the elf costumes and put him in one of the Santa’s workshops."

        #Visual show Larry 

        chrome "Geez, I knew that Santa ran a tight ship, but I didn’t think he ran it so tight that he’d off one of his elves."

        show mariah shocked 

        mariah "You think one of the Santa’s killed him for talking?"

        show chrome shocked 

        chrome "What? No. Just a joke."

        show mariah neutral 

        mariah "Right. Right. A joke. But I can’t really think of anyone that would kill ol’ Larry. He was a bit of a bore, but he kept to himself. Well, I guess he had to talk to Freddy."

        chrome "{i}And suddenly I was reminded about my original job. As interesting as this mystery murder is, I was supposed to find Bianca’s father.{/i}"

        chrome "Freddy? Is that someone that worked here?"

        show mariah shocked 

        mariah "What? I mean, yes. Freddy did work here. But not anymore. Today was supposed to be his last day, but he’s gone now. Just left early."

        show chrome neutral

        chrome "Well, that’s not suspicious"

        show mariah neutral 

        mariah "Yes… it is suspicious. The two of them were close, but I heard that they had a falling out this week. Maybe, you should go check that out."

        hide mariah neutral with dissolve

        call start_glitch

        #pause for transistion 

        pause 1.0

        chrome "{i}Here we go again. Energy surges through me. My systems flood with information, trusting me to interpret the proper pieces. I suspect that I am trying to tell myself something.{/i}"

        chrome "{i}Suspicion breeds blame. Blame then circles like a vulture, seeking a host.{/i}"

        chrome "{i}The victim needn’t be responsible. Blame is attracted far more to believability than responsibility.{/i}"

        chrome "{i}I’ve been on both sides of such condemnation. {/i}"

        chrome "{i}Blame is a defense mechanism. When placed successfully, it brings security to the accuser.{/i}"

        chrome "{i}When taken, blame accrues an aspect of chivalry in the form of penitence. Taking responsibility humbles the accused. It creates a challenge of improvement.{/i}"

        chrome "{i}Before I encrypted these memories, I often wished I were to blame for the vanishing of Forrest Cane.{/i}"

        chrome "{i}It would have been so much easier to shoulder the weight if I could have taken it freely.{/i}" 

        chrome "{i}Instead, it was forced upon me. A crucifixion of my character.{/i}"
        
        chrome "{i} I denied it voraciously. So much so, that I began to wonder if somehow, indirectly, I was to blame after all. {/i}"

        chrome "{i}Eventually, I was acquitted. The plague of blame infected the android unit until it had eaten through all ten of us.{/i}"

        chrome "{i}All remaining threads of trust were severed. The Bureau shuttered the Android Program.{/i}"

        chrome "{i}The only thing that kept us from complete annihilation was Cane. He had installed a biometric kill switch - we couldn’t be shut down with him.{/i}"

        chrome "{i}Naturally, it wasn’t long before the Bureau turned on their once great hero.{/i}"

        chrome "{i}That’s the nature of the beast. First, they blamed us androids for sowing Cane’s demise. Then they blamed Cane for extinguishing our own.{/i}"

        call end_glitch

        $ glitch_counter +=1 # increment glitch counter

        jump scene6_postchoice


    label scene6_postchoice:

        show chrome neutral 

        hide mariah neutral with moveoutright

        $ mariah_on = False
        $ update_layers() # stop Mariah layer

        chrome "{i}With that final suggestion, Mariah Fowler turned back to scowling at the cops that in her opinion were not leaving fast enough. I knew a dismissal when I saw one.{/i}"

        chrome "{i}Well, this missing person’s case has suddenly taken an interesting twist. I should see what else I can learn about Larry and if it has anything to do with our missing father.{/i}"

        jump scene7
