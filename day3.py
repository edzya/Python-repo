# Day 3

# Task 1

userTemp = float(input('Please enter your body temperature: '))

if userTemp < 35:  # if users body temperature below 35 degrees
    print("Isn't it too cold for you ?")
elif userTemp <= 37:  # if users body temperature is equal or below 37 degrees
    print("Your body temperature is fine")
elif userTemp > 37:  # if users body temperature exceeds 37 degrees
    print("Possible fewer!")
else:  # error handling ? :)
    print("Implausible value")


# Task 2

coeffcnt = 0.15
salary = int(input('Please enter your monthly salary: '))
print()
yrsWrkd = int(
    input('Please enter how much years you already work for the company: '))
print()

if yrsWrkd > 2:
    bonus = round((salary * coeffcnt) * (yrsWrkd - 2), 2)  # calculates bonus
    # outputs bonus to user
    print(f'This Christmas you will receive {bonus} EUR as a bonus!!! :)')
else:
    # if condition over 2 years was not met
    print('Sorry you cant receieve bonus')


# Task 3

num_1 = int(input('Please enter first number: '))
num_2 = int(input('Please enter second number: '))
num_3 = int(input('Please enter third number: '))


if num_1 > num_2:
    num_1, num_2 = num_2, num_1
if num_1 > num_3:
    num_1, num_3 = num_3, num_1
if num_2 > num_3:
    num_2, num_3 = num_3, num_2

print(num_1, "<", num_2, "<", num_3)
