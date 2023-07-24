import random
from mnemonic import Mnemonic

def shuffle_mnemonic(mnemonic):
    words = mnemonic.split()
    random.shuffle(words)
    return ' '.join(words)

def validate_mnemonic(mnemonic):
    mnemo = Mnemonic("english")
    return mnemo.check(mnemonic)

# Original mnemonic
original_mnemonic = "abandon ability able about above absent abandon ability able about above absent"

generated_mnemonics = set()

# Open the file "found.txt" for writing
with open("found.txt", "w") as found_file:
    i = 0
    while i < 50000:
        # Shuffle the mnemonic
        shuffled_mnemonic = shuffle_mnemonic(original_mnemonic)

        # Check if the mnemonic has already been generated
        if shuffled_mnemonic in generated_mnemonics:
            continue

        generated_mnemonics.add(shuffled_mnemonic)
        i += 1

        # Validate the shuffled mnemonic
        if validate_mnemonic(shuffled_mnemonic):
            print(f"Valid mnemonic {i}:", shuffled_mnemonic)
            # Write the valid mnemonic to "found.txt"
            found_file.write(f"Valid mnemonic {i}: {shuffled_mnemonic}\n")
        else:
            print(f"Invalid mnemonic {i}:", shuffled_mnemonic)
