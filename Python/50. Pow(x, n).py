class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if x==0:
                return 0
            if n==0:
                return 1
            result = power(x,n//2)
            result = result*result
            return result if n%2==0 else result*x
        result=power(x,abs(n))

        return result if n>0 else 1/result