class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap=defaultdict(int)
        for i in nums:
            hashmap[i]+=1
        majority_freq=max(list(hashmap.values()))
        majority_element=[x for x,y in hashmap.items() if y==majority_freq]
        return majority_element[0]
