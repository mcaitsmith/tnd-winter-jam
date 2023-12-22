# The script of the scene goes in this file.

######### SCENE 7: Alley

# The scene starts here.

label scene7:

    scene bg alley

    show chrome at right    

    show cop at left   

    menu:
        "Hm. He seems like a \"no nonsense, just the facts ma’am\" kinda guy. I wonder what approach I should take?"

    # Option One: (hardboiled)
        "Hardboiled":

            chrome hardboiled "Heyo, buddy boy! I’m looking for Freddy Font–"

            cop angry "Yeah? You and me both."

            chrome shocked "Excuse me?"

            cop angry "He’s a person of interest- might even say a suspect."

            chrome angry "Really?"

            cop angry "That woman right over there, found this poor schmuck dead as a doornail."

            cop angry "Combine that with the fact Freddy didn’t show up today, his last day…"

            chrome confused "Hm. Something seems fishy…"

            cop angry "The only thing fishy ‘round here is you! Now giddy up Jingle Horse and get the fuck out of my active crime scene!"

    # Option Two: (Logical. IDEAL PATH)
        "Logical":
            #programming - ideal choice += 1

            chrome logical "Hello, sir. I’m looking for Freddy Fontaine–"

            cop neutral "You’re not the only one."

            chrome logical "Hm. Interesting. Locate any evidence?"

            cop neutral "That’s the funny thing. He died from a heart attack."

            chrome confused "Heart attack? Something doesn’t add up here."

            cop neutral "Whelp, we’ve got a witness...."

            chrome confused "Who?"

            cop neutral "Mariah Fowler. Saw this poor sucker collapse on the ground, and Freddy running the other direction"

            chrome logical "Very interesting. Thanks."

    #Option Three: (Unassuming)
        "Unassuming":

            cop neutral "Alley’s closed."

            chrome unassuming "Oh, I work across the street."

            cop neutral "Where?"

            chrome thinking "..."

            cop neutral "..."

            chrome thinking "..."

            chrome hardboiled "Over there."

            cop shocked "In that boarded up bail bonds office?"

            cop angry "This is an active crime scene. Get outta here!"

            chrome angry "..."

            chrome logical "Under code 2034.44 You, sir, are interfering with the duties of a certified bail bonds agent…" 

            show cop angry

            chrome unassuming "Would you like me to report THAT to your superior?"

            cop angry  "Fine. Go through"


    jump scene8

    return