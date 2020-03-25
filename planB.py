import math

n = int(input('input n'))
m = int(input('input m'))

counter = [0] * (n * m)


def plus1(big_base_2_num_list, place):
    if big_base_2_num_list[place] == 0:
        big_base_2_num_list[place] = 1
    else:
        big_base_2_num_list[place] = 0
        plus1(big_base_2_num_list, place - 1)


p = 0

for i in range(int(math.pow(2, n * m))):
    plus1(counter, len(counter) - 1)
    print(counter)

    old_counter = counter
    # checker = [0] * (n * m)

    for j in range(m):
        counter.insert((j + 1) * n, 0)

    counter = counter + [0]*(n+1)

    print(counter)

    for j in range((n + 1) * (m + 1)):
        if counter[j] == 1:
            if counter[j + 1] + counter[j + m + 1] == 0:
                break
    else:
        p += 1

    counter = old_counter

print(p)
