# The script of the scene goes in this file.

######### SCENE 11: MARIAH'S OFFICE

# The scene starts here.

default pickedOne = False
default pickedTwo = False
default pickedThree = False
default pickedFour = False
default pickedFive = False


label scene11:


    scene bg mariahoffice with fade


    show chrome neutral at left:
        xzoom -1.0

    chrome "{i}Mariah’s office. It’s clean- meticulously so. Funny how the messiest people can also be the most fastidious.{/i}"

    chrome timid "{i}Seems Ms. Fowler isn’t in; surely she wouldn’t mind if I… poke around.{/i}"

    call searchMenu from _call_searchMenu

    chrome neutral "{i}Seems like that’s about everything of interest.{/i}"
    chrome "{i}I’ve got all the intel I need.{/i}"
    chrome shocked "{i}Wait- that smell! I recognize it from Freddy’s apartment!{/i}"

    chrome logical "{i}I know exactly where to find him...{/i}"

    # narration
    chrome neutral "{i}I send my regards to good ol' Jack Scanlon- as well as my location. A little insurance, just in case.{/i}"
    chrome "{i}I pause at the window to take one final look around the office.{/i}"
    chrome "{i}Who knew the search for a two-bit Santa would lead to all this.{/i}"
    chrome "{i}But first things first. Bianca’s hunch was right all along. Freddy was clean.{/i}"
    chrome "{i}And the fire escape beckoned. I'll deal with Mariah later.{/i}"

    #options 1 2 and 3 are "critical path" clues- options 4 and 5 are just flavor text

    #End



    jump scene12

    return

label searchMenu:
    show chrome confused left at left:
        xzoom -1.0
    menu:
        chrome "{i}Let’s see…{/i}"

        # option one:
        "The computer looks suspicious…" if pickedOne == False:

            chrome "{i}The computer looks suspicious…{/i}"
            $pickedOne = True
            # [LABELS for "deleted items", "games", "saved pictures", "recipes", "Santa Project". Kind of what we talked about in the writer/ programmer sync. Once they’ve been read, they don’t appear again as choices]
            call scene11comp from _call_scene11comp
            jump searchMenu

        # option two:
        "What’s that in the trash…?" if pickedTwo == False:
            chrome neutral "{i}What’s that in the trash…?{/i}"
            $pickedTwo = True
            # UNLIKE option one, my thought was that players would just click through all of these options- and the final one returns them to the office proper


            chrome "{i}A banana peel, an empty cigarette pack…{/i}"
            chrome "{i}Some used napkins…{/i}"
            chrome "{i}Half-eaten takeout…{/i}"
            chrome "{i}Stale donuts…{/i}"
            chrome confused left "{i}Gloves? Hm. Latex. But there’s something else–{/i}"
            chrome shocked "{i}Poison! Trace amounts, but it’s there.{/i}"
            chrome angry "{i}Even one bite of this could kill a man...{/i}"

            jump searchMenu

        # option three:
        "Can’t believe she left the window open…" if pickedThree == False:
            $pickedThree = True
            chrome neutral "{i}Can’t believe she left the window open…{/i}"
            chrome "{i}Organics are susceptible to cold.{/i}"
            # Close Window?
            chrome thinking left "{i}My sensors are detecting a scent blowing in from outside.{/i}"
            chrome thinking left "{i}Smoke- no, cloves. Clove cigarettes?{/i}"
            chrome shocked "{i}Smells… clove-y. And familiar.{/i}"
            jump searchMenu

        # option four: 
        "Some nice books on the shelf…" if pickedFour == False:
            $pickedFour = True
            chrome neutral "{i}Organics say there’s nothing like the smell of an old book.{/i}"
            chrome logical "{i}I think I see the appeal.{/i}"
            jump searchMenu

        # option five: 
        "That’s a nice plant." if pickedFive == False:
            $pickedFive = True
            chrome logical "{i}I should get myself a bonsai tree.{/i}"
            jump searchMenu
    return

label scene11comp:
    menu:
        chrome logical "{i}Let's see here...{/i}"
        "Select \'deleted items\'":
            chrome confused left "{i}Hmm. Totally empty. And nothing hidden as far as I can tell.{/i}"
            jump scene11comp
        "Select \'games\'":
            chrome happy "{i}She’s got cyber solitaire on here?? Ooh, and pinball!{/i}"
            jump scene11comp
        "Select \'saved pictures\'":
            chrome embarrassed "{i}Is that… Mariah in a bikini?{/i}"
            jump scene11comp
        "Select \'recipes\'":
            chrome unassuming "{i}Lots of cookie recipes here…{/i}"
            jump scene11comp
        "Select \'santa project\'": 
            chrome shocked "{i}Ah-ha! Now we’re getting somewhere!{/i}"
            chrome logical "{i}Let’s see- looks like Fowler’s has been in the red for years.{/i}"
            chrome logical "{i}Sales have been declining every holiday season…{/i}"
            chrome logical "{i}This program- some kind of credit card number skimming system.{/i}"
            chrome angry "{i}And here we’ve got some ‘creative’ accounting.{/i}"
            chrome angry "{i}Classic charity scam. Santas aggressively ask for donations, and the bulk of it goes to Mariah's pockets.{/i}"
            chrome shocked "{i}Seems like each Santa had a criminal record. Something Mariah was well aware of...{/i}"
            chrome angry "{i}Mariah must have kept their info under wraps in exchange for getting them to do her dirty work.{/i}"
            chrome angry "{i}Mariah offers them a job. And they don't dare push back because she threatens to expose them.{/i}"
            chrome angry "{i}Who are the cops to believe? An ex-con, like Freddy, or a respected business owner?{/i}"

    return