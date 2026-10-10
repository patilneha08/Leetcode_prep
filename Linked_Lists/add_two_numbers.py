class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tmp1,tmp2=l1,l2
        l3=ListNode(0)
        dummy=l3
        carry=0
        while tmp1 or tmp2 or carry:
            val1=tmp1.val if tmp1 else 0
            val2=tmp2.val if tmp2 else 0

            val = val1+val2+carry

            dummy.next=ListNode(val%10)
            carry=val//10

            dummy=dummy.next
            tmp1=tmp1.next if tmp1 else None
            tmp2=tmp2.next if tmp2 else None
            
        return l3.next


            