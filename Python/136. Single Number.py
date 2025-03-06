class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap={}
        for i in nums:
            hashmap[i]=hashmap.get(i,0)+1
        return next(i for i,j in hashmap.items() if j==1)
