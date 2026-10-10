class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=first=head
        t,l=0,1
        while curr:
            t+=1
            curr=curr.next
        i=t-n
        if i==0:
            head=head.next
            return head
        temp=head
        first=temp.next
        while first:
            if l==i:    
                temp.next=first.next
                return head
            else:
                first=first.next
                temp=temp.next
                l+=1
        return head
    
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        slow=fast=dummy
        while n:
            fast=fast.next
            n-=1
        
        while fast.next:
            slow=slow.next
            fast=fast.next

        slow.next=slow.next.next
        return dummy.next