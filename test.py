# # text_input = input('Enter word combination for guessing game: ')
# # word = hidden_word = text_input.lower()
# # for i in range(len(hidden_word)):
# #     hidden_word = hidden_word[0:i] + "*"
# #     if ' ' in word:
# #         hidden_word = hidden_word[:word.index(
# #             ' ')] + ' ' + hidden_word[word.index(' ')+1:]
# # print(hidden_word)

# # while hidden_word != word:
# #     guess = input("Enter a single letter: ")
# #     guess = guess.lower()
# #     for i in range(len(word)):
# #         if word[i] == guess:
# #             hidden_word = hidden_word[0:i] + guess + hidden_word[i + 1:]
# #     print(hidden_word)
# # print(f"You have guessed '{word}' correclty.")


# option1 = '\n1. Laiks nav slikts'
# option2 = '\n2. Auto nav jauns'
# option3 = '\n3. Tas biezpiens nav nemaz tik slikts'
# option4 = '\n\n4. Gribu ievadīt pats savu tekstu'

# print('Choose a text to modify (1 - 4):', option1, option2, option3, option4)

# choice = int(input('\nSelect a number from list above: \n'))

# if choice == 1:
#     print('\nChosen text: ' + option1[4:])
#     original_text = option1[4:]
# elif choice == 2:
#     print('\nChosen text: ' + option2[4:])
#     original_text = option2[4:]
# elif choice == 3:
#     print('\nChosen text: ' + option3[4:])
#     original_text = option3[4:]
# elif choice == 4:
#     choice = input('Enter your text: ')
#     print('\nChosen text: ' + choice)
#     original_text = choice
# else:
#     original_text = 'Only numbers 1 through 4 are accepted. Restart the application.'

# # #original_text = input('Input your negative text here: ')
# text = original_text.split(' ')
# starting_word = 'nav'
# ending_word = 'slikt'
# starting_word_replacement = 'ir'
# # ending_word_replacement = 'lab'
# # order = original_text.find(ending_word)

# # if starting_word in original_text and ending_word in original_text and text.index(starting_word) < text.index(ending_word + original_text[order + len(ending_word)]):
# #     text_before_starting_word = original_text.split(starting_word)[0]
# #     text_after_ending_word = original_text.split(ending_word)[1]
# #     print('Modified text: ' + text_before_starting_word + starting_word_replacement +
# #           ' ' + ending_word_replacement + text_after_ending_word)
# # else:
# #     if original_text != 'Only numbers 1 through 4 are accepted. Restart the application.':
# #         print('Nothing to fix here')
# #     else:
# #         print(original_text)


# # squares = [num*num for num in range(10)]  # so we come up with num on the spot
# # print(squares)
# # squares_matrix = [[num, "squared", num*num] for num in range(10)]
# # print(squares_matrix)  # so list of lists (2d array basically)
# # print(squares_matrix[9][2], squares_matrix[-1][-1])

# number_of_primes = input("cik primskaitļu nepieciešams atrast? ")
# try:
#     number_of_primes = int(number_of_primes)
#     i = 1
#     candidate = 3
#     primes = ["1: 2"]
#     while len(primes) < number_of_primes:
#         is_prime = True
#         i = 2
#         while True:
#             if candidate % i == 0:
#                 is_prime = False
#                 break
#             i += 1
#             if i > candidate**0.5:
#                 break
#         if is_prime:
#             primes.append(str(len(primes)+1)+": "+str(candidate))
#             # print(n)
#         candidate += 1
#     # print(primes)
#     print(*primes, sep="\n")
# except ValueError:
#     print("nekorekta ievade")


# my_tuple = tuple(range(5))
# print(my_tuple)
# a, b, c, d, e = my_tuple
# print(d)


class TC:
    my_val = ""

    def __init__(self, my_val):
        my_val = my_val


c1 = TC("doh")
c2 = TC("self")
print(c1.my_val)
