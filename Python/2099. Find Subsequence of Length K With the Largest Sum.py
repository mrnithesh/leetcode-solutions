class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        arr = [[i,nums[i]] for i in range(n)]
        arr.sort(key=lambda x :x[1],reverse=True) #sort values in descending order
        arr = sorted(arr[:k]) #get first k elements and sort based on index
        res = [y for x, y in arr]
        return res