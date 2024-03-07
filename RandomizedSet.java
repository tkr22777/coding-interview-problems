import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class RandomizedSet {

    Map<Integer, Integer> valueToIndex;
    ArrayList<Integer> valueList;

    public RandomizedSet() {
        valueToIndex = new HashMap<>();
        valueList = new ArrayList<>();
    }

    public boolean insert(int val) {
        if (!valueToIndex.containsKey(val)) {
            int valIndex = valueList.size();
            valueToIndex.put(val, valIndex);
            valueList.add(val);
            return true;
        } else {
            return false;
        }
    }

    public boolean remove(int val) {
        if (valueToIndex.containsKey(val)) {
            int valIndex = valueToIndex.get(val);
            valueToIndex.remove(val);

            int lastElemIndex = valueList.size() - 1;
            if (valIndex != lastElemIndex) {
                int lastElem = valueList.get(lastElemIndex);
                valueToIndex.put(lastElem, valIndex);
                valueList.set(valIndex, lastElem);
            }

            valueList.remove(lastElemIndex);
            return true;
        } else {
            return false;
        }
    }
}
