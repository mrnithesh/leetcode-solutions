class Solution:
    def maxDistinct(self, s: str) -> int:
        seen = set(s)
        return len(seen)