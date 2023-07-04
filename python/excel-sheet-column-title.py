class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title_array = []
        while 0 < columnNumber:
            c_int = columnNumber % 26 - 1
            if c_int == -1:
                c_int = 25
            c = chr(c_int + ord("A"))
            title_array.append(c)
            if c_int == 25:
                columnNumber -= 1
            columnNumber //= 26
        title_array.reverse()
        return "".join(title_array)
