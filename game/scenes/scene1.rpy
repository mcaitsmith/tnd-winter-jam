# The script of the scene goes in this file.

######### SCENE 1: "THE TEASE" (crime scene: bg of dept store, Larry dead)

# The scene starts here.

label scene1:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg office

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show dialogue_box at center

    show chrome neutral at left:
        xzoom -1
    show bianca neutral at right

    # These display lines of dialogue.

    # chrome "Welcome to Scene 1."

    bianca_right "Hey, you listening to me? It’s.. it’s my dad, Freddy…"

    bianca_right "He’s gone missing."

    chrome "Have you gone to the authorities?"

    bianca_right "Pff, the cops have no time for me and my dad."

    bianca_right "They just told me to wait ‘til he comes home from whatever bender he’s on."

    chrome "Perhaps they’re right."

    hide dialogue_box # return to ADV mode

    larry "Now we're going to Scene 2."

    # jump to the next scene

    jump scene2
