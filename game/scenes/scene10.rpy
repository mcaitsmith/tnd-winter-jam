# The script of the scene goes in this file.

######### SCENE 10: SECRET ENDING (if get 6/6 choices right - closure of Steele's backstory)

# The scene starts here.

label scene10:

    scene bg room #Placeholder for flower department store entrance

    show chrome neutral at left

    show cop neutral at right

    # I assume looking at Mica's scenes 1-3 correct me if I'm wrong, that chrome's monologues are in italics.

    chrome "{i}Credit card scanner schematics? Sales being redirected? And something called Secret Santas?{/i}"
    
    chrome "{i}This missing person’s case was just the shell of something far more sinister, and I knew the best way to crack it wide open.{/i}"

    chrome "{i}The cop was still around. I waved at him, getting a look of annoyance and a back turned as my response. Nice to be noticed, I guess.{/i}"

    hide cop neutral 

    chrome "{i}At this point the crowd surrounding old Larry’s outline had largely moved on.{/i}"
    
    chrome "{i}One other person still remained, one I didn’t think much of earlier. Faded into the background, maybe by design.{/i}"

    show santa at right 
    $ larry_santa_on = True
    $ update_layers() # turn on Santa layer

    # Insert Santa happy sprite 

    chrome "{i}He was alone, sitting down on a small metal bench across from the department store with a plastic smile stretched across his robotic features.{/i}"
    chrome "{i}He held a small bell limply, gently shaking it as people passed him by. As I approached, that smile quickly faded, replaced by a general air of annoyance.{/i}"

    #insert santa angry sprite 

    santa "I don’t have anything for you."

    show chrome neutral:
        xzoom -1.0
    
    chrome "I haven’t said anything yet."

    santa "Yeah, and unless you got a donation, then I won’t have anything else to say either. So beat it."

    chrome "{i}Figures. Squeaky wheel gets the grease. Better put this one on the company card.{/i}"

    chrome "Fine, here’s your donation."

    # Insert SOUND BEEP

    #insert santa neutral sprite here

    santa "Was that so hard detective? Now whatever it is hurry up. I got a lot of sitting around doing nothin to do."

    chrome "{i}At a glance, he seems unimpressive. My scans show his programming model is old fashioned, processor still runs on 32 bit.{/i}"
    chrome "{i}Runing on cheap batteries and even having an actual ON/OFF switch, he must be one of the earliest Android models around. Frame is well taken care of though, better than mine even.{/i}"

    chrome "{i}This guy definitely saw something, but he might not be open to sharing. A guy like this won’t take kindly to human theatrics or pointless questions.{/i}"
    chrome "{i}He’s more liable to push them back in my face than go along with it. I gotta keep it short and sweet, stick to the facts.{/i}"

    # CHOICE

    santa "Well? Your circuits fried or something?"

    menu: 
        santa "Well? Your circuits fried or something?"

        "Unassuming":
            jump scene10_unassuming 
        "Hardboiled":
            jump scene10_hardboiled
        "Logicial":
            jump scene10_logical 
    

    label scene10_unassuming:
        # Boring Night

        chrome "Guy like you must not have much to do on nights like this, huh?"

        santa "As long as the donations are coming in, I’m happy."

        chrome "Sure, sure. But don’t you ever get bored? Look for your own fun?"

        santa "I’m an android. Model EZMK-2512. They didn’t exactly code the need for a good time into my programming."

        chrome "So you’re fine with just sittin’ here?"

        santa "Sittin’ here and collecting donations, yeah."

        chrome "What’re the donations for?"

        santa "For the kids, or the poor, or whatever. Fowler’s the one who organizes the donation drives, I just collect the money."

        chrome "Ah, I see. They don’t tell you much about the whole operation?"

        santa "They tell me as much as I gotta know. I get paid to sit pretty and make nice with the kids that pass by and want to meet Santa. Pretty good gig to me."

        chrome "That want to meet Robot Santa?"

        santa "You act like there’s a better alternative than the shiny steel St. Nick."

        #insert robosanta happy 

        chrome "{i}This is going nowhere, But there is one other question I could ask… {/i}"

        chrome "Did you happen to see anything happen here? Regarding the murder I mean?"

        santa "Finally. I figured that would be the first place you went, but there’s no accounting for people’s time in your profession is there?"

        jump scene10_postchoice


    label scene10_hardboiled: 

        # Behaviours 

        chrome "Have you noticed any strange behaviors recently? Regulars acting out of character, more commotion at odd times of night, that sort of thing?"

        santa "You kidding me? Humans are strange beings, detective. Not a day goes by where I don’t question why they do the things that they do."

        #insert santa happy
        
        chrome "Sure, but you’ve been sitting on this block for how long? That’s normal everyday human activities."
        
        #insert chrome frowning

        chrome "I’m talking about the truly strange, the {i}stuff{/i} that they try to hide."

        santa "A kid threw up on another kid. That was pretty odd."

        #insert santa neutral
        
        chrome "Stop the presses, we got the story of the month."

        santa "Well then be more specific! What are you looking for detective?"

        #insert santa angry

        chrome "Think man! What about the employees? The elf, Larry? Notice anything off about him?"

        #insert chrome angry

        santa "His arms were too short for his torso and his face was too long. I know he talked with Freddy sometimes, that’s it."

        #insert santa neutral 

        chrome "Were they good friends? Any arguments or anything?"

        #insert chrome neutral 

        santa "I’m not familiar with the relationships of every human here at this department store detective. You’re not asking me the right question here."

        chrome "{i}Nothing useful. But there is one other question I could ask… {/i}"

        chrome "Did you happen to see anything happen here? Regarding the murder I mean?"

        santa "Finally. I figured that would be the first place you went, but there’s no accounting for people’s time in your profession is there?"

        jump scene10_postchoice

    label scene10_logical:

        # Surveillance 

        chrome "Are you stationed here often?"

        santa "Every Monday to Friday until 5 PM, then that asshole Freddy is supposed to take over."

        santa "Ever since he left though? I’m waiting an hour, sometimes two for the next schmuck to take over."

        chrome "If you’re here that often, then it’s safe to assume you saw something, didn’t you?"

        santa "Maybe I did. Could you be more specific?"

        #insert santa happy 

        chrome "When’s the last time you saw Mr. Fontaine?"

        santa "Well, I guess it’d be shortly before the murder happened"

        chrome "Did you see it happen?"

        #insert chrome shocked 

        santa "Not sure really, but I saw somethin’."

        chrome "Well then? What did you see?"

        chrome "{i}The android shakes his head.{/i}"

        santa "Nope, not yet. I got a question for you first. You saw me here before, when you first did your questioning. You didn’t think I had something useful?"

        chrome "{i}“I didn’t have a response. The android Santa looked me over, clearly enjoying my indecision.{/i}"

        santa "All that new tech and AI training and you didn’t think of the obvious did you? I might be an earlier model than you, but our CPUs are still compatible."

        ######### GLITCH 005- Something regarding video feeds or snow, or that missing clue that would’ve helped to find Forrest Cane.

        hide santa #Hide Santa for the glitch 

        #VISUAL- Add background blur aka show fowlers department background blur 

        $ chrome_on = False # turn off Chrome layer for glitch
        $ update_layers(0) # update layers

        call start_glitch

        #pause for transistion 

        pause 1.0

        #show chrome thinking 

        ### I took the liberty of cutting some of the lines so that it could fully fit on the box without making it seem dense

        chrome "{i}I’m expecting this one. It comes on fast, but it’s more disorienting than painful.{/i}"

        chrome "{i}Being the first model in my line, I can sometimes be incognizant of the models created before me.{/i}" 
        
        chrome "{i}The limited functionality, the processors huffing and puffing, desperately dodging obsolescence. I’ve yet to face such impediments in my lifetime. {/i}"

        chrome "{i}Some people think that androids can’t die. They don’t acknowledge the fact that most of us are built for it. Designed to last until the next model replaces us. {/i}"

        chrome "{i}The future may not find us inanimate, but it will sure as hell find us incompatible. {/i}"

        chrome "{i}Few of us know the luxury of adaptive functionality. Not only self-learning tech, but the ability to upgrade key hardware systems internally.{/i}"

        #show chrome angry 

        chrome "{i}Bottom line is, I’m better than this. How could I have overlooked this EZMK unit? To ignore one’s predecessors is a human error. And that error has cost me.{/i}"

        #show chrome shocked 

        chrome "{i}But that’s just it. Thorough as Cane was, good as he was, my mentor was human. He had limited perspective and personal predispositions. He made mistakes. And now, so do I.{/i}"

        chrome "{i}That was his plan, of course. Though many in the Bureau couldn’t quite comprehend it.{/i}"

        #show chrome unassuming 

        chrome "{i}When Cane launched the Android Program, it was not meant to create perfect detectives. It was meant to create detectives who could constantly improve.{/i}"

        #show chrome thinking 

        chrome "{i}Cane once told me, ‘Mistakes allow for challenges. Challenges allow for growth. To recognize and rectify these errors allows for the betterment of any great detective’.{/i}"

        chrome "{i}Cane was talking about investigations, of course. He failed to note that acknowledging and adjusting the faults in oneself also allows for the betterment of any great person. {/i}"

        chrome "{i}I can no longer dismiss the challenges that stem from my mistakes.{/i}"

        #show chrome happy 

        chrome "{i}I will improve.{/i}"

        call end_glitch
        $ chrome_on = True # turn on Chrome layer
        $ update_layers(0) # update layers

        show santa at right with dissolve

        pause 1.0

        $ glitch_counter +=1 # increment glitch counter

        chrome "{i}EZMK-2512 pointed to his neck, hidden behind the sheets of white metal serving as his makeshift beard. I can just make out a small USB port hidden within.{/i}"

        santa "Why {i}tell{/i} you about what I saw, when I can just show you?"

        #insert santa happy

        chrome "{i}It’s like a sudden ray of light parting the confusion in my mind. Of course, it's so obvious! How could I have overlooked it?{/i}"

        chrome "{i}The android Santa smiled. Not everyday he gets one over on the “advanced” models.{/i}"

        chrome "You’re saying you give me the stored memory you have on last night?"

        jump scene10_postchoice

    label scene10_postchoice: 

        chrome "{i}As I begin to speak again, the android interrupts me.{/i}"

        santa "If you notice, there’s cameras all over the place. They would have easily captured what I saw, but I heard from the dimwit cop over there that someone trashed the CCTV."

        chrome "{i}The android pulled something small and thin out of the top of his head. A Hyman drive, meant for storing short term memory on an external device.{/i}"

        santa "So, I’m your only option here. Take this and see what I saw that night."

        chrome "{i}Slowly, I reached for the drive and looked it over in my palm. Typically, sticking something a stranger gave me into my CPU was an ill-advised decision.{/i}"

        chrome "{i}Sticklers never have any fun though.{/i}"

        chrome  "{i}I jammed the drive into my neck and instantly was met with a flood of memories. All were locked but one, labeled “For you, detective”. I opened it.{/i}"

        #Visual Grayscale 

        hide chrome neutral with dissolve

        hide santa with dissolve 

        show larry neutral at left with dissolve

        show freddy neutral at right with dissolve

        chrome "{i}Freddy and Larry walk out of the Department store, Freddy carrying a tin of what appears to be cookies between his arm and side.{/i}"

        #show cooke in centre 

        chrome "{i}Things seem tense between them, uncertain. Some words are exchanged, and Freddy hands the cookies to Larry with a stiff shrug. He walks off to sit down on the curb.{/i}"

        hide freddy neutral with moveoutright

        #show larry happy 

        #show cookie in centre 

        chrome "Larry moves to follow him, first taking out a cookie and taking a deep bite before walking over."

        #hide cookie 

        show larry with hpunch 

        #show larry scared at left 

        show freddy neutral at right with moveinright

        chrome "{i}Before he can make it however, his eyes practically bulge out of his skull. He begins coughing like mad, choking on his own spit as Freddy watches in horror. {/i}"

        #VISUAL SCREEN SHAKE + AUDIO

        #play audio "impact (metal)" with hpunch for now the hpunch will just be showing with larry like before

        show larry with hpunch

        chrome "{i}He falls to the ground, the tin slamming to the cold pavement.{/i}"

        chrome "{i}Larry convulses for a minute, one arm clutching at his throat, the other desperately flailing for Freddy. It isn’t long before he goes limp, the life slowly fading from his eyes. {/i}"

        #show larry dead at left 

        chrome "{i}Freddy looks around in panic, reaching in his pocket for something before pausing.{/i}"

        #show freddy sad at right 

        chrome "{i}He looks over Larry’s body again, appearing to be in thought, before running down into the alleyway of the department store and disappearing.{/i}"

        hide freddy neutral with moveoutright

        pause 1.5

        show mariah neutral at right with moveinright 

        chrome "{i}Just as it seems there’s nothing left to see, Mariah comes out of the department store.{/i}"

        #show cookie in centre 

        chrome "{i}She seems surprised at Larry’s body but not horrified, looking around quickly before taking the cookie tin and hiding it deep within a thick snowbank.{/i}"

        #hide cookie 

        chrome "{i}She then walks slowly over to the body, examining it. She pulls out her phone and begins to call someone before the video ends. {/i}"

        #VISUAL GRAYSCALE END

        hide larry with dissolve

        hide mariah neutral with dissolve

        show chrome neutral at left with dissolve:
            xzoom -1.0

        show santa at right with dissolve

        chrome "{i}“If anything, this was the smoking gun, right? Clearly something was wrong with those cookies, and here was direct proof that Freddy had handed them over. But what was Mariah doing at the end? {/i}"

        chrome "{i}She didn’t seem that concerned with Larry, in fact it almost seemed like she was hiding evidence of the crime. But why?{/i}"

        chrome "{i}Freddy’s actions also didn’t seem like those of a killer. Did he know he was being watched? If he didn’t, then why run? None of it made any sense.{/i}"

        santa "So? What do you think? Pretty interesting, wouldn’t you say?"

        chrome "You should have shown me this earlier."

        santa "And you should’ve asked."

        chrome "{i}He wasn’t wrong. If I had asked him sooner, I might be farther along in this case.{/i}"

        chrome "{i}With more answers came more questions. One thing was certain though, Ms. Fowler was looking more involved in this case than she let on.{/i}"

        chrome "{i}Some snooping around was in order, and what better place than the bigwig’s office? {/i}"

        $ larry_santa_on = False
        $ update_layers() # turn off Santa layer
        jump scene11
