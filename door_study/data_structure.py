# -*- coding = utf-8 -*-
# @Time : 2022/6/15 19:09
# @Author : Antgo99
# @File : data_structure.py
# @Software : PyCharm

#链表
class ListNode:
    def __init__(self,x):
        self.val = x #节点值
        self.next = None #后继节点引用

#实例化节点
n1 = ListNode(4)
n2 = ListNode(5)
n3 = ListNode(1)

#构建引用指向
n1.next = n2
n2.next = n3


#栈 先进后出
stack = []
stack.append(1) #进栈

stack.append(2) #进栈

stack.pop() #出栈

stack.pop() #出栈

#队列 先进先出
#python通常使用双端队列collection.deque
from collections import deque

queue = deque()
queue.append(1)

queue.append(2)

queue.popleft()

queue.popleft()


#树
class TreeNode:
    def __init__(self,x):
        self.val = x #节点值
        self.left = None #左子节点
        self.right = None #右子节点

#初始化节点
N1 = TreeNode(3) #根节点
N2 = TreeNode(4)
N3 = TreeNode(5)
N4 = TreeNode(1)
N5 = TreeNode(2)

#构建引用指向
N1.left = N2
N1.right = N3
N2.left = N4
N2.right = N5

#图
#1.邻接矩阵
vertices_matrix = [1,2,3,4,5]
edges_matrix = [
    [0,1,1,1,1],
    [1,0,0,1,0],
    [1,0,0,0,1],
    [1,1,0,0,1],
    [1,0,1,1,0]
]
#2.邻接表
vertices_table = [1,2,3,4,5]
edges_table = [
    [1,2,3,4],
    [0,3],
    [0,4],
    [0,1,4],
    [0,2,3]
]

#邻接表 适合存储稀疏图（顶点较多、边较少）； 邻接矩阵 适合存储稠密图（顶点较少、边较多）。

#散列表
dic = {}
dic["小力"] = 1001
dic["小特"] = 1002
dic["小扣"] = 1003

# for key,value in dic.items():
#     print(key,value)

#堆
from heapq import heappush,heappop
#初始化小顶堆
heap = []
#元素入堆
heappush(heap,1)
heappush(heap,4)
heappush(heap,2)
heappush(heap,6)
heappush(heap,8)
#元素出堆（从小到大）
print(heap)
heappop(heap)
print(heap)
heappop(heap)
print(heap)
heappop(heap)
print(heap)
heappop(heap)
print(heap)
heappop(heap)
print(heap)

