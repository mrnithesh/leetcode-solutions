class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i=0
        while i*i<=num:
            i+=1
        if (i-1)*(i-1)==num:
            return True
        else:
            return False     