from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []
        q=deque([root])
        res=[root.val]
        while q:
            temp=[]
            for k in range(len(q)): 
                root=q.popleft()
                if root.left:
                    q.append(root.left)
                    temp.append(root.left.val)
                if root.right:
                    q.append(root.right)
                    temp.append(root.right.val)
            res.append(temp[-1]) if temp else None
        return res