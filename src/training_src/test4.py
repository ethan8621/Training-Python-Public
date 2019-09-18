# 唱票算法

aStr = 'aaaabbbbbbbaaaaaaacceeeeeeecccddddaaaeeeeeee'
# print(set(aStr))

# for i in set(aStr):
#     print(i, aStr.count(i))

aDict = {}
# for i in aStr:
#     # print(i)
#     if i in aDict:
#         aDict[i] += 1
#     else:
#         aDict[i] = 1

# print(aDict)

# for i in aStr:
#     # if i not in aDict:
#     #     aDict[i] = 0
#     # aDict[i] = aDict.get(i, 0) + 1
#     aDict.setdefault(i, 0)
#     aDict[i] = aDict[i] + 1


# print(aDict)

import collections
aDict = collections.Counter(aStr)

print(aDict)
