class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap=defaultdict(int)
        for i in nums:
            hashmap[i]+=1
        freq=sorted(list(hashmap.values()))
        #print(freq[-k:])
        result=[x for x,count in hashmap.items() if count in freq[-k:]]
        return result
    #o(nlogn) due to sorting