class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums=list(set(x for x in nums))
        return len(nums)