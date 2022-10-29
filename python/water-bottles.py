class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        full_bottles = numBottles
        empty_bottles = 0
        drank_bottles = 0
        while full_bottles:
            drank_bottles += full_bottles
            empty_bottles += full_bottles
            full_bottles = empty_bottles // numExchange
            empty_bottles = empty_bottles % numExchange
        return drank_bottles
