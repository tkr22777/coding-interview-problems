"""
Problem: Find all (data, timestamp) pairs that fall within a given timestamp range.
Input: Sorted list of (data, timestamp) pairs + start/end timestamps
Output: Subset of pairs with timestamps in the range [start_ts, end_ts]
"""

import bisect

TS_INDEX = 1

def find_in_range(test_data, start_ts, end_ts):
    # Find the starting position where timestamps >= start_ts
    start = bisect.bisect_left([item[TS_INDEX] for item in test_data], start_ts)
    
    # Find the ending position where timestamps > end_ts
    end = bisect.bisect_right([item[TS_INDEX] for item in test_data], end_ts)
    
    return test_data[start:end]

# Test data: list of (data, timestamp) pairs sorted by timestamp
test_data = [
    ( "1", 1),
    ( "5", 5),
    ( "9", 9),
    ( "9", 9),
    ( "9", 9),
    ( "9", 9),
    ( "9", 9),
    ( "10", 10),
    ( "11", 11),
    ( "12", 12),
    ( "13", 13),
]

start_ts = 0
end_ts = 100

data_in_range = find_in_range(test_data, start_ts, end_ts)
print(f"for range {start_ts} to {end_ts} data in range is {data_in_range}")

data_in_range = find_in_range(test_data, 3, end_ts)
print(f"for range {3} to {end_ts} data in range is {data_in_range}")

data_in_range = find_in_range(test_data, 6, end_ts)
print(f"for range {6} to {end_ts} data in range is {data_in_range}")

data_in_range = find_in_range(test_data, 9, 11)
print(f"for range {9} to {11} data in range is {data_in_range}")

data_in_range = find_in_range(test_data, 10, 12)
print(f"for range {10} to {12} data in range is {data_in_range}")