class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currentSum = sum(nums[:k])
        maxAvg = currentSum / k
        for i in range(k,len(nums)):
            currentSum += nums[i]
            currentSum -= nums[i-k]
            maxAvg = max(maxAvg, currentSum / k)
        return maxAvg