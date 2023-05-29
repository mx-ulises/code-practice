class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        A_set = [False] * len(A)
        B_set = [False] * len(A)
        C = []
        common = 0
        for i in range(len(A)):
            a = A[i] - 1
            b = B[i] - 1
            A_set[a] = True
            B_set[b] = True
            if B_set[a]:
                common += 1
            if A_set[b]:
                common += 1
            if a == b:
                common -= 1
            C.append(common)
        return C
