import java.util.*;

class KClosestPoints {

    public static void main(String[] args) {
        int[][] kthPoints;

        int[][] points01 = { {8,8}, {-5,5}, {5,4}, {-10,2}, {1,8}, {5,9}, {-2,-3} };
        print(points01);
        kthPoints = new KClosestPoints().kClosest(points01, 2);
        print(kthPoints);

        int[][] points02 = { {-2,-6}, {-7,-2}, {-9,6}, {10,3}, {-8,1}, {2,8} };
        print(points02);
        kthPoints = new KClosestPoints().kClosest(points02, 3);
        print(kthPoints);
    }

    public int[][] kClosest(int[][] points, int k) {

        int[] squaredDistances = new int[points.length];

        for(int i = 0; i < points.length; i++) {
            squaredDistances[i] = points[i][0] * points[i][0] + points[i][1] * points[i][1];
        }

        k--;
        int left = 0;
        int right = squaredDistances.length - 1;
        int pivot = -1;
        int ktSquaredDistance = -1;

        while (left < right) {

            pivot = QuickSort.partition(squaredDistances, left, right);

            if (pivot == k || right - left == 1) { // kth element is already sorted at this point
                ktSquaredDistance = squaredDistances[k];
                break;
            }

            if (pivot > k && pivot - 1 != k) { //we do not want the right to be k
                right = pivot - 1;
            } else if (pivot < k - 1) { //we do not want the left to be k
                left = pivot + 1;
            }
        }

        ArrayList<int[]> kthDistantPoints = new ArrayList<>();
        for(int i = 0; i < points.length ; i++) {
            if (ktSquaredDistance >= (points[i][0] * points[i][0] + points[i][1] * points[i][1]) ) {
                int[] aPoint = new int[2];
                aPoint[0] = points[i][0];
                aPoint[1] = points[i][1];
                kthDistantPoints.add(aPoint);
            }
        }

        int[][] kthDistantPointsArray = new int[kthDistantPoints.size()][2];
        for(int i = 0; i < kthDistantPoints.size(); i++) {
            kthDistantPointsArray[i] = kthDistantPoints.get(i);
        }

        return kthDistantPointsArray;
    }

    public static void print(int[][] points) {
        StringBuilder sb = new StringBuilder();
        for(int[] point: points) {
            sb.append(" " +  Arrays.toString(point));
        }
        System.out.println(sb.toString());
    }
}
