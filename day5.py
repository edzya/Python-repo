# Task 1

while True:

    userInput = input(
        "Lūdzu ievadi savu vārdu: (Lai izietu lūdzu ievadi Q) ")
    if userInput.upper() == 'Q':  # once q or Q is entered, loop is stopped;
        break
    # creation of new name, first letter from the end is being uppercased, rest of the letters are being lowercased
    newName = userInput[-1].upper() + userInput[-2::-1].lower()
    print(
        f"{userInput} -> {newName}, pamatīgs juceklis vai ne, {userInput[0].upper()} ? ")


# Task 2

#newName = None

guessName = input('Lūdzu ievadiet vārdu: ')
for letter in guessName:
    if letter.isalpha() == True:
        print('*', end=" ")
    else:
        print(letter, end=" ")

user2Input = input('\nLūdzu ievadiet burtu: ')

for letter in guessName:
    if user2Input.lower() == letter.lower():
        print(letter, end=" ")
    elif letter.isalpha() == False:
        print(letter, end=" ")
    else:
        print('*', end=" ")
