class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = defaultdict(int)
        for i in s:
            hashmap[i]+=1
        uniquechars = [x for x,y in hashmap.items() if y==1]
        if uniquechars:
            return s.find(uniquechars[0])
        else:
            return -1