import java.util.*;

class KeyFrequency {
    int key;
    int frequency;
    int value;
    int time;

    public KeyFrequency(int key, int value, int frequency, int time) {
        this.key = key;
        this.value = value;
        this.frequency = frequency;
        this.time = time;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        KeyFrequency kf = (KeyFrequency) o;
        return Objects.equals(this.key, kf.key);
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

class LFUCacheWithPQ {
    int capacity = 0, logicalTime = 0;
    HashMap<Integer, KeyFrequency> dataMap = new HashMap<Integer, KeyFrequency>(); 
    PriorityQueue<KeyFrequency> pq;

    public LFUCacheWithPQ(int capacity) {
        this.capacity = capacity;
        this.pq = new PriorityQueue<>(
                Comparator.comparingInt((KeyFrequency a) -> a.frequency) /* least frequent first */
                        .thenComparingInt(a -> a.time) /* least recent first */
        );
    }

    public int get(int key) {
        KeyFrequency kf = dataMap.get(key);
        if (kf == null) {
            return -1;
        }

        logicalTime++;
        pq.remove(kf);
        kf.frequency++;
        kf.time = logicalTime;
        pq.add(kf);
        return kf.value;
    }

    public void put(int key, int value) {
        if (capacity == 0) {
            return;
        }
        logicalTime++;
        if (dataMap.containsKey(key)) {
            KeyFrequency kf = dataMap.get(key);
            pq.remove(kf);
            kf.value = value;
            kf.frequency++;
            kf.time = logicalTime;
            pq.add(kf);
        } else {
            if (dataMap.size() == capacity) {
                dataMap.remove(pq.poll().key);
            }
            KeyFrequency kf =  new KeyFrequency(key, value, 1, logicalTime);
            dataMap.put(key, kf);
            pq.add(kf);
        }
    }
}

