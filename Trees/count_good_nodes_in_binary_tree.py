class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxval=root.val
        self.dfs(root,maxval)
        return self.res

    def dfs(self,root,maxval):
        if not root:
            return 0
        self.res = 1 if root.val>=maxval else 0
        maxval=max(maxval,root.val)
        self.res+=self.dfs(root.left,maxval)
        self.res+=self.dfs(root.right,maxval)
        return self.res