class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        A_set = set()
        B_set = set()
        C = []
        common = 0
        for i in range(len(A)):
            A_set.add(A[i])
            B_set.add(B[i])
            if A[i] in B_set:
                common += 1
            if B[i] in A_set:
                common += 1
            if A[i] == B[i]:
                common -= 1
            C.append(common)
        return C
