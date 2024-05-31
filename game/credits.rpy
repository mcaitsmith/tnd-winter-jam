# adapted from https://lemmasoft.renai.us/forums/viewtopic.php?t=42667
## ATL for scrolling screen object. In this case, credits roll.
## Speed is the time for object to move up from initial ypos to finish ypos.

# to call credits screen use commented code below at end of final game scene:
# $ quick_menu = False # hide quick menu
# call screen credits ## Show credits screen.
# return ## return to main menu

transform credits_scroll(speed):
    ypos 1080
    linear speed ypos -4500

## Credits screen.

screen credits():
    style_prefix "credits"

    add "#ffffff"

    # timer 10.0 action Return()
    timer 50.0 action Return()

    # frame at credits_scroll(10.0):
    frame at credits_scroll(40.0):
        background None
        xalign 0.5

        vbox:

            label "Credits"

            null height 20

            hbox:
                add "images/chrome_mini.png" 
                text "{b}CREATIVE\nDIRECTOR      {/b}"
                text "Andrea Saravia Pérez"

            hbox:
                add "images/santaboots_mini.png":
                    xzoom -1.0 
                text "{b}WRITING        {/b}"
                text "Robert Corra (Lead)\nLily Gwyer-Miller (Lead)\nJonathan Rhee (Lead)\nTiago Da Cunha\nCameron Daxon\nKyle Scarselli\nSalvador Bas Folch"

            hbox:
                add "images/bianca_mini.png"
                text "{b}EDITING        {/b}"
                text "Cameron Daxon\nJonathan Rhee\nSalvador Bas Folch\nSangita Nuli\nAnivette Wong"

            hbox:
                add "images/cookietin_mini.png" 
                text "{b}NARRATIVE\nDESIGN         {/b}"
                text "Robert Corra (Lead)\nLily Gwyer-Miller"

            hbox:
                add "images/freddy_mini.png"
                text "{b}ART               {/b}"
                text "Patrick Villegas (Lead)\nCharlotte Russe\nSerena Howard\nNajmah Salam"

            hbox:
                add "images/santatoy_mini.png":
                    xzoom -1.0
                text "{b}SOUND           {/b}"
                text "Andrea Saravia Pérez (Lead)\nArmoni Boone\nValentina \"Pache\" Bolívar\nFiorella Frieri\nVeronica Angulo"

            hbox:
                add "images/jack_mini.png" 
                text "{b}PROGRAMMING{/b}"
                text "Mica Smith (Lead)\nLeon Barillaro\nCameryn Tuliao\nAnivette Wong"

            hbox:
                add "images/gloves_mini.png"
                text "{b}PRODUCTION  {/b}"
                text "Salvador Bas Folch (Lead)\nTiago Da Cunha\nCameron Daxon\nAnivette Wong\nNajmah Salam"

            hbox:
                add "images/mariah_mini.png" 
                text "{b}LEAD\nGENERALIST  {/b}"
                text "Anivette Wong"

            hbox:
                add "images/santaclothes_mini.png"
                text "{b}MARKETING    {/b}"
                text "Najmah Salam (Lead)\nAndrea Saravia Pérez\nDylan Sands\nKyle Smith-Laird"

            hbox:
                add "images/santa_mini.png" 
                text "{b}QUALITY\nASSURANCE    {/b}"
                text "Sangita Nuli (Lead)\nMax Lincoln\nGideon Devendra\nLina Caro\nRafael Campbell\nCrowe Whitney\nRachel Lee\nLina Caro\nPatrick Christell"

            hbox:
                add "images/cigarettes_mini.png"
                text "{b}PLAYTESTERS{/b}"
                text "Max Lincoln\nGideon Devendra\nLina Caro\nRafael Campbell\nCrowe Whitney\nRachel Lee\nPatrick Christell\nAlice\nKyle Smith-Laird"

            hbox:
                add "images/larry_mini.png" 
                text "{b}PROJECT\nMANAGER       {/b}"
                text "Najmah Salam"

            vbox:
                text "{b}SPECIAL THANKS{/b}"
                text "Johans\nAlina Matson\nAlbert Bassili"

            vbox
            vbox
            vbox
            vbox

            vbox:
                add "images/logo.png"

            vbox:
                text "{b}SMALL LOAN STUDIO{/b}"
                text "https://smallloanstudio.wordpress.com"
                text "Thanks for playing!"

style credits_hbox:
    spacing 40
    ysize 30

style credits_vbox:
    xalign 0.5
    spacing 40
    ysize 30

style credits_vbox_logo:
    xalign 0.5
    spacing 40
    ysize 30

style credits_label:
    xalign 0.5

style credits_label_text:
    size gui.title_text_size*0.5

style credits_text:
    xalign 0.5
    color "#000"