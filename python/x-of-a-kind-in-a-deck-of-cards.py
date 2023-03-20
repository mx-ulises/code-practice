from math import gcd

class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        card_count = defaultdict(lambda: 0)
        for card in deck:
            card_count[card] += 1
        list_gdc = reduce(gcd, [card_count[card] for card in card_count])
        return 1 < list_gdc
