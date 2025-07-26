class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('inf')
        nums.sort()
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1

            while j<k:
                #print(i,j,k)
                total = nums[i] + nums[j]+nums[k]
                if abs(total-target) < abs(res-target):
                    res= total
                if total<target:
                    j+=1
                else:
                    k-=1
        return res