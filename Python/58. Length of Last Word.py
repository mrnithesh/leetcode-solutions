class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp = s.strip().split()
        return len(temp[-1])
