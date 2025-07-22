class Solution:
    def addDigits(self, num: int) -> int:
        while num>=10:
            n = 0
            while num>0:
                digit = num % 10
                n += digit
                #print(digit,n)
                num//=10
            num=n
        return num