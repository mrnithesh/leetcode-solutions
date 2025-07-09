/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        ArrayList<Integer> arr = new ArrayList<>();

        ListNode cur = head;
        while (cur != null){
            arr.add(cur.val);
            cur = cur.next;
        }
        int l = 0;
        int r = arr.size()-1;
        while (l<r){
            if (arr.get(l) != arr.get(r)){
                return false;
            }
            else{
                l++;
                r--;
            }
        }
        return true;
    }
}

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        //two pointers - fast and slow
        ListNode slow = head, fast = head;

        while (fast != null && fast.next!=null){
            fast = fast.next.next;
            slow = slow.next;
        } // slow will poiint the midddle and fast will point the end

        //now reverse the 2nd half
        ListNode prev = null;
        while (slow!=null){
            ListNode temp = slow.next;
            slow.next = prev;
            prev = slow;
            slow = temp;
        }
        // check for palindrome

        ListNode left = head, right = prev;
        while(right != null){
            if (left.val != right.val){
                return false;
            }
            left = left.next;
            right = right.next;
        }
        return true;
    }
}