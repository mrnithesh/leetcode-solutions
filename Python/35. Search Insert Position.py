class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        middle = (left + right) // 2
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle+1
            elif nums[middle] > target:
                right = middle-1
            
        if nums[middle]<target:
            return middle+1
        else:
            return middle