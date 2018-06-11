# 题目描述
# 把只包含因子2、3和5的数称作丑数（Ugly Number）。
# 例如6、8都是丑数，但14不是，因为它包含因子7。
# 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        list1 = [1]; num2 = 0; num3 = 0; num5 = 0
        while len(list1) < index:
            val = min([list1[num2]*2,list1[num3]*3,list1[num5]*5])
            if val == list1[num2]*2:num2+=1
            if val == list1[num3]*3:num3+=1
            if val == list1[num5]*5:num5+=1
            list1.append(val)
        print(list1)
s = Solution()
res = s.GetUglyNumber_Solution(1500)
print(res)