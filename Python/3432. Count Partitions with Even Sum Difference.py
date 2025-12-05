class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        total = sum(nums)
        res = 0
        left = 0
        for i in range(len(nums)-1):
            left+=nums[i]
            right = total -left
            if (left-right) %2 ==0:
                res +=1
        return res