class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        curr = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                curr = 0
                continue
            if (nums[i] == 1):
                curr+=1
                res = max(res,curr)
        return res