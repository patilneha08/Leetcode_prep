#Using DFS
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

#Using BFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q=deque()
        q.append(root)
        l=0
        while q:
            for i in range(len(q)):
                root=q.popleft()
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
            l+=1
        return l