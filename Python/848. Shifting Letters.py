class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        res = ''
        shift = 0
        for i in range(len(shifts)-1,-1,-1):
            res += chr((ord(s[i])- ord('a') + shift+ shifts[i]) %26 + ord('a'))
            shift +=shifts[i]
        return res[::-1]
