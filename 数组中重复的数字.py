# -*- coding:utf-8 -*-
from collections import Counter
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        dict1 = Counter(numbers)
        for i in numbers:
            if dict1[i] > 1:
                duplication[0] = i
                return True
        return False