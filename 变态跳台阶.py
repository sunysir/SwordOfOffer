# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        if number == 0:
            return 0
        a = 1;b = 1
        for i in range(number):
            a,b = b,a+b
        return a

# write code here


s = Solution()
print(s.rectCover(5))