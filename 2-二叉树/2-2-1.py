
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if pRoot is None:
            return []

        queue = [pRoot]
        res = []

        while queue:
            res_level = []
            for i in range(len(queue)):
                temp = queue.pop(0)
                res_level.append(temp.val)

                if temp.left is not None:
                    queue.append(temp.left)

                if temp.right is not None:
                    queue.append(temp.right)
            res.append(res_level)
        return res
