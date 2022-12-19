class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        content_children = 0
        g.sort()
        s.sort()
        for cookie in s:
            if content_children < len(g) and g[content_children] <= cookie:
                content_children += 1
        return content_children
