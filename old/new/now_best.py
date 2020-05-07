import math
import time

n = 7

while True:

    p = int(n * (n + 1) / 2)

    stamps = [0] * n

    k_list = []
    k_dict = {}

    for i in range(int(math.pow(p, n))):

        num_pos = 0
        for j in stamps:  # 下一種面值分配
            stamps[num_pos] += 1
            if stamps[num_pos] == p + 1:
                stamps[num_pos] = 1
                num_pos += 1
            else:
                break

        for j in stamps:  # must be one 1 stamp
            if j == 1:
                break
        else:
            continue  # no 1 in stamps

        if stamps[0] > stamps[-1]:  # Check this before.
            continue

        record = []

        for j in range(n):  # Methods of coloring.
            for r in range(j, n):
                summary = 0
                for q in range(j, r + 1):
                    summary += stamps[q]
                record.append(summary)

        record.append(p + 1)  # Make a BIG gap.
        record.sort()

        for j in range(len(record)):
            x = record[j]
            if x + 1 < record[j + 1]:
                k_list.append(x)
                k_dict[x] = i
                break
        else:
            print('error occur')
            print(record)
            input()

    k_list.sort()
    k = k_list[-1]
    print(n)
    print(k, k_dict[k])
    f = open('result.md', 'a')
    f.write(f'n: {n}\nk: {k} method: {k_dict[k]}')
    n += 1
