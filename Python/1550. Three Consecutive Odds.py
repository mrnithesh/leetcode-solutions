class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        i = 1
        while i+1 <= len(arr)-1:
            if (arr[i-1] % 2 != 0) and (arr[i] % 2 != 0) and (arr[i+1] % 2 != 0):
                return True
            i+=1
        return False