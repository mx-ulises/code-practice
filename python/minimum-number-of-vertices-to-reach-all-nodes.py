class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        visited = {edge[1] for edge in edges}
        smallest_set_of_vertices = [i for i in range(n) if i not in visited]
        return smallest_set_of_vertices
