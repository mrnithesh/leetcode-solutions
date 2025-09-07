class Solution {
    public int[] sumZero(int n) {
        int[] arr = new int[n];
        boolean isOdd =false;
        if (n%2!=0){
            isOdd= true;
            n--;
        }
        for (int i =0;i<n/2;i++){
            arr[i] = i+1;
            arr[n-i-1]= -(i+1);
        }
        if (isOdd){
            arr[n]=0;
        }
        return arr;
    }
}