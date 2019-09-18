# LEGB  Local Enclosed Global Buildin

# len = 34 

# def testFun():
#     global len
#     len = 42
#     print(len)

# testFun()

# 闭包，实现面向对象
# def addN():
#     n = 4
#     def add(x):
#         return x + n
#     return add

# add4 = addN(4)

# print(add4(3))

def addN(n):
    def add(x):
        '''
        add function
        n = %s
        ''' % n
        return x + n
    return add

add4 = addN(4)
add3 = addN(3)

help(add3)
add3.__doc__

print(add4(3), add3(5))
