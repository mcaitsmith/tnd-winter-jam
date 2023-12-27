# The script of the scene goes in this file.

######### SCENE 11

# The scene starts here.

default pickedOne = False
default pickedTwo = False
default pickedThree = False
default pickedFour = False
default pickedFive = False


label scene11:


    scene bg mariahoffice night


    show chrome neutral at left

    chrome "Mariah’s office. It’s clean- meticulously so. Funny how the messiest people can also be the most fastidious."

    chrome unassuming "Seems Ms. Fowler isn’t in; surely she wouldn’t mind if I… poke around."

    call searchMenu

    "Seems like that’s about anything of interest."
    "I’ve got all the files I need. Not to mention these incriminating gloves."
    chrome shocked "Wait- that smell! I recognize it from Freddy’s apartment!"

    chrome thinking "My regards to Jack Scanlon- I know exactly where to find Freddy."

    # narration
    "Chrome paused at the window. He took one final look around the office."
    "He had the evidence: Mariah Fowler was going down."
    "Bianca’s hunch was right. Freddy was clean."
    "Now, Chrome just had to talk him out of hiding."
    "With a vocaloid grunt and a self-conscious shimmy, the android clambered up the fire escape."

    #options 1 2 and 3 are "critical path" clues- options 4 and 5 are just flavor text

    #End



    jump scene12

    return

label searchMenu:
    menu:
        chrome thinking "Let’s see…"

        # option one:
        "The computer looks suspicious…" if pickedOne == False:

            chrome "The computer looks suspicious…"
            $pickedOne = True
            # [LABELS for "deleted items", "games", "saved pictures", "recipes", "Santa Project". Kind of what we talked about in the writer/ programmer sync. Once they’ve been read, they don’t appear again as choices]
            call scene11comp
            jump searchMenu

        # option two:
        "What’s that in the trash…?" if pickedTwo == False:
            chrome "What’s that in the trash…?"
            $pickedTwo = True
            # UNLIKE option one, my thought was that players would just click through all of these options- and the final one returns them to the office proper


            "A banana peel, an empty cigarette pack…"
            "Some used napkins…"
            "Half-eaten takeout…"
            "Stale donuts…"
            chrome confused "Gloves? Hm. Latex. But there’s something else–"
            chrome shocked "Poison! Trace amounts, but it’s there."

            #Narration  
            "It matches the cookies that killed Larry!"
            jump searchMenu

        # option three:
        "Can’t believe she left the window open…" if pickedThree == False:
            $pickedThree = True
            chrome "Can’t believe she left the window open…"
            chrome "Organics are susceptible to cold."
            # Close Window?
            chrome thinking "My sensors are detecting a scent blowing in from outside."
            chrome thinking "Smoke- no, cloves. Clove cigarettes?"
            chrome shocked "Smells… clove-y. And familiar."
            jump searchMenu

        # option four: 
        "Some nice books on the shelf…" if pickedFour == False:
            $pickedFour = True
            chrome "Organics say there’s nothing like the smell of an old book."
            chrome thinking "I think I see the appeal."
            jump searchMenu

        # option five: 
        "That’s a nice plant." if pickedFive == False:
            $pickedFive = True
            chrome thinking "I should get myself a bonsai tree."
            jump searchMenu
    return

label scene11comp:
    menu:
        chrome "Let's see here..."
        "Select \'deleted items\'":
            chrome confused "Hm. Totally empty. And nothing hidden as far as I can tell."
            jump scene11comp
        "Select \'games\'":
            chrome happy "She’s got cyber solitaire on here?? Oo, and pinball!"
            jump scene11comp
        "Select \'saved pictures\'":
            chrome timid "Is that… Mariah in a bikini?"
            jump scene11comp
        "Select \'recipes\'":
            chrome thinking "Lots of cookie recipes here…"
            jump scene11comp
        "Select \'santa project\'": 
            chrome shocked "Ah-ha! Now we’re getting somewhere!"
            chrome thinking "Let’s see- looks like Fowler’s has been in the red for years."
            chrome thinking "Sales have been declining every holiday season…"
            chrome thinking "This program- some kind of credit card number skimming system."
            chrome angry "And here we’ve got some ‘creative’ accounting."
            chrome shocked "This is the list of ex-con Santas! Jackpot!"
    return