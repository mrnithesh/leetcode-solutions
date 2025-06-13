class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i] +=1
        return [x for x,y in hashmap.items() if y>=2][0]
