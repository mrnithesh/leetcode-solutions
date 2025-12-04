class Solution:
    def countCollisions(self, directions: str) -> int:
        n = len(directions)
        l = 0
        r = n-1
        while (l<n and directions[l]=="L"):
            l+=1
        while (r>=0 and directions[r]=="R"):
            r-=1
        count =0
        while (l<=r):
            if directions[l]!="S":
                count+=1
            l+=1
        return count
            