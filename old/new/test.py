

a = [[1, 12, 34], [24, 43, 52]]
b = []
c = [1, [1, 2, 3], [1, [1, 2, 1, [1,[1], 2], 1]]]

list_list = []

for sub_list in c:
    x = 0
    while True:

        try:
            sub_list = sub_list[0]
            x += 1
        except:
            break
    print(sub_list)
    list_list.append(x)

list_list.sort()
print(c)
print(list_list[len(list_list)-1])




'''
1  12 34
34 32 34

-1 

1 12 34 -1 34 32 34
'''


