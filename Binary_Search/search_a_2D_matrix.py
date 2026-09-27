class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r=0,len(matrix)-1
        while l<=r:
            m=l+(r-l)//2
            l1,r1=0,len(matrix[m])-1
            while l1<=r1:
                m1=l1+(r1-l1)//2
                if target>matrix[m][m1]:
                    l1=m1+1
                elif target<matrix[m][m1]:
                    r1=m1-1
                elif target==matrix[m][m1]:
                    return True
            if target>matrix[m][-1]:
                l=m+1
            elif target<matrix[m][0]:
                r=m-1
            else:
                return False
        return False