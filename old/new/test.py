from multiprocessing import Process, Queue
import os, time, random


# 寫資料程序執行的程式碼:
def write(q):
    print('Process to write: {}'.format(os.getpid()))
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 讀資料程序執行的程式碼:
def read(q):
    print('Process to read:{}'.format(os.getpid()))
    while True:
        value = q.get()
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # 父程序建立Queue，並傳給各個子程序：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 啟動子程序pw，寫入:
    pw.start()
    # 啟動子程序pr，讀取:
    pr.start()
    # 等待pw結束:
    pw.join()
    # pr程序裡是死迴圈，無法等待其結束，只能強行終止:
    pr.terminate()
