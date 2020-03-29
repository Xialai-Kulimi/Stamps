import time

start_time = time.time()

a = '1' * 2147483647

# f = open('test_file', 'w')
# f.write('1'*2147483647)
# f.close()

print(time.time() - start_time)
