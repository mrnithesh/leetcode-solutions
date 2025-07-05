class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        start = 0
        windowsum = 0
        for end in range(len(nums)):
            windowsum += nums[end]
            while windowsum >= target:
                res = min(res, end-start+1)
                windowsum -= nums[start]
                start+=1
        return res if res!=float('inf') else 0