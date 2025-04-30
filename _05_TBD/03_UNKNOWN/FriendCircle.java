import java.util.*;

class FriendCircle {

    public static void main(String[] args) {
        System.out.println("code compiled and ran successfully.");
    }

    public int findCircleNum(int[][] M) {

        Map<Integer, Set<Integer>> friendToCirleMap = new HashMap<>();

        for (int friend = 0; friend < M.length; friend++) {
            Set<Integer> friendsSet = friendToCirleMap.getOrDefault(friend, new HashSet<>());
            friendToCirleMap.put(friend, friendsSet);
            friendsSet.add(friend);

            for (int otherFriend = friend + 1; otherFriend < M[friend].length; otherFriend++) {

                if (M[friend][otherFriend] == 1) {
                    Set<Integer> otherFriendSet = friendToCirleMap.getOrDefault(otherFriend, new HashSet<>());
                    friendToCirleMap.put(otherFriend, otherFriendSet);
                    otherFriendSet.add(otherFriend);
                    
                    // they have been merged in the same circle before
                    if (friendsSet != otherFriendSet) {
                        otherFriendSet.removeAll(friendsSet);
                        friendsSet.addAll(otherFriendSet);
                        for (Integer moreFriend: otherFriendSet) {
                            friendToCirleMap.put(moreFriend, friendsSet);
                        }
                    }
                }
            }
        }

        return new HashSet(friendToCirleMap.values()).size();
    }
}

