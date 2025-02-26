class Solution:
    def mySqrt(self, x: int) -> int:
        i=1
        while i*i<=x:
            i+=1
        return i-1