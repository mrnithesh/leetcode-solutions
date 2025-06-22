class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res =[]
        substr = ""
        for i in range(len(s)):
            substr += s[i]
            print(substr)
            if len(substr) == k:
                res.append(substr)
                substr= ""
        if substr:
            substr += fill*(k-len(substr))
            res.append(substr)
        return res