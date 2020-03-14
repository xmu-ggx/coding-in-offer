
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if root is None:
            return []

        queue = [root]
        res = []
        
        while queue:

            temp = queue.pop(0)
            res.append(temp.val)

            if temp.left is not None:
                queue.append(temp.left)

            if temp.right is not None:
                queue.append(temp.right)

        return res
