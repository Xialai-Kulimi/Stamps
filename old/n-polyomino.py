# import numpy as np
shape_num = [1]
f = open('shape.txt', 'r')
shapes = f.read()
f.close()

# print(shape)


def access_shape(n, i):  # 方便存取n-方垛中的第i個圖形的函式
    global shapes
    return shapes.split('===\n')[n - 1].split('---\n')[i - 1]


def add_shape(shape, uni_code):  # 方便將新的shape加進去shapes
    global shapes
    shapes = shapes + '---\n' + shape + '@' + str(uni_code) + '\n'
    return


def calculate_shape_num(n):
    global shapes, shape_num
    if len(shape_num) > n:
        return shape_num[n-1]
    else:
        old_shape = ''
        x = 0
        y = 0
        this_shape_num = 0

        for i in range(0, calculate_shape_num(n-1)-1):  # 第一步，找一個之前還沒被加工過的n-1-方垛

            shape = access_shape(n-1, i)

            old_shape = ' ' * (n+1) + '\n'
            for line in shape.split('\n'):
                old_shape = old_shape + ' ' + line + ' \n'  # 去頭去尾再多加一格空間
            old_shape = old_shape + ' ' * (n + 1) + '\n'

            old_shape = old_shape.split('\n')  # 之後比較方便換行繼續處理，也比較好編輯

            for j in range(0, n-1):  # 第二步，找到圖形最右下角的方塊，從他的右邊開始處理
                for k in range(0, n-1):
                    if old_shape[n-j-1][n-k-1] == '#':
                        y = j+1
                        x = k+2  # 紀錄位置

        while True:  # 使用while規避遞迴限制，因為整個函式最多只會呼叫自己一次，所以不會超出限制
            new_shape = old_shape  # 將 old_shape 複製後再對其進行修改

            if new_shape[y][x] == '#':  # 檢查此處是否有方塊
                print('err, there is already a block here.', n, this_shape_num, x, y)
                while True:  # 讓我可以在出錯時檢查或是讓他繼續執行
                    try:
                        print(exec(input()))
                    except:
                        print('command error, type \'exit()\' to terminate')  # 告訴不知道的人如何結束程式

            new_shape[y] = new_shape[y][0:x] + '#' + new_shape[y][x+1:len(new_shape[y])]  # 在該圖(x, y)處放置一個方塊




        shapes = shapes + '===\n'


while True:
    try:  # 輸入n
        n = int(input('n?'))
    except:  # 防呆機制
        print('err, pls input positive int')
        continue
    if n == 1:
        print(1)
        continue
    elif n < 1:
        print('err, negative or zero get')
        continue
    else:  # 從0開始算，可以幫助之後規避python的遞迴限制
        x = 0
        while x < n:
            x += 1
            print(str(x) + str(calculate_shape_num(x)))


print('Program finish')
