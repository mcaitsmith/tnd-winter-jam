# The main script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define larry = Character("Larry Moss", color="#2fb525")
define chrome = Character("Chrome Steele", color="#a5a5a5")
define bianca = Character("Bianca Fontaine", color="#45b7f0")
define freddy = Character("Freddy Fontaine", color="#f07635")
define jack = Character("Jack Scanlon", color="#dbd839")
define mariah = Character("Mariah Fowler", color="#d339db")
define cop = Character("Generic Cop", color="#2d30d9")
define santa = Character("Robot Santa", color="#ff0000")
define narration = Character("Narration", kind=nvl)

# define images for each character
image larry dead = "larry dead.png"
image chrome neutral = "chrome neutral.png"
image chrome neutral glitch = Glitch("chrome neutral.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
image chrome shocked = "chrome shocked.png"
image chrome thinking = "chrome thinking.png"
image chrome timid = "chrome timid.png"
image chrome angry = "chrome angry.png"
image bianca neutral = "bianca neutral.png"
image bianca angry = "bianca angry.png"
image bianca sad = "bianca sad.png"
image jack neutral = "jack neutral.png"
image jack happy = "jack happy.png"
image jack sad = "jack sad.png"
image jack shocked = "jack shocked.png"
image jack angry = "jack angry.png"
image mariah neutral = "mariah neutral.jpg"
image cop neutral = "cop neutral.jpg"
image santa = "santa.jpg"
image freddy neutral = "freddy neutral.jpg"

# define location images
image bg office = "bg office.png"
image bg office blur = im.Blur("bg office.png", 1.5) # blurred version
# image bg extstore = "bg extstore.png" # placeholder until we get asset
# image bg bar = "bg bar.png" # placeholder until we get asset
# image bg bar blur = im.Blur("bg bar.png", 1.5) # blurred version - placeholder until we get asset

# call this label when you want a glitch scene to start
label start_glitch():
    show chrome neutral glitch
    show bg:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
    return

# call this label when you want a glitch scene to end
label end_glitch:
    show chrome neutral
    show bg:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
    return

# The game starts here.

label start:

    menu:
        "Which Scene?"

        "One":
            call scene1

        "Two":
            call scene2

        "Three":
            call scene3

        "Four":
            call scene4

        "Five":
            call scene5

        "Six":
            call scene6

        "Seven":
            call scene7

        "Eight":
            call scene8

        "Nine":
            call scene9

        "Ten":
            call scene10

    jump start
    return

