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

#Using iterative DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res=1
        stack=[[root,1]]
        while stack:
            root,depth=stack.pop()
            if root:
                res=max(res,depth)
                stack.append([root.left,depth+1])
                stack.append([root.right,depth+1])   
        return res  