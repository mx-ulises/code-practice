class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        h = []
        while names:
            heappush(h, (-heights.pop(), names.pop()))
        output = []
        while h:
            output.append(heappop(h)[1])
        return output
