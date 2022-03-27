BILL_TYPES = [20, 10, 5]
COST = 5

def update_bills(bill, bill_count):
    change = bill - COST
    bill_count[bill] += 1
    for bill in BILL_TYPES:
        need = change // bill
        remove = min(need, bill_count[bill])
        bill_count[bill] -= remove
        change -= remove *bill
    return change == 0


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_count = defaultdict(lambda: 0)
        for bill in bills:
            if not update_bills(bill, bill_count):
                return False
        return True
