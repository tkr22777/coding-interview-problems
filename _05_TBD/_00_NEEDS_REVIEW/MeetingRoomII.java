package TOClean;

// https://leetcode.com/problems/meeting-rooms-ii/submissions/

import java.util.*;

public class MeetingRoomII {

    public int minMeetingRooms(int[][] intervals) {
        Comparator comp = new Comparator<int[]>()  {
            @Override
            public int compare(int[] o1, int[] o2) {
                int comp = Integer.compare(o1[0], o2[0]);
                return comp != 0 ? comp : Integer.compare(o1[1], o2[1]);
            }
        };
        Arrays.sort(intervals, comp);

        //Arrays.stream(intervals).forEach(v -> System.out.println(Arrays.toString(v)));
        Comparator comp2 = new Comparator<List<Integer>>()  {
            @Override
            public int compare(List<Integer> o1, List<Integer> o2) {
                int comp = Integer.compare(o1.get(0), o2.get(0));
                return comp != 0 ? comp : Integer.compare(o1.get(1), o2.get(1));
            }
        };
        TreeSet<List<Integer>> endTimes = new TreeSet<List<Integer>>(comp2);

        int minRoom = 0;
        for (int i = 0; i < intervals.length; i++) {
            int start = intervals[i][0];
            int end = intervals[i][1];
            Set<List<Integer>> meetingRemaining = endTimes.tailSet(Arrays.asList(start, i), false);
            minRoom = Math.max(minRoom, meetingRemaining.size() + 1);
            //System.out.println("i:" + i + " start:" + start + " end:" + end);
            //System.out.println("i:" + i + " endTime:" + endTimes.toString() + " minRoom:" + minRoom);
            //System.out.println("i:" + i + " meetingRemailing: " + meetingRemaining.toString());
            endTimes.add(Arrays.asList(end, i));
        }
        return minRoom;
    }
}