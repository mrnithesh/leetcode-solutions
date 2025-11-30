class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(x):
            n = 0
            while x>0:
                n = n*10 + x%10
                x//=10
            return n
        res = float('inf')
        rev_map = {}          
        for i in range(len(nums)):
            current = nums[i]
        
            if current in rev_map:
                res = min(res, i - rev_map[current])
                if res == 1:
                    return 1
        
            r = reverse(current)
            rev_map[r] = i
        if res==float('inf'):
            return -1
        return res