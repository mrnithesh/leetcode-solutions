# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        curr= head
        while curr:
            arr.append(curr.val)
            curr=curr.next
        l = 0
        r = len(arr)-1
        while (l<r):
            if (arr[l]!=arr[r]):
                return False
            l+=1
            r-=1
        return True 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #two pointer - fast and slow
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #fast will be at end, slow will be at middle

        #reverse 2dn half
        prev = None
        while slow:
            temp = slow.next
            slow.next=prev
            prev= slow
            slow = temp

        #check for palindrom
        l,r = head,prev

        while r:
            if (l.val != r.val):
                return False
            l = l.next
            r = r.next
        return True