class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        n = len(nums)
        res = [True] *n
        
        dec = 0
        for i in range(n):
            dec = (2*dec + nums[i])%5
            res[i]= dec%5==0

        return res