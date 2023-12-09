class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        rectangle_count = 0
        max_rectangle_size = 0
        while rectangles:
            rectangle_size = min(rectangles.pop())
            if max_rectangle_size < rectangle_size:
                max_rectangle_size = rectangle_size
                rectangle_count = 0
            if max_rectangle_size == rectangle_size:
                rectangle_count += 1
        return rectangle_count
