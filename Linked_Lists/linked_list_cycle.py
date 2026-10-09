class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s=set()
        if not head:
            return False
        curr=head
        while curr:
            if curr.next in s:
                return True
            elif curr.next==None:
                return False
            else:
                s.add(curr.next)
                curr=curr.next