class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l= 0
        r = len(matrix)-1
        while l<=r:
            mid = (l+r) //2
            print(matrix[mid])
            if target in matrix[mid]:
                return True
            elif matrix[mid][0]>target:
                r = mid-1
            else:
                l = mid+1
        return False