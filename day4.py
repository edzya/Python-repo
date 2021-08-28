# Task 1 FizzBuzz

i = 1
while i <= 100:

    if i % 5 == 0 and i % 7 == 0:
        print('FizzBuzz', end=", ")
    elif i % 5 == 0 and i == 100:
        print('Fizz', end="")
    elif i % 5 == 0:
        print('Fizz', end=", ")
    elif i % 7 == 0:
        print('Buzz', end=", ")
    else:
        print(i, end=", ")
    i += 1

# Task 2 Eglīte

height = int(input('Lūdzu ievadiet eglītes augstumu: '))

x_cord = 1
z_cord = height - 1
for i in range(height):
    print(" " * z_cord + "*" * x_cord + " " * z_cord)
    x_cord += 2
    z_cord -= 1

# Task 3 Pirmskaitlis

primeNum = int(input("Lūdzu ievadiet veselu skaitli: "))

if primeNum > 1:
    for i in range(2, int(primeNum)):
        print(i)
        if primeNum % i == 0:
            print(primeNum, 'nav pirmskaitlis')
            break
    else:
        print(primeNum, 'ir pirmskaitlis')

else:
    print(primeNum, 'ir pirmskaitlis')
