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

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i]+1 != 10:
                digits[i] += 1
                return digits
            digits[i] = 0
            if i==0:
                return [1]+digits

        
        