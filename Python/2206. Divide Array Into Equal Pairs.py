class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hashmap=defaultdict(int)
        for i in nums:
            hashmap[i]+=1
        count=set(hashmap.values())
        #print(count)
        for i in count:
            if i %2!=0:
                return False
        return True