class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        while columnNumber > 0:
            temp = (columnNumber-1) % 26
            res.insert(0,chr(temp+65))
            columnNumber = (columnNumber -1) // 26
        return "".join(res)