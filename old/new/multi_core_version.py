import math
import time
import multiprocessing

n = 6


def find_k(first_stamp):
    global n, p, k_dict, k, k_list, group_stamps, check_times
    stamps = [0] * (n - 1) + [first_stamp]

    for i in range(group_stamps):
        # print(i, stamps)
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
            if stamps[j] > stamps[n - j - 1]:
                break  # Skip this time
            elif stamps[j] == stamps[n - j - 1]:
                continue
            else:
                record = []
                # print(stamps, i)
                for m in range(n):  # Methods of coloring.
                    for r in range(m, n):
                        summary = 0
                        for q in range(m, r + 1):
                            summary += stamps[q]
                        record.append(summary)

                record.append(p + 1)  # Make a BIG gap.
                record.sort()

                for m in range(len(record)):
                    x = record[m]
                    if x + 1 < record[m + 1]:
                        if x > k:

                            k_list = [str(stamps)]
                            k = x
                        elif x == k:
                            k_list.append(str(stamps))
                        break
                else:
                    print('error occur')
                    print(record)
                    input()
                break


if __name__ == '__main__':
    start_time = time.time()
    multiprocessing.freeze_support()

    p = int(n * (n + 1) / 2)
    group_stamps = int(math.pow(p, n - 1))
    k = n
    k_list = []
    k_dict = {}
    check_times = int((n - (n % 2)) / 2)
    pools = multiprocessing.Pool(4)

    first_stamp_queue = multiprocessing.Queue()

    for i in range(p):
        first_stamp_queue.put(i)

    ps_list = []

    for i in range(p):
        ps_list.append(multiprocessing.Process(find_k(i)))
        ps_list[i].start()

    for i in range(p):
        ps_list[i].join()

    print(n)
    print(k, k_list)
    f = open('result.md', 'a')
    f.write(f'n: {n}\nk: {k} method: {k_list}\n')
    f.close()
    print(time.time() - start_time)
