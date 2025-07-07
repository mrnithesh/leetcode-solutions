class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}

        for i in range(len(s)):
            c1, c2 = s[i], t[i]
            if (c1 in hashmap1 and hashmap1[c1] != c2) or ( (c2 in hashmap2) and hashmap2[c2] != c1):
                return False
            hashmap1[c1] = c2
            hashmap2[c2] = c1
        return True