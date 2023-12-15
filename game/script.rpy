# The main script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define larry = Character("Larry Moss", color="#2fb525")
define chrome = Character("Chrome Steele", color="#a5a5a5", kind=nvl)
define bianca = Character("Bianca Fontaine", color="#45b7f0")
define bianca_right = Character("Bianca Fontaine", color="#45b7f0", kind=nvl, what_text_align=1, who_text_align=1)
define freddy = Character("Freddy Fontaine", color="#f07635")
define jack = Character("Jack Scanlon", color="#dbd839")
define mariah = Character("Mariah Fowler", color="#d339db")
define cop = Character("Generic Cop", color="#2d30d9")
define santa = Character("Robot Santa", color="#ff0000")
define narration = Character("Narration", kind=nvl)

# The game starts here.

label start:

    # jump to the first scene

    jump scene1