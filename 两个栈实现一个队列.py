# 题目描述
# 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。

import copy
#模拟栈
class Stack:
    def __init__(self):
        self.list1 = []
    def push(self,x):
        self.list1.insert(0,x)
    def pop(self):
        return self.list1.pop(0)
    def isEmpty(self):
        if len(self.list1) == 0:
            return True
        else:
            return False


# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        # 栈1
        self.stack1 = Stack()
        self.count = 0
    def put(self, x):
        self.stack1.push(x)
        self.count+=1
    def get(self):
        # 辅助栈2
        stack2 = copy.deepcopy(self.stack1)
        count_ = self.count
        temp = None
        while count_:
            temp = stack2.pop()
            count_-=1
        self.count-=1
        return temp





s = Solution()
s.put(1)
s.put(2)
print(s.get())
s.put(3)
print(s.get())
print(s.get())
print(s.get())





