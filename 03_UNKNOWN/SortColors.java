class Solution {
    
    //https://leetcode.com/problems/sort-colors/
    
    public void sortColors(int[] array) {
        int[] valFreq = new int[3];
        for (int val: array) {
            valFreq[val]++;
        }
        int start = 0;
        for (int i = 0; i < valFreq.length; i++) {
            for(int j = start; j < start + valFreq[i]; j++) {
                array[j] = i;
            }
            start += valFreq[i];
        }
    }
}

