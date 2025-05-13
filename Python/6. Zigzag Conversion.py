class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s

        res = [""] * numRows 
        currentRow = 0
        direction = 1
        for ch in s:
            res[currentRow] += ch
            if currentRow == numRows-1:
                direction = -1
            elif currentRow == 0:
                direction = 1
            currentRow += direction

        return "".join(res)