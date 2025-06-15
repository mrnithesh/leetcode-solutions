class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        hashmap = defaultdict(int)
        for i in nums:
            hashmap[i] +=1
        res = [x for x,y in hashmap.items() if y==2]
        for i in range(1,len(nums)+1):
            if i not in nums:
                res.append(i)
        return res

#math based, better TC and SC
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        expectedSum = n * (n + 1) // 2
        actualSum = sum(set(nums)) 
        duplicate = sum(nums) - actualSum
        missing = expectedSum - actualSum
        return [duplicate, missing]