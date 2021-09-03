# # Task 1

# while True:

#     userInput = input(
#         "Lūdzu ievadi savu vārdu: (Lai izietu lūdzu ievadi Q) ")
#     if userInput.upper() == 'Q':  # once q or Q is entered, loop is stopped;
#         break
#     # creation of new name, first letter from the end is being uppercased, rest of the letters are being lowercased
#     newName = userInput[-1].upper() + userInput[-2::-1].lower()
#     print(
#         f"{userInput} -> {newName}, pamatīgs juceklis vai ne, {userInput[0].upper()} ? ")


# # Task 2

# guessWord = ""

# guessName = input('Lūdzu ievadiet vārdu: ')
# guessName = guessName.lower()
# for letter in guessName:
#     if letter == ' ':
#         guessWord += letter
#     else:
#         guessWord += '*'
# print(guessWord)

# tries = 0
# MAXtries = 7
# while guessWord != guessName:
#     guess = input('Enter a single letter: ')
#     guess = guess[0].lower()
#     temp_word = ''

#     for c, guess_char in zip(guessName, guessWord):
#         if c == guess_char or c == guess:
#             temp_word += c
#         else:
#             temp_word += '*'
#     guessWord = temp_word
#     tries += 1
#     print(f'your guess so far {guessWord}, in {tries} tries')
#     if guessName == guessWord:
#         print(f'Hooray, you won - guessword was {guessWord} ')
#     if tries >= MAXtries:
#         print('Sorry, you lost')
#         break


# Task 3

# Uzrakstīt programmu teksta pārveidošanai
# Saglabā lietotāja ievadu
# Izdrukā ievadīto tekstu bez izmaiņām
# Izņēmums: ja ievadā ir vārdi nav .... slikts, TAD izvadā nav ... slikts posms jānomaina uz ir labs
# Laiks nav slikts -> Laiks ir labs
# Auto nav jauns -> Auto nav jauns
# Tas biezpiens nav nemaz tik slikts -> Tas biezpiens ir labs
# Droši vien noderēs find (vai index, vai pat rfind), tāpat arī in operātors var noderēt. Tāpat slice sintakse būs noderīga.
# Ja uzdevums risinās raiti, tad varam uzlabot un meklēt gan nav ... slikts -> ir labs, gan nav ... slikta -> ir laba

userInput = input('Please enter a sentence: ')

# if userInput.find('nav') and userInput.find('slikts'):
#     userInput = userInput.replace('nav', 'ir')
#     userInput = userInput.replace('slikts', 'labs')
#     print(userInput)
# else:
#     print(userInput)

startWord = 'nav'
endWord = 'slikt'
startWorRpl = 'ir'
endWorRpl = 'lab'

if startWord in userInput and endWord in userInput:
    userInputStart = userInput.split(startWord)
    userInputStart = userInputStart[0]

    userInput = userInput.replace(startWord, startWorRpl)
    userInput = userInput.replace(endWord, endWorRpl)
    wordEnding = userInput[-1]

    textOutput = userInput.split(startWorRpl)[
        0] + startWorRpl + " " + endWorRpl + wordEnding
    print(textOutput)

    # print(userInput)
else:
    print(userInput)
