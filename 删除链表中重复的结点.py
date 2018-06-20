# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead == None or pHead.next == None:
            return pHead
        temp = pHead
        l1 = []
        while temp!=None:
            l1.append(temp.val)
            temp = temp.next
        temp = []
        if len(set(l1)) == 1:
            return None
        for i in l1:
            if i not in temp:
                temp.append(i)
            else:
                temp.remove(i)
        l1 = temp
        if len(l1) == 0:
            return None
        pHead = ListNode(l1.pop(0))
        temp = pHead
        while len(l1):
            p = ListNode(l1.pop(0))
            temp.next = p
            temp = p
        return pHead