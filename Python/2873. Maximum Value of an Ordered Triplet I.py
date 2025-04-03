class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        result=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    triplet= (nums[i] - nums[j]) * nums[k]
                    result= max(result,triplet)
        
        return result
