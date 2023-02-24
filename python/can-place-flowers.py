class Solution:
    def is_no_flower(i: int, flowerbed: List[int]):
        return i < 0 or i == len(flowerbed) or flowerbed[i] == 0

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and Solution.is_no_flower(i - 1, flowerbed) and Solution.is_no_flower(i + 1, flowerbed):
                flowerbed[i] = 1
                n -= 1
                if n == 0:
                    return True
        return False
