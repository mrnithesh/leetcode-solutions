class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numSet = set(nums)
        res = 0
        for num in numSet:
            if num-1 not in numSet:
                currNum=num
                streak = 1
                while currNum+1 in numSet:
                    streak+=1
                    currNum +=1
                res = max(res,streak)
        return res