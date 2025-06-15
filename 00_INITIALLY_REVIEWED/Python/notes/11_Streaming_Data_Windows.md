# Streaming Data & Windows

<details>
<summary><strong>💡 Streaming Data Best Practices</strong></summary>

```python
# 🚨 COMMON PITFALLS TO AVOID:
# 1. Not handling edge cases: empty streams, single element, overlapping boundaries
# 2. Off-by-one errors in window boundaries (inclusive vs exclusive)
# 3. Memory leaks in sliding window (not removing old elements)
# 4. Incorrect merge logic for intervals (missing edge touching cases)
# 5. Not considering time complexity of window operations

# ✅ BEST PRACTICES:
# 1. Use deque for efficient sliding window operations
# 2. Sort intervals before merging operations
# 3. Handle stream termination gracefully
# 4. Consider space-time tradeoffs (buffer size vs processing delay)
# 5. Use heap/priority queue for time-based windows

# 🎯 PATTERN RECOGNITION:
# - "Process data as it arrives" → Streaming pattern
# - "Fixed/sliding window of size K" → Sliding window
# - "Merge overlapping intervals" → Interval merging
# - "Find intersection of multiple ranges" → Interval intersection
# - "Time-based aggregation" → Time window processing
```

</details>

<details>
<summary><strong>Sliding Window Patterns</strong></summary>

```python
# Time Complexity: O(n) for most sliding window problems
# Space Complexity: O(k) where k is window size

from collections import deque, defaultdict

# Fixed Size Sliding Window
def max_sliding_window(nums, k):
    """Find maximum in each sliding window of size k"""
    if not nums or k == 0:
        return []
    
    result = []
    window = deque()  # Store indices, maintain decreasing order of values
    
    for i in range(len(nums)):
        # Remove indices outside current window
        while window and window[0] <= i - k:
            window.popleft()
        
        # Remove indices with smaller values (they can't be max)
        while window and nums[window[-1]] < nums[i]:
            window.pop()
        
        window.append(i)
        
        # Add to result once we have first complete window
        if i >= k - 1:
            result.append(nums[window[0]])
    
    return result

# Variable Size Sliding Window - Longest Substring
def length_of_longest_substring(s):
    """Longest substring without repeating characters"""
    char_count = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # Add character to window
        if s[right] in char_count:
            char_count[s[right]] += 1
        else:
            char_count[s[right]] = 1
        
        # Shrink window if constraint violated
        while char_count[s[right]] > 1:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1
        
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Subarray Sum Equals K
def subarray_sum(nums, k):
    """Count subarrays with sum equal to k"""
    count = 0
    prefix_sum = 0
    sum_count = defaultdict(int)
    sum_count[0] = 1  # Empty prefix
    
    for num in nums:
        prefix_sum += num
        # If (prefix_sum - k) exists, we found valid subarray
        count += sum_count[prefix_sum - k]
        sum_count[prefix_sum] += 1
    
    return count

# Stream Processing with Buffer
class StreamProcessor:
    def __init__(self, window_size):
        self.window_size = window_size
        self.buffer = deque()
        self.window_sum = 0
    
    def process_element(self, value):
        """Process incoming stream element"""
        self.buffer.append(value)
        self.window_sum += value
        
        # Maintain window size
        if len(self.buffer) > self.window_size:
            removed = self.buffer.popleft()
            self.window_sum -= removed
        
        # Return current window average (or any aggregation)
        return self.window_sum / len(self.buffer)
```

</details>

<details>
<summary><strong>Interval Merging & Operations</strong></summary>

