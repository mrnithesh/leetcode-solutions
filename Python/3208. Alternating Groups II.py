class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        colors.extend(colors[:k-1])
        n=len(colors)
        result=0
        l=0
        for r in range(1,n):
            #print(colors[l:r+1])
            if colors[r]==colors[r-1]:
                l=r
            if r-l+1>=k:
                result+=1
        return result
            