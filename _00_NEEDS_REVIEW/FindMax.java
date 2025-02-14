package TOClean;

/*
A sequence of integers that is initially increasing until a certain index
then decreasing thereafter. You may assume no number in the sequence is repeated.
Write a function that accepts an increasing-decreasing sequence,
and returns the index where its maximum value is located.

Case 1:
      *
    *

  *
          *
             *

Case 2:

      *
        *
          *
            *
              *

    *

  *
*/

class Main {
    public static void main(String[] args) {
        System.out.println("Hello world!");
        int[] input = { 1, 3, 5, 4, 2};
        int index =  maxIndex(input);
        System.out.println("Index:" + index);

        int[] input2 = { 1, 3, 5, 6, 7};
        index =  maxIndex(input2);
        System.out.println("Index:" + index);

        int[] input3 = { 7, 6, 4, 2, 1};
        index =  maxIndex(input3);
        System.out.println("Index:" + index);

        int[] input4 = {};
        index =  maxIndex(input4);
        System.out.println("Index:" + index);
    }

    public static int maxIndex(int[] input) {
        int i = 0;
        int j = input.length - 1;

        while (i <= j) {
//      System.out.println("i:" + i + " val" + input[i] + " j:" + j + " val" + input[j]);

            if (j - i == 1) {
                if (input[i] > input[j]) {
                    return i;
                } else {
                    return j;
                }
            }

            int mid = (i + j) / 2;
//     System.out.println("mid " + mid + " val" + input[mid]);

            if (i == j) {
                return mid;
            }

            if (input[mid] > input[mid + 1]) {
                j = mid;
            } else {
                i = mid;
            }
        }

        return -1;
    }
}