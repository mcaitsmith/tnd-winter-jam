# The script of the scene goes in this file.

# SCENE 5: FOWLER'S DEPARTMENT STORE (INTRO)

$ intro_text = 0

	if intro_text < 1:

	label scene5:

    		scene bg extstore night with fade

    		show policelights with dissolve

    		show chrome neutral at left:
        		xzoom -1.0
    		with moveinleft

    		chrome "{i}Fowler’s Department Store. Still surviving. Barely.{/i}"

    		chrome "{i}Multi-colored lights litter the large storefront. Festive, if not for all the missing bulbs.{/i}"

    		chrome "{i}That and the flashing red and blue lights of the cop cars swarmed near the side of the building.{/i}"

    		chrome "{i}A small crowd of onlookers hover near the scene, the winter chill warding off all but the most curious.{/i}"

    		chrome "{i}When I join them, I spot a ghastly chalk outline on the ground. That can only mean one thing.{/i}"

    		#VISUAL- Police lights? 

    		# SOUND- Crowds murmuring. 

    		hide chrome with moveoutleft

    		show mariah angry at left with moveinleft

    		chrome "{i}Before I can get too cozy, a middle-aged woman bursts out the door, barking at everyone in sight.{/i}"

    		chrome "{i}I recognize her as Mariah Fowler, owner of the retail dinosaur. Grizzled by decades of holiday shoppers, she clears the crowd with practiced ease.{/i}"

    		show mariah angry at left:
        		xzoom -1.0
   		show mariah angry at right with moveinleft
    		show mariah angry at right:
        		xzoom 1.0

    		pause 0.5

    		show cop neutral at left with moveinleft:
        		xzoom -1.0

    		chrome "{i}A police officer follows behind her, trying his best to ask questions. By the look on his face, he’s not happy with the answers.{/i}"

    		chrome "{i}Mariah trades some words with the cop before scaring him away for good. Meanwhile, another cop walks out from the alleyway behind the department store with a grim look on their face.{/i}"

    		show cop neutral at left:
        		xzoom 1.0
    		hide cop neutral with moveoutleft

    		chrome "{i}Not satisfied with just one rough conversation, Mariah yells at a rickety Robot Santa stationed by the door.{/i}"

    		mariah "And ring that bell louder! Now that the lookie loos are gone, I expect you to hit your quota, you hear me!"

    		hide policelights with dissolve

    		show chrome thinking left at left:
        		xzoom -1.0
    		with moveinleft

    		chrome "{i}Having seen enough, I consider my next steps.{/i}"

$ scene5_choice1 = False
    $ scene5_choice2 = False
    $ scene5_choice3 = False

$ intro_text += 1

if intro_text >= 1:	
    menu helpful:
        chrome "What should I investigate now?"
        "Mariah Fowler" if scene5_choice1 == False:
            jump fowler
        "{s}Mariah Fowler{/s}" if scene5_choice1 == True:
            jump fowler
        "Police Officer" if scene5_choice2 == False:
            jump cop
        "{s}Police Officer{/s}" if scene5_choice2 == True:
            jump cop
        "Alleyway" if scene5_choice3 == False: 
            jump alley
        "{s}Alleyway{/s}" if scene5_choice3 == True: 
            jump alley


label fowler:

	if scene5_choice2 == True:

		show chrome neutral at left

		chrome sad "{i}Things just got a lot more complicated. A suspicious death? Freddy as a person of interest? The kid isn’t gonna like 		this.{/i}"

		chrome neutral "{i}I should speak with Fowler, try to get a sense of the relationship between Freddy and this ‘Larry’ character.{/i}"

		jump scene 6

	if scene5_choice3 == True:

		show chrome neutral at left

		chrome neutral "{i}Clearly this “Larry” character worked with Freddy, and they were arguing over something. Pretty harsh words for a 			little disagreement.{/i}"

		chrome neutral "{i}I should speak with Fowler, see if she knew why these two had it out for each other.{/i}"

		jump scene 6

	if scene 5_choice2 and scene5_choice3 == True:

		show chrome neutral at left

		chrome neutral "{i}If it wasn’t clear before then it is now: Freddy and Larry were friends. Seems like that relationship went sour 		recently.{/i}"

		chrome neutral "{i}What were they arguing about? Could it have driven Freddy to murder somehow?{/i}"

		chrome neutral "{i}No, murder is too far a leap to take so early in this investigation. I should speak to Fowler, get a better idea of 		the relationship between these two.{/i}" 

		jump scene 6

	else:

		show chrome neutral at left	
		chrome "{i}I should talk to the owner of the department store. If Freddy has been here, they’ll know.{/i}"
		jump scene 6

