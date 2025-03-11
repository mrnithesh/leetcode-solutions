class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        result=0
        count=defaultdict(int)
        left=0
        for right in range(len(s)):
            count[s[right]]+=1

            while len(count)==3:
                result+= (len(s)-right)
                count[s[left]]-=1
                if count[s[left]]==0:
                    count.pop(s[left])
                left+=1
        return result
