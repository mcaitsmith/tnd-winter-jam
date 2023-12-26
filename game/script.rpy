# The main script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define larry = Character("Larry Moss", color="#2fb525", image="larry")
define chrome = Character("Chrome Steele", color="#a5a5a5", image="chrome")
define chrome_nvl_left = Character("Chrome Steele", color="#a5a5a5", image="chrome", kind=nvl)
define chrome_nvl_right = Character("Chrome Steele", color="#a5a5a5", image="chrome", kind=nvl, what_text_align=1, who_text_align=1)
define bianca = Character("Bianca Fontaine", color="#45b7f0", image="bianca")
define bianca_nvl_left = Character("Bianca Fontaine", color="#45b7f0", image="bianca", kind=nvl)
define bianca_nvl_right = Character("Bianca Fontaine", color="#45b7f0", image="bianca", kind=nvl, what_text_align=1, who_text_align=1)
define freddy = Character("Freddy Fontaine", color="#f07635", image="freddy")
define jack = Character("Jack Scanlon", color="#dbd839", image="jack")
define jack_nvl_left = Character("Jack Scanlon", color="#dbd839", image="jack", kind=nvl)
define jack_nvl_right = Character("Jack Scanlon", color="#dbd839", image="jack", kind=nvl, what_text_align=1, who_text_align=1)
define mariah = Character("Mariah Fowler", color="#d339db", image="mariah")
define mariah_nvl_left = Character("Mariah Fowler", color="#dbd839", image="mariah", kind=nvl)
define mariah_nvl_right = Character("Mariah Fowler", color="#dbd839", image="mariah", kind=nvl, what_text_align=1, who_text_align=1)
define cop = Character("Generic Cop", color="#2d30d9", image="cop")
define santa = Character("Robot Santa", color="#ff0000", image="santa")
define santa1 = Character("Robot Santa", color="#ff0000", image="santa")
define santa2 = Character("Robot Santa", color="#ff0000", image="santa")
define narration = Character("Narration", kind=nvl)

image bg office = "bg office.png"
image chrome neutral = "chrome neutral.png"
image bianca neutral = "bianca neutral.png"
image dialogue_box = "gui/nvl_box.png"

# define images for each character (need to be updated when we get assets)

image larry dead = "characters/larry/larry dead.png"
image larry = "characters/larry/larry dead.png"
image chrome neutral = "characters/chrome/chrome neutral.png"
image chrome neutral glitch = Glitch("characters/chrome/chrome neutral.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
image chrome shocked = "characters/chrome/chrome shocked.png"
image chrome shocked glitch = Glitch("characters/chrome/chrome shocked.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
image chrome confused = "characters/chrome/chrome confused.png"
image chrome confused glitch = Glitch("characters/chrome/chrome confused.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
image chrome happy = "characters/chrome/chrome happy.png"
image chrome happy glitch = Glitch("characters/chrome/chrome happy.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
image chrome sad = "characters/chrome/chrome sad.png"
image chrome sad glitch = Glitch("characters/chrome/chrome sad.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
image chrome thinking = "characters/chrome/chrome thinking.png"
image chrome thinking glitch = Glitch("characters/chrome/chrome thinking.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
image chrome timid = "characters/chrome/chrome timid.png"
image chrome timid glitch = Glitch("characters/chrome/chrome timid.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
image chrome angry = "characters/chrome/chrome angry.png"
image chrome angry glitch = Glitch("characters/chrome/chrome angry.png", glitch_strength=.005, color_range1="#0a00", color_range2="#bcbcbc") # glitched version
image bianca neutral = "characters/bianca/bianca neutral.png"
image bianca angry = "characters/bianca/bianca angry.png"
image bianca sad = "characters/bianca/bianca sad.png"
image jack neutral = "characters/jack/jack neutral.png"
image jack happy = "characters/jack/jack happy.png"
image jack sad = "characters/jack/jack sad.png"
image jack shocked = "characters/jack/jack shocked.png"
image jack angry = "characters/jack/jack angry.png"
image mariah neutral = "characters/mariah/mariah neutral.png"
image cop neutral = "characters/cop/cop neutral.png"
image cop angry = "characters/cop/cop neutral.png"
image santa = "characters/santa/santa.png"
image santa1 = "characters/santa/santa.png"
image santa2 = "characters/santa/santa.png"
image freddy neutral = "characters/freddy/freddy neutral.png"


# Evidence & Props
image cookietin = "props/cookietin.png"
image creditcard = "props/creditcard.png"
image memorystick = "props/memorystick.png"
image santaboots = "props/santaclothes.png"
image santa toy = "props/santatoy.png"


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
define sfx_breakmetaltoy = "audio/sfx/BreakMetalToy_SantaSecret_SFX.wav"

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
    $ stop_layers(0) # stop bg music
    show chrome neutral glitch
    show bg:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(0.0)
    # play glitch music
    # play music "GlitchSequence_127BPM_CMaj.wav"
    play music "GlitchSequence.wav"
    return

# call this label when you want a glitch scene to end
label end_glitch:
    show chrome neutral
    show bg:
        matrixcolor TintMatrix("#ffffff") * SaturationMatrix(1.0)
    stop music
    $ start_layers(0) # resume bg music
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

    # VARIABLE: Create a glitch counter and set it to 0
    $ glitch_counter = 0

    # jump to the first scene

    jump scene1