class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        self.invert(root)
        return root

    def invert(self,node):
        if not node:
            return
        self.invert(node.left)
        self.invert(node.right)
        temp=node.left
        node.left=node.right
        node.right=temp