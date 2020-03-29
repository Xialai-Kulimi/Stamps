import math
import time

# 　record_file_name = f'record_{str(time.time())}.txt'
# 　output_file_name = f'output_{str(time.time())}.txt'

# record = {}

n = 5

# print('1 1')

while True:

    # start_time = time.time()
    # n = int(input('n?'))

    # n = 6

    # p = int(input('stamp max?'))
    p = int(n * (n + 1) / 2)

    stamps = [0] * n

    # record_txt = open('record.txt', 'w')
    # record = {}  # 記錄個面值的各種撕法的總額
    k_list = []
    k_dict = {}

    for i in range(int(math.pow(p, n))):

        # record.append(0)
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

        record.append(p + 1)  # 製造斷層
        record.sort()

        for j in range(len(record)):
            x = record[j]
            # print(record[n][i]['summary'])
            if x + 1 < record[j + 1]:
                # record[i] = x
                k_list.append(x)
                k_dict[x] = i
                break
        else:
            print('error occur')
            print(record)
            input()
        # print(i)
        # if i % 100 == 0:
        #     record_txt.write(str(record))
            # record = {}
    k_list.sort()
    # print(record[n]['k_list'])
    k = k_list[-1]

    # f = open(output_file_name, 'a')
    # f.write(f'n: {n}, k: {k}, method_num: {k_dict[k]}\n')
    print(n)
    print(k, k_dict[k])
    # f.close()
    n += 1
    # f = open(record_file_name, 'a')
    # f.write(str(record) + '\n')
    # f.close()
    # print(-start_time + time.time())
    # input()
    # print(record)
