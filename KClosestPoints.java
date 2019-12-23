import java.util.*;

/* Given a list of co-ordinates, an integer k, where k <= N return the co-ordinate(s) whose distance
 * from the origin is kth among all possible distances.
 */

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

        int[] squaredDists = new int[points.length];

        for (int i = 0; i < points.length; i++) {
            squaredDists[i] = points[i][0] * points[i][0] + points[i][1] * points[i][1];
        }

        k--; //kth item for the user is the (k-1)th distance item on the distance array
        int left = 0;
        int right = squaredDists.length - 1;
        int pivot = -1;
        int kthSquaredDists = -1;

        while (left < right) {

            pivot = QuickSort.partition(squaredDists, left, right);
            if (pivot == k || right - left == 1) { //kth distance is now at kth position
                kthSquaredDists = squaredDists[k];
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
            if (kthSquaredDists >= (points[i][0] * points[i][0] + points[i][1] * points[i][1])) {
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
