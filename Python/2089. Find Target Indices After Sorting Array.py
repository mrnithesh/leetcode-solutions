class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        return res
    
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        def quickSort(arr): #own sorting implementtation- quicksort
            if len(arr)<=1:
                return arr
            pivot = arr[len(arr)//2]

            left = [x for x in arr if x<pivot]
            middle =[x for x in arr if x==pivot]
            right =[x for x in arr if x>pivot]

            return quickSort(left)+middle+quickSort(right)
        nums=quickSort(nums)
        res = []
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)
        return res