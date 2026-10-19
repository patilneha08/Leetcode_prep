class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val>=root.val and q.val>=root.val:
            if p.val==root.val or q.val==root.val:
                return root
            else:
                return self.lowestCommonAncestor(root.right,p,q)
        elif p.val<=root.val and q.val<=root.val:
            if p.val==root.val or q.val==root.val:
                return root
            else:
                return self.lowestCommonAncestor(root.left,p,q)
        elif p.val<root.val<q.val or p.val>root.val>q.val:
            return root

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr=root
        while curr:
            if p.val>curr.val and q.val>curr.val:
                curr=curr.right
            elif p.val<curr.val and q.val<curr.val:
                curr=curr.left
            else:
                return curr