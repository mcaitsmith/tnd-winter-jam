# The script of the scene goes in this file.

### SCENE 13: FREDDY'S APARTMENT (ending)

# The scene starts here.

label scene13:

    scene bg office with fade

    show chrome neutral at right with dissolve

    if glitch_counter < 3: # bad ending
        chrome "{i}Back at the office, Bianca and Freddy reunite. Freddy is crestfallen- he's lost a friend after all. However, seeing his daughter's face brings some light back to his eyes.{/i}"
    else:
        chrome "{i}Back at the office, Bianca and Freddy get to reunite in peace.{/i}"

    chrome "{i}The kid’s been through a lot, but she’s a fighter.{/i}"
    chrome "{i}Just like her dad, I guess.{/i}"

    show bianca happy at left with dissolve
    bianca happy "Thanks again, Steele. You really came through."
    bianca neutral "I told you my dad was innocent. He just needs a chance."
    chrome neutral "You have that chance now, Freddy. Make the best of it. If not for you, then for Bianca’s sake."
    hide bianca with dissolve
    show freddy neutral at left:
        xzoom -1.0
    with dissolve
    freddy neutral "Yeah, I know how lucky I am. You don’t have to tell me twice!"
    freddy neutral "The whole Santa thing..."
    freddy angry "Before I knew it, I was in too deep."
    freddy angry "At first, I wanted to do something good for a change, but Mariah... she had other plans."
    freddy sad "I can’t believe how cold she is, to stoop that low. Poor Larry..."
    if glitch_counter < 3: # bad ending
        freddy sad "Jack too... if it weren't for me, he'd never have gotten caught up in this mess. {i}Qué mundo...{/i}"
    chrome sad "My... mentor... once said, there’s nothing colder than the human heart."
    chrome neutral "I now disagree."
    chrome neutral "For every Mariah there’s a Freddy, or a Jack, just trying their best."
    chrome neutral "Each one of a kind, like how two jazz sessions are never the same."
    hide freddy with dissolve
    show bianca at left
    bianca neutral "You think that’s true for androids too?"
    chrome "..."
    hide bianca with dissolve
    show freddy neutral at left:
        xzoom -1.0
    freddy neutral "Well, one thing’s for sure, there ain’t another android like you."
    freddy neutral "Hell, there ain’t no other detective like you either."
    chrome neutral "I suppose that’s true."
    freddy happy "You’re alright, Steele... for a droid, and all. No offense."
    freddy neutral "But seriously, thank you. I mean it."
    hide freddy with dissolve
    show bianca neutral at left with dissolve
    bianca neutral "Hey listen, I know I can never repay you, but if you need some help on the next case..."
    bianca happy "or a partner even, you know where to find me."
    chrome happy "I might take you up on that."
    hide bianca with dissolve
    show freddy neutral at left:
        xzoom -1.0
    freddy neutral "Speaking of which, what’s next for ya, Steele?"
    chrome neutral "I... may have a case in mind."
    chrome neutral "Either way, it’s time I stepped out of the shadows."
    hide freddy

    $ chrome_on = True
    $ update_layers() # turn on Chrome layer
    $ start_layers() # resume music
    chrome "{i}A wise man once said, there‘s no thicker malaise than one of your own making.{/i}"
    chrome "{i}For the first time in a long time, I’m sure of my purpose.{/i}"
    chrome "{i}Chrome Steele P.I. is back in business.{/i}"
    chrome "{i}I technically always was, but this time...{/i}"
    chrome "{i}...there ain’t no man or android that’s gonna hold me back.{/i}"
    chrome "{i}Myself included.{/i}"

    if glitch_counter >= 5:
        call secret_ending from _call_secret_ending # secret ending
    else:
        $ stop_layers(3) # stop playing layers
        play music bar_music fadein 1

    scene black # fade to black
    with fade

    # CALL CREDITS
    $ quick_menu = False # hide quick menu
    $ renpy.transition(dissolve)
    call screen credits ## Fade to credits screen.

    return ## return to main menu