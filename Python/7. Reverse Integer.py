class Solution:
    def reverse(self, x: int) -> int:
        sign=1
        if x<0:
            sign=-1
            x=abs(x)
        res=0
        while x>0:
            res=res*10 + x%10
            x//=10

        int_max=2**31+1
        int_min=-2**31

        if res<int_max and res>int_min:
            return res*sign
        else:
            return 0
        