```python
# Time Complexity: O(n log n) for sorting + O(n) for merging
# Space Complexity: O(n) for result

# Merge Overlapping Intervals
def merge_intervals(intervals):
    """Merge all overlapping intervals"""
    if not intervals:
        return []
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last_merged = merged[-1]
        
        # Check if current overlaps with last merged
        if current[0] <= last_merged[1]:
            # Merge: extend end time if necessary
            merged[-1] = [last_merged[0], max(last_merged[1], current[1])]
        else:
            # No overlap: add as new interval
            merged.append(current)
    
    return merged

# Insert Interval
def insert_interval(intervals, new_interval):
    """Insert new interval and merge if necessary"""
    result = []
    i = 0
    
    # Add all intervals before new_interval
    while i < len(intervals) and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1
    
    # Merge overlapping intervals
    while i < len(intervals) and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    
    result.append(new_interval)
    
    # Add remaining intervals
    while i < len(intervals):
        result.append(intervals[i])
        i += 1
    
    return result

# Interval Intersection
def interval_intersection(A, B):
    """Find intersection of two sorted interval lists"""
    result = []
    i = j = 0
    
    while i < len(A) and j < len(B):
        # Find intersection bounds
        start = max(A[i][0], B[j][0])
        end = min(A[i][1], B[j][1])
        
        # Valid intersection exists
        if start <= end:
            result.append([start, end])
        
        # Move pointer of interval that ends first
        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1
    
    return result

# Multi-Interval Intersection (your specific use case)
def intersect_multiple_intervals(interval_lists):
    """Find intersection common to ALL interval lists"""
    if not interval_lists:
        return []
    
    # Start with first list
    result = interval_lists[0]
    
    # Intersect with each subsequent list
    for intervals in interval_lists[1:]:
        result = interval_intersection(result, intervals)
        if not result:  # Early termination if no intersection
            break
    
    return result

# Advanced: Interval Union (opposite of intersection)
def interval_union(intervals):
    """Find union of all intervals (same as merge)"""
    return merge_intervals(intervals)
```

</details>

<details>
<summary><strong>Time-Based Window Processing</strong></summary>

```python
# Time Complexity: O(log n) per operation with heap
# Space Complexity: O(n) for storing time-stamped data

import heapq
from collections import defaultdict

class TimeWindowProcessor:
    """Process events within time windows"""
    
    def __init__(self, window_duration):
        self.window_duration = window_duration
        self.events = []  # Min-heap: (timestamp, event_data)
        self.active_count = 0
    
    def add_event(self, timestamp, data):
        """Add event with timestamp"""
        heapq.heappush(self.events, (timestamp, data))
        self.active_count += 1
        
        # Clean old events outside window
        self._clean_old_events(timestamp)
        
        return self.active_count
    
    def _clean_old_events(self, current_time):
        """Remove events older than window duration"""
        cutoff_time = current_time - self.window_duration
        
        while self.events and self.events[0][0] < cutoff_time:
            heapq.heappop(self.events)
            self.active_count -= 1

# Meeting Room Scheduler (Interval Scheduling)
def min_meeting_rooms(intervals):
    """Minimum meeting rooms needed for all meetings"""
    if not intervals:
        return 0
    
    # Create events: (time, type) where type: 1=start, -1=end
    events = []
    for start, end in intervals:
        events.append((start, 1))    # Meeting starts
        events.append((end, -1))     # Meeting ends
    
    # Sort by time, end events before start events at same time
    events.sort(key=lambda x: (x[0], x[1]))
    
    current_rooms = 0
    max_rooms = 0
    
    for time, event_type in events:
        current_rooms += event_type
        max_rooms = max(max_rooms, current_rooms)
    
    return max_rooms

# Time Series Data Aggregation
class TimeSeriesAggregator:
    """Aggregate streaming time series data"""
    
    def __init__(self, window_size_seconds):
        self.window_size = window_size_seconds
        self.data_points = deque()  # (timestamp, value)
        self.window_sum = 0.0
    
    def add_data_point(self, timestamp, value):
        """Add new data point and return current window average"""
        # Add new point
        self.data_points.append((timestamp, value))
        self.window_sum += value
        
        # Remove old points outside window
        cutoff_time = timestamp - self.window_size
        while self.data_points and self.data_points[0][0] < cutoff_time:
            old_timestamp, old_value = self.data_points.popleft()
            self.window_sum -= old_value
        
        # Return current window statistics
        count = len(self.data_points)
        return {
            'average': self.window_sum / count if count > 0 else 0,
            'count': count,
            'sum': self.window_sum
        }

# Advanced: Multi-Stream Merger
def merge_k_sorted_streams(streams):
    """Merge K sorted streams into single sorted stream"""
    import heapq
    
    # Min-heap: (value, stream_index, element_index)
    heap = []
    
    # Initialize heap with first element from each stream
    for i, stream in enumerate(streams):
        if stream:
            heapq.heappush(heap, (stream[0], i, 0))
    
    result = []
    
    while heap:
        value, stream_idx, elem_idx = heapq.heappop(heap)
        result.append(value)
        
        # Add next element from same stream
        if elem_idx + 1 < len(streams[stream_idx]):
            next_value = streams[stream_idx][elem_idx + 1]
            heapq.heappush(heap, (next_value, stream_idx, elem_idx + 1))
    
    return result
```

