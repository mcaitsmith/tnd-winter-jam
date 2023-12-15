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

    chrome "Welcome to Scene 1."

    bianca_right "This is some dialogue. This is some more dialogue."

    chrome "And even more dialogue for good measure."

    hide dialogue_box # return to ADV mode

    larry "Now we're going to Scene 2."

    # jump to the next scene

    jump scene2
