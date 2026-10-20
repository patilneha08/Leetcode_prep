class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        low=float('-inf')
        high=float('inf')
        return self.dfs(root,low,high)

    def dfs(self,root,low,high):
        if not root:
            return True
        if root.val<=low or root.val>=high:
            return False
        return self.dfs(root.left,low,root.val) and self.dfs(root.right,root.val,high)