class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force approach
        for i in range (len(nums)):
            for j in range (i+1,len(nums)):
                if (nums[j]==target-nums[i]):
                    return [i,j]
        return [i,j]

        #hashmap approach
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i, num in enumerate(nums):
            diff=target-nums[i]
            if diff in hashmap:
                return[i,hashmap[diff]]
            hashmap[num]=i 
        
        return []