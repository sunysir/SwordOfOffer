# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        temp = pHead1
        l1 = []; l2 = []
        while temp != None:
            l1.append(temp.val)
            temp = temp.next
        temp = pHead2
        while temp != None:
            if temp.val in l1:
                return temp
            else:
                temp = temp.next