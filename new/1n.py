import math

record = {}

n = 1

print('1 1')

while True:
    # n = int(input('n?'))
    n += 1

    # p = int(input('stamp max?'))
    p = int(n * (n + 2) / 2)

    stamps = [0] * n

    record[n] = {}
    record[n]['k_list'] = []
    record[n]['k_dict'] = {}

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

        record[n][i] = {'summary': []}

        for j in range(n):
            for r in range(j, n):
                summary = 0
                for q in range(j, r + 1):
                    summary += stamps[q]
                record[n][i]['summary'].append(summary)

        record[n][i]['summary'].append(p + 1)
        record[n][i]['summary'].sort()

        for j in range(len(record[n][i]['summary'])):
            x = record[n][i]['summary'][j]
            # print(record[n][i]['summary'])
            if x + 1 < record[n][i]['summary'][j + 1]:
                record[n][i]['k'] = x
                record[n]['k_list'].append(x)
                record[n]['k_dict'][x] = i
                break
        else:
            print('error occur')
            print(record)
            input()

    record[n]['k_list'].sort()
    # print(record[n]['k_list'])
    k = record[n]['k_list'][-1]
    print(k, record[n]['k_dict'][k])
    # print(record)
