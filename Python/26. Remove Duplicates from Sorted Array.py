class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = 0
        temp = set()
        for i in range(len(nums)):
            if nums[i] not in temp:
                nums[res] = nums[i]
                temp.add(nums[i])
                res+=1
        return res