# Algorithm

| Date | Time | Title | Content |
| ---- | ---- | ----- | ------- |
| 第 1 天 | 上午 | [lab-01 基础模型](#lab-01-基础模型) | |
| | | [lab-02 排序](#lab-02-排序) | |
| | 下午 | [lab-03 查找](#lab-03-查找) | |
| 第 2 天 | 上午 | [lab-04 图](#lab-04-图) | |
| | 下午 | [lab-05 字符串](#lab-05-字符串) | |
| | | [lab-06 递归](#lab-06-递归) | |
| 第 3 天 | 上午 | [lab-07 回溯](#lab-07-回溯) | |
| | 下午 | [lab-08 动态规划](#lab-08-动态规划) | |
| | | [lab-09 贪心算法](#lab-09-贪心算法) | |
| 第 4 天 | 上午 | [lab-10 广度优先](#lab-10-广度优先) | |
| | | [lab-11 流量与切割](#lab-11-流量与切割) | |
| | 下午 | [lab-12 NP困难](#lab-12-np困难) | |

## lab-00 Reference

- [LeetCode](https://github.com/wu-wenxiang/Training-Python-Public/tree/master/src/leetcode)

## lab-01 基础模型

- 数组和链表
- 栈、列表和背包（集合）
- 标准库的实现

## lab-02 排序

### lab-02-01 选择排序

```python
def findSmallest(a):
    s = 0
    for i, j in enumerate(a):
        if j < a[s]:
            s = i
    return s


def selectionSort(a):
    for i in range(len(a) - 1):
        s = findSmallest(a[(i + 1):]) + i + 1
        if a[i] > a[s]:
            a[i], a[s] = a[s], a[i]
    return a


if __name__ == '__main__':
    myList = [1, 13, 75, 71, 9, 41]
    print(sorted(myList))
    print(selectionSort(myList))
```

### lab-02-02 注入比较逻辑

```python
def findSmallest(a, key=lambda x: x):
    s = 0
    for i, j in enumerate(a):
        if key(j) < key(a[s]):
            s = i
    return s


def selectionSort(a, key=lambda x: x):
    for i in range(len(a) - 1):
        s = findSmallest(a[(i + 1):], key) + i + 1
        if key(a[i]) > key(a[s]):
            a[i], a[s] = a[s], a[i]
    return a


if __name__ == '__main__':
    myList = [1, 13, 75, 71, 9, 41]
    print(sorted(myList, key=lambda x: str(x)))
    print(selectionSort(myList, key=lambda x: str(x)))
```

### lab-02-03 快速排序

```python
def quickSort(a):
    if len(a) < 2:
        return a
    l = quickSort([i for i in a[1:] if i <= a[0]])
    r = quickSort([i for i in a[1:] if i > a[0]])
    return l + [a[0]] + r

if __name__ == '__main__':
    myList = [1, 13, 75, 71, 9, 41]
    print(sorted(myList))
    print(quickSort(myList))
```

### lab-02-04 归并排序

```python
def merge(l, r):
    if not l or not r:
        return l + r
    if l < r:
        return [l[0]] + merge(l[1:], r)
    else:
        return [r[0]] + merge(l, r[1:])


def mergeSort(a):
    # print(a)
    if len(a) < 2:
        return a
    m = len(a) // 2
    return merge(mergeSort(a[:m]), mergeSort(a[m:]))


if __name__ == '__main__':
    myList = [1, 13, 75, 71, 9, 41]
    print(sorted(myList))
    print(mergeSort(myList))
```

### 堆

## lab-03 查找

### lab-03-01 二分查找

```python
import bisect


def bisearch(a, x):
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            hi = mid - 1
        else:
            lo = mid + 1
    return None


def bisearch2(a, x):
    left = bisect.bisect_left(a, x)
    right = bisect.bisect_right(a, x)
    if left == right:
        return None
    return left


if __name__ == '__main__':
    myList = [1, 3, 5, 7, 9, 11]
    print(bisearch(myList, 3))  # 1
    print(bisearch2(myList, 3))  # 1
    print(bisearch(myList, -1))  # None
    print(bisearch2(myList, -1))  # None
```

### lab-03-02 二分排序

```python
import bisect


def bisort(a):
    ret = []
    for i in a:
        bisect.insort(ret, i)
    return ret


if __name__ == '__main__':
    myList = [1, 13, 75, 71, 9, 41]
    print(sorted(myList))
    print(bisort(myList))
```

- 二叉查找树
- 平衡查找树
- 散列表

## lab-04 图

- 无向图
- 有向图
- 最小生成树
- 最短路径

## lab-05 字符串

- 字符串排序
- 单词查找树
- 子字符串查找
- 正则表达式
- 数据压缩

## lab-06 递归

- 分而治之：基线条件和归纳法

### lab-06-02 加法问题

```python
from functools import reduce


def fact(x):
    if x <= 1:
        return 1
    else:
        return x * fact(x - 1)


def fact2(x):
    if x <= 1:
        return 1
    ret = 1
    for i in range(1, x + 1):
        ret *= i
    return ret


if __name__ == '__main__':
    factNum = 5
    print(reduce(lambda x, y: x * y, range(1, factNum + 1), 1))
    print(fact(factNum))
    print(fact2(factNum))
```

- 斐波那契数列
- 分地问题（最小公约数问题）

## lab-07 回溯

- 深度优先算法

## lab-08 动态规划

- 背包问题
- 最长公共子串

## lab-09 贪心算法

- 优先

## lab-10 广度优先

- 广度优先搜索
- 迪克斯特拉算法

## lab-11 流量与切割

- 最大流
- 最小割

## lab-12 NP困难

- 旅行商问题
- 遗传算法
- K临近算法（KNN）