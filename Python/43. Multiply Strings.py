class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        a,b =0,0
        for i in range(len(num1)):
            a = a * 10 + (ord(num1[i])-ord('0'))
        for i in range(len(num2)):
            b = b * 10 + (ord(num2[i])-ord('0'))
        return str(a*b)