# The script of the scene goes in this file.

# SCENE 5: FOWLER'S DEPARTMENT STORE (INTRO)

label scene5:

    scene bg extstore night

    show chrome neutral at left:
        xzoom -1.0

    chrome "{i}Fowler’s Department Store. Still surviving. Barely.{/i}"

    chrome "{i}Multi-colored lights litter the large storefront. Festive, if not for all the missing bulbs.{/i}"

    chrome "{i}That and the flashing red and blue lights of the cop cars swarmed near the side of the building.{/i}"

    chrome "{i}A small crowd of onlookers hover near the scene, the winter chill warding off all but the most curious.{/i}"

    chrome "{i}When I join them, I spot a ghastly chalk outline on the ground. That can only mean one thing.{/i}"

    #VISUAL- Police lights? 

    # SOUND- Crowds murmuring. 

    hide chrome with dissolve

    show mariah angry at left with moveinleft

    chrome "{i}Before I can get too cozy, a middle-aged woman bursts out the door, barking at everyone in sight.{/i}"

    chrome "{i}I recognize her as Mariah Fowler, owner of the retail dinosaur. Grizzled by decades of holiday shoppers, she clears the crowd with practiced ease.{/i}"

    show mariah angry at right with moveinleft

    pause 0.5

    show cop neutral at left with moveinleft:
        xzoom -1.0

    chrome "{i}A police officer follows behind her, trying his best to ask questions. By the look on his face, he’s not happy with the answers.{/i}"

    chrome "{i}Mariah trades some words with the cop before scaring him away for good.{/i}"

    hide cop neutral with moveoutleft

    chrome "{i}Not done yet, she yells at a rickety Robot Santa stationed by the door.{/i}"

    mariah "And ring that bell louder! Now that the lookie loos are gone, I expect you to hit your quota, you hear me!"

    show chrome thinking left at left with moveinleft

    chrome "{i}Having seen enough, I consider my next steps...{/i}"

    chrome "{i}I should talk to the owner of the department store. If Freddy has been here, they’ll know.{/i}"
    
    jump scene6