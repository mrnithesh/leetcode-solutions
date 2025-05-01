class Solution(object):
    def titleToNumber(self, columnTitle):
        ans = 0
        for char in columnTitle:
            ans = ans * 26 + (ord(char) - 64)
        return ans