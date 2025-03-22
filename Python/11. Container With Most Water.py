class Solution:
    def maxArea(self, height: List[int]) -> int:
        res=0
        l=0
        r=len(height)-1
        while l<r:
            #print(l,r)
            min_height=min(height[l],height[r])
            width=r-l
            curr_area=min_height*width
            res=max(res,curr_area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return res

            