label cop:

	if scene5_choice1 == True:

		show chrome neutral at left

		chrome "{i}Well that wasn’t very pleasant. Still, it did give me an idea of what’s going on here.{/i}"
		
		chrome "{i}Freddy and Larry get into an argument. Suddenly one is dead and the other’s missing?{/i}"

		chrome "{i}If I didn’t know any better, I’d say this was an open and shut case. Our dear Freddy’s out on the lam.{/i}"

		chrome sad "{i}But unfortunately, things are rarely that simple.{/i}"

		chrome sad "{i}Might as well see what the fuzz have found out. Although knowing the cops in this city… it probably isn’t much.{/i}"
		jump scene 7

	if scene5_choice3 == True:

		show chrome neutral at left

		chrome "{i}So I’m guessing our victim is Larry… and he knew Freddy somehow. Some sort of argument between them? Maybe this little 		detour will bear some fruit.{/i}"

		chrome "{i}Not a lot to go off of here Freddy-wise. I should speak with the boys in blue, see if they’ve heard anything about him. 		It's doubtful, but I'm feeling lucky.{/i}"
		jump scene 7

	if scene5_choice1 and scene5_choice3 == True:

		show chrome neutral at left

		chrome "{i}Well Mariah wasn’t wrong, these two definitely had a pretty bad falling out. But could it lead to murder?{/i}"

		chrome "{i}I should speak with the boys in blue, see what they’ve figured out.{/i}"

		chrome sad "{i}Although knowing the cops in this city… it probably isn’t much.{/i}"
		jump scene 7

	else:
	
		show chrome neutral at left
		chrome "{i}Cops can't be good news. I should figure out what all the commotion is about before starting my investigation.{/i}"
		jump scene 7	

label alley:

	if scene5_choice 1 == True:

		show chrome neutral at left

		chrome "{i}So Freddy and this Larry character get into an argument. Suddenly one is dead and the other’s missing?{/i}"

		chrome "{i}If I didn’t know any better, I’d say this was an open and shut case. Our dear Freddy’s out on the lam.{/i}"

		chrome sad "{i}But unfortunately, things are rarely that simple. I’d better take a look at our poor victim, see if there’s any 		evidence that hasn’t been picked over by the fuzz.{/i}"

	if scene5_choice 2 == True:

		show chrome neutral at left

		chrome "{i}Things just got a lot more complicated. A suspicious death? Freddy as a person of interest? The kid isn’t gonna like this.		{/i}"
			
		chrome "{i}I should take a look at the crime scene, see if Freddy left any clues in his rush out of here.{/i}"
	
		jump scene 8

	if scene5_choice 1 and scene5_choice 2 == True:

		show chrome neutral at left

		chrome "{i}The more I learn about this, the more things look worse for Freddy.{/i}"

		chrome "{i}Something’s gnawing at me though. It’s never that simple. He clearly ran, but why? And why was Mariah so insistent on 			Freddy’s guilt?{/i}"

		chrome "{i}I’ve put it off long enough. I should look at the actual crime scene, see if Freddy left any clues in his rush out of 			here.{/i}"
		
		jump scene 8

	else: 
	
	show chrome neutral at left
	chrome "{i}That cop seemed mighty perturbed by whatever's in that alleyway. Maybe I should poke around.{/i}"
	jump scene 8
    
    