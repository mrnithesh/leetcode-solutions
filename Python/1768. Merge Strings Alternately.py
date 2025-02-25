class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=""
        max_len=max(len(word1),len(word2))
        for i in range (max_len):
            if i<len(word1):
                result+=word1[i]
            if i<len(word2):
                result+=word2[i]
        return result