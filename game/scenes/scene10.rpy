# The script of the scene goes in this file.

######### SCENE 10: SECRET ENDING (if get 6/6 choices right - closure of Steele's backstory)

# The scene starts here.

label scene10:

    scene bg Fowler Department

    show chrome neutral at left:
        xzoom -1.0

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

    # show santa happy

    chrome "{i}He was alone, sitting down on a small metal bench across from the department store with a plastic smile stretched across his robotic features.{/i}"
    chrome "{i}He held a small bell limply, gently shaking it as people passed him by. As I approached, that smile quickly faded, replaced by a general air of annoyance.{/i}"

    # show santa angry

    show dialogue_box
    nvl show 

    santa_nvl_right "I don’t have anything for you."
    
    chrome_nvl_left "I haven’t said anything yet."

    santa_nvl_right "Yeah, and unless you got a donation, then I won’t have anything else to say either. So beat it."

    hide dialogue_box

    chrome "{i}Figures. Squeaky wheel gets the grease. Better put this one on the company card.{/i}"

    show dialogue_box

    chrome_nvl_left "Fine, here’s your donation."

    play sound sfx_santabeepscan

    show santa  

    santa_nvl_right "Was that so hard detective? Now whatever it is hurry up. I got a lot of sitting around doing nothin to do."

    hide dialogue_box

    chrome "{i}At a glance, he seems unimpressive. My scans show his programming model is old fashioned, processor still runs on 32 bit.{/i}"
    chrome "{i}Runing on cheap batteries and even having an actual ON/OFF switch, he must be one of the earliest Android models around. Frame is well taken care of though, better than mine even.{/i}"

    chrome "{i}This guy definitely saw something, but he might not be open to sharing. A guy like this won’t take kindly to human theatrics or pointless questions.{/i}"
    chrome "{i}He’s more liable to push them back in my face than go along with it. I gotta keep it short and sweet, stick to the facts.{/i}"

    # CHOICE

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

        show dialogue_box

        chrome_nvl_left "Guy like you must not have much to do on nights like this, huh?"

        santa_nvl_right "As long as the donations are coming in, I’m happy."

        chrome_nvl_left "Sure, sure. But don’t you ever get bored? Look for your own fun?"

        santa_nvl_right "I’m an android. Model EZMK-2512. They didn’t exactly code the need for a good time into my programming."

        chrome_nvl_left "So you’re fine with just sittin’ here?"

        santa_nvl_right "Sittin’ here and collecting donations, yeah."

        chrome_nvl_left "What’re the donations for?"

        santa_nvl_right "For the kids, or the poor, or whatever. Fowler’s the one who organizes the donation drives, I just collect the money."

        chrome_nvl_left "Ah, I see. They don’t tell you much about the whole operation?"

        santa_nvl_right "They tell me as much as I gotta know. I get paid to sit pretty and make nice with the kids that pass by and want to meet Santa. Pretty good gig to me."

        chrome_nvl_left "That want to meet Robot Santa?"

        # show santa happy

        santa_nvl_right "You act like there’s a better alternative than the shiny steel St. Nick."

        hide dialogue_box

        chrome "{i}This is going nowhere, But there is one other question I could ask… {/i}"

        show dialogue_box

        chrome_nvl_left "Did you happen to see anything happen here? Regarding the murder I mean?"

        santa_nvl_right "Finally. I figured that would be the first place you went, but there’s no accounting for people’s time in your profession is there?"

        hide dialogue_box

        jump scene10_postchoice


    label scene10_hardboiled: 

        # Behaviours 

        show dialogue_box

        chrome_nvl_left "Have you noticed any strange behaviors recently? Regulars acting out of character, more commotion at odd times of night, that sort of thing?"

        # show santa happy 
        
        santa_nvl_right "You kidding me? Humans are strange beings, detective. Not a day goes by where I don’t question why they do the things that they do."

        show chrome neutral # was frowning unsure what this should be? 
        
        chrome_nvl_left "Sure, but you’ve been sitting on this block for how long? That’s normal everyday human activities."
    
        chrome_nvl_left "I’m talking about the truly strange, the {i}stuff{/i} that they try to hide."

        # show santa neutral 
        
        santa_nvl_right "A kid threw up on another kid. That was pretty odd."
        
        chrome_nvl_left "Stop the presses, we got the story of the month."

        #show santa angry 

        santa_nvl_right "Well then be more specific! What are you looking for detective?"

        #insert santa angry

        chrome_nvl_left "Think man! What about the employees? The elf, Larry? Notice anything off about him?"

        #show santa neutral 

        santa_nvl_right "His arms were too short for his torso and his face was too long. I know he talked with Freddy sometimes, that’s it."

        show chrome neutral 

        chrome_nvl_left "Were they good friends? Any arguments or anything?"

        santa_nvl_right "I’m not familiar with the relationships of every human here at this department store detective. You’re not asking me the right question here."

        hide dialogue_box

        chrome "{i}Nothing useful. But there is one other question I could ask… {/i}"

        show dialogue_box

        chrome_nvl_left "Did you happen to see anything happen here? Regarding the murder I mean?"

        santa_nvl_right "Finally. I figured that would be the first place you went, but there’s no accounting for people’s time in your profession is there?"

        hide dialogue_box

        jump scene10_postchoice

    label scene10_logical:

        # Surveillance 

        show dialogue_box

        chrome_nvl_left "Are you stationed here often?"

        santa_nvl_right "Every Monday to Friday until 5 PM, then that asshole Freddy is supposed to take over."

        santa_nvl_right "Ever since he left though? I’m waiting an hour, sometimes two for the next schmuck to take over."

        chrome_nvl_left "If you’re here that often, then it’s safe to assume you saw something, didn’t you?"

        #show santa happy

        santa_nvl_right "Maybe I did. Could you be more specific?"

        chrome_nvl_left "When’s the last time you saw Mr. Fontaine?"

        santa_nvl_right "Well, I guess it’d be shortly before the murder happened"

        show chrome shocked

        chrome_nvl_left "Did you see it happen?"

        santa_nvl_right "Not sure really, but I saw somethin’."

        chrome_nvl_left "Well then? What did you see?"

        hide dialogue_box

        chrome "{i}The android shakes his head.{/i}"

        show dialogue_box

        santa_nvl_right "Nope, not yet. I got a question for you first."
        
        santa_nvl_right "You saw me here before, when you first did your questioning."
        
        santa_nvl_right "You didn’t think I had something useful?"

        hide dialogue_box

        chrome "{i}“I didn’t have a response. The android Santa looked me over, clearly enjoying my indecision.{/i}"

        show dialogue_box

        santa_nvl_right "All that new tech and AI training and you didn’t think of the obvious did you?"
        
        santa_nvl_right "I might be an earlier model than you, but our CPUs are still compatible."

        hide dialogue_box
        

        ######### GLITCH 005- Something regarding video feeds or snow, or that missing clue that would’ve helped to find Forrest Cane.

        hide santa #Hide Santa for the glitch 

        #VISUAL- Add background blur aka show fowlers department background blur 

        $ chrome_on = False # turn off Chrome layer for glitch
        $ update_layers(0) # update layers

        call start_glitch

        #pause for transistion 

        pause 1.0

        show chrome thinking glitch

        chrome "{i}I’m expecting this one. It comes on fast, but it’s more disorienting than painful.{/i}"

        chrome "{i}Being the first model in my line, I can sometimes be incognizant of the models created before me.{/i}" 
        
        chrome "{i}The limited functionality, the processors huffing and puffing, desperately dodging obsolescence. I’ve yet to face such impediments in my lifetime. {/i}"

        chrome "{i}Some people think that androids can’t die. They don’t acknowledge the fact that most of us are built for it. Designed to last until the next model replaces us. {/i}"

        chrome "{i}The future may not find us inanimate, but it will sure as hell find us incompatible. {/i}"

        chrome "{i}Few of us know the luxury of adaptive functionality. Not only self-learning tech, but the ability to upgrade key hardware systems internally.{/i}"

        show chrome angry glitch

        chrome "{i}Bottom line is, I’m better than this. How could I have overlooked this EZMK unit? To ignore one’s predecessors is a human error. And that error has cost me.{/i}"

        show chrome shocked glitch 

        chrome "{i}But that’s just it. Thorough as Cane was, good as he was, my mentor was human. He had limited perspective and personal predispositions. He made mistakes. And now, so do I.{/i}"

        chrome "{i}That was his plan, of course. Though many in the Bureau couldn’t quite comprehend it.{/i}"

        show chrome neutral glitch

        chrome "{i}When Cane launched the Android Program, it was not meant to create perfect detectives. It was meant to create detectives who could constantly improve.{/i}"

        show chrome thinking glitch

        chrome "{i}Cane once told me, ‘Mistakes allow for challenges. Challenges allow for growth. To recognize and rectify these errors allows for the betterment of any great detective’.{/i}"

        chrome "{i}Cane was talking about investigations, of course. He failed to note that acknowledging and adjusting the faults in oneself also allows for the betterment of any great person. {/i}"

        chrome "{i}I can no longer dismiss the challenges that stem from my mistakes.{/i}"

        show chrome happy glitch 

        chrome "{i}I will improve.{/i}"

        call end_glitch
        $ chrome_on = True # turn on Chrome layer
        $ update_layers(0) # update layers

        show santa at right with dissolve

        pause 1.0

        $ glitch_counter +=1 # increment glitch counter

        chrome "{i}EZMK-2512 pointed to his neck, hidden behind the sheets of white metal serving as his makeshift beard. I can just make out a small USB port hidden within.{/i}"

        santa "Why {i}tell{/i} you about what I saw, when I can just show you?"

        #show santa happy

        chrome "{i}It’s like a sudden ray of light parting the confusion in my mind. Of course, it's so obvious! How could I have overlooked it?{/i}"

        chrome "{i}The android Santa smiled. Not everyday he gets one over on the “advanced” models.{/i}"

        chrome "You’re saying you give me the stored memory you have on last night?"

        jump scene10_postchoice

    label scene10_postchoice: 

        chrome "{i}As I begin to speak again, the android interrupts me.{/i}"

        show dialogue_box

        santa_nvl_right "If you notice, there’s cameras all over the place."

        santa_nvl_right "They would have easily captured what I saw, but I heard from the dimwit cop over there that someone trashed the CCTV."

        hide dialogue_box

        chrome "{i}The android pulled something small and thin out of the top of his head. A Hyman drive, meant for storing short term memory on an external device.{/i}"

        show dialogue_box

        santa_nvl_right "So, I’m your only option here. Take this and see what I saw that night."

        hide dialogue_box

        chrome "{i}Slowly, I reached for the drive and looked it over in my palm. Typically, sticking something a stranger gave me into my CPU was an ill-advised decision.{/i}"

        chrome "{i}Sticklers never have any fun though.{/i}"

        chrome  "{i}I jammed the drive into my neck and instantly was met with a flood of memories. All were locked but one, labeled “For you, detective”. I opened it.{/i}"

        #Visual Grayscale 

        hide chrome neutral with dissolve

        hide santa with dissolve 

        show larry sad at left with dissolve 

        show freddy sad at right with dissolve

        show cookietin at center with dissolve

        chrome "{i}Freddy and Larry walk out of the Department store, Freddy carrying a tin of what appears to be cookies between his arm and side.{/i}"

        hide cookietin in center with dissolve

        chrome "{i}Things seem tense between them, uncertain. Some words are exchanged, and Freddy hands the cookies to Larry with a stiff shrug. He walks off to sit down on the curb.{/i}"

        hide freddy neutral with moveoutright

        show cookies at center with dissolve

        pause 0.5

        hide cookies in center with dissolve

        show larry ecstatic 

        show eatencookie at center with dissolve 

        chrome "Larry moves to follow him, first taking out a cookie and taking a deep bite before walking over."

        pause 0.5

        hide eatencookie in center with dissolve 

        show larry neutral with hpunch

        show freddy shocked at right with moveinright

        chrome "{i}Before he can make it however, his eyes practically bulge out of his skull. He begins coughing like mad, choking on his own spit as Freddy watches in horror. {/i}"

        #VISUAL SCREEN SHAKE + AUDIO

        play sound sfx_impactmetal

        pause 0.5

        show larry dead with hpunch

        chrome "{i}He falls to the ground, the tin slamming to the cold pavement.{/i}"

        chrome "{i}Larry convulses for a minute, one arm clutching at his throat, the other desperately flailing for Freddy. It isn’t long before he goes limp, the life slowly fading from his eyes. {/i}"

        show freddy angry

        chrome "{i}Freddy looks around in panic, reaching in his pocket for something before pausing.{/i}"

        show freddy sad

        chrome "{i}He looks over Larry’s body again, appearing to be in thought, before running down into the alleyway of the department store and disappearing.{/i}"

        hide freddy neutral with moveoutright

        pause 1.0

        show mariah neutral at right with moveinright 

        chrome "{i}Just as it seems there’s nothing left to see, Mariah comes out of the department store.{/i}"

        show cookietin at center with dissolve

        show mariah confused 

        chrome "{i}She seems surprised at Larry’s body but not horrified, looking around quickly before taking the cookie tin and hiding it deep within a thick snowbank.{/i}"

        hide cookietin at center with dissolve

        chrome "{i}She then walks slowly over to the body, examining it. She pulls out her phone and begins to call someone before the video ends. {/i}"

        #VISUAL GRAYSCALE END

        hide larry with dissolve

        hide mariah neutral with dissolve

        show chrome neutral at left with dissolve:
            xzoom -1.0

        show santa at right with dissolve

        chrome "{i}If anything, this was the smoking gun, right? Clearly something was wrong with those cookies, and here was direct proof that Freddy had handed them over. But what was Mariah doing at the end? {/i}"

        chrome "{i}She didn’t seem that concerned with Larry, in fact it almost seemed like she was hiding evidence of the crime. But why?{/i}"

        chrome "{i}Freddy’s actions also didn’t seem like those of a killer. Did he know he was being watched? If he didn’t, then why run? None of it made any sense.{/i}"

        show dialogue_box

        santa_nvl_right "So? What do you think? Pretty interesting, wouldn’t you say?"

        chrome_nvl_left "You should have shown me this earlier."

        santa_nvl_right "And you should’ve asked."

        hide dialogue_box
        nvl clear

        chrome "{i}He wasn’t wrong. If I had asked him sooner, I might be farther along in this case.{/i}"

        chrome "{i}With more answers came more questions. One thing was certain though, Ms. Fowler was looking more involved in this case than she let on.{/i}"

        chrome "{i}Some snooping around was in order, and what better place than the bigwig’s office? {/i}"

        $ larry_santa_on = False
        $ update_layers() # turn off Santa layer
        jump scene11
