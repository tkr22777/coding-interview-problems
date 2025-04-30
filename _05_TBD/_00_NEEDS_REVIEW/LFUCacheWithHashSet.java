import java.util.*;

class LFUCacheWithHashSet {

    class LFUContainer {
        int key;
        int frequency;
        int value;
        int time;

        public LFUContainer(int key, int value, int frequency, int time) {
            this.key = key;
            this.value = value;
            this.frequency = frequency;
            this.time = time;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || getClass() != o.getClass()) return false;
            LFUContainer lfuCon = (LFUContainer) o;
            return Objects.equals(this.toString(), lfuCon.toString());
        }

        @Override
        public int hashCode() {
            return Objects.hash(this.key);
        }

        @Override
        public String toString() {
            return String.format("{Key:%s, Value:%s, Frequency:%s, Time:%s}", key, value, frequency, time);
        }
    }

    int capacity = 0;
    HashMap<Integer, LFUContainer> dataMap = new HashMap<Integer, LFUContainer>(); 

    public LFUCacheWithHashSet(int capacity) {
        this.capacity = capacity;
    }

    public int get(int key) {

        LFUContainer lfuCon = dataMap.get(key);
        if (lfuCon == null) {
            return -1;
        }

        updateInfo(lfuCon);
        return lfuCon.value;
    }

    public void put(int key, int value) {

        if (capacity == 0) {
            return;
        }

        if (dataMap.containsKey(key)) {
            LFUContainer lfuCon = dataMap.get(key);
            lfuCon.value = value; //updating the value
        } else {
            if (dataMap.size() == capacity) {
                //remove the least recently used
                LFUContainer toRemove = removeLeastRecentlyUsed();
                dataMap.remove(toRemove.key);
            }
            LFUContainer lfuCon =  new LFUContainer(key, value, 0, 0);
            dataMap.put(key, lfuCon);
        }

        updateInfo(lfuCon);
    }

    int logicalTime = 0;
    int leastFrequent = 1;
    HashMap<Integer, Set<LFUContainer>> freqToObjectMapping = new HashMap<Integer, HashSet<LFUContainer>>();

    private void updateInfo(LFUContainer lfuCon) {
        logicalTime++;
        lfuCon.time = logicalTime;
        Set<LFUContainer> values = freqToObjectMapping.get(lfuCon.frequency);
        values.remove(lfuCon);
        if (value.size() == 0) {
            freqToObjectMapping.remove(lfuCon.frequency);
            if (leastFrequent == lfuCon.frequency) {
                leastFrequent++;
            }
        }
        lfuCon.frequency++; 
        freqToObjectMapping.computeIfAbsent(lfuCon.frequency).add(lfuCon);
    }

    private LFUContainer removeLeastRecentlyUsed() {
        Set<LFUContainer> vals = freqToObjectMapping.get(leastFrequent);
        LFUContainer lfuContainer = vals.iterator().next();
        vals.remove(lfuContainer);

        if (vals.size() == 0) {
            freqToObjectMapping.remove(vals);
            for (int i = 1; i < leastFrequent; i++) {
                if (freqToObjectMapping.containsKey(i) {
                    leastFrequent = i;
                    break;
                }
            }
        }

        return lfuContainer;
    }
}

