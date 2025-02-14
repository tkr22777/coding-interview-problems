import java.util.*;

public class FindingUsersActiveMinutes {
    public static void main(String[] args) {

        int[][] logs = {{0,5},{1,2},{0,2},{0,5},{1,3}};
        int[] result = new FindingUsersActiveMinutes().findingUsersActiveMinutes(logs, 5);
        System.out.println(Arrays.toString(result));

        int[][] logs_2 = {{1,1},{2,2},{2,3}};
        result = new FindingUsersActiveMinutes().findingUsersActiveMinutes(logs_2, 4);
        System.out.println(Arrays.toString(result));
    }
    public int[] findingUsersActiveMinutes(int[][] logs, int k) {

        Map<Integer, Set<Integer>> uid_mins = new HashMap<>();
        for (int[] user: logs) {
            int uid = user[0];
            int min = user[1];
            // System.out.println("UserID: " + uid);
            // System.out.println("Min: " + min);
            uid_mins.computeIfAbsent(uid, v -> new HashSet<Integer>())
                    .add(min);
        }

        Map<Integer, Integer> uam_to_users = new HashMap<>();
        for (int uid: uid_mins.keySet()) {
            int uam = uid_mins.get(uid).size();
            uam_to_users.put(uam, uam_to_users.getOrDefault(uam, 0) + 1);
        }

        int[] out = new int[k];
        for (int uam: uam_to_users.keySet()) {
            // System.out.println("Size: " + uam + " Users: " + uam_to_users.get(uam));
            out[uam - 1] = uam_to_users.get(uam);
        }

        return out;
    }
}
