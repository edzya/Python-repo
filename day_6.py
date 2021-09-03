# 1.a Vidējā vērtība
# Uzrakstīt programmu, kas liek lietotājam ievadīt skaitļus(float).
# Programma pēc katra ievada rāda visu ievadīto skaitļu vidējo vērtību.
# PS. 1a var iztikt bez lists
# 1.b Programma rāda gan skaitļu vidējo vērtību, gan VISUS ievadītos skaitļus
# PS Iziešana no programmas ir ievadot "q"
# 1.c Programma nerāda visus ievadītos skaitļus bet gan tikai TOP3 un BOTTOM3 un protams joprojām vidējo.
numList = []
sum = 0
while True:

    avgInput = input(
        'Pleasa enter floating number, one by one: (Press Q to exit) ')
    if avgInput.lower().startswith('q'):
        numList.clear()
        sum = 0
        print('List cleaned, sum counter reset.')
        break
    else:
        numList.append(float(avgInput))
        sum += float(avgInput)
        avrgSum = sum / (len(numList))
        print(avrgSum)
        print(len(numList))
        print(f"Ievadītie skaitļi: {numList}")
        if len(numList) >= 3:
            print(f"TOP3: {max(numList)}, ANTI TOP3: {min(numList)}")

# 2. Kubu tabula
# Lietotājs ievada sākumu (veselu skaitli) un beigu skaitli.
# Izvads ir ievadītie skaitļi un to kubi
# Piemēram: ievads 2 un 5 (divi ievadi)
# Izvads
# 2 kubā: 8
# 3 kubā: 27
# 4 kubā: 64
# 5 kubā: 125
# Visi kubi: [8,27,64,125]
# PS teoretiski varētu iztikt bez list, bet ar list būs ērtāk

uInput = int(input('Please enter number 1: '))
u2Input = int(input('Please enter number 2: '))

###############################
# cubeMatrix = [[num, "kubā", num*num*num] for num in range(uInput, u2Input+1)]
# print(cubeMatrix[0] + cubeMatrix[1] + cubeMatrix[2])

# cube = [num*num*num for num in range(uInput, u2Input+1)]
# print(f"Visi kubi: {cube}")


###############################

###############################
cubeList = []
for num in range(uInput, u2Input + 1):
    formula = num**3
    print(f"{num} kubā: {formula}")
    cubeList.append(formula)
print(cubeList)


# 3. Apgrieztie vārdi

# Lietotājs ievada teikumu.
# Izvadam visus teikuma vārdus apgrieztā formā.
# Alus kauss -> Sula ssuak
# PS Te varētu noderēt split un join operācijas.


# 4. Pirmskaitļi - šis varētu būt nedēļas nogales uzdevums, klasē diez vai pietiks laika
# Atrodiet un izvadiet pirmos 20 (vēl labāk iespēja izvēlēties cik pirmos pirmskaitļus gribam)
# pirmskaitļus saraksta veidā t.i. [2,3,5,7,11,...]
