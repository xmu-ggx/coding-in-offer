
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if pRoot is None or k <= 0:
            return None

        stack = [pRoot]
        count = 0

        while stack:

            while pRoot:
                stack.append(pRoot)
                pRoot = pRoot.left

            temp = stack.pop()
            count += 1

            if count == k:
                return temp

            if temp.right is not None:
                pRoot = temp.right

        return None
