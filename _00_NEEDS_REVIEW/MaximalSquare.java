package com.company;

import java.util.HashMap;
import java.util.Objects;

class Solution {

    class Triplet {
        int x, y, size;

        public Triplet(int x, int y, int size) {
            this.x = x;
            this.y = y;
            this.size = size;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            Triplet triplet = (Triplet) o;
            return x == triplet.x &&
                    y == triplet.y &&
                    size == triplet.size;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y, size);
        }
    }


    public int maximalSquare(char[][] matrix) {
        int largestSquareWidth = 0;
        for ( int i = 0 ; i < matrix.length; i++) {
            for ( int j = 0; j < matrix[i].length ; j++) {

                int maxPossibleWidth = Math.min(matrix.length - i, matrix[i].length - j);
                if ( largestSquareWidth >= maxPossibleWidth ) {
                    continue;
                }
                largestSquareWidth = Math.max(bfsMaxSquareWidthHunter(matrix, i, j), largestSquareWidth);
            }
        }

        return largestSquareWidth * largestSquareWidth;
    }

    private int bfsMaxSquareWidthHunter(char[][] matrix, int x, int y) { //

        int maxPossibleWidth = Math.min(matrix.length - x , matrix[x].length - y);

        for (int size = 1; size <= maxPossibleWidth; size++) {

            for( int i = x ;  i < x + size ; i++) { //column calculation
                if ( matrix[i][ y + size - 1] == '0' ) {
                    return size - 1; //returning the previous size that worked
                }
            }

            for( int j = y; j < y + size ; j++) { //row calculation
                if (matrix[x + size -1][j] == '0') {
                    return size - 1;
                }
            }
        }

        return maxPossibleWidth;
    }

    private boolean containsSquare(char[][] matrix, int x, int y, int width) {
        for (int i = x; i < x + width ; i++) {
            for (int j = y; j < y + width ; j++) {
                if (matrix[i][j] == '0') {
                    return false;
                }
            }
        }
        return true;
    }

    HashMap<Triplet, Boolean> tripletBooleanHashMap = new HashMap<>();

    private boolean containsSquareOptimized(char[][] matrix, int x, int y, int width) {

        //System.out.println("x:" + x + " y:" + y + " width:" + width);

        if (width == 1) {
            return matrix[x][y] == '1' ? true : false;
        }

        Triplet triplet = new Triplet(x, y, width);
        if (tripletBooleanHashMap.containsKey(triplet)) {
            return tripletBooleanHashMap.get(triplet).booleanValue();
        }

        //Compute the width column
        for (int i = x; i < x + width; i++) {
            //System.out.println("Comparing column [" + i + "][" + ( y + width -1 ) + "]" + matrix[i][y + width - 1]);
            if (matrix[i][y + width - 1]  == '0') {
                tripletBooleanHashMap.put(triplet, false);
                return false;
            }
        }

        //Compute the width row
        for (int j = y ; j < y + width; j++) {
            //System.out.println("Comparing row [" + ( x + width - 1 ) + "][" + j + "]" + matrix[x + width - 1][j]);
            if (matrix[x + width - 1][j]  == '0') {
                tripletBooleanHashMap.put(triplet, false);
                return false;
            }
        }

        boolean subProblemResult = containsSquareOptimized(matrix, x, y, width - 1);
        tripletBooleanHashMap.put(triplet, subProblemResult);
        return subProblemResult;
    }

    public static void main(String[] args) {
        char[][] matrix1 = {
            {'0' , '1'},
            {'1' , '0'}
        };

        char[][] matrix2 = {
                {'1' , '1'},
                {'1' , '1'}
        };

        char[][] matrix3 = {
                {'0' , '0'},
                {'0' , '0'}
        };

        char[][] matrix4 = {
                {'1' , '0'},
                {'0' , '0'}
        };

        char[][] matrix5 = {
                {'0' , '0', '0'},
                {'0' , '0', '0'},
                {'0' , '0', '0'},
                {'0' , '0', '1'}
        };

        char[][] matrix6 = {
                {'1','1','1','1','1','1'},
                {'1','1','1','1','1','1'},
                {'1','1','1','1','1','1'},
                {'1','1','1','1','1','0'},
                {'0','1','1','1','1','1'}
        };

        char[][] matrix7 = {
                {'0','0','0','0','0'},
                {'1','0','0','0','0'},
                {'0','0','0','0','0'},
                {'0','0','0','0','0'}
        };

        System.out.println("Max Square " + new Solution().maximalSquare(matrix7));
    }
}
