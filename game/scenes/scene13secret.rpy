
### SCENE 13 SECRET ENDING

# glitch starts

# gray out bg

# glitch effect

label secret_ending:
#INSERT GLITCH COUNTER 6/6?
######### SCENE 2A: GLITCH 000 (flashback with glitching animation on Steele & bg grayed out)
    # scene bg office blur with fade # blurs the background
    $ chrome_on = False # turn off Chrome layer for glitch
    $ update_layers(0) # update layers
    call start_glitch from _call_start_glitch_2 # shows Chrome glitching and grays out the background

    # pause for transition
    # pause 1.0

    ### GLITCH SCENE #004
    show chrome confused glitch at right

    chrome confused glitch "{i}Am I glitching again? Hard to notice anymore. It feels natural. Like an old friend at my side.{/i}"

    chrome happy glitch "{i}I’ve been embracing the glitches, if I’m being honest. Every now and then, one will come along and I’ll get a glimpse of Cane. Reliving each memory as my system decrypts them.{/i}"
    
    chrome happy glitch "{i}It’s comforting. Each new file makes me feel a bit more whole.{/i}" 
    
    chrome happy glitch "{i}I’m finally at home in my own steel. I know who I am and why I am. I feel good and hopeful about that case I let slip to Freddy…{/i}"
    
    chrome happy glitch "{i}I’m ready to find Forrest Cane.{/i}"

    # screen shake
    show bg glitchvoid with hpunch

    chrome confused glitch "{i}What’s going on?!{/i}"
    
    chrome confused glitch "{i}Wait a minute. This…{/i}"

    chrome shocked glitch "{i}This isn’t my glitch!{/i}"

    show figure at left:
        xzoom -1.0

    figure "{i}No. It’s MINE.{/i}"

    chrome shocked glitch "{i}Are you - ?{/i}"

    figure "{i}Am I you? No. Not exactly.{/i}"

    figure "{i}More like a copy of your consciousness.{/i}"

    show chrome angry glitch at right

    figure "{i}Now pay attention, Chrome Steele. We have much to discuss about Forrest Cane.{/i}"

    return

