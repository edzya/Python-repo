# Task 1

import datetime  # imports library

userName = input('Please enter username: ')  # User input 1; getting username

# User input 2; getting age
while True:
    try:
        age = input(f'Hey {userName}, could you tell me what is your age ? ')
        age = int(age)
        break
    except ValueError:
        # error message if entered input is not an integer
        print('Sorry, I understand only whole numbers')

currYear = datetime.datetime.now().year  # gets current year using library
remainingYears = 100 - age  # calculates years left till 100
print(
    f'You will be 100 years old after {remainingYears} years and it will happen on year {currYear + remainingYears} ! :)')  # output

# Task 2

print('Hello! Here I will calculate the volume of a room. I will kindly ask you to provide room dimensions.')

while True:
    try:
        roomHeight = float(input('Please enter room height in cm: '))

        roomLength = float(input('Please enter room lenght in cm: '))

        roomWidth = float(input('Please enter room width in cm: '))

        break
    except ValueError:
        print('Sorry I understand only floating numbers')


volume = roomHeight * roomLength * roomWidth
print(f'Your room volume is {volume} cm³')

# Task 3

while True:
    try:
        celsiusInput = float(input('Please enter temperature in Celsius: '))
        farenheitReturn = 32+celsiusInput*(9/5)
        break
    except ValueError:
        print('Sorry, number must be entered, try once again!')
print(f'Your entered temperature in farenheit is {farenheitReturn}')

print('Thank you for your time! :)')
