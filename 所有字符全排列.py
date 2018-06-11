import copy
class Solution:
    def Permutation(self, ss):
        #特殊边界判断
        if len(ss) == 0:
            return []
        if len(ss) == 1:
            return [ss]
        # write code here
        ss = list(ss)
        count = 0
        list1 = []
        def change(arr,count,list1):
            #遍历字符从count开始，其实count为0，没递归依次count加1
            for i in range(count,len(arr)):
                #直接递归到count == len(arr)-2开始储存结果
                if count == len(arr)-2:
                    temp = copy.copy(arr)
                    temp[count], temp[i] = temp[i], temp[count]
                    list1.append("".join(temp))
                    continue
                temp = copy.copy(arr)#对字符串浅复制，以保证原字符串不变
                temp.insert(0,temp[i])#temp[count], temp[i] = temp[i], temp[count]这种方式交换也可
                temp.pop(i+1)
                list1=change(temp,count+1,list1)
            return list1
        list1 = change(ss, count, list1)
        list2 = []
        #筛选出重复字符串
        for i in list1:
            if i not in list2:
                list2.append(i)
        return list2

s = Solution()
res = s.Permutation("abc")
print(res)