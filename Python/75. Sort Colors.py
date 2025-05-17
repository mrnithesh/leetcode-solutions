class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0,0,0]
        for i in nums:
            freq [i] += 1
        i = 0
        for color in range(3):
            for _ in range(freq[color]):
                nums[i] = color
                i+=1