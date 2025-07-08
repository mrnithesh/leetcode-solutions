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