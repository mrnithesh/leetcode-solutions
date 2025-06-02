class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        step, count = 0, 0
        for i in nums:
            step += i
            if step == 0:
                count += 1
        return count