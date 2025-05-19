class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return "none"
        uniqueSides = set()
        for i in nums:
            uniqueSides.add(i)
        if len(uniqueSides) == 1:
            return "equilateral"
        elif len(uniqueSides) == 2:
            return "isosceles"
        else:
            return "scalene"

            