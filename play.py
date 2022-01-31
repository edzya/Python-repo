

from publicsuffix2 import PublicSuffixList


def is_valid_walk(walk):
    start = 0

    for i in walk:
        if i == 'n' or i == 'w':
            start += 1
        if i == 's' or i == 'e':
            start -= 1
    if start == 0:
        return True
    else:
        return False


# lala = is_valid_walk(['s', 'e', 'w', 'n', 'n', 'n', 'e', 'w', 'e', 's'])
# print(lala)


psl = PublicSuffixList()


def domain_name(url):
    suffix = psl.get_tld(url)
    newurl = url.replace('.'+suffix, '')

    print(newurl)
    pass


# domain_name("http://google.com")
# domain_name("www.xakep.ru")


def create_phone_number(n):
    print(
        f'(${n[0]}${n[1]}${n[2]}) ${n[3]}${n[4]}${n[5]}-${n[-4]}${n[-3]}${n[-2]}${n[-1]}')


# def descending_order(num):
#     print(num)
#     y =
#     # for i in y:
#     #     print(i)


# descending_order(123456789)

def array_diff(a, b):
    for i in b:
        for l in a
        if i == l:
            a.pop(a.index(i))
            print(i, 'removed')
            print(a)


array_diff([1, 2, 2], [2])
