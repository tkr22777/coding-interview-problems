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
        //at the "very" beginning col starts with 0
        if (col >= v[row].length) { //col at the end of current row
            while (row < v.length) {
                row++; //new row
                if (v[row].length > 0) { //this row has some value, reset col
                    col = 0;
                    break;
                }
            }
        }
        return v[row][col++];
    }
    
    public boolean hasNext() {
        // first check if we are in row's bound before able to check col in the current row
        if (row >= v.length) return false;

        // since we are in row's bound check if there is a value for col
        if (col < v[row].length) return true;

        // iterating up to row with values
        for (row = row + 1; row < v.length; row++) {
            if (v[row].length > 0) {
                return true;
            }
        }
        return false;
    }
}
