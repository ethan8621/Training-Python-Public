import time

# 默认参数陷阱，ts值在定义时已给定，再次调用时，并不会再赋默认值
def logging(msg, ts = time.time()):
    print('%s: %s' % (ts, msg))

def logging2(msg, ts = None):
    if ts is None:
        ts = time.time()
    print('%s: %s' % (ts, msg))

logging('msg1', time.time()+2)
logging('msg2')
print(time.time())


a = 32
def addA(a):
    # global a 和 local a 其实是不同的a
    a = a + 1
    return a

print(addA(32))