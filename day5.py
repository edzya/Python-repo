# Task 1

while True:

    userInput = input(
        "Lūdzu ievadi savu vārdu: (Lai izietu lūdzu ievadi Q) ")
    if userInput.upper() == 'Q':  # once q or Q is entered loop is stopped;
        break
    # creation of new name, first letter from the end is being uppercased, rest of the letters are being lowercased
    newName = userInput[-1].upper() + userInput[-2::-1].lower()
    print(
        f"{userInput} -> {newName}, pamatīgs juceklis vai ne, {userInput[0].upper()} ? ")
