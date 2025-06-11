class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = defaultdict(list)

        for i, num in enumerate(nums):
            hashmap[num].append(i)

        for indexes in hashmap.values():
            if len(indexes)>=2:
                for i in range(1,len(indexes)):
                    if indexes[i] - indexes[i-1] <= k:
                        return True
        return False 