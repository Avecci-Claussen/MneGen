# MneGen
Mnemonic Generator / Addresses deriver from Mnemonics

*MNE.py*

 
This Python code generates and shuffles mnemonic phrases while ensuring that each generated mnemonic is unique. It then validates the mnemonics and writes the valid ones to a file named "found.txt." Here's a simple explanation of how it works:

The code imports the necessary libraries: random for random number generation and mnemonic for generating and validating mnemonic phrases.

The shuffle_mnemonic function takes a mnemonic phrase as input, splits it into words, shuffles the order of the words randomly, and returns the shuffled mnemonic.

The validate_mnemonic function takes a mnemonic phrase as input and checks its validity using the Mnemonic class from the "mnemonic" library. It returns True if the mnemonic is valid and False otherwise.

The code defines an original mnemonic phrase and creates an empty set named generated_mnemonics to keep track of the generated mnemonics.

The code enters a loop to generate and validate mnemonics. It will stop once it has found and validated 50,000 unique mnemonics.

In each iteration, the code shuffles the original mnemonic to generate a new one.

If the shuffled mnemonic has already been generated (i.e., it exists in the generated_mnemonics set), the loop continues to the next iteration to ensure uniqueness.

If the shuffled mnemonic is unique, it adds it to the set of generated mnemonics and proceeds to validate it.

If the shuffled mnemonic is valid, it prints it as a valid mnemonic along with its index (i) and writes it to the "found.txt" file.

If the shuffled mnemonic is invalid, it prints it as an invalid mnemonic, and the loop continues.



*Mne_ad.py*

This Python code interacts with the "bitcoinlib" library to derive Bitcoin addresses from the mnemonic phrases stored in the "found.txt" file. The derived addresses are then written to a new file named "adr.txt". Here's a simple explanation of how it works:

The code imports the "Wallet" class from the "bitcoinlib.wallets" module.

The function derive_addresses_from_mnemonic takes a mnemonic phrase and a wallet name as inputs. It tries to load an existing wallet with the given name. If the wallet doesn't exist, it creates a new one using the provided mnemonic and specifies the Bitcoin network as "bitcoin".

The function derives addresses for the first 10 child indices of the wallet by looping from 0 to 9. For each index, it derives the corresponding private key and then obtains the Bitcoin address associated with that private key.

The function returns a list of 10 derived addresses.

The code reads the mnemonics from the "found.txt" file and processes each line to derive the addresses using the derive_addresses_from_mnemonic function.

For each mnemonic, a wallet with a unique name ("wallet_1", "wallet_2", etc.) is created, and 10 addresses are derived and stored in a list.

The code writes the derived addresses to the "adr.txt" file, with each address on a separate line.








