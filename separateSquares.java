class Solution {
    public double separateSquares(int[][] squares) {
        double low=0.0, high=1e9;
        for(int i=0;i<100;i++){
            double mid=(low+high)/2.0;
            double below=0.0, above=0.0;
            for(int[] sq:squares){
                double y=sq[1];
                double l=sq[2];
                double bottom=y;
                double top=y+l;
                double area=l*l;

                if(mid<=bottom){
                    above+=area;
                }else if(mid>=top){
                    below+=area;
                }else{
                    below+=(mid-bottom)*l;
                    above+=(top-mid)*l;
                }
            }
            if(below<above){
                low=mid;
            }else{
                high=mid;
            }
        }
        return low;
    }
}
