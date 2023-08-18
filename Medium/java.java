class Solution {
    public int minDominoRotation(int[] A, int[] B){
        int minSwaps = Math.min(
            numSwaps(A[0], A, B),
            numSwaps(B[0], A, B)
        );
        minSwaps = Math.min(minSwaps, numSwaps(A[0], B, A));
        minSwaps = Math.min(minSwaps, numSwaps(B[0], B, A));

        return minSwaps == Integer.MAX_VALUE ? -1 : minSwaps;
    }

    public int numSwaps(int target, int[] A, int[] B){
        int numSwaps = 0;
        for(int i = 0; i < A.length; i++){
            if(A[i] != target && B[i] != target){
                return Integer.MAX_VALUE;
            } else if(A[i] != target){
                numSwaps++;
            }
        }
        return numSwaps;
    }
}