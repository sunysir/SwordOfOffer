
#题目描述
#小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,他马上就写出了正确答案是100。
#但是他并不满足于此,他在想究竟有多少种连续的正数序列的和为100(至少包括两个数)。
#没多久,他就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把问题交给你,
#你能不能也很快的找出所有和为S的连续正数序列? Good Luck!
#输出描述:
#输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序

# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        n_max = int((2*tsum)**.5)
        n_min = 2
        l1 = []
        for i in range(n_min, n_max+1)[::-1]:
            #整数   n为奇   非整数  n为偶
           if tsum%i==0 and i%2!=0:#整数 n为奇
               st = tsum//i-i//2
               l1.append([st+i for i in range(i)])
           elif tsum/i-tsum//i==0.5 and i%2==0:#非整 n为偶
               st = tsum//i - i//2+1
               l1.append([st+i for i in range(i)])
        return l1

s = Solution()
res = s.FindContinuousSequence(3)
print(res)

