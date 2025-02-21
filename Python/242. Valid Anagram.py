class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s=[x for x in s]
        list_t=[x for x in t]
        list_s.sort()
        list_t.sort()
        return  list_s==list_t

        #alternative approach 
        from collections import Counter
        return Counter(s)==Counter(t)