class ListNone():
    def __init__(self,root):
        self.root = root
        self.next = None
class queue():
    def __init__(self):
        self.list1 = []
    def put(self,x):
        self.list1.append(x)
    def get(self):
        return self.list1.pop(0)

    def empty(self):
        return len(self.list1)==0

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        q = queue()
        # write code here
        def mr(root):
            q.put(root)
            while not q.empty():
                r = q.get()
                r.left,r.right = r.right,r.left
                if r.left!=None:
                    q.put(r.left)
                if r.right!=None:
                    q.put(r.right)
            return root
        return mr(root)
root = TreeNode(8);root.left = TreeNode(6);root.right = TreeNode(10);root.left.left = TreeNode(5)
root.left.right = TreeNode(7);root.right.left = TreeNode(9);root.right.right = TreeNode(11)
s = Solution()
root = s.Mirror(root)

def mr1(root):
    q = queue()
    q.put(root)
    while not q.empty():
        r = q.get()
        print(r.val,end=" ")
        if r.left != None:
            q.put(r.left)
        if r.right != None:
            q.put(r.right)
    return root
mr1(root)