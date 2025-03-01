class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        length=len(nums1)
        median=0.0
        if length % 2 ==0:
            x=nums1[(length//2)-1]
            y=nums1[(length//2)]
            median = (x+y)/2
            return median
        else:
            x= nums1[(length//2)]
            median=float(x)
            return median