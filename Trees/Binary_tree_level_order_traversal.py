from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:

        if not root:
            return []
        q=deque([root])
        res=[]
        while q:
            temp=[]
            for k in range(len(q)):
                root=q.popleft()
                temp.append(root.val)
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            res.append(temp) if temp else None
        return res