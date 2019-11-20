import java.util.*;

class Flatten2DVector {

    int[][] v;
    int row = 0;
    int col = 0;
    
    public Flatten2DVector(int[][] v) {
        this.v = v;
    }
    
    public int next() {
        if (col >= v[row].length) {
            while(row < v.length) {
                row++;
                if (v[row].length > 0) {
                    col = 0;
                    return v[row][col++];
                }
            }
        }
        return v[row][col++];
    }
    
    public boolean hasNext() {
        if (row >= v.length) return false;
        if (col < v[row].length) return true;
        
        for(int tempRow = row + 1; tempRow < v.length; tempRow++) {
            if (v[tempRow].length > 0) {
                return true;
            }
        }
        return false;
    }
}

