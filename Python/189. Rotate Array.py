class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = [0]*len(nums)
        for i in range(len(nums)):
            if i+k < len(nums):
                temp[i+k] = nums[i]
            else:
                temp[(i+k)%len(nums)] = nums[i]
        for i in range(len(nums)):
            nums[i] = temp[i]


class Solution: #O(1) SC : no addtional memory space
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        def reverse(l,r):
            while l<r:
                nums[l] , nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        reverse(0,len(nums)-1)
        reverse(0,k-1)
        reverse(k,len(nums)-1) 