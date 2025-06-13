# Intervals & Pointer Patterns

<details>
<summary><strong>💡 Pattern Best Practices</strong></summary>

```python
# 🚨 COMMON PITFALLS TO AVOID:
# 1. Intervals: Not sorting by the right criteria (start vs end time)
# 2. Fast/Slow Pointers: Off-by-one errors in cycle detection
# 3. Sliding Window: Not handling edge cases (empty arrays, k > n)

# ✅ BEST PRACTICES:
# 1. Intervals: Draw timeline diagrams to visualize overlaps
# 2. Two Pointers: Consider if array needs to be sorted first
# 3. Pattern Recognition: Many problems have multiple solution approaches

# 🎯 WHEN TO USE EACH PATTERN:
# - Intervals: Scheduling, merging, overlapping problems
# - Fast/Slow Pointers: Cycle detection, finding middle element
# - Sliding Window: Subarray/substring problems with constraints
```

</details>

<details>
<summary><strong>Interval Problems</strong></summary>

```python
# Time Complexity: O(n log n) for sorting + O(n) for processing
# Space Complexity: O(n) for result

# 🎯 INTERVAL PROBLEM PATTERNS:
# 1. Merge overlapping intervals
# 2. Insert new interval
# 3. Remove minimum intervals to make non-overlapping
# 4. Find maximum non-overlapping intervals

# Merge Intervals
# Problem: Merge overlapping intervals in a list of intervals
def merge_intervals(intervals):
    if not intervals:
        return []
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        
        # Check if intervals overlap
        if current[0] <= last[1]:
            # Merge intervals
            merged[-1] = [last[0], max(last[1], current[1])]
        else:
            # No overlap, add new interval
            merged.append(current)
    
    return merged

# 💡 INSIGHT: Always sort by start time for merging problems
# Key condition: start <= last_end means overlapping

# Insert Interval
# Problem: Insert new interval into sorted non-overlapping intervals list
def insert_interval(intervals, new_interval):
    result = []
    i = 0
    n = len(intervals)
    
    # Add all intervals that end before new interval starts
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1
    
    # Merge overlapping intervals
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    
    result.append(new_interval)
    
    # Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1
    
    return result

# 🚨 COMMON MISTAKE: Wrong overlap condition
# Correct: intervals[i][0] <= newInterval[1] (start <= end)
# Wrong: intervals[i][0] < newInterval[1] (misses touching intervals)

# Non-overlapping Intervals
# Problem: Find minimum number of intervals to remove to make rest non-overlapping
def erase_overlap_intervals(intervals):
    if not intervals:
        return 0
    
    # Sort by end time (greedy approach)
    intervals.sort(key=lambda x: x[1])
    
    count = 0
    last_end = intervals[0][1]
    
    for i in range(1, len(intervals)):
        if intervals[i][0] < last_end:
            # Overlapping interval found
            count += 1
        else:
            # Update last_end to current interval's end
            last_end = intervals[i][1]
    
    return count

# 💡 INSIGHT: Greedy approach - always keep interval with earliest end time
# This leaves maximum room for future intervals

# Meeting Rooms II
# Problem: Find minimum number of meeting rooms required
def min_meeting_rooms(intervals):
    if not intervals:
        return 0
    
    # Separate start and end times
    starts = sorted([interval[0] for interval in intervals])
    ends = sorted([interval[1] for interval in intervals])
    
    rooms = 0
    max_rooms = 0
    start_ptr = end_ptr = 0
    
    while start_ptr < len(starts):
        if starts[start_ptr] < ends[end_ptr]:
            # Meeting starts, need a room
            rooms += 1
            max_rooms = max(max_rooms, rooms)
            start_ptr += 1
        else:
            # Meeting ends, free a room
            rooms -= 1
            end_ptr += 1
    
    return max_rooms

# 🚀 ALTERNATIVE: Using heap (more intuitive)
def min_meeting_rooms_heap(intervals):
    import heapq
    
    if not intervals:
        return 0
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    # Min heap to track end times
    heap = []
    
    for interval in intervals:
        start, end = interval
        
        # Remove meetings that have ended
        while heap and heap[0] <= start:
            heapq.heappop(heap)
        
        # Add current meeting's end time
        heapq.heappush(heap, end)
    
    return len(heap)

# 💡 INSIGHT: Two approaches for meeting rooms:
# 1. Two pointers on sorted start/end times (more efficient)
# 2. Heap to track end times (more intuitive)

# Interval List Intersections
def interval_intersection(first_list, second_list):
    """Find intersection of two interval lists"""
    result = []
    i = j = 0
    
    while i < len(first_list) and j < len(second_list):
        # Find intersection
        start = max(first_list[i][0], second_list[j][0])
        end = min(first_list[i][1], second_list[j][1])
        
        if start <= end:  # Valid intersection
            result.append([start, end])
        
        # Move pointer of interval that ends first
        if first_list[i][1] < second_list[j][1]:
            i += 1
        else:
            j += 1
    
    return result

# Employee Free Time
def employee_free_time(schedule):
    """Find common free time for all employees"""
    # Flatten all intervals
    intervals = []
    for employee in schedule:
        intervals.extend(employee)
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    # Merge overlapping intervals
    merged = [intervals[0]]
    for current in intervals[1:]:
        if current[0] <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], current[1])
        else:
            merged.append(current)
    
    # Find gaps between merged intervals
    free_time = []
    for i in range(1, len(merged)):
        if merged[i-1][1] < merged[i][0]:
            free_time.append([merged[i-1][1], merged[i][0]])
    
    return free_time
```

