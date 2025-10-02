class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        emp = 0
        exc = numExchange
        res = 0
        full = numBottles

        while full>0:
            res += full
            emp += full
            full = 0
            while emp>=exc:
                full+=1
                emp-=exc
                exc+=1

        return res
