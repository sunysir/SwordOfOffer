#-*- coding:utf-8 -*-
import copy
from functools import partial
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
l_total = []
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if root == None:
            return []
        list1 = []
        def rec(root,list1):
            global l_total
            #局部根节点不变
            list1.append(root.val)
            #独立复制改变存储子节点
            temp = copy.copy(list1)
            if root.left == None and root.right == None:
                temp1 = copy.copy(temp)
                l_total.append(temp1)
                temp.pop(len(temp)-1)
                return
            if root.left != None:
                rec(root.left,temp)
                temp = copy.copy(list1)
            if root.right != None:
                rec(root.right,temp)
                temp = copy.copy(list1)
        rec(root,list1)
        def filter_owm(obj,expectNumber):
            return sum(obj)==expectNumber
        filt = partial(filter_owm,expectNumber=expectNumber)
        return list(filter(filt,l_total))

root = TreeNode(1); root.left = TreeNode(2); root.right = TreeNode(3); root.left.left = TreeNode(4)
root.left.right = TreeNode(5); root.right.left = TreeNode(6)
s = Solution()
res = s.FindPath(root,7)
print(res)





