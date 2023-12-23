# The script of the scene goes in this file.

label scene5:


    scene bg Fowlers department

    show chrome neutral at left:
        xzoom -1.0

    chrome "{i}Fowler’s Department Store. Still surviving, but barely.{/i}"

    chrome "{i}Fowler’s was a lot like every other department store out there, just missing the large corporate logos for a smaller one.{/i}"

    chrome "{i}The large store was littered with multi-colored lights that would have been artful if it weren’t for all the missing bulbs.{/i}"

    chrome "{i}The holiday season was in full swing, yet the parking lot was only half full.{/i}"

    chrome "{i}Maybe it’s because in person shopping was dying a slow death.{/i}"

    chrome "{i}Maybe it was because of the horde of cop cars swarmed near the side of the store overpowering the festive lights with flashing red and blue.{/i}"

    chrome "{i}There was a small crowd of onlookers. It would have been larger, but the winter chill was warding all but the most curious.{/i}"

    chrome "{i}I join them and my advanced height makes it easy to see what has gathered the crowd.{/i}"

    chrome "{i}A chalk outline on the ground. It can only mean one thing. There was a death here.{/i}"

    #VISUAL- Police lights? 

    # SOUND- Crowds murmuring. 

    hide chrome with dissolve

    show mariah angry at left with moveinleft

    chrome "{i}Someone comes out of the front door and starts yelling. A middle aged woman, grisled by decades of holiday shoppers, clears the crowd out with practiced ease.{/i}"

    chrome "{i}That was Mariah Fowler, owner of the dying store.{/i}"

    show mariah angry at right with moveinleft

    pause 0.5

    show cop neutral at left with moveinleft:
        xzoom -1.0

    chrome "{i}A police officer follows behind her, asking questions. Judging from the prominent scowl on his face, he’s not happy with the answers he’s receiving.{/i}"

    chrome "{i}Mariah Fowler trades some words with the cop on the scene before scaring him away with a vicious scowl.{/i}"

    hide cop neutral with moveoutleft

    chrome "{i}Finally, Mariah Fowler yells at the Robot dressed as Santa Claus standing at the door.{/i}"

    mariah "And ring that bell louder! Now that the lookie loos are gone, I expect you to hit your quota, you hear me!"

    show chrome thinking at left with moveinleft: 
        xzoom -1.0

    chrome "Well, it seems like I’ve found the best people to talk to about Freddy."

    menu: 
        chrome "{i}I should talk to… {/i}"

        "The owner of the department store. They’ll know the store better than anyone. If Freddy has been here, they’ll know.":
            jump scene5_owner 
        "That crime scene is super suspicious. It might be connected to Freddy and his suspicious behavior at home. I should investigate.":
            jump scene5_crimescene 

        "There are cops all over the place. Something important happened here. I should talk to one of them and see if they know anything about Freddy… and this crime.":
            jump scene5_cops


    label scene5_owner: 

        chrome "This menu choice wasn't written yet by the time of implementation."

        jump scene5_postchoice 

    label scene5_crimescene:

        chrome "This menu choice wasn't written yet by the time of implementation."

        jump scene5_postchoice


    label scene5_cops:

        chrome "This menu choice wasn't written yet by the time of implementation."

        jump scene5_postchoice

    label scene5_postchoice: 

        chrome "Now we're going to Scene 6."

        # jump to the next scene

        jump scene6