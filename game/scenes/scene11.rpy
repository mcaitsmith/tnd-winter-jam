# The script of the scene goes in this file.

######### SCENE 11: MARIAH'S OFFICE

# The scene starts here.

default pickedOne = False
default pickedTwo = False
default pickedThree = False
default pickedFour = False
default pickedFive = False

default computer_choice1 = False
default computer_choice2 = False
default computer_choice3 = False
default computer_choice4 = False
default computer_choice5 = False


label scene11:


    scene bg mariahoffice with fade


    show chrome neutral at left:
        xzoom -1.0

    chrome "{i}Mariah’s office. It’s clean- meticulously so. Funny how the messiest people can also be the most fastidious.{/i}"

    chrome timid "{i}Seems Ms. Fowler isn’t in; surely she wouldn’t mind if I… poke around.{/i}"

    jump searchMenu

label searchMenu:
    show chrome confused left at left:
        xzoom -1.0
    menu:
        chrome "{i}Let’s see…{/i}"

        # option one:
        "The computer looks suspicious…" if pickedOne == False:
            call computer
        "{s}The computer looks suspicious…{/s}" if pickedOne == True:
            call computer

        # option two:
        "What’s that in the trash…?" if pickedTwo == False:
            call trash
        "{s}What’s that in the trash…?{/s}" if pickedTwo == True:
            call trash

        # option three:
        "Can’t believe she left the window open…" if pickedThree == False:
            call window
        "{s}Can’t believe she left the window open…{/s}" if pickedThree == True:
            call window

        # option four: 
        "Some nice books on the shelf…" if pickedFour == False:
            call books
        "{s}Some nice books on the shelf…{/s}" if pickedFour == True:
            call books

        # option five: 
        "That’s a nice plant." if pickedFive == False:
            call plant
        "{s}That’s a nice plant.{/s}" if pickedFive == True:
            call plant

menu scene11comp:
    chrome logical "{i}Let's see here...{/i}"
    "Select \'deleted items\'" if computer_choice1 == False:
        call deleteditems
    "{s}Select \'deleted items\'{/s}" if computer_choice1 == True:
        call deleteditems
    "Select \'games\'" if computer_choice2 == False:
        call games
    "{s}Select \'games\'{/s}" if computer_choice2 == True:
        call games
    "Select \'saved pictures\'" if computer_choice3 == False:
        call savedpictures
    "{s}Select \'saved pictures\'{/s}" if computer_choice3 == True:
        call savedpictures
    "Select \'recipes\'" if computer_choice4 == False:
        call recipes
    "{s}Select \'recipes\'{/s}" if computer_choice4 == True:
        call recipes
    "Select \'santa project\'" if computer_choice5 == False: 
        call santaproject
    "{s}Select \'santa project\'{/s}" if computer_choice5 == True: 
        call santaproject

label computer:
    chrome "{i}The computer looks suspicious…{/i}"
    $pickedOne = True
    # [LABELS for "deleted items", "games", "saved pictures", "recipes", "Santa Project". Kind of what we talked about in the writer/ programmer sync. Once they’ve been read, they don’t appear again as choices]
    call scene11comp from _call_scene11comp
    if pickedOne == True and pickedTwo == True and pickedThree == True and pickedFour == True and pickedFive == True:
        jump finished_search
    else:
        jump searchMenu

label trash:
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

    if pickedOne == True and pickedTwo == True and pickedThree == True and pickedFour == True and pickedFive == True:
        jump finished_search
    else:
        jump searchMenu

label window:
    $pickedThree = True
    chrome neutral "{i}Can’t believe she left the window open…{/i}"
    chrome "{i}Organics are susceptible to cold.{/i}"
    # Close Window?
    chrome thinking left "{i}My sensors are detecting a scent blowing in from outside.{/i}"
    chrome thinking left "{i}Smoke- no, cloves. Clove cigarettes?{/i}"
    chrome shocked "{i}Smells… clove-y. And familiar.{/i}"
    if pickedOne == True and pickedTwo == True and pickedThree == True and pickedFour == True and pickedFive == True:
        jump finished_search
    else:
        jump searchMenu

label books:
    $pickedFour = True
    chrome neutral "{i}Organics say there’s nothing like the smell of an old book.{/i}"
    chrome logical "{i}I think I see the appeal.{/i}"
    if pickedOne == True and pickedTwo == True and pickedThree == True and pickedFour == True and pickedFive == True:
        jump finished_search
    else:
        jump searchMenu

label plant:
    $pickedFive = True
    chrome logical "{i}I should get myself a bonsai tree.{/i}"
    if pickedOne == True and pickedTwo == True and pickedThree == True and pickedFour == True and pickedFive == True:
        jump finished_search
    else:
        jump searchMenu

label deleteditems:
    chrome confused left "{i}Hmm. Totally empty. And nothing hidden as far as I can tell.{/i}"
    $computer_choice1 = True
    if computer_choice1 == True and computer_choice2 == True and computer_choice3 == True and computer_choice4 == True and computer_choice5 == True:
        if pickedOne == True and pickedTwo == True and pickedThree == True and pickedFour == True and pickedFive == True:
            jump finished_search
        else:
            jump searchMenu
    else:
        jump scene11comp

label games:
    chrome happy "{i}She’s got cyber solitaire on here?? Ooh, and pinball!{/i}"
    $computer_choice2 = True
    if computer_choice1 == True and computer_choice2 == True and computer_choice3 == True and computer_choice4 == True and computer_choice5 == True:
        if pickedOne == True and pickedTwo == True and pickedThree == True and pickedFour == True and pickedFive == True:
            jump finished_search
        else:
            jump searchMenu
    else:
        jump scene11comp

label savedpictures:
    chrome embarrassed "{i}Is that… Mariah in a bikini?{/i}"
    $computer_choice3 = True
    if computer_choice1 == True and computer_choice2 == True and computer_choice3 == True and computer_choice4 == True and computer_choice5 == True:
        if pickedOne == True and pickedTwo == True and pickedThree == True and pickedFour == True and pickedFive == True:
            jump finished_search
        else:
            jump searchMenu
    else:
        jump scene11comp

label recipes:
    chrome unassuming "{i}Lots of cookie recipes here…{/i}"
    $computer_choice4 = True
    if computer_choice1 == True and computer_choice2 == True and computer_choice3 == True and computer_choice4 == True and computer_choice5 == True:
        if pickedOne == True and pickedTwo == True and pickedThree == True and pickedFour == True and pickedFive == True:
            jump finished_search
        else:
            jump searchMenu
    else:
        jump scene11comp

label santaproject:
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
    $computer_choice5 = True
    if computer_choice1 == True and computer_choice2 == True and computer_choice3 == True and computer_choice4 == True and computer_choice5 == True:
        if pickedOne == True and pickedTwo == True and pickedThree == True and pickedFour == True and pickedFive == True:
            jump finished_search
        else:
            jump searchMenu
    else:
        jump scene11comp

label finished_search:
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