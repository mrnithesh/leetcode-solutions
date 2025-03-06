class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        hashmap={}
        for i in range(1,len(grid)**2+1):
            hashmap.update({i:0})
        for i in grid:
            for j in i:
                hashmap[j]+=1
        a= next(k for k,v in hashmap.items() if v==2)
        b= next(k for k,v in hashmap.items() if v==0)
        return [a,b]  