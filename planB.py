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


for i in range(int(math.pow(2, n * m))):
    plus1(counter, len(counter) - 1)
    print(counter)

    checker = [0] * (n * m)  # If the block is colored, the value will be 1, and 0 otherwise.

    # Check the counter
    for j in range((n - 1) * m):
        if j == 1:  # If the block is colored
            # if j % m == 0:  # At edge (left)
            #     if counter[j + 1] == 1:
            #         pass
            if j % m == m - 1:  # At edge (right)
                pass
        else:
            continue
