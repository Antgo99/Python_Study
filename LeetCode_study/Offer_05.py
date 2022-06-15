# 剑指 Offer 05. 替换空格
# 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。
# 示例 1：
# 输入：s = "We are happy."
# 输出："We%20are%20happy."

def replaceSpace(s):
#     self = ""
#     for item in s:
#         if item == " ":
#             self += "%20"
#         else:
#             self += item

#     return self
    res = []
    for c in s:
        if c==" ":res.append("%20")
        else:res.append(c)
    return "".join(res) #组成一个新的字符串

s="We are happy."
print(replaceSpace(s))
