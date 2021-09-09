# 1.a Vidējā vērtība
# Uzrakstīt programmu, kas liek lietotājam ievadīt skaitļus(float).
# Programma pēc katra ievada rāda visu ievadīto skaitļu vidējo vērtību.
# PS. 1a var iztikt bez lists
# 1.b Programma rāda gan skaitļu vidējo vērtību, gan VISUS ievadītos skaitļus
# PS Iziešana no programmas ir ievadot "q"
# 1.c Programma nerāda visus ievadītos skaitļus bet gan tikai TOP3 un BOTTOM3 un protams joprojām vidējo.
# numList = []
# while True:

#     avgInput = input(
#         'Pleasa enter floating number, one by one: (Press Q to exit) ')
#     if avgInput.lower().startswith('q'):
#         numList.clear()

#         print('List cleaned.')
#         break
#     else:
#         numList.append(float(avgInput))
#         avrgSum = sum(numList) / (len(numList))

#         print(f"\nVidējais svērtais: {round(avrgSum,2)}")

#         numList.sort()
#         print('*' * 20)
#         print("TOP3 MIN: ", numList[:3])
#         print("TOP 3 MAX: ", numList[-3:])
#         print('*' * 20)
#         print(f"Ievadītie skaitļi: {numList}")


# # 2. Kubu tabula
# # Lietotājs ievada sākumu (veselu skaitli) un beigu skaitli.
# # Izvads ir ievadītie skaitļi un to kubi
# # Piemēram: ievads 2 un 5 (divi ievadi)
# # Izvads
# # 2 kubā: 8
# # 3 kubā: 27
# # 4 kubā: 64
# # 5 kubā: 125
# # Visi kubi: [8,27,64,125]
# # PS teoretiski varētu iztikt bez list, bet ar list būs ērtāk

# uInput = int(input('Please enter number 1: '))
# u2Input = int(input('Please enter number 2: '))

# cubeList = []
# for num in range(uInput, u2Input + 1):
#     formula = num**3
#     print(f"{num} kubā: {formula}")
#     cubeList.append(formula)
# print(cubeList)


# 3. Apgrieztie vārdi

# Lietotājs ievada teikumu.
# Izvadam visus teikuma vārdus apgrieztā formā.
# Alus kauss -> Sula ssuak
# PS Te varētu noderēt split un join operācijas.

# words = input('Lūdzu ievadiet teikumu: ')
# # newList = [word[::-1] for word in words.split()]
# newList = []
# for word in words.split(): # each word from the list words is being iterated
#     newList.append(word[::-1]) # each word is added to newList reversed


# print(words, "->", " ".join(newList).capitalize()) # new list is joined into string and capitalized


# 4. Pirmskaitļi - šis varētu būt nedēļas nogales uzdevums, klasē diez vai pietiks laika
# Atrodiet un izvadiet pirmos 20 (vēl labāk iespēja izvēlēties cik pirmos pirmskaitļus gribam)
# pirmskaitļus saraksta veidā t.i. [2,3,5,7,11,...]

primeNum = int(input('Lūdzu ievadiet cik tālu meklēsim pirmsskaitļus: '))

nums = [2]
# for num in range(1, primeNum):
#     if num % 1 == 0 and num % num == 0:
#         nums.append(num)
# print(nums)
# for num in range(1, int(primeNum)+1):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 print(i, 'nav pirmskaitlis')
#                 break

#         else:
#             print(num, 'ir pirmskaitlis')
#             nums.append(num)


# print(nums)
i = 0
checkNum = 3
while len(nums) < primeNum:
    isPrimeNum = True
    i = 2
    while True:
        if checkNum % i == 0:
            print(checkNum, 'nav pirmskaitlis')
            isPrimeNum = False
            break
        i += 1
        if i > checkNum ** 0.5:
            break
    if isPrimeNum:
        nums.append(checkNum)
    checkNum += 1
print(nums)
