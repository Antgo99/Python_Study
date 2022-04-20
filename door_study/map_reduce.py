# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：[‘adam’, ‘LISA’, ‘barT’].
# 输出：[‘Adam’, ‘Lisa’, ‘Bart’]。
from functools import reduce


def normalize(name):
    name = name[0].upper() + name[1:].lower()
    return name


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)



---------------------------------------------------------------------------
 # 写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    def mul(x, y):
        return x * y

    return reduce(mul, L)
    pass


print(prod([3, 10, 100]))




---------------------------------------------------------------------------

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

def str2float(s):
    def fn(x, y):
        return 10 * x + y

    n = s.index('.')
    s1 = list(map(int, [x for x in s[:n]]))
    s2 = list(map(int, [x for x in s[n + 1:]]))
    return reduce(fn, s1) + reduce(fn, s2) / 10 ** len(s2)


if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
