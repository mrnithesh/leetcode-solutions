class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=0
        for i in range(len(digits)):
            num=num*10 + digits[i]
        num+=1
        result=[]
        while num>0:
            result.insert(0,num%10)
            num//=10
        return result
#O(N) Time complexity
        