</details>

<details>
<summary><strong>Fast & Slow Pointers</strong></summary>

```python
# Time Complexity: O(n) for most two-pointer problems
# Space Complexity: O(1)

# 🧠 KEY INSIGHT: Fast/slow pointers detect cycles and find middle elements
# Fast moves 2 steps, slow moves 1 step - they meet if there's a cycle

# Linked List Cycle
# Problem: Detect if linked list has a cycle
def has_cycle(head):
    if not head or not head.next:
        return False
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    
    return False

# 💡 INSIGHT: If there's a cycle, fast will eventually catch up to slow
# Think of it as two runners on a circular track

# Find Cycle Start
# Problem: Find the node where cycle begins
def detect_cycle(head):
    if not head or not head.next:
        return None
    
    # Phase 1: Detect if cycle exists
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            break
    else:
        return None  # No cycle
    
    # Phase 2: Find cycle start
    # Move one pointer to head, keep other at meeting point
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    return slow

# 🧠 MATHEMATICAL INSIGHT: Why does this work?
# If cycle starts at distance 'a' from head and has length 'c':
# When they meet, slow traveled 'a + b', fast traveled 'a + b + c'
# Since fast = 2 * slow: a + b + c = 2(a + b) → c = a + b
# So distance from head to cycle start = distance from meeting point to cycle start

# Find Duplicate Number
# Problem: Find duplicate number in array containing n+1 integers from 1 to n
def find_duplicate(nums):
    # Treat array as implicit linked list
    # nums[i] points to nums[nums[i]]
    
    # Phase 1: Find intersection point
    slow = fast = nums[0]
    
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        
        if slow == fast:
            break
    
    # Phase 2: Find entrance to cycle (duplicate number)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow

# 💡 INSIGHT: This is Floyd's cycle detection applied to arrays!
# The duplicate number is the "cycle start" in the implicit linked list

# Happy Number
# Problem: Determine if number is happy (sum of squares of digits eventually becomes 1)
def is_happy(n):
    def get_sum_of_squares(num):
        total = 0
        while num > 0:
            digit = num % 10
            total += digit * digit
            num //= 10
        return total
    
    slow = fast = n
    
    while True:
        slow = get_sum_of_squares(slow)
        fast = get_sum_of_squares(get_sum_of_squares(fast))
        
        if fast == 1:
            return True
        
        if slow == fast:  # Cycle detected
            return False

# Find Middle of Linked List
def find_middle(head):
    """Find middle node of linked list"""
    if not head:
        return None
    
    slow = fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

# Palindrome Linked List
def is_palindrome_linked_list(head):
    """Check if linked list is palindrome"""
    if not head or not head.next:
        return True
    
    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    def reverse_list(node):
        prev = None
        while node:
            next_temp = node.next
            node.next = prev
            prev = node
            node = next_temp
        return prev
    
    second_half = reverse_list(slow)
    
    # Compare first and second half
    first_half = head
    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next
    
    return True

# Remove Nth Node From End
def remove_nth_from_end(head, n):
    """Remove nth node from end of linked list"""
    dummy = ListNode(0)
    dummy.next = head
    
    first = second = dummy
    
    # Move first n+1 steps ahead
    for _ in range(n + 1):
        first = first.next
    
    # Move both until first reaches end
    while first:
        first = first.next
        second = second.next
    
    # Remove nth node from end
    second.next = second.next.next
    
    return dummy.next

# Reorder List
def reorder_list(head):
    """Reorder list: L0→L1→...→Ln-1→Ln to L0→Ln→L1→Ln-1→..."""
    if not head or not head.next:
        return
    
    # Find middle
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    # Split into two halves
    second_half = slow.next
    slow.next = None
    
    # Reverse second half
    def reverse_list(node):
        prev = None
        while node:
            next_temp = node.next
            node.next = prev
            prev = node
            node = next_temp
        return prev
    
    second_half = reverse_list(second_half)
    
    # Merge two halves
    first_half = head
    while second_half:
        temp1 = first_half.next
        temp2 = second_half.next
        
        first_half.next = second_half
        second_half.next = temp1
        
        first_half = temp1
        second_half = temp2
```

</details> 