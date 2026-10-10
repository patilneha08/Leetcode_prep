class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1
        for i in range(len(digits)-1,-1,-1):
            temp=digits[i]
            temp+=carry
            carry=temp//10
            digits[i]=temp%10
        if carry:
            digits.insert(0,carry)
        return digits