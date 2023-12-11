# The script of the scene goes in this file.

######### SCENE 4: FOWLER'S DEPARTMENT STORE (outside store - woman by door, officer near alley, crime scene)

# The scene starts here.

label scene4:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show chrome neutral at left

    # These display lines of dialogue.

    chrome "Welcome to Scene 4."

    # next 3 subscenes can be played in any order

    ######### SCENE 4A: MARIAH FOWLER

    show mariah neutral at right

    mariah "This is Scene 4A."

    hide mariah

    ######### SCENE 4A-1: GLITCH 3

    show chrome neutral

    chrome "GLITCH GLITCH GLITCH"

    ######### back to SCENE 4A

    chrome "Woah that was weird"

    ######### SCENE 4B: COP

    show cop neutral at right

    cop "This is Scene 4B."

    hide cop

    ######### SCENE 4B-1: GLITCH 4

    show chrome neutral

    chrome "GLITCH GLITCH GLITCH"

    ######### back to SCENE 4B

    chrome "Woah that was weird"

    ######### SCENE 4C: CRIME SCENE (images of clues + internal narration? maybe clickable areas to discover clues?)

    chrome "This is Scene 4C."

    ######### SCENE 4D: MONOLOGUE (this looks like a murder, I'm dropping the case)

    chrome "Now we're going to Scene 5."

    # jump to next scene

    jump scene5