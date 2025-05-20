class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero = 0
        for i in nums:
            if i:
                prod*=i
            else:
                zero+=1
        if zero>1 : return [0] * len(nums)
        res = [0] * len(nums)
        for i, num in enumerate(nums):
            if zero:
                if num:
                    res[i] = 0
                else:
                    res[i] = prod
            else:
                res[i] = prod // num
        return res