</details>

<details>
<summary><strong>Advanced Stream Processing</strong></summary>

```python
# Complex streaming patterns for difficult problems

from collections import Counter
import bisect

# Top K Frequent Elements in Stream
class TopKFrequentStream:
    """Maintain top K frequent elements in real-time"""
    
    def __init__(self, k):
        self.k = k
        self.freq_count = Counter()
        self.count_to_elements = defaultdict(set)
        self.min_count = 0
    
    def add_element(self, element):
        """Add element to stream and update top K"""
        # Update frequency
        old_count = self.freq_count[element]
        new_count = old_count + 1
        self.freq_count[element] = new_count
        
        # Update reverse mapping
        if old_count > 0:
            self.count_to_elements[old_count].discard(element)
        self.count_to_elements[new_count].add(element)
        
        # Update minimum count for top K
        self._update_min_count()
        
        return self.get_top_k()
    
    def get_top_k(self):
        """Get current top K frequent elements"""
        result = []
        counts = sorted(self.count_to_elements.keys(), reverse=True)
        
        for count in counts:
            if len(result) >= self.k:
                break
            for element in self.count_to_elements[count]:
                if len(result) >= self.k:
                    break
                result.append((element, count))
        
        return result
    
    def _update_min_count(self):
        """Update minimum count threshold"""
        top_k = self.get_top_k()
        if len(top_k) >= self.k:
            self.min_count = top_k[-1][1]

# Sliding Window Maximum with Custom Comparator
class SlidingWindowMax:
    """Generic sliding window maximum with custom comparison"""
    
    def __init__(self, window_size, compare_func=None):
        self.window_size = window_size
        self.compare = compare_func or (lambda a, b: a < b)
        self.window = deque()  # Store (value, index)
        self.monotonic_deque = deque()  # Store indices in decreasing order
        self.index = 0
    
    def add_element(self, value):
        """Add element and return current window maximum"""
        # Add to window
        self.window.append((value, self.index))
        
        # Maintain window size
        while len(self.window) > self.window_size:
            self.window.popleft()
        
        # Remove outdated indices from monotonic deque
        while (self.monotonic_deque and 
               self.monotonic_deque[0] <= self.index - self.window_size):
            self.monotonic_deque.popleft()
        
        # Maintain monotonic property (decreasing)
        while (self.monotonic_deque and 
               self.compare(self.window[self.monotonic_deque[-1] - (self.index - len(self.window) + 1)][0], value)):
            self.monotonic_deque.pop()
        
        self.monotonic_deque.append(self.index)
        self.index += 1
        
        # Return maximum of current window
        if self.monotonic_deque:
            max_idx = self.monotonic_deque[0]
            window_start = self.index - len(self.window)
            return self.window[max_idx - window_start][0]
        return None

# Data Stream Median
class StreamMedian:
    """Maintain median of data stream"""
    
    def __init__(self):
        self.small = []  # Max heap (negative values)
        self.large = []  # Min heap
    
    def add_number(self, num):
        """Add number and maintain median property"""
        # Add to appropriate heap
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)
        
        # Balance heaps (sizes differ by at most 1)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
        
        return self.find_median()
    
    def find_median(self):
        """Get current median"""
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2.0
        elif len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return self.large[0]
```

</details> 