old_num_list = []

for i in range(10000):
    if i < 1000:
        old_num_list.append('0' * (4 - len(str(i))) + str(i))
    else:
        old_num_list.append(str(i))

print(old_num_list)

target_list = []

for num in old_num_list:
    old_num = int(num)
    num_int = ''
    num = list(num)
    num.reverse()
    for letter in list(num):
        num_int = num_int + letter
    num_int = int(num_int)
    # print(num_int)
    if old_num > num_int:
        target_list.append(old_num)

print(target_list)

ans_list = []

for i in range(1, len(target_list)):
    ans_list.append(target_list[i] - target_list[i - 1])

print(ans_list)

analysis_dict = {}
ans_list2 = []

x = 1

for i in range(1, len(ans_list)):
    if ans_list[i] == ans_list[i - 1]:
        x += 1
    else:
        if x == 1:
            print(str(ans_list[i - 1]) + ', ', end='')
        else:
            print(str(ans_list[i - 1]) + f' * {x}, ', end='')
            x = 1

if ans_list[len(ans_list) - 1] == ans_list[len(ans_list) - 2]:
    x += 1
print(str(ans_list[len(ans_list) - 1]) + f' * {x}, ', end='')
