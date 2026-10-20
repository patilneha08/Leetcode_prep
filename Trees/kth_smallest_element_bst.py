class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        cur=root
        stack=[]
        while cur or stack:
            while cur:
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            k-=1
            if k==0:
                return cur.val
            cur=cur.right