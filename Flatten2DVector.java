/*
    https://leetcode.com/problems/flatten-2d-vector/
 */

class Flatten2DVector {
    int[][] v;
    int row = 0;
    int col = 0;
    
    public Flatten2DVector(int[][] v) {
        this.v = v;
    }

    // next will only be called if hasNext returns true
    public int next() {
        if (col >= v[row].length) { //col at the end of current row
            while(row < v.length) {
                row++; //new row
                if (v[row].length > 0) { //this row has some value
                    col = 0;
                    return v[row][col++];
                }
            }
        }
        return v[row][col++];
    }
    
    public boolean hasNext() {
        //first check if we are in row's bound before able to check col in the current row
        if (row >= v.length) return false;

        // since we are in row's bound check if there is a value for col
        if (col < v[row].length) return true;

        //current row and col have exhausted, checking if there's any future row with values
        for (int tempRow = row + 1; tempRow < v.length; tempRow++) {
            if (v[tempRow].length > 0) {
                return true;
            }
        }
        return false;
    }
}
