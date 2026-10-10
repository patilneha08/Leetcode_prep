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
            if curr.next==None:
                h[curr].next=None
            else:
                h[curr].next=h[curr.next]
            if curr.random==None:
                h[curr].random = None
            else:
                h[curr].random = h[curr.random]
            curr=curr.next
        return h[head]