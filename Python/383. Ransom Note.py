class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hm = {}
        for c in magazine:
            hm[c] = 1+hm.get(c,0)
        for c in ransomNote:
            if c not in hm:
                return False
            if hm[c] <=0:
                return False
            hm[c] -=1
        return True
        