class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        if tomatoSlices % 2 == 1:
            return []
        if (tomatoSlices // 2) < cheeseSlices:
            return []
        if cheeseSlices < (tomatoSlices // 4):
            return []
        total_burgers = cheeseSlices
        total_jumbo = (tomatoSlices - total_burgers * 2) // 2
        total_small = total_burgers - total_jumbo
        return [total_jumbo, total_small]
