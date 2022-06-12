class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        if (n * m) != (r * c):
            return mat
        new_mat = []
        #print("n: {}, m: {}".format(n, m))
        for i in range(n * m):
            x, y = i // m, i % m
            #print("{}, {}, {}".format(i, x, y))
            if len(new_mat) == i // c:
                new_mat.append([])
            new_mat[-1].append(mat[x][y])
        return new_mat
