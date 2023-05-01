DIVISORS = [3, 5, 7]

class Solution:
    def is_excluded(x: int, divisors: List[int], divisor_i: int) -> bool:
        for i in range(divisor_i):
            if x % divisors[i] == 0:
                return True
        return False

    def add_integers(n: int, divisors: List[int], divisor_i: int) -> int:
        sum_of_multiples = 0
        current = 0
        divisor = divisors[divisor_i]
        while current <= n:
            if Solution.is_excluded(current, divisors, divisor_i) == False:
                sum_of_multiples += current
            current += divisor
        return sum_of_multiples

    def sumOfMultiples(self, n: int) -> int:
        sum_of_multiples = 0
        for divisor_i in range(len(DIVISORS)):
            sum_of_multiples += Solution.add_integers(n, DIVISORS, divisor_i)
        return sum_of_multiples
