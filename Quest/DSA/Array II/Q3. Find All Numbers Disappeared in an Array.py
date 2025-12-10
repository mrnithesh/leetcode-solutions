class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for num in nums:
            idx = abs(num) - 1         
            if nums[idx] > 0:          
                nums[idx] = -nums[idx]

        missing = [i + 1 for i, val in enumerate(nums) if val > 0]
        return missing