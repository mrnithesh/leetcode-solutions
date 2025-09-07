class Solution:
    def sumZero(self, n: int) -> List[int]:
        arr = []
        isOdd = False
        if (n%2!=0):
            isOdd = True
            n-=1
        for i in range(n//2):
            arr.append(i+1)
            arr.append(-(i+1))
        if isOdd:
            arr.append(0)
        return arr