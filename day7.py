# task 1

def add_mult(a: int, b: int, c: int):
    nums = [a, b, c]
    nums.sort()
    formula = (nums[0]+nums[1])*nums[2]
    print(f"({nums[0]} + {nums[1]}) * {nums[2]} = {formula}")
    return (a+b)*c


add_mult(2, 5, 4)

# task 2


def is_palindrome(text):
    return text == text[::-1]


text = input('PLEASE ENTER TXT: ')
if is_palindrome(text):
    print('Yes')

else:
    print('No')

# task 3


def get_city_year(p0, perc, delta, p):
    i = 0
    while p > p0:
        formula = p0 * (perc * 0.01) + delta
        if delta > formula:
            print(-1)
            break
        else:
            p0 = p0 + formula
            i += 1
    print(i)
    return i
