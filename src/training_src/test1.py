import random

# a = random.random()
# b = random.random()

# print(a, b)

a = random.random()
b = random.random()

# print(a, b)

a = round(a, 2)
b = round(b, 2)

# print(a, b)

inputSum = input('%.2f + %.2f = \n' % (a, b))
print(inputSum)

if abs(a+b-float(inputSum)) <= 0.0000000001:
    print('Correct')
else:
    print('Incorrect')
