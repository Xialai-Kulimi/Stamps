import math
import time

n = 8

while True:

    p = int(n * (n + 1) / 2)

    stamps = [0] * n

    k = n
    k_list = []

    check_times = int((len(stamps) - (len(stamps) % 2))/2)

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

        for j in range(check_times):
            if stamps[j] > stamps[n-j-1]:
                break
        else:
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
                    if x > k:
                        k_list = [i]
                        k = x
                    elif x == k:
                        k_list.append(i)
                    break
            else:
                print('error occur')
                print(record)
                input()

    print(n)
    print(k, k_list)
    f = open('result.md', 'a')
    f.write(f'n: {n}\nk: {k} method: {k_list}')
    n += 1
