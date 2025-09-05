/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    List<Integer> arr= new ArrayList<>();
    public List<Integer> inorderTraversal(TreeNode root) {
        if (root==null) return arr;
        traverse(root);
        return arr;
    }
    public void traverse(TreeNode node){
        if (node ==null) return;
        traverse(node.left);
        arr.add(node.val);
        traverse(node.right);
    }
}