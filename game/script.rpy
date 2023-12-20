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
image larry = "larry.jpg"
image chrome neutral = "chrome neutral.png"
image chrome neutral glitch = Glitch("chrome neutral.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
image bianca neutral = "bianca neutral.jpg"
image jack neutral = "jack neutral.jpg"
image mariah neutral = "mariah neutral.jpg"
image cop neutral = "cop neutral.jpg"
image santa = "santa.jpg"
image freddy neutral = "freddy neutral.jpg"

# define location images
image bg office = "bg office.png"
image bg office blur = im.Blur("bg office.png", 1.5) # blurred version

init python:
    # define music channels
    renpy.music.register_channel("layer_chrome", "music")
    renpy.music.register_channel("layer_bianca", "music")
    renpy.music.register_channel("layer_freddy", "music")
    renpy.music.register_channel("layer_mariah", "music")
    renpy.music.register_channel("layer_larry_santa", "music")

    # function to start playing layers
    def start_layers(delay=3):
        renpy.music.play("audio/Dept Store Main Chrom.wav", channel='layer_chrome', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/Dept Store Main Bianca.wav", channel='layer_bianca', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/Dept Store Main Freddie.wav", channel='layer_freddy', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/Dept Store Main Mariah.wav", channel='layer_mariah', loop=True, synchro_start=True, fadein=delay)
        renpy.music.play("audio/Dept Store Main Larry_Santa.wav", channel='layer_larry_santa', loop=True, synchro_start=True, fadein=delay)

    # function to stop playing layers
    def stop_layers(delay=None):
        renpy.music.stop(channel='layer_chrome', fadeout=delay)
        renpy.music.stop(channel='layer_bianca', fadeout=delay)
        renpy.music.stop(channel='layer_freddy', fadeout=delay)
        renpy.music.stop(channel='layer_mariah', fadeout=delay)
        renpy.music.stop(channel='layer_larry_santa', fadeout=delay)

    # function to update layers
    def update_layers(delay=1):
        layer_chrome = 0.2 if chrome_on else 0
        layer_bianca = 1 if bianca_on else 0
        layer_freddy = 1 if freddy_on else 0
        layer_mariah = 1 if mariah_on else 0
        layer_larry_santa = 1 if larry_santa_on else 0
        
        renpy.music.set_volume(layer_chrome, delay=delay, channel='layer_chrome')
        renpy.music.set_volume(layer_bianca, delay=delay, channel='layer_bianca')
        renpy.music.set_volume(layer_freddy, delay=delay, channel='layer_freddy')
        renpy.music.set_volume(layer_mariah, delay=delay, channel='layer_mariah')
        renpy.music.set_volume(layer_larry_santa, delay=delay, channel='layer_larry_santa')

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

    # fadeout intro music
    stop music fadeout 3.0

    # initialize music layers
    $ chrome_on = False
    $ bianca_on = False
    $ freddy_on = False
    $ mariah_on = False
    $ larry_santa_on = False

    # jump to the first scene

    jump scene1