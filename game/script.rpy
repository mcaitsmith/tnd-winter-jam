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
image chrome neutral = "chrome neutral.jpg"
image bianca neutral = "bianca neutral.jpg"
image jack neutral = "jack neutral.jpg"
image mariah neutral = "mariah neutral.jpg"
image cop neutral = "cop neutral.jpg"
image santa = "santa.jpg"
image freddy neutral = "freddy neutral.jpg"

# The game starts here.

label start:

    # jump to the first scene

    jump scene1