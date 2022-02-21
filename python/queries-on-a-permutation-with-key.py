class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        P = [i+1 for i in range(m)]
        output = []
        for x in queries:
            i = P.index(x)
            output.append(i)
            P.insert(0, P.pop(i))
        return output
