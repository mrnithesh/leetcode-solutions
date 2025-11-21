class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        j = n
        res = [0]*len(nums)
        for k in range(0,len(nums),2):
            res[k] = nums[i]
            res[k+1] = nums[j]
            i+=1
            j+=1
        return res