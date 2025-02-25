class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first_str=strs[0]
        last_str=strs[-1]
        min_len=min(len(first_str),len(last_str))
        i=0
        while i<min_len and first_str[i]==last_str[i]:
            i+=1
        return first_str[:i]
            
                    


