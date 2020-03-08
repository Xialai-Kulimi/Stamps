import math
import time

m = 1
record = open('1m-record.txt', 'a')
now_max_list = []
max_dict = {}
max_max = {}

while True:
    m += 1
    now_list = []
    max_dict[m] = {}
    max_max[m] = 0

    for i in range(m):  # 初始化陣列
        now_list.append(1)

    for i in range(int(math.pow(m*(m+1)/2, m))):  # 下一種面值分配
        k = 0
        for j in now_list:
            now_list[k] += 1
            if now_list[k] == int(m*(m+1)/2) + 1:
                now_list[k] = 1
                k += 1
            else:
                break
        # print(now_list)
        for j in range(m):  # 每一種撕法
            for k in range(j, m):
                now_max = 0
                for p in range(j, k+1):
                    now_max += now_list[p]  # 紀錄該撕法的總值
                # now_max_list.append(now_max)
                max_dict[m][now_max] = now_list + [j, k, now_max]  # 將總值以及撕法登陸
        # now_max_list.sort()
        for p in range(int(m*(m+1)/2)):  # 檢查連續最大值
            try:
                max_dict[m][p+1]
            except:
                if max_max[m] < p:
                    max_max[m] = p
                # print(str(p)+'23232322232')
                # print(max_dict[m][p])
                break
    print(max_max)
    try:
        print(max_dict[m][max_max[m]])
    except:
        pass
