class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if root.val==subRoot.val:
            if self.check(root,subRoot):
                return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)


    def check(self,p,q):
        if not p and not q:
            return True
        if not p or not q or p.val!=q.val:
            return False
        return self.check(p.left,q.left) and self.check(p.right,q.right)