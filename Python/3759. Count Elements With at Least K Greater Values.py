class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        if k==0:
            return len(nums)
        nums.sort(reverse=True)
        a = nums[k-1]
        res = [x for x in nums if x<a]
        return len(res)