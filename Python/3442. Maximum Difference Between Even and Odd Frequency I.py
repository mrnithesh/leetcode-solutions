class Solution:
    def maxDifference(self, s: str) -> int:
        hashmap = defaultdict(int)
        for i in s:
            hashmap[i] +=1
        odd = max([x for x in hashmap.values() if x%2 !=0])
        even = min([x for x in hashmap.values() if x%2 ==0])
        #print(odd,even)
        return odd-even
