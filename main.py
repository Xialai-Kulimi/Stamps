# import math


def safe_input(question):
    while True:
        try:
            return int(input(question))
        except:
            print('plz input int')


while True:

    k = safe_input('k?')
    a = safe_input('length?')
    b = safe_input('height?')
    n = safe_input('num of the prices?')

    p = []

    for i in range(n):
        p.append(safe_input('price ' + str(i + 1) + '?'))
    print(p)

    if k > a * b:
        k = a * b


