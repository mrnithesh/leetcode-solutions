class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = set()
        keyindxs = []
        
        for i in range(len(nums)):
            if nums[i] == key:
                keyindxs.append(i)
        
        for i in range(len(nums)):
            for keyindx in keyindxs:
                if abs(i-keyindx) <= k:
                    res.add(i)
        return list(res)