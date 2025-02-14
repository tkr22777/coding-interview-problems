import java.io.*;
import java.util.*;

/*
 * To execute Java, please define "static void main" on a class
 * named Solution.
 *
 * If you need more classes, simply define them inline.
 */

class CampusBikes {

  public static void main(String[] args) {

    int[][] workers = {{0,0},{2,1}};
    int[][] bikes = {{1,2},{3,3}};
    System.out.println(Arrays.toString(new CampusBikes().assignBikes(workers, bikes)));
  }

  class WBDistance {
    int dist;
    int bike;
    int worker;
    public WBDistance(int[][] workers, int[][] bikes, int worker, int bike) {
      this.worker = worker;
      this.bike = bike;
      int mDistance = Math.abs(workers[worker][0] - bikes[bike][0]);
      mDistance += Math.abs(workers[worker][1] - bikes[bike][1]);
      this.dist = mDistance;
    }

    public String toString() {
      return String.format("Worker:%d Bike:%d Distance:%d", this.worker, this.bike, this.dist);
    }
  }

  private PriorityQueue<WBDistance> populatePQ(int[][] workers, int[][] bikes) {

    PriorityQueue<WBDistance>pq = new PriorityQueue<WBDistance>((a,b) -> {
      if (a.dist != b.dist) {
        return a.dist - b.dist;
      } else if (a.worker != b.worker) {
        return a.worker - b.worker;
      } else {
        return a.bike - b.bike;
      }
    });

    for (int i = 0; i < workers.length; i++) {
      for (int j = 0; j < bikes.length; j++) {
        WBDistance wb = new WBDistance(workers, bikes, i, j);
        pq.offer(wb);
      }
    }
    return pq;
  }

  public int[] assignBikes(int[][] workers, int[][] bikes) {

    int totalWorkers = workers.length;
    int totalBikes = bikes.length;

    PriorityQueue<WBDistance> pq = populatePQ(workers, bikes);

    int[] toReturn = new int[workers.length];
    Arrays.fill(toReturn, -1);
    boolean[] bikeUsed = new boolean[bikes.length] ;

    int completed = 0;
    while(completed < workers.length) {
      WBDistance wbd = pq.poll();
      if (toReturn[wbd.worker] == -1 && !bikeUsed[wbd.bike]) {
        toReturn[wbd.worker] = wbd.bike;
        bikeUsed[wbd.bike] = true;
        completed++;
      }
    }

    return toReturn;
  }
}

