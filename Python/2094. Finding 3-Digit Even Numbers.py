class Solution: #O(n^3) TC
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = set()
        n = len(digits)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and j != k and i != k:
                        a, b, c = digits[i], digits[j], digits[k]
                        if a != 0 and c % 2 == 0:
                            num = a * 100 + b * 10 + c
                            res.add(num)
        return sorted(res)

class Solution: #O(N)
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res = []
        from collections import Counter
        freq = Counter(digits)
        for i in range(100,1000,2):
            num = [(i//100), (i//10)%10, i%10]
            temp = Counter(num)
            if all(freq[d] >= temp[d] for d in temp):
                res.append(i)
        return res
            