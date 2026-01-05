class Solution {
    public long maxMatrixSum(int[][] matrix) {
        int n = matrix.length;
        int leastElement=100001;
        long sum=0L;
        int negativeCount=0;

        for(int[] rows:matrix){
            for(int value:rows){
                if(value<0){
                    negativeCount++;
                    value=-value;
                }
                sum+=value;
                if(value<leastElement){
                    leastElement=value;
                }
            }
        }
        return (negativeCount%2==0)? sum:(sum-2*leastElement); //only when odd number of negatives are there- there will always be a negative number- so its better to leave out the number with the least value from the sum
    }
}
