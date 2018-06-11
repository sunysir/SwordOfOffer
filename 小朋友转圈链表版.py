# 每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,
# 今年亦是如此。HF作为牛客的资深元老,自然也准备了一些小游戏。
# 其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。然后,
# 他随机指定一个数m,让编号为0的小朋友开始报数。
# 每次喊到m-1的那个小朋友要出列唱首歌,
# 然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,从他的下一个小朋友开始,
# 继续0...m-1报数....这样下去....直到剩下最后一个小朋友,可以不用表演,
# 并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。
# 请你试着想下,哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)

#模拟链表节点
class LinkList():
    def __init__(self,val):
        self.val = val
        self.next = None
class Solution:
    def LastRemaining_Solution(self, n, m):
        pHead = LinkList(0)
        temp = pHead
        #创建环形链表
        for i in range(1,n):
            p = LinkList(i)
            temp.next = p
            temp = p
        temp.next = pHead
        temp = pHead
        count = 0
        #每次m-1出列，知道剩最后一名
        while temp.next.val != temp.val:
            if count == m-2:
                temp.next = temp.next.next
                temp = temp.next
                count = 0
                continue
            temp = temp.next
            count+=1
        return  temp.val

s = Solution()
res = s.LastRemaining_Solution(10,7)
print(res)