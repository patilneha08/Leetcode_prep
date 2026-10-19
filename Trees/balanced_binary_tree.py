class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        self.mx=0
        self.checkb(root)
        return self.mx<=1
    def checkb(self,root):
        if not root:
            return 0
        left=self.checkb(root.left)
        right=self.checkb(root.right)
        self.mx=max(self.mx,abs(left-right))
        return 1+max(left,right)