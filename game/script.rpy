# The main script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define larry = Character("Larry Moss", color="#2fb525", image="larry")
define chrome = Character("Chrome Steele", color="#a5a5a5", image="chrome")
define bianca = Character("Bianca Fontaine", color="#45b7f0", image="bianca")
define freddy = Character("Freddy Fontaine", color="#f07635", image="freddy")
define jack = Character("Jack Scanlon", color="#dbd839", image="jack")
define mariah = Character("Mariah Fowler", color="#d339db", image="mariah")
define cop = Character("Generic Cop", color="#2d30d9", image="cop")
define santa = Character("Robot Santa", color="#ff0000", image="santa")
define narration = Character("Narration", kind=nvl)

# define images for each character (need to be updated when we get assets)

image larry dead = "larry dead.png"
image larry = "larry dead.jpg"
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
image santa toy = "santa.jpg"

# define location images
image bg office = "bg office.png"
image bg office blur = im.Blur("bg office.png", 1.5) # blurred version
# image bg extstore = "bg extstore.png" # placeholder until we get asset
# image bg bar = "bg bar.png" # placeholder until we get asset
# image bg bar blur = im.Blur("bg bar.png", 1.5) # blurred version - placeholder until we get asset

# define sound effects
define sfx_clatter = "audio/sfx/Clatter_SantaSecret_SFX.wav"
define sfx_door = "audio/sfx/Door_SantaSecret_SFX.wav"
define sfx_footsteps = "audio/sfx/FootSteps_SantaSecret_SFX.wav"
define sfx_gunshots = "audio/sfx/Gunshots_SantaSecret_SFX.wav"
define sfx_impactmetal = "audio/sfx/ImpactMetal_SantaSecret_SFX.wav"
define sfx_mariahclap = "audio/sfx/MariahClap_SantaSecret_SFX.wav"
define sfx_punch = "audio/sfx/Punch_SantaSecret_SFX.wav"
define sfx_rattle = "audio/sfx/Rattle_SantaSecret_SFX.wav"
define sfx_santabeepscan = "audio/sfx/SantaBeepScan_SantaSecret_SFX.wav"


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
    # play glitch music
    play music "GlitchSequence_127BPM_CMaj.wav"
    return

# call this label when you want a glitch scene to end
label end_glitch:
    show chrome neutral
    show bg:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
    stop music
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