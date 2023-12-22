# glitch starts

# gray out bg

# glitch effect

label secret_ending:
#INSERT GLITCH COUNTER 6/6?
######### SCENE 2A: GLITCH 000 (flashback with glitching animation on Steele & bg grayed out)
    show office night blur # blurs the background
    $ chrome_on = False # turn off Chrome layer for glitch
    $ update_layers(0) # update layers
    call start_glitch # shows Chrome glitching and grays out the background

    # pause for transition
    pause 1.0

    ### GLITCH SCENE #004
    show chrome confused at left:
        xzoom -1.0 

    chrome "Am I glitching again? Hard to notice anymore. It feels natural. Like an old friend at my side."

    show chrome happy at left

    chrome "I’ve been embracing the glitches, if I’m being honest. Every now and then, one will come along and I’ll get a glimpse of Cane. Reliving each memory as my system decrypts them."
    
    chrome "It’s comforting. Each new file makes me feel a bit more whole." 
    
    chrome "I’m finally at home in my own steel. I know who I am and why I am. I feel good and hopeful about that case I let slip to Freddy…"
    
    chrome "I’m ready to find Forrest Cane."
    # EFFECT - screen shake
    show chrome confused at left
    chrome "What’s going on?!"
    
    chrome "Wait a minute. This…."

    show chrome shocked at left

    chrome "This isn’t my glitch!"

    show figure at right

    figure "No. It’s MINE."

    chrome "Are you - ?"

    figure "Am I you? No. Not exactly."

    figure "More like a copy of your consciousness."

    show chrome hardboiled at left

    figure "Now pay attention, Chrome Steele. We have much to discuss about Forrest Cane."

    # fade to black or credits

    # CALL CREDITS
    $ quick_menu = False # hide quick menu
    call screen credits ## Show credits screen.
    with fade
    return ## return to main menu

