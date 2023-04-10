/*
    https://leetcode.com/problems/flatten-2d-vector/
 */

class Flatten2DVector {
    int[][] v;
    int row = 0;
    int column = 0;

    public static void main(String[] args) {
        System.out.println("Compiling");
    }

    public Flatten2DVector(int[][] v) {
        this.v = v;
    }

    // next will only be called if hasNext returns true
    public int next() {
        if (column >= v[row].length) { // column is at the end of current row
            // find the next row with some values
            while (row < v.length && v[row].length == 0) {
                row++;
            }
            column = 0;
        }
        return v[row][column++];
    }
    
    public boolean hasNext() {
        //first check if we are in row's bound before able to check col in the current row
        if (row >= v.length) {
            return false;
        }

        // since we are within row's bound, check if there is a value for col
        if (column < v[row].length) {
            return true;
        }

        //current row and col have exhausted, checking if there's any future row with values
        for (int tempRow = row + 1; tempRow < v.length; tempRow++) {
            if (v[tempRow].length > 0) {
                return true;
            }
        }
        return false;
    }
}
