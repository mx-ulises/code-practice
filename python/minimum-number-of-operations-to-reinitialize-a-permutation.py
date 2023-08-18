class Solution:
    def update_operation(i: int, perm: List[int]) -> int:
        if i & 1 == 0:
            j = i // 2
        else:
            n = len(perm)
            j = (n // 2) + ((i - 1) // 2)
        return perm[j]

    def reinitializePermutation_full_array(self, n: int) -> int:
        perm = list(range(n))
        reinitialized = False
        operation_count = 0
        print([(i, perm[i]) for i in range(len(perm))])
        while reinitialized != True:
            operation_count += 1
            reinitialized = True
            new_perm = []
            for i in range(len(perm)):
                new_value = Solution.update_operation(i, perm)
                new_perm.append(new_value)
                if new_value != i:
                    reinitialized = False
            perm = new_perm
            print([(i, perm[i]) for i in range(len(perm))])
        return operation_count

    def reinitializePermutation(self, n: int) -> int:
        position = 1
        for operation_count in range(1, n + 1):
            if position % 2 == 0:
                position = position // 2
            else:
                position = (n // 2) + (position - 1) // 2
            if position == 1:
                return operation_count
        return 0
