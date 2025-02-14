import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.*;

class Line {
    boolean vertical = false;
    double x = 0;
    BigDecimal slope;
    float intercept;

    @Override
    public boolean equals(Object o) { return this.hashCode() == o.hashCode(); }

    @Override
    public int hashCode() { return Objects.hash(vertical, x, slope, intercept); }
}

class Point {
    int x;
    int y;
    int index;

    public Point(int x, int y, int index) {
        this.x = x;
        this.y = y;
        this.index = index;
    }

    @Override
    public boolean equals(Object o) { return this.hashCode() == o.hashCode(); }

    @Override
    public int hashCode() { return Objects.hash(x, y, index); }
}

public class MaxPointsOnALine {

    public static void main(String[] args) {
        int[][] array = { {1, 1}, {2, 2}, {3, 3} };
        int[][] array2 = { {1, 1}, {3, 2}, {5, 3}, {4, 1}, {2, 3}, {1, 4} };
        int[][] array3 = { {0, 0} };
        int[][] array4 = { {0, 0}, {94911151, 94911150}, {94911152, 94911151} };

        System.out.println(new MaxPointsOnALine().maxPoints(array));
        System.out.println(new MaxPointsOnALine().maxPoints(array2));
        System.out.println(new MaxPointsOnALine().maxPoints(array3));
        System.out.println(new MaxPointsOnALine().maxPoints(array4));
    }

    public int maxPoints(int[][] points) {
        if (points.length < 2) {
            return points.length;
        }

        Map<Line, HashSet<Point>> lineToPointsMap = new HashMap<>();

        for (int i = 0; i < points.length; i++) {
            for (int j = i + 1; j < points.length; j++) {
                Point p1 = new Point(points[i][0], points[i][1], i);
                Point p2 = new Point(points[j][0], points[j][1], j);

                Line line = new Line();
                if (p1.x == p2.x) { //vertical line
                    line.vertical = true;
                    line.x = p1.x;
                } else { //non-vertical lines
                    BigDecimal dividend = new BigDecimal(p2.y - p1.y);
                    BigDecimal divisor = new BigDecimal(p2.x - p1.x);
                    line.slope = dividend.divide(divisor, 64, RoundingMode.HALF_UP);
                    line.intercept = p2.y - line.slope.floatValue() * p2.x;
                }

                HashSet<Point> pointsSet = lineToPointsMap.computeIfAbsent(line, k -> new HashSet<>());
                pointsSet.add(p1);
                pointsSet.add(p2);
            }
        }

        int highest = 0;
        for (Map.Entry<Line,HashSet<Point>> entry : lineToPointsMap.entrySet()) {
            highest = Math.max(highest, entry.getValue().size());
        }
        return highest;
    }
}
