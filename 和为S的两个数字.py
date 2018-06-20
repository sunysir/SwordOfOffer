
#题目描述
#输入一个递增排序的数组和一个数字S，在数组中查找两个数，是的他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。
#输出描述:
#对应每个测试案例，输出两个数，小的先输出。
# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if len(array) == 0:
            return []
        if len(array) == 1:
            if tsum == array[0]:
                return array[0]
            else:
                return []
        dict1 = {}
        l1 = []
        for i in range(len(array)):
            if tsum-array[i] not in dict1:
                dict1[array[i]] = i
            else:
                l1.append([array[i],tsum-array[i]])
        minu = 2**31
        temp_list = []
        for i in l1:
            temp = i[0]*i[1]
            if minu > temp:
                minu = temp
                temp_list = [i[0], i[1]]
        if len(temp_list) == 0:
            return []
        return [min(temp_list),max(temp_list)]

s = Solution()
res = s.FindNumbersWithSum([0], 5)
print(res)
