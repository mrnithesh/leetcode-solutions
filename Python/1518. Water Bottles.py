class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res  = numBottles
        while numBottles>=numExchange:
            temp =  numBottles//numExchange
            res += temp
            numBottles = temp + numBottles%numExchange
        return res
