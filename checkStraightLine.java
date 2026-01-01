class Solution {
    public boolean checkStraightLine(int[][] coordinates) {
        int x0=coordinates[0][0], y0=coordinates[0][1];
        int x1=coordinates[1][0], y1=coordinates[1][1];
        for(int i=2;i<coordinates.length;i++){
            int xi=coordinates[i][0],yi=coordinates[i][1];
            if((yi-y0)*(x1-x0)!=(y1-y0)*(xi-x0))
                return false;
        }
        return true;
    }
}
