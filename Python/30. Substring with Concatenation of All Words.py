class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words[0])
        total_len = word_len * len(words)
        word_counter = Counter(words)
        l = 0
        r = total_len
        res = []

        while r <= len(s):
            window = s[l:r]
            #print(window)
            windowWords = [window[i:i + word_len] for i in range(0, total_len, word_len)]
            windowCounter = Counter(windowWords)
            if windowCounter == word_counter:
                res.append(l)
            l += 1
            r += 1

        return res
