# def addN(n):
#     def add(x):
#         return x+n
#     return add


class addN(object):
    def __init__(self, n):
        self.n = n
# 括号运算符

    def __call__(self, x):
        return x+self.n


add3 = addN(3)
add4 = addN(4)

print(add3(42), add4(42))
