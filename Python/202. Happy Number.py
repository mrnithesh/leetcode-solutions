class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(n):
            num = 0
            while n>0:
                digit = n%10
                num += digit **2
                n//= 10
            return num
        visited = set()
        while n not in visited:
            visited.add(n)
            n = helper(n)
        return n==1