class Solution {

    public int[] pourWater(int[] heights, int V, int K) {

        for(int i = 0; i < V; i++) { //drops of water

            if (this.fillLeft(heights, K)) continue;
            if (this.fillRight(heights, K)) continue;
            heights[K]++;
        }
        return heights;
    }

    public boolean fillLeft(int[] heights, int K) {

        int lowest = -1;
        for (int left = K - 1; left >= 0; left--) {
            if (heights[left] > heights[K]) break;

            if (lowest >= 0) {
                if (heights[left] > heights[lowest]) {
                    break;
                } else if(heights[left] == heights[lowest]) {
                    continue;
                }
            }

            if (heights[left] < heights[K]) {
                lowest = left;
            }
        }

        if (lowest >= 0) {
            heights[lowest]++;
            return true;
        }

        return false;
    }

    public boolean fillRight(int[] heights, int K) {

        int highest = heights.length;

        for(int right = K + 1; right < heights.length; right++) {

            if (heights[right] > heights[K]) break;

            if (highest < heights.length) {
                if (heights[right] > heights[highest]) {
                    break;
                } else if (heights[right] == heights[highest]) {
                    continue;
                }
            }

            if (heights[right] < heights[K]) {
                highest = right;
            }
        }

        if (highest < heights.length) {
            heights[highest]++;
            return true;
        }

        return false;
    }
}

