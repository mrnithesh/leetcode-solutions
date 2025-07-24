class Solution:
    def countDigits(self, num: int) -> int:
        res = []
        n = num
        while num>0:
            digit = num%10
            if n%digit==0:
                res.append(digit)
            num//=10
        return len(res)