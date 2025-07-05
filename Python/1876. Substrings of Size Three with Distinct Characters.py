class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res = 0
        i = 0
        j = 3
        while j<=len(s):
            window =  s[i:j]
            if (len(set(window)) == 3):
                res+=1
            i+=1
            j+=1
        return res