class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        left=0
        chars=set()
        for right in range(len(s)):
            #print(chars)
            while s[right] in chars:
                chars.remove(s[left])
                left+=1
            chars.add(s[right])
            current_len=right-left+1
            max_len=max(max_len,current_len)
        return max_len
      

