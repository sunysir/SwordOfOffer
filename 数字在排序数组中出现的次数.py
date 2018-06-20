

# -*- coding:utf-8 -*-
#题目描述
#统计一个数字在排序数组中出现的次数。
from collections import Counter
class Solution:
    def GetNumberOfK(self, data, k):
        dict1 = Counter(data)
        return dict1[k]


s = Solution()
res = s.GetNumberOfK([1,1,2,3,4],1)
print(res)