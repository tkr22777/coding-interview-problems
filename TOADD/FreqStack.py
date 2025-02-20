from collections import defaultdict
from sortedcontainers import SortedDict, SortedSet

# https://leetcode.com/problems/maximum-frequency-stack/

class Val:
    def __init__(self, val: int, freq: int) -> None:
        self.val = val
        self.freq = freq
        self.counters = []
    
    def __lt__(self, other):
        return self.counters[-1] > other.counters[-1]
    
    def __repr__(self):
        return f"<val: {self.val}, freq: {self.freq}, counter: {self.counters}>"

class FreqStack:
    def __init__(self):
        self.counter = 0
        self.freq_to_vals_heap = SortedDict()
        self.vals_map = defaultdict(lambda: Val)
        
    def push(self, val: int) -> None:
        self.counter += 1
        if val not in self.vals_map:
            self.vals_map[val] = Val(val, 0)

        v = self.vals_map[val]

        if v.freq > 0:
            key = -1 * (v.freq)
            ss = self.freq_to_vals_heap[key]
            ss.remove(v)
            if len(ss) == 0: del self.freq_to_vals_heap[key]

        v.freq += 1
        v.counters.append(self.counter)
        key = -1 * v.freq
        if key not in self.freq_to_vals_heap:
            self.freq_to_vals_heap[key] = SortedSet()

        ss = self.freq_to_vals_heap[key]
        ss.add(v)
       
    def pop(self) -> int:
        h_freq_key = next(iter(self.freq_to_vals_heap.keys()))
        ss = self.freq_to_vals_heap[h_freq_key]
        v = ss.pop(0)
        if len(ss) == 0: del self.freq_to_vals_heap[h_freq_key]

        v.freq -= 1
        v.counters.pop()
        if v.freq == 0:
            del self.vals_map[v.val]
            return v.val
        else:
            key = -1 * v.freq
            if key not in self.freq_to_vals_heap:
                self.freq_to_vals_heap[key] = SortedSet()
            ss = self.freq_to_vals_heap[key]
            ss.add(v)
        return v.val

# Test cases
freqStack = FreqStack()
freqStack.push(5)
freqStack.push(7)
freqStack.push(5)
freqStack.push(7)
freqStack.push(4)
freqStack.push(5)
print(freqStack.pop())
print(freqStack.pop())
print(freqStack.pop())
print(freqStack.pop()) 