import time

a, b = 1, 2
for i in range(100):
    print(a)
    time.sleep(1)
    a, b = b, a + b 
