import math

while True:
    n = int(input('n?'))
    pos_num = int(input('pos_num?'))
    p = int(n * (n + 1) / 2)

    stamps = [0] * n

    for i in range(pos_num+1):

        num_pos = 0
        for j in stamps:  # 下一種面值分配
            stamps[num_pos] += 1
            if stamps[num_pos] == p + 1:
                stamps[num_pos] = 1
                num_pos += 1
            else:
                break

        print(stamps)
