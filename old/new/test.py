import time
import math

b = 0
a = int(4294967296*4294967296)

start_time = time.time()

while a != 1:
    a = math.pow(a, 0.5)
    b += 1

print(time.time() - start_time, b)

b = 0

a = int(4294967296*4294967296)

start_time = time.time()

while a != 1:
    a = pow(a, 0.5)
    b += 1

print(time.time() - start_time, b)

b = 0

a = int(4294967296*4294967296)

start_time = time.time()

while a != 1:
    a = a ** 0.5
    b += 1

print(time.time() - start_time, b)
