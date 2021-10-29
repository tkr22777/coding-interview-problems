import java.util.*;

class PascalsTriangle {

    public static void main(String[] args) {
        for(int i = 0; i <= 5; i++) {
            System.out.println(new PascalsTriangle().getRow(i).toString());
        }
    }

    public List<Integer> getRow(int rowIndex) {

        int totalColumn = rowIndex + 1;
        int array[][] = new int[2][totalColumn];

        for (int row = 0; row < totalColumn; row++) {
            for (int col = 0; col < row + 1; col++) {
                if (row == 0 || row == 1 || col == 0 || col == row) {
                    array[row%2][col] = 1;
                } else {
                    array[row%2][col] = array[(row - 1)%2][col - 1] +  array[(row - 1)%2][col];
                }
            }
        }

        List<Integer> values = new ArrayList<>();
        for (int i = 0; i < array[rowIndex%2].length; i++) {
            values.add(i,array[rowIndex%2][i]);
        }

        return values;
    }
}

