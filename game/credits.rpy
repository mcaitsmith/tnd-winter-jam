# adapted from https://lemmasoft.renai.us/forums/viewtopic.php?t=42667
## ATL for scrolling screen object. In this case, credits roll.
## Speed is the time for object to move up from initial ypos to finish ypos.

# to call credits screen use commented code below at end of final game scene:
# $ quick_menu = False # hide quick menu
# call screen credits ## Show credits screen.
# return ## return to main menu

transform credits_scroll(speed):
    # ypos 720
    ypos 1080
    # linear speed ypos -720
    linear speed ypos -2000

## Credits screen.

screen credits():
    style_prefix "credits"

    add "#ffffff"

    timer 10.0 action Return()

    frame at credits_scroll(10.0):
        background None
        xalign 0.5

        vbox:
            label "Credits"

            null height 20

            hbox:
                add "images/chrome_mini.png" 
                text "{b}ROLE{/b}"
                text "NAME\nNAME\nNAME"

            hbox:
                add "images/bianca_mini.png" 
                text "{b}ROLE{/b}"
                text "NAME\nNAME\nNAME"

            hbox:
                add "images/freddy_mini.png" 
                text "{b}ROLE{/b}"
                text "NAME\nNAME\nNAME"

            hbox:
                add "images/jack_mini.png" 
                text "{b}ROLE{/b}"
                text "NAME\nNAME\nNAME"

            hbox:
                add "images/mariah_mini.png" 
                text "{b}ROLE{/b}"
                text "NAME\nNAME\nNAME"

            hbox:
                add "images/santa_mini.png" 
                text "{b}ROLE{/b}"
                text "NAME\nNAME\nNAME"

            hbox:
                add "images/larry_mini.png" 
                text "{b}ROLE{/b}"
                text "NAME\nNAME\nNAME"


style credits_hbox:
    spacing 40
    ysize 30

style credits_label:
    xalign 0.5

style credits_label_text:
    size gui.title_text_size*0.5

style credits_text:
    xalign 0.5
    color "#000"