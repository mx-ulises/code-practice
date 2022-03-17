def get_needs_cost(needs, price):
    cost = 0
    for i in range(len(needs)):
        cost += needs[i] * price[i]
    return cost


def is_valid(needs, memory):
    if str(needs) in memory:
        return False
    for item in needs:
        if item < 0:
            return False
    return True


def get_new_need(needs, s):
    new_needs = list(needs)
    for i in range(len(new_needs)):
        new_needs[i] -= s[i]
    return new_needs


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        h = [(0, needs)]
        minimal = get_needs_cost(needs, price)
        memory = set()
        while h:
            cost, needs = heappop(h)
            if is_valid(needs, memory) == False:
                continue
            minimal = min(minimal, cost + get_needs_cost(needs, price))
            for s in special:
                new_need = get_new_need(needs, s)
                heappush(h, (cost + s[n], new_need))
            memory.add(str(needs))
        return minimal
