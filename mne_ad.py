from bitcoinlib.wallets import Wallet

def derive_addresses_from_mnemonic(mnemonic, wallet_name):
    try:
        # Try to load an existing wallet with the given name
        wallet = Wallet(wallet_name)
    except Exception:
        # If the wallet doesn't exist, create a new one from the mnemonic
        wallet = Wallet.create(wallet_name, keys=mnemonic, network='bitcoin')

    addresses = []

    # Derive addresses for the first 10 child indices
    for i in range(10):
        # Derive the child private key and corresponding address
        child_private_key = wallet.get_key(i)
        address = child_private_key.address

        addresses.append(address)

    return addresses

# Read mnemonics from the "found.txt" file
with open("found.txt", "r") as found_file:
    lines = found_file.readlines()

# Open the file "adr.txt" for writing
with open("adr.txt", "w") as adr_file:
    # Process each line and derive the addresses
    for i, line in enumerate(lines):
        # Split the line by the colon, get the mnemonic (second part), and strip any leading or trailing whitespace
        mnemonic = line.split(':', 1)[1].strip()
        wallet_name = f"wallet_{i+1}"
        addresses = derive_addresses_from_mnemonic(mnemonic, wallet_name)
        
        # Write the addresses to "adr.txt"
        adr_file.write(f"")
        for address in addresses:
            adr_file.write(f"{address}\n")