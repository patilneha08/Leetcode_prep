class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.mx = 0

        self.depth(root)

        return self.mx

    def depth(self, root):
        if not root:
            return 0

        left = self.depth(root.left)
        right = self.depth(root.right)

        self.mx=max(self.mx,left+right)

        return 1 + max(left,right)