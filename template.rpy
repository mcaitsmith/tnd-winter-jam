# Your script goes in this file! 
# In Python, any line with a # is a comment - it doesn't get parsed as code.
# Use comments often to let your programmers know what you want to happen! If you don't know the code for something, just leave a comment describing what you want.

# Start a scene by telling us the location it takes place, which background to show:
LOCATION: Office

# tell us which characters are visible:

show bianca center happy    # this shows Bianca in the center, using the happy expression.

show steele left neutral    # this shows Steele on the left, using the neutral expression.

# Now start dialogue using this format, which shows the character, their expression, and what they say:

bianca neutral "Hello, I'm Bianca."

bianca neutral "Are you Detective Steele?"

# For narration, don't put a character name or emotion: 

"Steele wonders what gave it away. Maybe his nametag."

steele neutral "That I am."

# If you want us to implement an effect, give us a comment like these examples:

# SOUND: door closes

bianca worried "What was that?"

# VISUAL: the screen shakes

steele worried "Earthquake!!"

# VARIABLE: Add 1 to Clues Gathered

##################
# Making Choices #
##################

# In RenPy, every choice has a prompt and options that branch the story. We'll take care of writing the code, but whenever you want to make a branch, set it up like this:

# CHOICE

# Prompt:
bianca worried "Will you help me?"

# Option One: 
    "Sure."
    
    steele neutral "Sure."

    bianca happy "Thank you!"
 
    # once a branch ends, tell us what line comes next in the story: 
    # jump to Bianca saying "So here's the deal"


# Option Two:
    "Nah."

    steele neutral "Nah."

    bianca worried "Oh. That's sad."

    # you can ask us to jump to an entirely different scene if you want:
    # jump to Game Over scene

bianca determined "So here's the deal."

bianca neutral "We're headed to the scene of the crime."

# End