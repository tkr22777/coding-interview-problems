/*
 * Given a list of co-ordinates, an integer k, where k <= N return the co-ordinate(s) whose distance
 * from the origin is kth among all possible distances.
 */
import java.util.*;

class KClosestPoints {
    public static void main(String[] args) {
        int[][] kthPoints;

        int[][] points01 = {{8,8}, {-5,5}, {5,4}, {-10,2}, {1,8}, {5,9}, {-2,-3}};
        print(points01);
        kthPoints = new KClosestPoints().kClosest(points01, 2);
        print(kthPoints);

        int[][] points02 = {{-2,-6}, {-7,-2}, {-9,6}, {10,3}, {-8,1}, {2,8}};
        print(points02);
        kthPoints = new KClosestPoints().kClosest(points02, 3);
        print(kthPoints);
    }

    public int[][] kClosest(int[][] points, int k) {
        int[] squaredDistances = new int[points.length];
        for (int i = 0; i < points.length; i++) {
            squaredDistances[i] = points[i][0] * points[i][0] + points[i][1] * points[i][1];
        }

        k--; //the user provided kth items, are the 0 .. (k-1)th items on the array
        int left = 0;
        int right = squaredDistances.length - 1;
        int pivot = -1;
        int kthSquaredDistance = -1;

        while (left < right) {
            pivot = QuickSort.partition(squaredDistances, left, right);
            if (pivot == k || right - left == 1) { //kth distance is now at kth position
                kthSquaredDistance = squaredDistances[k];
                break;
            }
            
            if (k < pivot) {  //pivot is on the right of K, set right to the pivot
                right = pivot;
            } else if (pivot < k) {  //pivot is on the left of K, set left to the pivot
                left = pivot;
            }
        }

        ArrayList<int[]> kthDistantPoints = new ArrayList<>();
        for (int i = 0; i < points.length ; i++) {
            if (kthSquaredDistance >= (points[i][0] * points[i][0] + points[i][1] * points[i][1])) {
                kthDistantPoints.add(new int[] {points[i][0], points[i][1]});
            }
        }

        int[][] kthDistantPointsArray = new int[kthDistantPoints.size()][2];
        for (int i = 0; i < kthDistantPoints.size(); i++) {
            kthDistantPointsArray[i] = kthDistantPoints.get(i);
        }
        return kthDistantPointsArray;
    }

    public static void print(int[][] points) {
        StringJoiner sj = new StringJoiner(", ", "Points: ", ".");
        Arrays.stream(points).forEach(point -> sj.add(Arrays.toString(point)));
        System.out.println(sj.toString());
    }
}
