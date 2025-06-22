class Solution: #O(n) - SC
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i] +=1
        return [x for x,y in hashmap.items() if y>=2][0]

class Solution: #O(n) - SC
    def findDuplicate(self, nums: List[int]) -> int:
        numSet = set()
        res = None
        for i in nums:
            if i not in numSet:
                numSet.add(i)
            elif i in numSet:
                res=i
        return res

