class Solution:
    def toLowerCase(self, s: str) -> str:
        s = list(s)
        for i,j in enumerate(s):
            if j.isupper():
                s[i] = j.lower()
        return ''.join(s)