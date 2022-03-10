# 回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：

def is_palindrome(num):
    st1 = str(num)  # 转字符串
    st2 = st1[::-1]  # 字符串反转
    return st1 == st2


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
                                                  111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
    
    
    
 ------------------------------------
 
 # 用filter求素数
 def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n
        pass


def _not_divisible(n):
    return lambda x: x % n > 0


def prims():
    yield 2
    its = _odd_iter()  # 初始序列
    while True:
        ns = next(its)  # 返回序列的第一个数
        yield ns
        its = filter(_not_divisible(ns), its)  # 构造新序列


for n in prims():
    if n < 1000:
        print(n)
    else:
        break
