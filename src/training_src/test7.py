def echo(*args):
    print(args)

def echo2(argv, *args, **kwargs):
    print(argv)



a = list(range(5))
print(a)
a = list(range(3))
print(a)
a[0] = a
print(a)

print(id(a[1]))
print(id(a[0][1]))


b = list(range(5))
print(a)
c = b
c[2] = 'hello'
print(c)


import copy
c= copy.copy(6)

d = copy.deepcopy(7)

aList = [[0]]*2
aList[0][0] = 'hello'
aList[['hello'], ['hello']]

# 链表中的乘法，只是复制了引用关系
