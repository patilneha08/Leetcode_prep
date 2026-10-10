class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        h={}
        curr=head
        if not head:
            return None
        while curr:
            h[curr]=Node(curr.val)
            curr=curr.next
        curr=head
        while curr:
            h[curr].next = h.get(curr.next,None)
            h[curr].random = h.get(curr.random,None)
            curr=curr.next
        return h[head]