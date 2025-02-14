import java.io.*;
import java.util.*;
import java.util.stream.*;

class Solution {

  public static void main(String[] args) {
    int[][] matrix = {{1, 2, 3, 4, 11},
                      {4, 5, 6, 3, 1},
                      {4, 8, 6, 2, 8},
                      {4, 5, 6, 3, 1},
                      {7, 8, 9, 2, 5}};

    Arrays.stream(matrix).forEach( v -> {
      System.out.println(Arrays.toString(v));
    });

    new Solution().rotate(matrix);

    System.out.println("After rotation:");

    Arrays.stream(matrix).forEach( v -> {
      System.out.println(Arrays.toString(v));
    });
  }

  public void rotate(int[][] matrix) {
    //top to bottom rows reverse
    for (int i = 0; i < matrix.length / 2; ++i) {
      int[] a = matrix[i];
      matrix[i] = matrix[matrix.length - i - 1];
      matrix[matrix.length - i - 1] = a;
    }

    //swap symmetry diagonally
    for (int i = 0; i < matrix.length - 1; ++i) {
      for (int j = i + 1; j < matrix[i].length; ++j) {
        int a = matrix[i][j];
        matrix[i][j] = matrix[j][i];
        matrix[j][i] = a;
      }
    }
  }
}

