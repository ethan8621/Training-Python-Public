# inputStr = "45 100 34 45.2 66      78"

# print(inputStr)


# aList = inputStr.split()

# print(aList)


# bList = []
# sum = 0
# for i in aList:
#     bList.append(float(i))
#     sum += float(i)


# print(bList)

# print(sum)

# bList = [float(i) for i in aList]
# print(bList)

# bList.sort()

# bList = bList[1:-1]

# bList = sorted(bList)[1:-1]


# print(sum(bList)/len(bList))

fruit = {'apple': 15, 'pear': 8, 'orange': 6.5, 'banana': 10, 'mango': 23}
for i in sorted(fruit, key=lambda x: fruit[x]):
    print(i, fruit[i])
